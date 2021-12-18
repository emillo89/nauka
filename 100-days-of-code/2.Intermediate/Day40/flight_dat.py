class FlightData:
    def __init__(self, price, city_code_from, city_code_to, city_from, city_to, utc_arrival, utc_departure, stop_overs=0, via_city="" ):
        self.price = price
        self.city_code_from = city_code_from,
        self.city_code_to = city_code_to
        self.city_from = city_from
        self.city_to = city_to
        self.utc_arrival = utc_arrival
        self.utc_departure = utc_departure
        self.stop_overs = stop_overs
        self.via_city = via_city
