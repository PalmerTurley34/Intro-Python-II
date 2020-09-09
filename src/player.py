# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name='Player 1', current_loc='Outside'):
        self.name = name
        self.current_loc = current_loc

