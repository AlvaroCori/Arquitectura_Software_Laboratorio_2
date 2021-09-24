class Artists:
    def __init__(self, name, experience, followers) :
        self.__name = name
        self.__experience = experience
        self.__followers = followers
    def get_name(self):
        return self.__name
    def get_info(self):
        return f"{self.__name}\n{self.__experience}\n{self.__followers}"