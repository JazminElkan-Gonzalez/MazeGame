from character import *
from utils import *
from level import *

class Player (Character):
    def __init__ (self,x,y,window):
        Character.__init__(self,'android.gif',x,y,window)

    def at_exit_old (self):
        return (self._y == 0)

    def at_exit (self,exitPos):
        return (index(self._x,self._y) == exitPos)

    def dig(self, key, q):
        xDict = {'a':-1, 'z':1}
        brickY = self._y+1
        brickX = self._x+xDict[key]
        if Level.game._board[index(brickX, brickY)] == 1 and Level.game._board[index(brickX, self._y)] == 0:
            Level.game._objects[index(brickX,brickY)].undraw()
            Level.game._board[index(brickX,brickY)] = 0
            q.enqueue(50,Level.game._objects[index(brickX,brickY)])

            
    def move (self,dx,dy):
        tx = self._x + dx
        ty = self._y + dy
        if tx >= 0 and ty >= 0 and tx < LEVEL_WIDTH and ty < LEVEL_HEIGHT:
            if Level.game._board[index(tx,ty)] == 0:    #empty
                if Level.game._board[index(self._x,self._y)] == 2:
                    self._y = ty
                    self._img.move(0,dy*CELL_SIZE)
                if Level.game._board[index(tx,ty+1)] == 0 or Level.game._board[index(tx,ty+1)] == 3:
                    for i in xrange(LEVEL_HEIGHT-ty):
                        if Level.game._board[index(tx,ty+i)] != 0:
                            if Level.game._board[index(tx,ty+i)] == 3:
                                self._img.move(0, (dy+i)*CELL_SIZE)
                                self._y = ty + i
                            elif Level.game._board[index(tx,ty+i)] == 4:
                                Level.game._objects[index(tx,ty+i)].undraw()
                                Level.game._board[index(tx,ty+i)] = 0
                                self._img.move(0, (dy+i)*CELL_SIZE)
                                self._y = ty + i
                            else:
                                self._img.move(0, (dy+i-1)*CELL_SIZE)
                                self._y = ty + i - 1
                            break
                        if ty+i == LEVEL_HEIGHT-1:
                            self._img.move(0, (dy+i)*CELL_SIZE)
                            self._y = ty + i
                            break

                self._x = tx
                self._img.move(dx*CELL_SIZE,0)
            if Level.game._board[index(tx,ty)] == 1:    #brick
                pass
            if Level.game._board[index(tx,ty)] == 2:    #ladder
                self._x = tx
                self._y = ty
                self._img.move(dx*CELL_SIZE,dy*CELL_SIZE)
            if Level.game._board[index(tx,ty)] == 3:    #rope
                self._x = tx
                self._y = ty
                self._img.move(dx*CELL_SIZE,dy*CELL_SIZE)
            if Level.game._board[index(tx,ty)] == 4:    #gold
                Level.game._objects[index(tx,ty)].undraw()
                Level.game._board[index(tx,ty)] = 0
                self._x = tx
                self._y = ty
                self._img.move(dx*CELL_SIZE,dy*CELL_SIZE)
