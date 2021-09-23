#import inc_dec    # The code to test
from Song import Song

def test_song():
    duration = 192
    genre = "pop"
    song = Song("first","mp4",artist=None, duration=192,genre="pop")
    request = song.getDuration()
    assert request == "3:12"
#https://code.visualstudio.com/docs/python/testing