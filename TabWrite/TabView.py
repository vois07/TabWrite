import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key
from utils import singleton
from ctypes import *
import platform

STD_OUTPUT_HANDLE = -11

class CONSOLE_CURSOR_INFO(Structure):
    _fields_ = [('dwSize', c_int),
                ('bVisible', c_int)]
 
class WindowsConsole:
    def __init__(self):
        self.consoleWindow = windll.kernel32.GetConsoleWindow()
        self.stdOut = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        self.cursorInfo = CONSOLE_CURSOR_INFO()

    def hide_cursor(self):
        self.cursorInfo.dwSize = 1
        self.cursorInfo.bVisible = 0
        windll.kernel32.SetConsoleCursorInfo(self.stdOut, byref(self.cursorInfo))

    def is_active(self):
        return windll.user32.GetForegroundWindow() == self.consoleWindow

@singleton
class View:
    def __init__(self):
        self.console = None

    def clear(self): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    def print(self, tab, bar, curr_str, curr_pos):
        if platform.system() == 'Windows':
            self.console = WindowsConsole()
            self.console.hide_cursor()
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
        print()
        print()

            
           


