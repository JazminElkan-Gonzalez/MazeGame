from character import *
from utils import *
import math
import random


class Baddie (Character):

    def __init__ (self,x,y,window,player, baddie_Delay, q):
        Character.__init__(self,'red.gif',x,y,window)
        self._player = player
        self.delay = baddie_Delay
        q.enqueue(baddie_Delay,self)

    def event(self,q):
        sX = self.x()
        pX = self._player.x()
        sY = self.y()
        pY = self._player.y()
        if sX == pX and sY == pY:
            lost(self._window)
        else:
            x = random.randrange(2)
            if (x == 0 and (pX-sX) != 0) or (pY-sY) == 0:
                self.move(int(math.copysign(1,pX-sX)), 0) 
            elif (x == 1 and (pY-sY) != 0) or (pX-sX) == 0:
                self.move(0 , int(math.copysign(1,pY-sY)))

        # enqueue next event for the baddie, another move
        q.enqueue(self.delay,self)

