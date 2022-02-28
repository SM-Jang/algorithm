from time import ctime


class MyHome:
    def __init__(self, strAddress):
        self.colorRoof = 'red'
        self.stateDoor = 'closed'
        print('Build on', strAddress)
        print('Build at', ctime())

    def paintRoof(self, color):
        self.colorRoof = color

    def openDoor(self):
        self.stateDoor = 'open'

    def closedDoor(self):
        self.stateDoor = 'closed'

    def printStatus(self):
        print('Roof color is', self.colorRoof,
              ', and door is', self.stateDoor)

    def __del__(self):
        print('Destroyed at', ctime())

