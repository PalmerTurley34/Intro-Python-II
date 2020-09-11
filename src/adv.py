from room import Room

# add a couple items for testing
from item import Item
items = {
    'sword': Item('Sword', 'A standard sword'),
    'torch': Item('Torch', 'A useful light source')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['sword'], items['torch']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['torch']]),

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
print(f'Items in the room are:')
player.current_room.print_items()
user_input = input("\nWhich direction would you like to go? [n]orth, [e]ast, [s]outh, or [w]est ")

while user_input != 'q':

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if user_input in ['n', 'e', 's', 'w']:
        try:
            player.change_room(user_input)
        
        except:
            print('\nNot a valid direction for this room')
            user_input = input()

        else:
            print('\nNew Room:')
            print(player.current_room)
            print(f'Items in the room are:')
            player.current_room.print_items()
            user_input = input('\nChoose a new direction. Or "q" to quit. ')
            continue

    elif len(user_input.split()) == 2 and user_input.split()[0] == 'take':
        _, item = user_input.split()

        if items[item] in player.current_room.items_in_room:
            # remove item from room and add it to inventory
            player.add_to_inventory(items[item])
            player.current_room.remove_from_room(items[item])
            print(items[item].on_take())
            # print out the rest of items in room and your inventory
            print(f'Items left in room:')
            player.current_room.print_items()
            print(f'Your inventory:')
            player.check_inventory()

            user_input = input('What would you like to do now? ')
            continue

        else:
            print('That item does not exist in this room.')
            user_input = input('What would you like to do now? ')
            continue

    elif len(user_input.split()) == 2 and user_input.split()[0] == 'drop':
        _, item = user_input.split()
        if items[item] in player.inventory:
            # remove item from inventory and add it to room
            player.remove_from_inventory(items[item])
            player.current_room.add_to_room(items[item])
            print(items[item].on_drop())
            # print out the rest of items in room and your inventory
            print(f'Items left in room:')
            player.current_room.print_items()
            print(f'Your inventory:')
            player.check_inventory()
            
            user_input = input('What would you like to do now? ')
            continue

        else:
            print('That item does not exist in your inventory.')
            user_input = input('What would you like to do now? ')
            continue

    elif user_input == 'inventory':
        player.check_inventory()
        user_input = input('What would you like to do now? ')
        continue

    else:
        print('This is not a valid input. Valid inputs are: "n", "e", "s", or "w"')
        direction = input()

# If the user enters "q", quit the game.
print(f'\nYou have quit the game.\nGoodbye, {player.name}!\n')