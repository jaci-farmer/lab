class Television:
    """
    Class to represent the Television objects
    """
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """"
        Method to set default state of the TV
        """
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False

    def power(self) -> None:
        """
        Method to turn the TV on/off
        """
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True


    def channel_up(self) -> None:
        """
        Method to turn the channel up
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel = self.__channel + 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to turn the channel down
        """
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel = self.__channel - 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self)-> None:
        """
        Method to turn the volume up
        """
        if self.__status == True:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume = self.__volume + 1
            else:
                self.__volume = Television.MAX_VOLUME


    def volume_down(self)-> None:
        """
        Method to turn the volume down
        """
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume = self.__volume - 1
            else:
                self.__volume = Television.MIN_VOLUME


    def __str__(self) -> str:
        """
        Method to access state of the TV
        :return: TV Status
        """
        return (f"TV Status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume} ")
