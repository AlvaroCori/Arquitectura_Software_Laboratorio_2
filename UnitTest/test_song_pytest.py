#import inc_dec    # The code to test
from Song import Song
def test_song_duration():
    audio = {}
    audio["name"] = "Tomas"
    audio["format_audio"] = "mp4"
    audio["artist"] = None
    channel = {}
    channel["link"] = "-"
    channel["name_channel"] = "-"
    song = Song(audio, channel,192,"pop")
    request = song.get_duration()
    assert request == "3:12"

def test_song_fichure():
    audio = {}
    audio["name"] = "Tomas"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    song = Song(audio, channel,180,"pop")
    request = song.get_info()
    assert request == "3:00\npop\nTomas\ndesconocido\nGLD - www.youtube.com"
#https://code.visualstudio.com/docs/python/testing