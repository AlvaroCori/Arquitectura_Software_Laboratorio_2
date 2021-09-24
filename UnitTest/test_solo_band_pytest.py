from Band import Band
from Solo_Artist import Solo_Artist
def test_band_info():
    artist = {}
    artist["name"] = "The Meat Boys"
    artist["experience"] = 5
    artist["followers"] = 3000000
    band = Band(artist,0.95)
    request = band.get_info()
    assert request == "The Meat Boys\n5\n3000000\n95.0%"

def test_band_info_with_artist():
    band_information = {}
    band_information["name"] = "The Inverts"
    band_information["experience"] = 3
    band_information["followers"] = 5000000
    band = Band(band_information,0.95)
    artist = {}
    artist["name"] = "Jeff Elims"
    artist["experience"] = 10
    artist["followers"] = 345000
    a = Solo_Artist(artist,[20,9,1994])
    band.insert_artist(a)
    artist = {}
    artist["name"] = "Rita Das"
    artist["experience"] = 5
    artist["followers"] = 376000
    a = Solo_Artist(artist,[20,9,1994])
    band.insert_artist(a)
    artist = {}
    artist["name"] = "Alyn Ynnuf"
    artist["experience"] = 5
    artist["followers"] = 319000
    a = Solo_Artist(artist,[20,9,1994])
    band.insert_artist(a)
    request = band.get_info()
    assert request == "The Inverts\n3\n5000000\n95.0%\n* Jeff Elims\n* Rita Das\n* Alyn Ynnuf"

