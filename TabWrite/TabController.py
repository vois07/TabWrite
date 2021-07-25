
#self.bar = remove_last_bar()

import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key
from TabView import View
from TabModel import Sound, Bar, Tab, Strng
from itertools import groupby

class Controller:
    def __init__(self):
        self.tab = Tab()
        self.bar = Bar()
        self.cursor_string = 1
        self.cursor_position = 0
        self.curr_input = ""
        self.view = View()
        self.view.print(self.tab, self.bar, self.curr_input, self.cursor_string, self.cursor_position)
        listener = Listener(on_press=self.input_handler)
        listener.start()
        listener.join()

    def add_sound(self, fret):
        s = Sound(self.cursor_position, fret)
        self.bar.add_sound(s, self.cursor_string)
        self.cursor_position += len(s)
    
    def remove_sound(self):
        if cursor_position == 0:
            self.bar = self.tab.remove_last_bar()
        self.bar.remove_last_sound()
    
    def commit_bar(self):
        self.tab.add_bar(self.bar)
        self.bar = Bar()
        self.cursor_position = 0
    

    def parse_input(self, strng=None, pos=None):
        strng = strng if strng else self.cursor_string
        pos = pos if pos else self.cursor_position
        res = [''.join(g) for _, g in groupby(self.curr_input, str.isalpha)]
    
        for el in res:
            self.bar.add_sound(strng, Sound(pos, el))
        self.curr_input = ""
        return res
    

    def input_handler(self, input):
        print("hey!")
        if (input == Key.space or input == Key.enter):
            if (self.curr_input != ""):
                _ = self.parse_input() 
            else:
                self.bar.barstrings[Strng(self.cursor_string)].add_spaces() 
            self.cursor_position += 1
            self.bar.normalize(self.cursor_position)
            if (input == Key.enter):
                self.commit_bar() # + obsługa strzałek
        elif (input == Key.up):
            self.cursor_string = (self.cursor_string+5) % 6
        elif (input == Key.down):
            self.cursor_string  = (self.cursor_string+1) % 6
        elif (input == Key.left): 
            self.cursor_position = 0 if self.cursor_position == 0 else self.cursor_position-1
        elif (input == Key.right):
            self.cursor_position += 1 #
        #elif (input == Key.backspace):
        #    remove_sound()
        try:
            if (input.char == '|'):
                self.bar.add_break()
            elif (input.char == '-'):
                self.bar.spaces()
                self.bar.normalize()
            else:
                self.curr_input = str(self.curr_input) + str(input.char)
        except AttributeError:
            pass
        self.view.clear()
        self.view.print(self.tab, self.bar, self.curr_input, self.cursor_string, self.cursor_position)

