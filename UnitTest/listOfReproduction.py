import Audio
class ListOfReproduction:
    def __init__(self):
        self.audios = []
    def insert(self, audio):
        self.audios.append(audio)
    def getAllDuration(self):
        return 0