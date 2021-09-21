from Artists import Artists
class SoloArtists(Artists):
    def __init__(self, name, experience, followers, birthday) :
        super(SoloArtists, self).__init__(name,experience,followers)
        self.__birtday = birthday