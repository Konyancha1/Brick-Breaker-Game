# import tkinter library
import tkinter as tk
from tkinter import messagebox  
# import from pygame library
from pygame import mixer 


# Create a parent class for the game objects and canvas
class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    # define a function that takes the position of the items on the canvas
    def get_pos(self):
        return self.canvas.coords(self.item)

    # define a function that takes the movements of the items on the canvas
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    # define the function/method that deletes item on the canvas
    def delete(self):
        self.canvas.delete(self.item)


# create a ball class that inherits attributes(Canvas, position and move) from Game Objects' class
class Ball(GameObject):
    def __init__(self, canvas, x, y):

        # Create the size and shape of the ball, its position on the canvas
        # The direction with which it will move on the canvas and its speed
        self.radius = 5
        self.direction = [-1, 1]
        self.speed = 4
        item = canvas.create_oval(x - self.radius, y - self.radius, x + self.radius, y + self.radius,
                                  fill='mediumvioletred', outline='purple')

        # call the super class method
        super(Ball, self).__init__(canvas, item)

    # create a method/function that updates the position of the ball
    def update(self):
        coords = self.get_pos()
        width = self.canvas.winfo_width()

        # Handles what happens when ball hits the left and right walls of the canvas
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        # Handles what happens when ball hits the bottom and top walls of the canvas
        if coords[1] <= 0 or coords[1] >= 385:
            self.direction[1] *= -1
        # Scale direction vector by the speed of the ball
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        # Moves the ball
        self.move(x, y)

    # create a method/function that define the action/direction and position
    # of the ball after collision
    def collide(self, game_objects):
        coords = self.get_pos()
        x = (coords[0] + coords[2]) * 0.5
        # Takes care of what happens when ball collides with more than one brick
        if len(game_objects) > 1:
            self.direction[1] *= -1
        # Takes care of what happens when ball collides with one brick
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_pos()
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1

        # Takes care of every brick instance that collides with ball
        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit()


# create board class that inherits attributes(Canvas, position and move) from Game Objects' class
class Board(GameObject):
    def __init__(self, canvas, x, y):
        # create a rectangle that will be used as the board, the board takes no ball
        self.width = 60
        self.height = 5
        self.ball = None
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2, x + self.width / 2,
                                       y + self.height / 2, fill='purple', outline='pink')
        super(Board, self).__init__(canvas, item)

    # create a function that will be used to place ball on te canvas, replace the ball when
    # the user misses the ball
    def set_ball(self, ball):
        self.ball = ball

    # Handles movement of the board on the canvas
    def move(self, offset):
        coords = self.get_pos()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Board, self).move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)


# create brick class that inherits attributes(Canvas, position and move) from Game Objects' class
class Brick(GameObject):
    COLORS = {1: 'dark violet', 2: 'purple', 3: 'indigo'}

    def __init__(self, canvas, x, y, hits):
        # create a rectangle that will be used as a brick
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(x - self.width / 2, y - self.height / 2, x + self.width / 2,
                                       y + self.height / 2, fill=color, tags='brick')
        super(Brick, self).__init__(canvas, item)

    # Function that handles what happens if brick is hit
    def hit(self):
        self.hits -= 1
        if self.hits == 0:
            # Brick gets deleted
            self.delete()
        else:
            # Brick changes color
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])


