# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def change_room(self, direction):
        if direction == 'n':
            self.current_room = self.current_room.n_to

        elif direction == 'e':
            self.current_room = self.current_room.e_to

        elif direction == 's':
            self.current_room = self.current_room.s_to

        elif direction == 'w':
            self.current_room = self.current_room.w_to

    def check_inventory(self):
        for item in self.inventory:
            print(item)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)