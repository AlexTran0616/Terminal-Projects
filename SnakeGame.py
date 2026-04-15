import curses
import random

game_width = 25
game_height = 20

def fruit():
    fruitPosition = (0, 0)
    
    fruitPosition_Y = random.randint(0,24)
    fruitPosition_X = random.randint(0,24)

    fruitPosition = (fruitPosition_Y, fruitPosition_X)
    return fruitPosition

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    position = [game_height //2, game_width //2]
    direction = (0,1)
    gameOn = True

    while(gameOn):
        stdscr.clear()
        for y in range(game_height):
            for x in range(game_width):
                if [y, x] == position:
                    stdscr.addstr(y, x*3, "[O]")
                else:
                    stdscr.addstr(y, x*3, "[ ]")
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
fruit()