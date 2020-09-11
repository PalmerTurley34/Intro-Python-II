class Item():
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __str__(self):
        return f'Name: {self.name}, Desc: {self.desc}'

    def on_take(self):
        return f'You have picked up {self.name}'

    def on_drop(self):
        return f'You have dropped {self.name}'