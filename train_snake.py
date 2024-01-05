import gymnasium as gym
import matplotlib.pyplot as plt
from pprint import pprint as pp
import Snake_game
import random
import numpy as np

from PIL import ImageGrab, Image




env = gym.make('Snake_game/SnakeWorld-v0')
# plt.imshow(env.reset()[0])
# plt.show()

env.reset()
for i in range(10):
    action = random.randint(0, 3)
    obs, r, end, _, _ = env.step(action=action)
    plt.imsave(f"./images/img{i}.jpg", obs)
    if end:
        env.reset()
env.close()