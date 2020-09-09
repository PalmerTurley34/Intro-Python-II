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

# print(player.current_loc, ':')
# print(room[player.current_loc].desc)
# direction = input("Which direction would you like to go? [n]orth, [e]ast, [s]outh, or [w]est")

print('Starting Location:', player.current_loc.name)
print(player.current_loc.desc)
direction = input("Which direction would you like to go? [n]orth, [e]ast, [s]outh, or [w]est ")

while direction[0].lower() != 'q':

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if direction[0].lower() == 'n':
        try:
            player.current_loc.n_to
        except:
            print('Not a valid direction for this room')
            direction = input()
        else:
            player.current_loc = player.current_loc.n_to
            print(f'New Room: {player.current_loc.name}')
            print(f'Description: {player.current_loc.desc}')
            direction = input('Choose a new direction. Or "q" to quit. ')
            continue

    elif direction[0].lower() == 'e':
        try:
            player.current_loc.e_to
        except:
            print('Not a valid direction for this room')
            direction = input()
        else:
            player.current_loc = player.current_loc.e_to
            print(f'New Room: {player.current_loc.name}')
            print(f'Description: {player.current_loc.desc}')
            direction = input('Choose a new direction. Or "q" to quit. ')
            continue

    elif direction[0].lower() == 's':
        try:
            player.current_loc.s_to
        except:
            print('Not a valid direction for this room')
            direction = input()
        else:
            player.current_loc = player.current_loc.s_to
            print(f'New Room: {player.current_loc.name}')
            print(f'Description: {player.current_loc.desc}')
            direction = input('Choose a new direction. Or "q" to quit. ')
            continue

    elif direction[0].lower() == 'w':
        try:
            player.current_loc.w_to
        except:
            print('Not a valid direction for this room')
            direction = input()
        else:
            player.current_loc = player.current_loc.w_to
            print(f'New Room: {player.current_loc.name}')
            print(f'Description: {player.current_loc.desc}')
            direction = input('Choose a new direction. Or "q" to quit. ')
            continue
# If the user enters "q", quit the game.
print('You have quit the game.')