from Snake import Snake
#EnemySnake        
#==========================================
# Purpose: An object represnts an enemy snake.
# Instance variables: Inherits all instance variables for class Snake. See documentation.
# Methods: Inherits all but one method from class Snake. See documentation.
#   -chase_food: While player snake is controlled by user, EnemySnake chases food pellets automatically. Takes in foodxpos and foodypos, which represent the current food pellet's location. Comparisons keep the object following food pellets.
#==========================================     
class EnemySnake(Snake):
    def chase_food(self, foodxpos, foodypos):
        self.foodx = foodxpos
        self.foody = foodypos
        if self.x < self.foodx:
            self.vx = 30
            self.vy = 0
        elif self.x > self.foodx:
            self.vx = -30
            self.vy = 0
        if self.y < self.foody:
            self.vx = 0
            self.vy = 30
        elif self.y > self.foody:
            self.vx = 0
            self.vy = -30
