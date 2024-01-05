from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0,260)
        self.Score = 0
        self.color('white')
        self.update_score()
        
        
    
    def update_score(self):
        self.write(f'Score: {self.Score}', False, align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, align='center', font=('Courier', 24, 'normal'))

    
    def increased_score(self):
        self.Score += 1
        self.clear()
        self.update_score()
        
        
