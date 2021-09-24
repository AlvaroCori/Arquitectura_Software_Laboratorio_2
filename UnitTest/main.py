from Song import Song
from Album import Album
from Solo_Artist import Solo_Artist
from Band import Band
from List_Of_Reproduction import List_Of_Reproduction
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
#request = a.get_info()
#print(request)
artist = {}
artist["name"] = "Bob Sailor"
artist["experience"] = 20
artist["followers"] = 300000

a = Solo_Artist(artist,[20,9,1994])
#request = a.get_info()
#print(request)

artist = {}
artist["name"] = "The Meat Boys"
artist["experience"] = 5
artist["followers"] = 3000000
b = Band(artist,0.95)
#request = b.get_info()
#print(request)

artist = {}
artist["name"] = "Jeff Elims"
artist["experience"] = 10
artist["followers"] = 345000
a = Solo_Artist(artist,[20,9,1994])
b.insert_artist(a)
artist = {}
artist["name"] = "Rita Das"
artist["experience"] = 5
artist["followers"] = 376000
a = Solo_Artist(artist,[20,9,1994])
b.insert_artist(a)
artist = {}
artist["name"] = "Alyn Ynnuf"
artist["experience"] = 5
artist["followers"] = 319000
a = Solo_Artist(artist,[20,9,1994])
b.insert_artist(a)
#request = b.get_info()
#print(request)


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

l = List_Of_Reproduction()
l.insert(a)
l.insert(s1)
l.insert(s2)

request = l.get_all_durations()
print(request)

