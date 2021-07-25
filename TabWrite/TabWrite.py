import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key
from TabController import Controller
#from TabView import View
#from TabModel import Bar, BarString, Sound, Tab, Strng

#remove podobnie jak add z posiotion

#def on_press(key):
#    try:
#        print('alphanumeric key {0} pressed'.format(
#            key.char)) # cyferki i literki~i znaki
#    except AttributeError:
#        print('special key {0} pressed'.format(
#            key))

def main():
    control = Controller()
    #listener = Listener(on_press=on_press)
    #listener.start()
    #listener.join()
    

if (__name__ == '__main__'):
    main()



