from SetupScreen import WINDOW_WIDTH, WINDOW_HEIGHT, X_INIT, Y_INIT
from curses import KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT # Constants which are interpreted as the corresponding key presses
import curses
import random
import os

# Map each direction to the curses enumeration, and the reverse of the direction
DIRECTIONS = {'Up':[KEY_UP, 'Down'],
              'Down':[KEY_DOWN, 'Up'],
              'Right':[KEY_RIGHT, 'Left'],
              'Left':[KEY_LEFT, 'Right']}

class Snake(object):

    def __init__(self, Window, char = '=', init_length = 5):

        ''' Initialise snake with the following
        attributes '''

        # Create the head of the snake
        self.body = ['0']

        # Game score is initially zero
        self.score = 0

        # Define window object
        self.Window = Window

        # Append 4 body elements to head of the snake
        for x in range(0,init_length - 1):
            self.body.append(char)

        # Set the initial coordinates if the head of the snake
        self.x_coord, self.y_coord = X_INIT, Y_INIT

        # Set the initial direction of the snake randomly (string)
        self.direction = list(DIRECTIONS.keys())[random.randint(0, 3)]

        # Set the head coordinate within the body list
        self.list_coords = [(self.x_coord, self.y_coord)]
        # Set the list of body coordinates for the snake
        if self.direction == 'Up':
            for pos in range(1,init_length):
                self.list_coords.append((self.x_coord, self.y_coord + pos))
        elif self.direction == 'Down':
            for pos in range(1,init_length):
                self.list_coords.append((self.x_coord, self.y_coord - pos))
        elif self.direction == 'Right':
            for pos in range(1,init_length):
                self.list_coords.append((self.x_coord - pos, self.y_coord))
        elif self.direction == 'Left':
            for pos in range(1,init_length):
                self.list_coords.append((self.x_coord + pos, self.y_coord))

    def move(self, grow =False, char = '='):

        ''' Method to update the coordinates of the body when moving '''

        # Update the head position
        if self.direction == 'Up':
            self.x_coord , self.y_coord = self.x_coord , self.y_coord - 1
        elif self.direction == 'Down':
            self.x_coord , self.y_coord = self.x_coord , self.y_coord + 1
        elif self.direction == 'Right':
            self.x_coord , self.y_coord = self.x_coord + 1, self.y_coord
        elif self.direction == 'Left':
            self.x_coord , self.y_coord = self.x_coord - 1, self.y_coord

        # Add the new head position to the front of the list of coordinates
        self.list_coords.insert(0,self.head_coords)

        # Remove the final coordinate from the list of coordinates
        if grow:
            self.body.append(char)
        else:
            self.list_coords.pop()

    def draw(self):

        ''' Draw the Snake on the screen '''
        for element,i in enumerate(S.body):
            self.Window.addstr( , S.list_coords, element)


                len(self.body)



    def grow(self):

        ''' Add another element to the list of elements
        in the body of the snake '''

        self.body.append(self.body[-1])

    @property
    def head_coords(self):
        return (self.x_coord, self.y_coord)

    @property
    def game_score(self):
        return ''.join((' Game Score: ', str(self.score), ' '))



class Food(object):

    def __init__(self, Window, Snake, char = '*'):

        ''' Initialise food with the following
        attributes '''

        self.char = char

        # Define snake object
        self.Snake = Snake

        # Define window object
        self.Window = Window

        self.reposition()

    def draw(self):

        ''' Draw the Food on the screen '''

        self.Window.addstr(self.y_coord, self.x_coord, self.char)



    def reposition(self):

        ''' Reset the position of the food '''

        make_rand = lambda x: random.randint(0, x)
        while True:
            (self.x_coord, self.y_coord) = map(make_rand, [WINDOW_WIDTH, WINDOW_HEIGHT])
            if (self.x_coord, self.y_coord) not in self.Snake.list_coords:
                # If not setting the position of the food to a position of the snake body
                break
    @property
    def food_coords(self):
        return (self.x_coord, self.y_coord)
