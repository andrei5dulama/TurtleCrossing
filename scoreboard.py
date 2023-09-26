from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.level = 1
        self.scoreboard_update()

    def scoreboard_update(self):
        self.write(f'Level = {self.level}', align='left', font=FONT)


    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write('GAME OVER', align='center' , font=FONT)

    def what_level(self):
        self.clear()
        self.level += 1
        self.scoreboard_update()
