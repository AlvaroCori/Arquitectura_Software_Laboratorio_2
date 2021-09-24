class ChannelYoutube:
    def __init__(self,link,name_channel):
        self.__link = link
        self.__name_channel = name_channel
    def get_info_channel(self):
        return f"{self.__name_channel} - {self.__link}"