# Create class that starts the game
class Breakout_Game(tk.Frame):
    def __init__(self, master):
        super(Breakout_Game, self).__init__(master)
        # number of lives a user has
        self.lives = 5
        # create canvas which will contain game objects
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='pink', width=self.width, height=self.height, )
        self.canvas.pack()
        self.pack()
        # Empty dictionary to hold items that ball can collide with
        self.items = {}
        self.ball = None

        # create bricks on the canvas
        self.board = Board(self.canvas, self.width / 2, 30)
        self.items[self.board.item] = self.board
        for x in range(5, self.width - 5, 75):
            # Sets the brick positions and number of hits
            self.add_brick(x + 37.5, 180, 3)
            self.add_brick(x + 37.5, 200, 2)
            self.add_brick(x + 37.5, 240, 1)
            self.add_brick(530 + 37.5, 240, 1)
            self.add_brick(5 + 37.5, 260, 3)
            self.add_brick(305 + 37.5, 260, 3)
            self.add_brick(305 + 37.5, 280, 3)
            self.add_brick(305 + 37.5, 300, 3)
            self.add_brick(230 + 37.5, 260, 3)
            self.add_brick(230 + 37.5, 280, 3)
            self.add_brick(230 + 37.5, 300, 3)
            self.add_brick(530 + 37.5, 260, 3)
            self.add_brick(5 + 37.5, 280, 3)
            self.add_brick(530 + 37.5, 280, 3)
            self.add_brick(5 + 37.5, 300, 3)
            self.add_brick(530 + 37.5, 300, 3)
            self.add_brick(x + 37.5, 320, 1)
            self.add_brick(x + 37.5, 360, 2)
            self.add_brick(x + 37.5, 380, 3)

        # Create instance of object before being called
        self.hud = None

        self.setup_game()
        # Sets focus on canvas
        self.canvas.focus_set()
        # Left key on keyboard moves board to the left
        self.canvas.bind('<Left>', lambda _: self.board.move(-10))
        # Right key on keyboard moves board to the right
        self.canvas.bind('<Right>', lambda _: self.board.move(10))

        # Function that exits program
        def close():
            exit()

        quit = tk.Button(self, text='Quit', bg='purple', fg='white', activebackground='pink', font=('Verdana', 10),
                         command=close)
        quit.place(relx=0.87, rely=0.02, relheight=0.11, relwidth=0.11)

    # Function that sets up the game ready for playing
    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 80, '      Press the Enter key to start\nClick the Quit button to quit game')
        self.canvas.bind('<Return>', lambda _: self.start_game())

    # Function to add a ball on the canvas
    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        board_coords = self.board.get_pos()
        x = (board_coords[2] + board_coords[0]) * 0.5
        self.ball = Ball(self.canvas, x, 40)
        self.board.set_ball(self.ball)

    # Function to add a brick on the canvas
    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    # Function that returns a text on the canvas
    def draw_text(self, x, y, text, size='10'):
        font = ('Verdana', size, 'bold')
        return self.canvas.create_text(x, y, text=text, font=font)

    # Shows the number of lives user has at the top left corner of canvas
    def update_lives_text(self):
        text = 'Lives: %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 10)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    # Handles how the game is to start
    def start_game(self):
        # Enter button starts the game
        self.canvas.unbind('<Return>')
        self.canvas.delete(self.text)
        self.board.ball = None
        self.game_loop()

    # Main program loop
    def game_loop(self):
        try:
            self.check_collisions()
            num_bricks = len(self.canvas.find_withtag('brick'))
            # Handles what happens when all bricks are destroyed
            if num_bricks == 0:
                self.ball.speed = None
                self.draw_text(300, 200, 'Great! You break all the balls.')
                # Plays victory sound
                mixer.init()
                win_sound = mixer.Sound('mixkit-huge-crowd-cheering-victory-462.wav')
                win_sound.play()
            # Handles what happens when all lives are used up
            elif self.ball.get_pos()[3] <= 30:
                self.ball.speed = None
                self.lives -= 1
                # Plays victory sound
                mixer.init()
                loss_sound = mixer.Sound('mixkit-losing-bleeps-2026.wav')
                loss_sound.play()
                if self.lives < 0:
                    self.draw_text(300, 200, 'Oops! Game Over!')
                    # Plays losing sound
                    mixer.init()
                    loss_sound = mixer.Sound('mixkit-player-losing-or-failing-2042.wav')
                    loss_sound.play()

                else:
                    self.after(1000, self.setup_game)
            else:
                # Ball position is updated according to direction and speed
                self.ball.update()
                # Creates loop that runs when game is not over
                # Sets timeout of 50 milliseconds before game_loop function is called again
                self.after(50, self.game_loop)
        except FileNotFoundError as e:
            print("Some files are missing")
            response = messagebox.showerror(title='ERROR!',
                                            message="Kindly put the all the files in the same directory")
            if response:
                quit()

    # Checks whether if ball has hit bricks
    def check_collisions(self):
        ball_coords = self.ball.get_pos()
        # List of colliding items
        items = self.canvas.find_overlapping(*ball_coords)
        # Filters out objects that cannot collide with the ball
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)


# Function that runs the program
def play():
    root = tk.Tk()
    root.title('Beginner')
    beginner_level = Breakout_Game(root)
    beginner_level.mainloop()


# Call the function
play()
