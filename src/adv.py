from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
from player import Player
player = Player('Palmer', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
print(f'Welcome {player.name}!\n')
print('Starting Location:')
print(player.current_room)
print(f'Items in the room are: {player.current_room.items_in_room}\n')
direction = input("Which direction would you like to go? [n]orth, [e]ast, [s]outh, or [w]est ")

while direction != 'q':

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if direction in ['n', 'e', 's', 'w']:
        try:
            player.change_room(direction)
        
        except:
            print('\nNot a valid direction for this room')
            direction = input()

        else:
            print('\nNew Room:')
            print(player.current_room)
            print(f'Items in the room are: {player.current_room.items_in_room}\n')
            direction = input('Choose a new direction. Or "q" to quit. ')
            continue

    else:
        print('This is not a valid input. Valid inputs are: "n", "e", "s", or "w"')
        direction = input()

# If the user enters "q", quit the game.
print(f'\nYou have quit the game.\nGoodbye, {player.name}!\n')