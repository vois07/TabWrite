from TabModel import BarString, Tab, Bar, Strng

#dodawanie, usuwanie
#-dzwiekow, spacji, literek
#-break - czy ta sama pozycja na wszystkich strng
#normalizacja - dodać dzwieki na jednej strunie - czy wszystkie ta sama dlugosc?


def test_add_break():
    bs = BarString("test")

    s = Sound(4, 10)
    bs.add_sound(s)
    s = Sound(1, 10)
    bs.add_sound(s)
    s = Sound(5, 9)
    bs.add_sound(s)
    
    bs1 = BarString("test")
    
    s = Sound(1, 10)
    bs1.add_sound(s)
    s = Sound(4, 10)
    bs1.add_sound(s)
    s = Sound(5, 9)
    bs1.add_sound(s)

    bs.sort_by_postions()
    
    assert bs == bs1




