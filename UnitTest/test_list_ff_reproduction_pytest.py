from ls.List_Of_Reproduction import List_Of_Reproduction
from ls.Song import Song
from ls.Album import Album
def test_list_void():
    list_of_reproduction = List_Of_Reproduction()
    request = list_of_reproduction.get_all_durations()
    assert request == 0

def test_list_songs():
    list_of_reproduction = List_Of_Reproduction()
    audio = {}
    audio["name"] = "Solitario 1"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GS"
    s1 = Song(audio, channel,254,"electronica")
    audio = {}
    audio["name"] = "Solitario 2"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GS"
    s2 = Song(audio, channel,580,"electronica")
    list_of_reproduction.insert(s1)
    list_of_reproduction.insert(s2)
    request = list_of_reproduction.get_all_durations()
    assert request == 834

def test_list_album():
    list_of_reproduction = List_Of_Reproduction()
    audio = {}
    audio["name"] = "Las esperanzas del pasado"
    audio["artist"] = None
    a = Album(audio)

    audio = {}
    audio["name"] = "El agua"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    s = Song(audio, channel,380,"pop")
    a.insert_song(s)
    audio = {}
    audio["name"] = "El fuego"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    s = Song(audio, channel,278,"pop")
    a.insert_song(s)
    list_of_reproduction.insert(a)
    request = list_of_reproduction.get_all_durations()
    assert request == 658

def test_list_songs_and_album():
    list_of_reproduction = List_Of_Reproduction()

    audio = {}
    audio["name"] = "Solitario 1"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GS"
    s1 = Song(audio, channel,254,"electronica")
    audio = {}
    audio["name"] = "Solitario 2"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GS"
    s2 = Song(audio, channel,580,"electronica")

    audio = {}
    audio["name"] = "Las esperanzas del pasado"
    audio["artist"] = None
    a = Album(audio)
    audio = {}
    audio["name"] = "El agua"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    s = Song(audio, channel,380,"pop")
    a.insert_song(s)
    audio = {}
    audio["name"] = "El fuego"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    s = Song(audio, channel,278,"pop")
    a.insert_song(s)
    list_of_reproduction.insert(s1)
    list_of_reproduction.insert(a)
    list_of_reproduction.insert(s2)
    request = list_of_reproduction.get_all_durations()
    assert request == 1492