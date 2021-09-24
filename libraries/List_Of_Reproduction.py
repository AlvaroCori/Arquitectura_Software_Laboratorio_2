from libraries.Audio import Audio
class List_Of_Reproduction:
    def __init__(self):
        self.audios = []
    def insert(self, audio):
        self.audios.append(audio)
    def get_all_durations(self):
        duration = 0
        for audio in self.audios:
            duration += audio.get_number_duration()
        return duration