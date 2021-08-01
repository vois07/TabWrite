import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key
from utils import singleton
from ctypes import *

STD_OUTPUT_HANDLE = -11
 
class COORD(Structure):
    pass
 
COORD._fields_ = [("X", c_short), ("Y", c_short)]

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
                    if i == curr_pos:
                        print (':', end='')
                    try:
                        print (barstring.sounds[i], end='')
                    except IndexError:
                        pass
                print()
            else:
                print(barstring)
        #self.print_at(0, 0, "") cursor
        print()
        print()

    def print_at(self, r, c, s):
        h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
 
        c = s.encode("windows-1252")
        windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
            
           


