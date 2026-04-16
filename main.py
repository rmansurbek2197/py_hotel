class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.is_booked = False


class Guest:
    def __init__(self, name):
        self.name = name
        self.rooms = []


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = {}

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests[guest.name] = guest

    def book_room(self, guest_name, room_number):
        guest = self.guests.get(guest_name)
        for room in self.rooms:
            if room.number == room_number and not room.is_booked:
                room.is_booked = True
                guest.rooms.append(room_number)
                return "Booked"
        return "Failed"

    def available_rooms(self):
        return [r.number for r in self.rooms if not r.is_booked]
