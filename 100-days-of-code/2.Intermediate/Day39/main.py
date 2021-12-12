from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data = DataManager()
print(data.destination)
sheet_data = data.get_destination()
flight = FlightSearch()
notification_manager = NotificationManager()
# pprint(sheet_data)


if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row['iataCode'] = flight.get_destination_code(row["city"])
    print(sheet_data)
    data.destination = sheet_data
    data.update_destination_code()

tommorow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    find_fly = flight.check_flight(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        from_time=tommorow,
        to_time=six_month_from_today
    )
    try:
        if destination["lowestPrice"] > find_fly.price :
            print("ok")
            notification_manager.send_sms(f"""Low price alert! Only £{find_fly.price} to fly from {find_fly.city_code_from}-{find_fly.city_from}
                                          to {find_fly.city_code_to}-{find_fly.city_to},
                                        from {find_fly.utc_departure} to {find_fly.utc_arrival}""")
    # # print(sheet_data)
    except AttributeError:
        print(f"NoneType object")