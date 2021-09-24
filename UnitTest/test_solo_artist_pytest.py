from ls.Solo_Artist import Solo_Artist
def test_artist_info():
    artist = {}
    artist["name"] = "Bob Sailor"
    artist["experience"] = 20
    artist["followers"] = 300000

    a = Solo_Artist(artist,[20,9,1994])
    request = a.get_info()
    print(request)
    assert request == "Bob Sailor\n20\n300000\n20/9/1994"

def test_artist_info():
    artist = {}
    artist["name"] = "Bob Sailor"
    artist["experience"] = 20
    artist["followers"] = 300000

    a = Solo_Artist(artist,[20,9,1994])
    request = a.get_info()
    print(request)
    assert request == "Bob Sailor\n20\n300000\n20/9/1994"
