from character import *
from utils import *


class Baddie (Character):
    def __init__ (self,x,y,window,player):
        Character.__init__(self,'red.gif',x,y,window)
        self._player = player

