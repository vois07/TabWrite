from TabModel import Sound, BarString, Tab, Bar

def test_always_passes():
    assert True

def test_always_fails():
    assert False

def test_init_sound():
    s = Sound(0, 10)
    assert len(s) == 2
    s = Sound(0, 9)
    assert len(s) == 1
    s = Sound(0, 10).add_ozddobnik('p')
    assert len(s) == 3
    s = Sound(0, 9).add_ozddobnik('h')
    assert len(s) == 2
    s = Sound(0, 9).add_ozddobnik('~')
    assert len(s) == 2
    s = Sound(0, 12).add_ozddobnik('rb')
    assert len(s) == 4
    s = Sound(0, 9).add_ozddobnik('s')
    assert len(s) == 2

def test_barstring():
    bs = BarString('E')
    position = len(bs)

    s = Sound(position, 10)
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    s = Sound(position, 9)
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    s = Sound(position, 10).set_expression('p')
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    s = Sound(position, 9).set_expression('h')
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    s = Sound(position, 9).set_expression('~')
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    s = Sound(position, 12).set_expression('rb')
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    s = Sound(position, 9).set_expression('s')
    bs.add_sound(s)
    position += len(s)
    bs.add_sound(Sound(position, -1))
    position += 1
    
    print(bs)
    
    assert len(bs) == 23
    assert len(bs) == position
    
    bs.remove_last_sound()
    bs.remove_last_sound()
    
    print(bs)
    
    assert len(bs) == 20


def test_add_break():
    bs = BarString()

    s = Sound(4, 10)
    bs.add_sound(s)
    s = Sound(1, 10).set_expression('p')
    bs.add_sound(s)
    s = Sound(5, 9).set_expression('~')
    bs.add_sound(s)
    s = Sound(2, 12).set_expression('rb')
    bs.add_sound(s)
    
    bs1 = BarString()
    
    s = Sound(1, 10).set_expression('p')
    bs1.add_sound(s)
    s = Sound(2, 12).set_expression('rb')
    bs1.add_sound(s)
    s = Sound(4, 10)
    bs1.add_sound(s)
    s = Sound(5, 9).set_expression('~')
    bs1.add_sound(s)
    
    assert sorted(bs) == bs1


def test_spaces():
    bs = BarString()

    s = Sound(0, 10)
    bs.add_sound(s)
    bs.add_spaces()
    s = Sound(1, 10).set_expression('p')
    bs.add_sound(s)
    bs.add_spaces()
    s = Sound(3, 9).set_expression('~')
    bs.add_sound(s)
    bs.add_spaces(3)
    s = Sound(2, 12).set_expression('rb')
    bs.add_sound(s)
    bs.add_spaces()
    
    assert len(bs) == 17


def test_spaces():
    bs = BarString()

    s = Sound(0, 10)
    bs.add_sound(s)
    bs.add_spaces()
    s = Sound(1, 10).set_expression('p')
    bs.add_sound(s)
    bs.add_spaces()
    s = Sound(3, 9).set_expression('~')
    bs.add_sound(s)
    bs.add_spaces(3)
    s = Sound(2, 12).set_expression('rb')
    bs.add_sound(s)
    bs.add_spaces()
    bs.add_break() #'-|'
    
    print(bs)
    
    assert len(bs) == 19

def test_print_tab():
    tab = Tab()

    s = Sound(0, 10)
    tab.add_sound((Strng.e, s))
    s = Sound(1, 10).set_expression('p')
    tab.add_sound((Strng.B, s))
    s = Sound(3, 9).set_expression('~')
    tab.add_sound((Strng.e, s))
    s = Sound(2, 12).set_expression('rb')
    tab.add_sound((Strng.D, s))
    
    print(tab)
    
    assert true

def test_print_tab():
    tab = Tab()
    bar = Bar()

    s = Sound(0, 10)
    tab.add_sound((Strng.e, s))
    s = Sound(1, 10).add_ozddobnik('p')
    tab.add_sound((Strng.B, s))
    s = Sound(0, 9).add_ozddobnik('~')
    bar.add_sound((Strng.e, s))
    s = Sound(1, 12).add_ozddobnik('rb')
    bar.add_sound((Strng.D, s))
    
    print(View(tab, bar, '1', Strng.G, 2))
    
    assert true


def test_parseinput():
    #-9h10p9-
    assert ['9','h','10','p','9'] == parse_input()

def test_bar():
    bar.normalize()
    print(bar)

    #assert z forem
    #assert len(bar.strings) ==
    assert False


