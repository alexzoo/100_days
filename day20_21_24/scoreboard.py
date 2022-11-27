from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.score = 0
        self.high_score = self.read_score_from_file()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(
            f'Score: {self.score} High Score: {self.high_score}', align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score_to_file()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def read_score_from_file(self):
        with open('day20_21/data.txt', mode='r') as file:
            score = int(file.read())
            return score

    def write_score_to_file(self):
        with open('day20_21/data.txt', mode='w') as file:
            file.write(f'{self.score}')
