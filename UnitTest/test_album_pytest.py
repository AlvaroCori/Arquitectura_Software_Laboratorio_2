from Album import Album
from Song import Song
def test_album_duration():
    audio = {}
    audio["name"] = "Las esperanzas del pasado"
    audio["artist"] = None
    album = Album(audio)
    request = album.get_duration()
    assert request == []

def test_album_info():
    audio = {}
    audio["name"] = "Las esperanzas del pasado"
    audio["artist"] = None
    album = Album(audio)
    request = album.get_info()
    assert request == "canciones del album: 0\nLas esperanzas del pasado\ndesconocido"

def test_album_duration():
    audio = {}
    audio["name"] = "Las esperanzas del pasado"
    audio["artist"] = None
    album = Album(audio)
    request = album.get_duration()
    assert request == []

def test_album_duration_with_songs():
    audio = {}
    audio["name"] = "El agua"
    audio["artist"] = None
    album = Album(audio)
    channel = {}
    channel["link"] = "-"
    channel["name_channel"] = "-"
    song = Song(audio, channel,180,"pop")
    album.insert_song(song)
    audio = {}
    audio["name"] = "El fuego"
    audio["artist"] = None
    channel = {}
    channel["link"] = "-"
    channel["name_channel"] = "-"
    song = Song(audio, channel,178,"pop")
    album.insert_song(song)
    request = album.get_duration()
    assert request == ['El agua = 3:00', 'El fuego = 2:58']

def test_album_info_with_songs():
    
    audio = {}
    audio["name"] = "Elementos"
    audio["artist"] = None
    album = Album(audio)
    audio = {}
    audio["name"] = "El agua"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    s = Song(audio, channel,180,"pop")
    album.insert_song(s)
    audio = {}
    audio["name"] = "El fuego"
    audio["artist"] = None
    channel = {}
    channel["link"] = "www.youtube.com"
    channel["name_channel"] = "GLD"
    s = Song(audio, channel,178,"pop")
    album.insert_song(s)
    request = album.get_info()
    assert request == 'canciones del album: 2\nElementos\ndesconocido'