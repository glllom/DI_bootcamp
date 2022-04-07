import datetime
import re
from time import sleep


class Company:
    def __init__(self, id: str, name: str, planes: list):
        if not re.match(r"\w\w", id):
            raise ValueError('Invalid ID')
        else:
            self.id = id
        self.name = name
        self.planes = planes


class Airport:
    def __init__(self, city: str, planes: list, scheduled_departures: list, scheduled_arrivals: list):
        self.city = city
        self.planes = planes
        self.scheduled_departures = scheduled_departures
        self.scheduled_arrivals = scheduled_arrivals

    def schedule_flight(self, destination, date_time):
        """Finds when an available airplane from an airline that serve the origin"""
        """ and the destination and schedule a flight for it."""
        pass

    def info(self, start_date, end_date):
        """Display every scheduled flight from start_date to end_date."""
        print("Arrivals:")
        for flight in self.scheduled_arrivals:
            if start_date < flight.date < end_date:
                print(flight.id)

        print("\nDepartures:")
        for flight in self.scheduled_departures:
            if start_date < flight.date < end_date:
                print(flight.id)


class Airplane:
    def __init__(self, id: int, current_location: Airport, company: Company, next_flights: list):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = next_flights

    def fly(self, destination):
        sleep(3)
        print(f"{self.id} arriving from {self.current_location} to {destination}.")
        sleep(1)

    def location_on_date(self, date):
        """Returns where the plane will be on this date"""
        locations = []
        for flight in self.next_flights:
            if flight.date == date:
                locations.append(flight.destination.city)
        return locations

    def available_on_date(self, date, location):
        """Returns True if the plane can fly from this location on this date"""
        """It can fly if it is in this location on this date and if it doesn't already have a flight planned."""
        return location == self.location_on_date(date)[len(self.location_on_date(date)) - 1]


class Flight:
    def __init__(self, date: datetime.datetime, destination: Airport, origin: Airport, plane: Airplane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = destination.city + plane.company.id + str(date)

    def take_off(self):
        self.origin.scheduled_departures.pop(self)
        print(f"{self.plane.id} took off.")

    def land(self):
        self.destination.scheduled_arrivals.pop(self)
        self.plane.current_location = self.destination.city
        print(f"{self.plane.id} landed in {self.destination.city}.")


british_airways = Company('BA', 'British Airways', [])
heathrow = Airport('LHR', [], [], [])
dubai = Airport('DXB', [], [], [])
delhi = Airport('DEL', [], [], [])
phoenix = Airport('PHX', [], [], [])

boeing1 = Airplane(737, phoenix, british_airways, [])
boeing2 = Airplane(747, heathrow, british_airways, [])
airbus1 = Airplane(320, dubai, british_airways, [])
airbus2 = Airplane(380, delhi, british_airways, [])

heathrow.scheduled_departures.append(Flight(datetime.datetime(2022, 3, 1, 10, 30), dubai, heathrow, boeing2))
heathrow.scheduled_departures.append(Flight(datetime.datetime(2022, 3, 1, 12, 30), phoenix, heathrow, boeing1))
phoenix.scheduled_departures.append(Flight(datetime.datetime(2022, 4, 1, 10, 30), delhi, phoenix, airbus1))
delhi.scheduled_departures.append(Flight(datetime.datetime(2022, 5, 1, 10, 30), heathrow, phoenix, airbus2))
heathrow.scheduled_arrivals.append(Flight(datetime.datetime(2022, 3, 11, 10, 30), heathrow, phoenix, boeing2))
heathrow.scheduled_arrivals.append(Flight(datetime.datetime(2022, 3, 11, 12, 30), heathrow, heathrow, boeing1))
phoenix.scheduled_arrivals.append(Flight(datetime.datetime(2022, 4, 11, 10, 30), phoenix, heathrow, airbus1))
delhi.scheduled_arrivals.append(Flight(datetime.datetime(2022, 5, 11, 10, 30), delhi, phoenix, airbus2))

heathrow.info(datetime.datetime(2022, 1, 1, 10, 30), datetime.datetime(2022, 4, 1, 10, 30))
