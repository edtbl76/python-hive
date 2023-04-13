hotel_rate = 140
car_rate = 40
flight_rates = {
    "Charlotte": 183,
    "Tampa": 220,
    "Pittsburgh": 222,
    "Los Angeles": 475
}


def hotel_cost(nights):
    return hotel_rate * nights


def plane_ride_cost(city):
    if city in flight_rates:
        return flight_rates[city]
    else:
        return "We don't fly there."


def rental_car_cost(days):
    total = car_rate * days
    if days >= 7:
        return total - 50
    elif days >= 3:
        return total - 20
    else:
        return total


def trip_cost(city, days, spending_money):
    return hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money


print(trip_cost("Los Angeles", 5, 600))
