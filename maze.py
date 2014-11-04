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





MOVE = {
    'Left': (-1,0),
    'Right': (1,0),
    'Up' : (0,-1),
    'Down' : (0,1)
}

# 0 empty
# 1 brick
# 2 ladder
# 3 rope
# 4 gold
# 5 winladder
# 6 winspace
# p player
# b baddie


def main (levelNum):
    levelLayout = []
    totalLevels = 0
    with open('levels.txt') as inputfile:
        # for allLine in inputfile:
        #     if allLine == "\n":
        #         totalLevels = totalLevels + 1
        # if levelNum == totalLevels+1:
        #     exit(0)
        levelN = 0
        bQuantity = 0
        # print "here"
        # print inputfile
        for line in inputfile:
            # print "line!!"
            if line == "\n":
                levelN = levelN + 1
            if levelN == levelNum:
                line = line.replace(",","").strip()
                for block in line:
                    try:
                        block = int(block)
                    except:
                        pass
                    if block == 'b':
                        bQuantity = bQuantity + 1
                    levelLayout.append(block)
    if levelLayout == []:
        exit(0)

    window = GraphWin("Maze", WINDOW_WIDTH+20, WINDOW_HEIGHT+20)

    rect = Rectangle(Point(5,5),Point(WINDOW_WIDTH+15,WINDOW_HEIGHT+15))
    rect.setFill('sienna')
    rect.setOutline('sienna')
    rect.draw(window)
    rect = Rectangle(Point(10,10),Point(WINDOW_WIDTH+10,WINDOW_HEIGHT+10))
    rect.setFill('white')
    rect.setOutline('white')
    rect.draw(window)

    Eq = Queue()
    sx, sy = screen_pos_index(index(17,18))
    levelLayoutCopy = levelLayout[:]
    exitPos = levelLayout.index(6)

    lol = Level(levelLayout)

    level = lol.create_level(levelLayout)
    screen = lol.create_screen(window)

    if 'p' in levelLayoutCopy:
        pIndex = levelLayoutCopy.index('p')
        x,y = index_xy(pIndex)
        sx, sy = screen_pos_index(pIndex)
        p = Player(x,y,window)
        levelLayout[pIndex] = 0
        levelLayoutCopy[pIndex] = 0

    if 'b' in levelLayoutCopy:
        for i in range(bQuantity):
            bIndex = levelLayoutCopy.index('b')
            sx, sy = screen_pos_index(bIndex)
            x,y = index_xy(bIndex)
            b = Baddie(x,y,window,p,5,Eq)
            levelLayout[bIndex] = 0
            levelLayoutCopy[bIndex] = 0

    while not p.at_exit(exitPos):
        key = window.checkKey()
        if key == 'q':
            window.close()
            exit(0)
        if key == 'a' or key == 'z':
            p.dig(key, Eq)
        if 4 in lol.board():
            lol.win(window)
        if key in MOVE:
            (dx,dy) = MOVE[key]
            p.move(dx,dy)
        if lol._board[index(p.x(), p.y())] == 1:
            lost(window) 
        time.sleep(0.03)
        Eq.dequeue_if_ready(window)
        # baddies should probably move here

    won(window)
    try:
        main(levelNum+1)
    except:
        exit(0)

if __name__ == '__main__':
    main(0)
