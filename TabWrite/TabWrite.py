import enum
import operator
import itertools
from os import system, name 
from pynput.keyboard import Listener, Key

curr_fret = 0

class Strng(enum.Enum):
    e = 1
    B = 2
    G = 3
    D = 4
    A = 5
    E = 6

class Sound:

    def __init__(self, strng, fret):
        try:
            self.strng = strng.value
        except AttributeError:
            self.strng = strng
        self.fret = fret
        
        self._vibratto = False
        self._hammer_on = False
        self._pull_off = False
        self._slide = False

    def __str__(self):
        return str(self.fret)

    def is_vibratto(self):
        return self._vibratto
    def vibratto(self,val = True):
        self._vibratto = val

    def is_hammer_on(self):
        if self._hammer_on:
            return "h"
        else: return ""
    def hammer_on(self,val = True):
        self._hammer_on = val

    def is_pull_off(self):
        if self._pull_off:
            return "p"
        else: return ""
    def pull_off(self,val = True):
        self._pull_off = val

    def is_slide(self):
        if self._slide:
            return "s"
        else: return ""
    def slide(self,val = True):
        self._slide = val


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Tab_new:
    def __init__(self):
        self.bars = []

    def add_bar(self, bar):
        self.bars.append(bar)

    def __str__(self):
        for bar in self.bars:
            print(bar)


class Tab:
    def __init__(self):
        self.tab = []
        self.position = 0
        self.cursor = 0

    def __str__(self):
        tmp_tab = self.tab
        tmp_tab = tmp_tab + [(-1,Sound(x,'x')) for x in range(1,7)]
        tmp_tab = sorted(tmp_tab, key=lambda t: t[1].strng)
        print()
        for nb, strng in enumerate(self.get_strngs(tmp_tab)):
            ans = '|--'
            l = strng[1] #list of position + fret number pairs
            for i in range(self.position+1):
                add_space = 0
                try:
                    pos = l[0][0]
                except IndexError:
                    pos = -1
                if pos == i:
                    try:
                        if (l[0][1] < 10):  ans += '-'
                    except TypeError:
                        ans += '-'
                    ans += str(l[0][1])
                    l = l[1:]
                    # tmp_ans = (sound.is_hammer_on()+sound.is_pull_off()+sound.is_slide() + "--") 
                    #add_space += (len(tmp_ans)-3)
                    # ans += tmp_ans + add_space*"-"
                else:
                    ans += '--'
                
                #if (sound.is_vibratto()):
                                #ans += '~-'
                            #else:
                ans += '--'
            if (nb == self.cursor): ans += ':'
            print(ans + '--|')
        return ''#.join([str(t[1]) for t in tmp])

    #return SOUND
    def get_strngs(self, tmp_tab):
        it = itertools.groupby(tmp_tab,  key=lambda t: t[1].strng)
        for key, subiter in it:
           yield key, [(item[0], item[1].fret) for item in subiter]

    def add_sound(self, sound):
        self.tab.append((self.position, sound))
        self.position += 1

    def remove_last(self):
        self.tab = self.tab[:-1]


class Visuals:
    def __init__(self):
        self.curr_input = 0
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()

    def clear(self): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
  
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 

    def on_press(self, key):
        print("Key pressed: {0}".format(key))
        if (key == Key.down): tab.cursor = (tab.cursor+1) % 6
        elif (key == Key.up): tab.cursor = (tab.cursor+5) % 6

        elif (key == Key.left):
            tab.position -= 1 

        elif (key == Key.right):
            tab.position += 1 

        elif (key == Key.enter):
            for i in range(1,7):
                tab.add_sound(Sound(i, '|'))
                tab.position -= 1
            tab.position += 1

    
        elif (key == Key.space):
            tab.add_sound(Sound(tab.cursor,self.curr_input))
            self.curr_input = 0

        else:
            try:
                if (key.char in [str(d) for d in range(0,10)]):
                    self.curr_input = (10*self.curr_input + int(key.char))
            except AttributeError:
                pass

        #elif (key.name in [str(x) for x in range(0,10)]):
        #    tab.add_sound(Sound(tab.cursor+1, key.char))

        self.clear()
        print(tab)


vis = Visuals()
tab = Tab()
tab.add_sound(Sound(Strng.e,7))
tab.add_sound(Sound(Strng.E,4))
tab.add_sound(Sound(Strng.D,7))
tab.add_sound(Sound(Strng.e,3))
tab.add_sound(Sound(Strng.e,13))
print(tab)


vis.listener.join()




