from Audio import Audio
from ChannelYoutube import ChannelYoutube
class Song(Audio, ChannelYoutube):

    def __init__(self, audio, channel, duration,genre):
        Audio.__init__(self, audio["name"],audio["artist"])
        ChannelYoutube.__init__(self, channel["link"],channel["name_channel"])
        self.__duration = duration
        self.__genre = genre

    def get_duration(self):
        return str(int(self.__duration/60))+":"+("0" if (self.__duration%60<10) else "")+str(self.__duration%60)
    
    def get_info(self):
        return self.get_duration()+"\n"+self.__genre+"\n"+super().get_info()+"\n"+super().get_info_channel()