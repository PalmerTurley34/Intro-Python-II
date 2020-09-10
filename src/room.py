# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, desc, items_in_room=['None']):
        self.name = name
        self.desc = desc
        self.items_in_room = items_in_room

    def __str__(self):
        return f'Name: {self.name}\nDescription: {self.desc}\n'