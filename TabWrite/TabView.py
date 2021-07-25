import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key
from utils import singleton

@singleton
class View:
    def clear(self): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
  
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 


    def print(self, tab, bar, curr_input, curr_str, curr_pos):
        print(tab)
        for name, barstring in bar.barstrings.items():
            position = 0
            print (name.name + '|--', end='')
            for i in range(len(barstring)+1):
                if barstring.name.value == curr_str:
                    if position == curr_pos:
                        print (curr_input + ':', end='')
                        position += 1
                try:
                    print (barstring.sounds[i], end='')
                    position += len(barstring.sounds[i])
                except IndexError:
                    pass
            print()


                 






