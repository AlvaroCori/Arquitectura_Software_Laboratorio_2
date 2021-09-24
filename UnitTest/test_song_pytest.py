#import inc_dec    # The code to test
from ls.Song import Song
from ls.Solo_Artist import Solo_Artist
from ls.Band import Band
def test_song_duration():
    audio = {}
    audio["name"] = "The Wind"
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
    audio["name"] = "The Wind"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    song = Song(audio, channel,180,"pop")
    request = song.get_info()
    assert request == "3:00\npop\nThe Wind\ndesconocido\nGLD - www.youtube.com"

def test_song_solo_artist():
    artist = {}
    artist["name"] = "Bill Bucker"
    artist["experience"] = 20
    artist["followers"] = 300000
    art = Solo_Artist(artist,[20,9,1988])
    audio = {}
    audio["name"] = "Rain"
    audio["artist"] = art
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "ASSA"
    song = Song(audio, channel,180,"pop")
    request = song.get_info()
    request_artist = art.get_info()
    assert request == "3:00\npop\nRain\nBill Bucker\nASSA - www.youtube.com" and request_artist == "Bill Bucker\n20\n300000\n20/9/1988"

def test_song_solo_band():
    band = {}
    band["name"] = "The Formidables"
    band["experience"] = 5
    band["followers"] = 340000
    bd = Band(band,0.925)

    audio = {}
    audio["name"] = "Flow"
    audio["artist"] = bd
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    song = Song(audio, channel,180,"g pop")
    request = song.get_info()
    request_album = bd.get_info()
    assert request == "3:00\ng pop\nFlow\nThe Formidables\nGLD - www.youtube.com" and request_album == "The Formidables\n5\n340000\n92.5%"
#https://code.visualstudio.com/docs/python/testing