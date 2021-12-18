from data_man import DataManager
from flight_sear import FlightSearch
from datetime import datetime, timedelta
from notification_man import NotificationManager
from data_users import DataUsers

ORIGIN_CITY_IATA = "LON"

data = DataManager()
print(data.destination)
sheet_data = data.get_destination()
flight = FlightSearch()
notification_manager = NotificationManager()
data_users = DataUsers()
# pprint(sheet_data)


if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data.city_code = flight.get_destination_code(city_names)
    # print(sheet_data)
    data.update_destination_code()
    sheet_data = data.get_destination()

tommorow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

for destination in destinations:
    find_fly = flight.check_flight(
        ORIGIN_CITY_IATA,
        destination,
        from_time=tommorow,
        to_time=six_month_from_today
    )

    if find_fly is None:
        continue

    try:
        if destinations[destination]["price"] > find_fly.price:
            users = data_users.get_customer_emails()
            emails = [row["emails"] for row in users]
            names = [row["first_name"] for row in users]
            message = f"""Low price alert! Only £{find_fly.price} to fly from {find_fly.city_code_from}-{find_fly.city_from}
                                          to {find_fly.city_code_to}-{find_fly.city_to},
                                        from {find_fly.utc_departure} to {find_fly.utc_arrival}"""

            if find_fly.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)

            link = f"https://www.google.co.uk/flights?hl=en#flt={find_fly.price}.{find_fly.city_code_from}.{find_fly.city_to}"
            # notification_manager.send_sms(message)
            notification_manager.send_emails(emails, message, link)
    except AttributeError:
        print(f"NoneType object")