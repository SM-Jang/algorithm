import abc


class Room(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def openDoor(self):
        pass

    @abc.abstractmethod
    def openWindow(self):
        pass


class BedRoom(Room):
    def openDoor(self):
        print("Open bedroom door")

    def openWindow(self):
        print("Open bedroom window")


class Lobby(Room):
    def openDoor(self):
        print("Open lobby door")


room1 = BedRoom()
print(issubclass(BedRoom, Room), isinstance(room1, Room))

lobby1 = Lobby()
print(issubclass(Lobby, Room), isinstance(lobby1, Room))
