#Hany Yacoub
import tkinter as tk, random
from Snake import Snake
from EnemySnake import EnemySnake

#SnakeGui
#==========================================
# Purpose: This class represents the game instance running.
# Instance variables:
#   -self.win: the window running the game.
#   -self.canvas: a tk Canvas object where shapes will be animated.
#   -self.gameover: Boolean representing if game is over. Controls when program should be stopped.
#   -self.atefood: Boolean representing whether a Snake object ate food on its last move. Used to differentiate between snake eating and hitting its own body.
#   -self.board: A rectangle to show the area where the snake can be. If snake goes out of bounds of self.board, self.gameover becomes True and game stops.
#   -self.snake1: Snake object representing player snake
#   -self.snake2: Snake object represnting enemy snake
# Methods:
#   -Constructor: creates window of 660x660 pixels, with rectangle inside of 630x630 pixels. Creates two snake objects. Keeps window in focus if game is restarted. Runs functions gameloop and createfood.
#   -gameloop: main animating function. Calls the move function on each snake object to begin animation and recursively calls itself every 100 ms. contains actions of snakes eating food, hitting walls, hitting own bodies, or hitting each other.
#   -restart: restarts the game if the key 'r' is pressed on the keyboard.
#   -create_food: creates a food pellet randomly on the board. Is called repeatedly whenever a pellet is eaten.
#==========================================
class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Snake but much cooler")
        self.win.focus_force()
        self.canvas = tk.Canvas(self.win, width = 660, height = 660)
        self.canvas.pack()
        self.gameover = False
        self.atefood = False
        self.board = self.canvas.create_rectangle(30, 30, 630, 630)
        self.snake1 = Snake(330, 330, 'green', self.canvas)
        self.snake2 = EnemySnake(120, 270, 'black', self.canvas)
        self.create_food()
        self.win.bind('<Down>',self.snake1.go_down)
        self.win.bind('<Up>',self.snake1.go_up)
        self.win.bind('<Left>',self.snake1.go_left)
        self.win.bind('<Right>',self.snake1.go_right)
        self.win.bind('r', self.restart)
        self.gameloop()
    def gameloop(self):
        self.atefood = False
        self.snake1.move()
        self.snake2.move()
        self.snake2.chase_food(self.foodxpos, self.foodypos)
        
        #Eating Food
        if self.snake1.x == self.foodxpos and self.snake1.y == self.foodypos: #player eating food
            self.atefood = True
            self.canvas.delete(self.food)
            new_square = self.snake1.canvas.create_rectangle(self.snake1.x, self.snake1.y,
                                                             self.snake1.x+30, self.snake1.y+30,
                                                             fill = self.snake1.color)
            self.snake1.segments.append(new_square)
            self.create_food()
        elif self.snake2.x == self.foodxpos and self.snake2.y == self.foodypos: #enemy eating food
            self.canvas.delete(self.food)
            new_square = self.snake2.canvas.create_rectangle(self.snake2.x, self.snake2.y,
                                                             self.snake2.x+30, self.snake2.y+30,
                                                             fill = self.snake2.color)
            self.snake2.segments.append(new_square)
            self.create_food()
        #Hitting the Walls
        if not (0 < self.snake1.x < 630) or not (0 < self.snake1.y < 630):
            self.gameover = True
            self.canvas.delete('all')
            w = tk.Label(self.win, text="Game Over! Your Score: " + str(len(self.snake1.segments)))
            w.pack()
        #Player head hitting own body
        for i in range(1, len(self.snake1.segments)):
            if not self.gameover and not self.atefood and self.snake1.x == self.canvas.coords(self.snake1.segments[i])[0] and self.snake1.y == self.canvas.coords(self.snake1.segments[i])[1]:
                self.gameover = True
                self.canvas.delete('all')
                w = tk.Label(self.win, text="Game Over! Your Score: " + str(len(self.snake1.segments)))
                w.pack()
        #Player head hitting enemy snake body
        for i in range(1, len(self.snake2.segments)):
            if not self.gameover and not self.atefood and self.snake1.x == self.canvas.coords(self.snake2.segments[i])[0] and self.snake1.y == self.canvas.coords(self.snake2.segments[i])[1]:
                self.gameover = True
                self.canvas.delete('all')
                w = tk.Label(self.win, text="Game Over! Your Score: " + str(len(self.snake1.segments)))
                w.pack()
        #Enemy head hitting player body
        for i in range(1, len(self.snake1.segments)):
            if not self.gameover and not self.atefood and self.snake2.x == self.canvas.coords(self.snake1.segments[i])[0] and self.snake2.y == self.canvas.coords(self.snake1.segments[i])[1]:
                self.gameover = True
                self.canvas.delete('all')
                w = tk.Label(self.win, text="Game Over! Your Score: " + str(len(self.snake1.segments)))
                w.pack()
                
        if not self.gameover:
            self.canvas.after(100, self.gameloop)
    
    def restart(self, event):
        #if self.gameover == True:
        self.win.destroy()
        SnakeGUI()
    def create_food(self):
        self.foodxpos = random.randrange(30, 629, 30)
        self.foodypos = random.randrange(30, 629, 30)
        self.food = self.canvas.create_oval(self.foodxpos, self.foodypos, self.foodxpos+30, self.foodypos+30, fill='red')

SnakeGUI()
tk.mainloop()
