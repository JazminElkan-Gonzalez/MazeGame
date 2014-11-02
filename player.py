from character import *
from utils import *
from level import *

class Player (Character):
    def __init__ (self,x,y,window):
        Character.__init__(self,'android.gif',x,y,window)

    def at_exit (self):
        return (self._y == 0)

    def dig(self, key):
        xDict = {'a':-1, 'z':1}
        brickY = self._y+1
        brickX = self._x+xDict[key]
        if Level.game._board[index(brickX, brickY)] == 1 and Level.game._board[index(brickX, self._y)] == 0:
            Level.game._objects[index(brickX,brickY)].undraw()
            Level.game._board[index(brickX,brickY)] = 0