
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
    
    def remove_last_bar(self):
        try:
            curr_bar = self.bars[-1]
            self.bars = self.bars[:-1]
        except IndexError:
            curr_bar = Bar()
        return curr_bar
    
    def __str__(self):
        return '\n\n'.join([str(b) for b in self.bars])


class Bar:    
    def __init__(self):
        self.barstrings = dict()
        self.strings = range(1,7)
        for i in self.strings:
            self.barstrings[Strng(i)] = BarString(Strng(i))

    def __str__(self):
        return '\n'.join([str(b) for _, b in self.barstrings.items()])

    def __add__(self, other):
        for i in self.strings:
            self.barstrings[Strng(i)] = self.barstrings[Strng(i)] + other.barstrings[Strng(i)]
        return self
        
    def add_sound(self, strng, sound, position, n=1): 
        self.barstrings[Strng(strng)].add_sound(sound, position, n)

    def add_break(self, position):
        for i in self.strings:
            self.barstrings[Strng(i)].add_sound('|', position)

    def remove_sound(self, strng, position):
        if self.barstrings[Strng(strng)].is_break(position-1):
            for i in self.strings:
                self.barstrings[Strng(i)] = self.barstrings[Strng(i)].remove_sound(position-1)
            return False
        self.barstrings[Strng(strng)] = self.barstrings[Strng(strng)].sound_at(position-1, '-')
        return True


    def str_len(self, strng):
        return len(self.barstrings[Strng(strng)])

    def __len__(self):
        return max([len(self.barstrings[Strng(i)]) for i in self.strings])
    
    def normalize(self, position):
        for i in self.strings:
            self.barstrings[Strng(i)].add_sound('-', position, position - len(self.barstrings[Strng(i)]))



class BarString:
    def __init__(self, name, sounds=[]):
        self.name = name
        self.sounds = sounds

    def __str__(self):
        sounds = ''
        if len(self.sounds) > 0:
            sounds = ''.join([str(s) for s in self.sounds])
        return str(self.name.name) + "|--" + sounds
    
    def __len__(self):
        return len(self.sounds)

    def __add__(self, other):
        sounds = self.sounds + other.sounds
        return BarString(self.name, sounds)
    
    def remove_sound(self, position):
        if position == len(self.sounds)-1:
            self.sounds = self.sounds[:-1]
        else: 
            try:
                self.sounds = self.sounds[:position] + self.sounds[position+1:]
            except IndexError:
                pass
        return self
    
    def add_sound(self, sound, position, n=1):
        self.sounds = self.sounds[:position] + [sound]*n + self.sounds[position:]

    def sound_at(self, position, value):
        self.sounds[position] = value
        return self
    
    def is_break(self, position):
        return self.sounds[position] == '|' or self.sounds[position] == '-'

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



