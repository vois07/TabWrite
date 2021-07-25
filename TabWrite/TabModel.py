
import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key

class Strng(enum.Enum):
    e = 1
    B = 2
    G = 3
    D = 4
    A = 5
    E = 6


class Tab: 
    def __init__(self):
        self.bars = []

    def add_bar(self, bar):
        self.bars.append(bar)
    
    #def remove_last_bar(self):
    #    try:
    #        curr_bar = self.tab[-1]
    #        self.bar = self.tab[:-1]
    #    except IndexError:
    #        curr_bar = Bar()
    #    return curr_bar
    
    def __str__(self):
        return '\n\n'.join([str(b) for b in self.bars])


class Bar:    
    def __init__(self):
        self.barstrings = dict()
        self.strings = range(1,7)
        for i in self.strings:
            self.barstrings[Strng(i)] = BarString(Strng(i))
        
    def add_sound(self, strng, sound): 
        self.barstrings[Strng(strng)].add_sound(sound)
        self.normalize(sound.position + 1)
    
    def __str__(self):
        return '\n'.join([str(b) for _, b in self.barstrings.items()])
    
    #def remove_last_sound(self, strng):s
    #    self.barstrings[strng] = self.barstrings[strng].remove_last_sound()
    
    def normalize(self, position):
        for i in self.strings:
            self.barstrings[Strng(i)].add_spaces(position - len(self.barstrings[Strng(i)]))
    
    def add_break(self):
        for name, bstring in self.barstrings.items():
            bstring.add_break()


class BarString:
    def __init__(self, name):
        self.name = name
        self.sounds = []

    def __str__(self):
        sounds = ''
        if len(self.sounds) > 0:
            sounds = ''.join([str(s) for s in self.sounds])
        return str(self.name.name) + "|--" + sounds
    
    def __len__(self):
        return len(self.sounds)
    
    #dodać funkcję że podaje się pozycję i szuka się po soundach i usuwa
    #def remove_last_sound(self):
    #    try:
    #        self.sounds = self.sounds[:-1]
    #    except IndexError:
    #        pass
    #    return self
    
    def add_sound(self, sound):
        self.sounds.append(sound)
    
    def add_break(self):
        self.sounds.append("|") 
    
    def add_spaces(self, n=1):
        for i in range(n):
            self.sounds.append("-")
    
    def sort_by_postions(self): 
        self.sounds = sorted(self.sounds, key=lambda x: x.position) 
    
    def __eq__(self, other):
        ans = self.name == other.name
        if len(self.sounds) != len(other.sounds):
            return False
        for s1, s2 in zip(self.sounds, other.sounds):
            ans &= (s1 == s2)
        return ans

    def __ne__(self, other):
        ans = self.name != other.name
        if len(self.sounds) != len(other.sounds):
            return True
        for s1, s2 in zip(self.sounds, other.sounds):
            ans &= (s1 != s2)
        return ans


class Sound:
    def __init__(self, position, fret):
        self.position = position
        self.fret = str(fret)
            
    def __str__(self):
        return str(self.fret)
    
    def __len__(self):
        return len(str(self.fret))

    def __eq__(self, other):
        return self.position == other.position and self.fret == other.fret
        
    def __ne__(self, other):
        return self.position != other.position and self.fret != other.fret
        



