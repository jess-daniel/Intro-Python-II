from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("ball", "round and bouncy")),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Michael", "outside")

# Write a loop that:
#
is_playing = True

while is_playing is True:

# * Prints the current room name
    print("Current Location: " + player.current_room)
# * Prints the current description (the textwrap module might be useful here).
    print("Description: " + room[player.current_room].description + "\n")
# * Waits for user input and decides what to do.
    player_input = input("What is your next move? ")
# If the user enters a cardinal direction, attempt to move to the room there.
    def check_move(input):
        global is_playing
        if input == "n":
            new_room = room[player.current_room].n_to
            if new_room == None:
                print("Invalid Movement")
                return
            player.current_room = new_room.name.lower()
        elif input == "s":
            new_room = room[player.current_room].s_to
            if new_room == None:
                print("Invalid Movement")
                return
            player.current_room = new_room.name.lower()
        elif input == "e":
            new_room = room[player.current_room].e_to
            if new_room == None:
                print("Invalid Movement")
                return
            player.current_room = new_room.name.lower()
        elif input == "w":
            new_room = room[player.current_room].w_to
            if new_room == None:
                print("Invalid Movement")
                return
            player.current_room = new_room.name.lower()
        elif input == "q":
            is_playing = False
            return
        else:
            print("Invalid movement")
# Print an error message if the movement isn't allowed.
    check_move(player_input)

    print("Room Items: " + str(room[player.current_room].items))
# If the user enters "q", quit the game.

