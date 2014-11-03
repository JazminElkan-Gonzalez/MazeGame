from utils import *
from graphics import *

class Level(object):

    game = None

    def __init__(self):
        self._board=self.create_level()
        self._objects = []
        Level.game = self

    def board(self):
        return self._board

    def objects(self):
        return self._objects

# 0 empty
# 1 brick
# 2 ladder
# 3 rope
# 4 gold

    def win(self,window):
        def image (sx,sy,what):
            return Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2),what)
            
        Level.game._board[index(34,0)] = 2
        Level.game._board[index(34,1)] = 2
        Level.game._board[index(34,2)] = 2
        for i in range(3):
            (sx,sy) = screen_pos_index(index(34,i))
            elt = image(sx,sy, "ladder.gif")
            elt.draw(window)

    def create_level(self):
        screen = []
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,0])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        screen.extend([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0])
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1])
        screen.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,2,1,0,0,0,1,2,0,1])
        screen.extend([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,1,1,1,1])
        screen.extend([3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,0,0,0,0,0,0,0,0,2,0,0,0,0,3,3,3,3])
        screen.extend([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0])
        screen.extend([2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1])
        screen.extend([2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,2,3,3,3,3,3,3,3,2])
        screen.extend([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2])
        screen.extend([2,0,0,0,0,0,3,3,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2])
        screen.extend([2,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,2,1,0,0,0,0,3,3,3,2,0,0,1,1,1,1,1,2])
        screen.extend([2,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,2,1,1,1,1,1,1,0,0,2,0,0,1,0,0,0,1,2])
        screen.extend([2,0,1,4,4,1,0,0,1,0,4,4,4,1,0,0,1,2,0,4,4,4,0,1,0,0,2,0,0,1,4,4,4,1,2])
        screen.extend([2,0,1,1,1,1,0,0,1,2,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,2,0,0,1,1,1,1,1,2])
        screen.extend([2,0,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,3,3,3,3,3,3,3,2])
        screen.extend([1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1])
        screen.extend([1,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,2,0,0,0,0,0,0,0,1])
        screen.extend([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        return screen
    
    def create_screen(self,window):
        # use this instead of Rectangle below for nicer screen
        brick = "brick.gif"
        ladder = "ladder.gif"
        rope = "rope.gif"
        gold = "gold.gif"
        pictures = ["blank", brick, ladder, rope, gold]
        def image (sx,sy,what):
            if what != pictures[1]:
                return Image(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2),what)
            else:
                return Brick(Point(sx+CELL_SIZE/2,sy+CELL_SIZE/2), index, window, what)

        for (index,cell) in enumerate(self._board):
            if cell != 0:
                (sx,sy) = screen_pos_index(index)
                elt = image(sx,sy, pictures[cell])
                self._objects.append(elt)
                # elt = Rectangle(Point(sx+1,sy+1),
                #                 Point(sx+CELL_SIZE-1,sy+CELL_SIZE-1))
                # elt.setFill('sienna')
                elt.draw(window)
            else:
                self._objects.append(None)

from brick import *
