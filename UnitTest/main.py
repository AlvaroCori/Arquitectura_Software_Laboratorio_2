from Song import Song
from Album import Album
audio = {}
audio["name"] = "Tomas"
audio["artist"] = None
channel = {}
channel["link"] = "www.youtube.com"
channel["name_channel"] = "GLD"
s = Song(audio, channel,180,"pop")
#request = s.get_duration()
request = s.get_info()
#print(request)

audio = {}
audio["name"] = "Las esperanzas del pasado"
audio["artist"] = None
a = Album(audio)
#request = a.get_duration()
#request = a.get_info()
#print(request)

audio = {}
audio["name"] = "El agua"
audio["artist"] = None
channel = {}
channel["link"] = "www.youtube.com"
channel["name_channel"] = "GLD"
s = Song(audio, channel,180,"pop")
a.insert_song(s)
audio = {}
audio["name"] = "El fuego"
audio["artist"] = None
channel = {}
channel["link"] = "www.youtube.com"
channel["name_channel"] = "GLD"
s = Song(audio, channel,178,"pop")
a.insert_song(s)

#request = a.get_duration()
request = a.get_info()
print(request)