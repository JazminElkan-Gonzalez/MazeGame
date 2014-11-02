from utils import *
from graphics import *
from level import *

class Character (object):
    def __init__ (self,pic,x,y,window):
        (sx,sy) = screen_pos(x,y)
        self._img = Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2+2),pic)
        self._window = window
        self._img.draw(window)
        self._x = x
        self._y = y

    def same_loc (self,x,y):
        return (self._x == x and self._y == y)

# 0 empty
# 1 brick
# 2 ladder
# 3 rope
# 4 gold

    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx >= 0 and ty >= 0 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if Level.game._board[index(tx,ty)] == 0:    #empty
                self._x = tx
                self._y = ty
                self._img.move(dx*CELL_SIZE,dy*CELL_SIZE)
            if Level.game._board[index(tx,ty)] == 4:    #gold
                Level.game._objects[index(tx,ty)].undraw()
                Level.game._board[index(tx,ty)] = 0
                self._x = tx
                self._y = ty
                self._img.move(dx*CELL_SIZE,dy*CELL_SIZE)

                