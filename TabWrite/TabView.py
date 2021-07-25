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


    def print(self, tab, bar, curr_str, curr_pos):
        print(tab)
        print()
        for name, barstring in bar.barstrings.items():
            if barstring.name.value == curr_str:
                print (name.name + '|--', end='')
                for i in range(len(barstring)+1):
                    try:
                        print (barstring.sounds[i], end='')
                    except IndexError:
                        pass
                    if i == curr_pos:
                        print (':', end='')
                print()
            else:
                print(barstring)
        print()
        print()
            
           

                 






