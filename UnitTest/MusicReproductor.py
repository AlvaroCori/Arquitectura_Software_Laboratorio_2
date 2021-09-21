import Audio
import listOfReproduction
class ListOfReproduction:
    def __init__(self):
        self.__reproductor = listOfReproduction()
        self.__index = 0
        self.__size = 0
    def insert(self, audio):
        self.__reproductor.insert(audio)
        self.__size = self.__size + 1
    def __controlIndex(self, movement):
        if (self.index == 0 and movement == -1):
            self.index = self.__size - 1
            return True
        elif (self.index == self.__size-1 and movement == 1):
            self.index = 0
            return True
        return False
    def nextSong(self):
        if (self.__controlIndex(1)==False):
            self.index = self.index + 1

    def previousSong(self):
        if (self.__controlIndex(-1)==False):
            self.index = self.index - 1
    