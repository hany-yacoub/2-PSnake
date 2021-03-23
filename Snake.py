
#Snake
#==========================================
# Purpose: an object represents an animated snake on the board.
# Instance variables: 
#   -self.x: the snake's x position
#   -self.y: the snake's y position
#   -self.vx: the snake's "x velocity", or how much its horizontal position changes every 100ms(as set by function gameloop). Defaults to 30.
#   -self.vy: the snake's "y velocity", or how much its vertical position changes every 100ms(as set by function gameloop). Defaults to 0.
#   -self.color: the color of the snake
#   -self.canvas: the canvas for animations to appear. Canvas created in SnakeGUI is passed in.
#   -self.snakeid: square representing the first "segment" of the snake.
#   -self.segments: list containing "segments" of the snake as they increase(when the snake eats a pellet) or increase and decrease simulatenously (see the move function documentation).
# Methods:
#   -Constructor: Creates the first segment of the snake and adds it to a list representing the length of the snake.
#   -move: increase the first segments vertical and horizontal position, creates a square, inserts it to the beginning of self.segments, and removes the last square inside self.segments. Essentially "moves" the snake by adding a square in the specified direction and removing the last segment of the snake.
#   -go_down: sets the snake's direction to downwards. Is binded to the "Down" arrow key on the keyboard.
#   -go_up: sets the snake's direction to upwards. Is binded to the "Up" arrow key on the keyboard.
#   -go_left: sets the snake's direction to the left. Is binded to the "Left" arrow key on the keyboard.
#   -go_right: sets the snake's direction to the right. Is binded to the "Right" arrow key on the keyboard.
#==========================================
class Snake:
    def __init__(self, x, y, color, canvas, vx=30, vy=0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.canvas = canvas
        self.snakeid = self.canvas.create_rectangle(self.x, self.y, self.x+30, self.y+30, fill = self.color)
        self.segments = []
        self.segments.append(self.snakeid)
    def move(self):
        self.x += self.vx
        self.y += self.vy
        new_square = self.canvas.create_rectangle(self.x, self.y, self.x+30, self.y+30, fill = self.color)    
        self.segments.insert(0, new_square)
        old_square = self.segments.pop(-1)
        self.canvas.delete(old_square)
    def go_down(self, event):
        self.vx = 0
        self.vy = 30
    def go_up(self, event):
        self.vx = 0
        self.vy = -30
    def go_left(self, event):
        self.vx = -30
        self.vy = 0
    def go_right(self, event):
        self.vx = 30
        self.vy = 0
            
