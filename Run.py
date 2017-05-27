from Classes import Snake, Food
from SetupScreen import WINDOW_HEIGHT, WINDOW_WIDTH, setup_window
import curses

W = setup_window()
S = Snake(Window = W)
F = Food(Window = W, Snake = S)
i = 0
while True:
    i+=1

    W.clear()

    W.border(0)

    # Write the game score on the screen
    W.addstr(WINDOW_HEIGHT-1,int(WINDOW_WIDTH*1/10),S.game_score)

    W.getch()
    if i>10:
        break

print("{}".format(S.head_coords))
curses.endwin()
