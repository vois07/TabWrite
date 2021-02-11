import enum
import operator
import itertools
from pynput.keyboard import Listener

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

    def __str__(self):
        return str(self.fret)

class Tab:
    def __init__(self):
        self.tab = []
        self.position = 0

    def __str__(self):
        tmp_tab = self.tab
        tmp_tab = tmp_tab + [(-1,Sound(x,'x')) for x in range(1,7)]
        tmp_tab = sorted(tmp_tab, key=lambda t: t[1].strng)
        for strng in self.get_strngs(tmp_tab):
            ans = '|--'
            l = strng[1] #list of position + fret number pairs
            for i in range(self.position):
                try:
                    pos = l[0][0]
                except IndexError:
                    pos = -1
                if pos == i:
                    ans += str(l[0][1])
                    l = l[1:]
                else:
                    ans += '-'
                ans += '--'
            print(ans + '--|')
        return ''#.join([str(t[1]) for t in tmp])

    def get_strngs(self, tmp_tab):
        it = itertools.groupby(tmp_tab,  key=lambda t: t[1].strng)
        for key, subiter in it:
           yield key, [(item[0], item[1].fret) for item in subiter]

    def add_sound(self, sound):
        self.tab.append((self.position, sound))
        self.position += 1

    def remove_last(self):
        self.tab = self.tab[:-1]


tab = Tab()
tab.add_sound(Sound(Strng.e,7))
tab.add_sound(Sound(Strng.E,4))
tab.add_sound(Sound(Strng.D,7))
tab.add_sound(Sound(Strng.e,3))
tab.add_sound(Sound(Strng.e,13))
print(tab)

def on_press(key):
    print("Key pressed: {0}".format(key))

with Listener(on_press=on_press) as listener:
    listener.join()




