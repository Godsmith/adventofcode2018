from . import day13

STATE = r"""/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """.splitlines()

STATE2 = r"""/-->\        
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/   """.splitlines()

STATE3 = r"""/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/""".splitlines()


def test_track():
    track = day13.Track(STATE)
    assert repr(track.carts) == '[Cart(2, 0, ">", "L"), Cart(9, 3, "v", "L")]'
    assert track.terrain(2, 0) == '-'
    assert track.terrain(9, 3) == '|'


def test_tick():
    track = day13.Track(STATE)
    track.tick()
    assert str(track) == '\n'.join(STATE2)


def test_first_crash():
    track = day13.Track(STATE)
    assert track.first_crash() == (7, 3)


def test_last_cart_location():
    track = day13.Track(STATE3)
    assert track.last_cart_location() == (6, 4)
