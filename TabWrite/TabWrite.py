import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key
from TabController import Controller

import ctypes
from time import sleep
from ctypes import windll

def main():
    #ACTIVE window by pid
    #last_id = 0
    #for i in range(50):
    #    sleep(20)
    #    hwnd = windll.user32.GetForegroundWindow()
    #    pid = ctypes.c_ulong()
    #    windll.user32.GetWindowThreadProcessId(hwnd,ctypes.byref(pid))
    #    if last_id != pid.value:
    #        print(pid.value)
    #        last_id = pid.value
    control = Controller()
    #listener = Listener(on_press=on_press)
    #listener.start()
    #listener.join()
    

if (__name__ == '__main__'):
    main()



