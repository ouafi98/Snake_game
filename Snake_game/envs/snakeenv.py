from typing import Any, SupportsFloat
import gymnasium as gym
from gymnasium import spaces
from turtle import Screen


from Snake_game.utils.snake import Snake
from Snake_game.utils.food import Food
from Snake_game.utils.scoreboard import Scoreboard
import time
import numpy as np
from PIL import ImageGrab, Image
import io

FPS = 10 

class SnakeWorldEnv(gym.Env):

    def __init__(self):

        # Observation is a screenshot of the current state of the game
        self.observation_space = spaces.Box(0, 255, (600,600,3), np.uint8)

        # We have 4 actions, corresponding to "right", "up", "left", "down"
        self.action_space = spaces.Discrete(4)

        self._action_to_direction = {
            0: "up",
            1: "down",
            2: "left",
            3: "right",
        }



        self.screen = Screen()
        self.screen.setup(width=600, height=600, startx=0, starty=0)
        self.screen.bgcolor("black")
        self.screen.title("My snake game")
        self.screen.tracer(0)

        random_x = np.random.randint(-280, 280)
        random_y = np.random.randint(-280, 280)

        self.snake = Snake((random_x, random_x))
        self.food = Food()
        self.scoreboard = Scoreboard()
    
    def step(self, action):
        direction = self._action_to_direction[action]

        if direction == "up":
            self.snake.up()

        if direction == "down":
            self.snake.down()

        if direction == "left":
            self.snake.left()

        if direction == "right":
            self.snake.right()

        # apply action
        self.snake.move()


        # reward
        reward = 0

        # Detect collision with food
        if self.snake.head.distance(self.food) < 15:
            self.food.refresh()
            self.snake.extend()
            self.scoreboard.increased_score()


        terminated = False

        # Detect collision with wall
        if self.snake.head.xcor() > 280 or self.snake.head.xcor() < -280 or self.snake.head.ycor() > 280 or self.snake.head.ycor() < -280:
            terminated = True
            # self.scoreboard.game_over()

    
        # Detect collision with tail
        for segment in self.snake.segments[1:]:
            if self.snake.head.distance(segment) < 10:
                terminated = True
                # scoreboard.game_over()

        
        reward = self.scoreboard.Score if not terminated else 0

        self.render()
        obs = self._get_obs()

        return obs, reward, terminated, False, self._get_info()

    def _get_info(self):
        return {}


    def _get_obs(self):
        cv = self.screen.getcanvas()
        x = cv.winfo_rootx() 
        y = cv.winfo_rooty() 

        print(x, y)
        # img = ImageGrab.grab()#.crop((x, y, x + cv.winfo_width(), y + cv.winfo_height()))
        img = ImageGrab.grab(bbox=(x*0, y*0, x + cv.winfo_width(), y + cv.winfo_height()), include_layered_windows=True)#.crop((x, y, x + cv.winfo_width(), y + cv.winfo_height()))
        # cv.pack()
        # rect = cv.create_rectangle(-300,-300,600,600, fill="black", )
        # ps = cv.postscript(colormode='color')
        # img = Image.open("./img.eps")
        # img = Image.open(io.BytesIO(ps.encode('utf-8')))


        # img.show()
        # print(np.array(simg).shape)
        return np.array(img)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.screen.resetscreen()
        random_x = np.random.randint(-280, 280)
        random_y = np.random.randint(-280, 280)
        self.snake = Snake((random_x, random_x))
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.render()
        obs = self._get_obs()
        info = self._get_info()
        return obs, info
        

    def render(self):
        self.screen.update()
        time.sleep(1/FPS)

    def close(self):
        self.screen.bye()
        # self.screen.exitonclick( )


