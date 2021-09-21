from Artists import Artists
class Band(Artists):
    def __init__(self, name, experience, followers, popularity) :
        super(Band, self).__init__(name,experience,followers)
        self.__popularity = popularity