from character import *
from utils import *

class Player (Character):
    def __init__ (self,x,y,window):
        Character.__init__(self,'android.gif',x,y,window)

    def at_exit (self):
        return (self._y == 0)

