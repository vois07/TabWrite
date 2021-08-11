
#self.bar = remove_last_bar()

import enum
import operator
import itertools
from os import system, name, path
from pynput.keyboard import Listener, Key
from TabView import View
from TabModel import Bar, Tab, Strng
from itertools import groupby

class Controller:
    def __init__(self):
        self.tab = Tab()
        self.bar = Bar()
        self.cursor_string = 1
        self.cursor_position = 0
        self.max_len = 0
        self.current_keys = set()
        self.view = View()
        self.view.print(self.tab, self.bar, self.cursor_string, self.cursor_position)
        listener = Listener(on_press=self.on_press)
        listener.start()
        listener.join()

    def inc_cursor_position(self):
        self.cursor_position += 1
        if self.bar.str_len(self.cursor_string) > self.max_len:
            self.max_len = self.bar.str_len(self.cursor_string)

    def add_sound(self, fret):        
        if fret == '|':
            self.bar.add_break(self.cursor_position)
            self.inc_cursor_position()
        else:
            self.bar.add_sound(self.cursor_string, fret, self.cursor_position)
            self.inc_cursor_position()
            self.bar.normalize(self.max_len)
    
    def remove_sound(self, position):
        if position <= 0:
            self.bar = self.bar + self.tab.remove_last_bar()
        else:
            self.bar.remove_sound(self.cursor_string, position)
    
    def commit_bar(self):
        self.bar.add_break(self.cursor_position)
        self.tab.add_bar(self.bar)
        self.bar = Bar()
        self.cursor_position = 0
        self.max_len = 0

    def on_press(self, key):
        try:
            self.input_handler(key)
        except AttributeError:
            pass
    
    def input_handler(self, input):
        if (input == Key.space):
            self.add_sound('-') 
        elif (input == Key.enter):
            self.commit_bar() 
        elif (input == Key.up):
            self.cursor_string = (self.cursor_string+4) % 6 + 1
        elif (input == Key.down):
            self.cursor_string  = self.cursor_string % 6 + 1
        elif (input == Key.left): 
            self.cursor_position = 0 if self.cursor_position == 0 else self.cursor_position-1
        elif (input == Key.right):
            if self.cursor_position < self.max_len:
                self.cursor_position += 1 
        elif (input == Key.backspace):
            self.remove_sound(self.cursor_position)
            self.max_len -= 1
            self.cursor_position = self.cursor_position-1 if self.cursor_position > 0 else 0
        elif (input == Key.esc):
            self.save_to_file()
        else:
            self.add_sound(str(input.char))
        self.view.clear()
        self.view.print(self.tab, self.bar, self.cursor_string, self.cursor_position)


    def save_to_file(self, file_name='tab.txt'):
        with open(file_name, 'w') as f:
            f.write(str(self.tab) + '\n\n' + str(self.bar))
            print('\nFile saved to ' + path.realpath(f.name) + '\n')


    



