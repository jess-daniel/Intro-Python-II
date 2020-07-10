# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def add_inventory(self, item):
        return self.inventory.append(item)

    def __str__(self):
        return "Player \n Name=" + self.name + "\n current_room" + self.current_room