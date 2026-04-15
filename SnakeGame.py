import curses
import random

game_width = 25
game_height = 20

def newFruitPosition():
    fruitPosition = (0, 0)
    
    fruitPosition_Y = random.randint(0,game_height-1)
    fruitPosition_X = random.randint(0,game_width-1)

    fruitPosition = (fruitPosition_Y, fruitPosition_X)
    return fruitPosition

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(150)

    position = [game_height //2, game_width //2]
    fruitPosition = [game_height //2, game_width //2 + 5]
    direction = (0,1)
    gameOn = True
    isFruit = False

    while(gameOn):
        stdscr.clear()

        for y in range(game_height):
            for x in range(game_width):
                if [y, x] == position:
                    stdscr.addstr(y, x*3, "[O]")
                else:
                    stdscr.addstr(y, x*3, "[ ]")
                if position == fruitPosition:
                    isFruit = False
                    stdscr.addstr(fruitPosition[0], fruitPosition[1]*3, "[ ]")
                    
        if isFruit:
            stdscr.addstr(fruitPosition[0], fruitPosition[1]*3, "[X]")
        else:
            fruitPosition[:] = newFruitPosition()
            stdscr.addstr(fruitPosition[0], fruitPosition[1]*3, "[X]")
            isFruit = True

                    
        stdscr.refresh()

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

        position[0] = max(0, min(game_height - 1, position[0]))
        position[1] = max(0, min(game_width - 1, position[1]))

curses.wrapper(main)
