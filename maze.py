#
# MAZE
# 
# Example game
#
# Version without baddies running around
#

from level import *
from character import *
from graphics import *
from player import *
from baddie import *
from utils import *
from queue import *



def won (window):
    t = Text(Point(WINDOW_WIDTH/2+10,WINDOW_HEIGHT/2+10),'YOU WON!')
    t.setSize(36)
    t.setTextColor('red')
    t.draw(window)
    window.getKey()
    exit(0)

MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}


def main ():
    lol = Level()
    window = GraphWin("Maze", WINDOW_WIDTH+20, WINDOW_HEIGHT+20)

    rect = Rectangle(Point(5,5),Point(WINDOW_WIDTH+15,WINDOW_HEIGHT+15))
    rect.setFill('sienna')
    rect.setOutline('sienna')
    rect.draw(window)
    rect = Rectangle(Point(10,10),Point(WINDOW_WIDTH+10,WINDOW_HEIGHT+10))
    rect.setFill('white')
    rect.setOutline('white')
    rect.draw(window)

    level = lol.create_level()

    screen = lol.create_screen(window)
    Eq = Queue()
    p = Player(17,18,window)
    baddie1 = Baddie(19,2,window,p,5, Eq)
    baddie2 = Baddie(19,7,window,p,5, Eq)
    baddie3 = Baddie(24,18,window,p,5, Eq)
    print Eq.queue
    while not p.at_exit():
        key = window.checkKey()
        if key == 'q':
            window.close()
            exit(0)
        if key == 'a' or key == 'z':
            p.dig(key)
        if 4 not in lol.board():
            lol.win(window)
        if key in MOVE:
            (dx,dy) = MOVE[key]
            p.move(dx,dy)
        time.sleep(0.05)
        Eq.dequeue_if_ready()
        # baddies should probably move here

    won(window)

if __name__ == '__main__':
    main()
