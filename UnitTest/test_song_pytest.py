#import inc_dec    # The code to test
from Song import Song


def test_song():
    song = Song(192,"pop")
    request = song.getDuration()
    assert request == "3:12"
#https://code.visualstudio.com/docs/python/testing