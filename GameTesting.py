# Import unittest library
import unittest


# Create class for all functions to be used in the game
class GameObject(object):
    def __init__(self):
        # Initialize value of the functions to False
        self.move = False
        self.delete = False
        self.get_pos = False

    # Function to get position of object
    def get_position(self):
        # Reinitialize value of the function to True
        self.get_pos = True
        print("Gets position of object")

    def moving(self):
        # Reinitialize value of the function to True
        self.move = True
        print("Function for object to move")

    def deleting(self):
        # Reinitialize value of the function to True
        self.delete = True
        print("Function to delete object")


# Create class to hold Ball object attributes and methods
class Ball(GameObject):
    def __init__(self):
        # Initialize value of the functions to False
        super(GameObject, self).__init__()
        self.collide = False
        self.update = False

    def updating(self):
        # Reinitialize value of the function to True
        print("Took care of what happens when ball bounces off canvas wall")
        self.update = True

    def colliding(self):
        # Reinitialize value of the function to True
        print("Took care of what happens when ball hits game object")
        self.collide = True

# Create class to hold Board object attributes and methods
class Board(GameObject):
    def __init__(self):
        # Initialize value of the functions to False
        super(GameObject, self).__init__()
        self.set_ball = False
        self.board_move = False

    # Function to add ball on the board  
    def sets_ball(self):
        # Reinitialize value of the function to True
        print("Ball is on board")
        self.set_ball = True

    # Function to move board
    def board_moves(self):
        # Reinitialize value of the function to True
        print("Board moves")
        self.board_move = True


# Create class to hold Brick object attributes and methods
class Brick(GameObject):
    def __init__(self):
        # Initialize value of the function to False
        super(GameObject, self).__init__()
        self.hit = False

    def hits(self):
        # Reinitialize value of the function to True
        """
        self.hit takes care of number of hits on a brick
        self.deleting takes care when the number of hits left on a brick are zero 
        """
        self.hit = True
        print("If number of hits left on a brick are zero, brick gets deleted")
        self.deleting()
        print("If number of hits left on a brick are not zero, brick changes color")


# Create class to hold Ball object attributes and methods
class BreakoutGame(object):
    def __init__(self, Text=None):
        # Initialize the objects here as well as functions with value False
        self.text = Text
        self.ball = Board()
        self.board = Board()
        self.brick = Brick()
        self.collision = False
        self.game_start = False
        self.game_run = False
        self.lives = False
        self.game = False

    # Function to handle game setup
    def setup_game(self):
        # Add ball to the game
        ball = self.add_ball()
        ball.sets_ball()
        print("Adding ball")
        # Show text informing player number of lives in the game
        self.update_lives_text()
        # Reinitialize function to True
        self.game = True

    # Function to handle how game runs
    def game_loop(self):
        print("If there are no bricks left")
        text = "Winner"
        # Display text when player has won game
        self.draw_text(text)
        print("If all number of lives are used up")
        text = "Loser"
        # Display text when player has lost the game
        self.draw_text(text)
        # Reinitialize value of function to True
        self.game_run = True

    # Function to handle how game starts
    def start_game(self):
        print("Game started")
        # Reinitialized value of function to True
        self.game_start = True

    # Function to handle if object hit is a brick
    def check_collision(self):
        print("It is a brick that has been hit")
        # Reinitialized value of function to True
        self.collision = True

    # Function to add ball to game
    def add_ball(self):
        return self.ball

    # Function to add brick to game
    def add_brick(self):
        return self.brick

    # Function to show text within the game
    def draw_text(self, text):
        print("(draw_text function prints out text when called)")
        print(text)

    # Function to show user number of lives left throughout the game
    def update_lives_text(self):
        text = "You have X number of lives"
        self.draw_text(text)
        # Reinitialized value of function to True
        self.lives = True


# Class to conduct the testcase scenarios
# The Expected statements are meant to show what is expected once the function is called
class TestGame(unittest.TestCase):
    # Testing the move function in GameObject class
    def test_move_function(self):
        c = GameObject()
        c.moving()
        self.assertTrue(c.move, 'Expected Function for object to move')

    # Testing the deleting function in GameObject class
    def test_delete_function(self):
        c = GameObject()
        c.deleting()
        self.assertTrue(c.delete, 'Expected Function to delete object')

    # Testing the get pos function in GameObject class
    def test_get_position_function(self):
        c = GameObject()
        c.get_position()
        self.assertTrue(c.get_pos, 'Expected Gets position of object')

    # Testing the updating function in Ball class
    def test_ball_reaction_on_hitting_wall(self):
        c = Ball()
        c.updating()
        self.assertTrue(c.update, 'Expected Took care of what happens when ball bounces off canvas wall')

    # Testing the colliding function in Ball class
    def test_ball_reaction_on_colliding_game_objects(self):
        c = Ball()
        c.colliding()
        self.assertTrue(c.collide, 'Expected Took care of what happens when ball hits game object')

    # Testing the board move function in Board class
    def test_how_board_moves(self):
        c = Board()
        c.board_moves()
        self.assertTrue(c.board_move, 'Expected Board moves')

    # Testing the set ball function in Board class
    def test_ball_position_on_board(self):
        c = Board()
        c.sets_ball()
        self.assertTrue(c.set_ball, 'Expected Ball is on Board')

    # Testing the hit function in Brick class
    def test_brick_hit(self):
        c = Brick()
        c.hits()
        self.assertTrue(c.hit, 'Expected If number of hits left on a brick are zero, brick gets deleted'
                               'If number of hits left on a brick are not zero, brick changes color')

    # Testing the start game function in BreakoutGame class
    def test_how_game_starts(self):
        c = BreakoutGame()
        c.start_game()
        self.assertTrue(c.game_start, 'Expected Game Started')

    # Testing the add ball function in BreakoutGame class
    def test_how_ball_added(self):
        c = BreakoutGame()
        ball = c.add_ball()
        self.assertEqual(c.ball, ball, 'Expected ball to be added')

    # Testing the add brick function in BreakoutGame class
    def test_how_brick_added(self):
        c = BreakoutGame()
        brick = c.add_brick()
        self.assertEqual(c.brick, brick, 'Expected brick to be added')

    # Testing the check collision function in BreakoutGame class
    def test_how_collision_happens(self):
        c = BreakoutGame()
        c.check_collision()
        self.assertTrue(c.collision, 'Expected It is a brick that has been hit')

    # Testing the game loop function in BreakoutGame class
    def test_how_game_runs(self):
        c = BreakoutGame()
        c.game_loop()
        self.assertTrue(c.game_run, 'Expected If there are no bricks left, Winner, '
                                    'If all number of lives are used up, Loser')

    # Testing the update lives function in BreakoutGame class
    def test_how_lives_updated(self):
        c = BreakoutGame()
        c.update_lives_text()
        self.assertTrue(c.lives, 'Expected You have X number of lives')

    # Testing the setup function in BreaoutGame class
    def test_game_setup(self):
        c = BreakoutGame()
        c.setup_game()
        self.assertTrue(c.game, 'Expected Ball is on board, Adding ball, '
                                '(draw_text function prints out text when called),'
                                'You have X number of lives')


# Call the main function
if __name__ == '__main__':
    unittest.main()
