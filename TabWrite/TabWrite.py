import enum

class String(enum.Enum):
    e = 1
    B = 2
    G = 3
    D = 4
    A = 5
    E = 6

class Sound:
    def __init__(self, string, fret):
        self.string = string
        self.fret = fret

class Tab:
    def __init__(self):
        self.tab = []

    def add_sound(self, sound):
        self.tab.append(sound)

    def remove_last(self):
        self.tab = self.tab[:-1]


