import curses
import random
import numpy as np

game_width = 20
game_height = 20
def newFruitPosition():
    fruitPosition = (0, 0)
    
    fruitPosition_Y = random.randint(1,game_height-1)
    fruitPosition_X = random.randint(1,game_width-1)

    fruitPosition = (fruitPosition_Y, fruitPosition_X)
    return fruitPosition

def zeros(list, y, x):
    for i in range(y):
        for j in range(x):
            list.append(0)
    return list

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(150)

    position = [game_height //2, game_width //2]
    previousPositionX = []
    previousPositionY = []

    fruitPosition = [game_height, game_width]

    zeros(previousPositionX, game_height, game_width)
    zeros(previousPositionY, game_height, game_width)

    direction = (0,1)
    points = 0

    gameOn = True
    isFruit = False
    
    while(gameOn):
        stdscr.clear()

        for y in range(game_height+1):
            for x in range(game_width+1): 
                if [y, x] == position:
                    stdscr.addstr(y, x*3, ("   "), curses.A_STANDOUT)
                elif y == 0 or y == game_height or x == 0 or x == game_width:
                    stdscr.addstr(y, x*3, ("   "), curses.A_STANDOUT)
                else:
                    stdscr.addstr(y, x*3, "   ")
                if points > 0:
                    for i in range(points):
                        stdscr.addstr(previousPositionY[game_height*game_width - i - 1], previousPositionX[game_width*game_height - i - 1]*3, ("   "), curses.A_STANDOUT)
                        if position == [previousPositionY[game_height*game_width - i - 1], previousPositionX[game_width*game_height - i - 1]]:
                            gameOn = False

        if position == fruitPosition:
            isFruit = False
            points = points + 1
            stdscr.addstr(fruitPosition[0], fruitPosition[1]*3, "   ", curses.A_STANDOUT)

        stdscr.addstr(game_height + 1, 1, f"points: {points}")
        previousPositionX.append(position[1])        
        previousPositionY.append(position[0])     

        if len(previousPositionX) > game_height * game_width:
            previousPositionX.pop(0);
        if len(previousPositionY) > game_height * game_width:
            previousPositionY.pop(0);
        
        if isFruit:
            stdscr.addstr(fruitPosition[0], fruitPosition[1]*3, " X ")
        else:
            fruitPosition[:] = newFruitPosition()
            stdscr.addstr(fruitPosition[0], fruitPosition[1]*3, " X ")
            isFruit = True


        key = stdscr.getch()
        if key == ord('x'):
            gameOn = False

        if key == ord('w'):
            direction = (-1, 0)
        elif key == ord('a'):
            direction = (0, -1)
        elif key == ord('s'):
            direction = (1, 0)
        elif key == ord('d'):
            direction = (0, 1)


        position[0] += direction[0]
        position[1] += direction[1]

        if position[0] != max(1, min(game_height - 1, position[0])):
            gameOn = False

        if position[1] != max(1, min(game_width - 1, position[1])):
            gameOn = False

curses.wrapper(main)
