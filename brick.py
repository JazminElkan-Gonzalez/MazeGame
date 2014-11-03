from graphics import *

class Brick(Image):

    idCount = 0
    imageCache = {} # tk photoimages go here to avoid GC while drawn 
    
    def __init__(self, p, index , window, *pixmap):
        Image.__init__(self, p , *pixmap)
        self.window = window
        self.index = index

    def event(self,q):
        self.draw(self.window)
        Level.game._board[self.index] = 1
        

from level import *
