from gymnasium.envs.registration import register

register(
     id="Snake_game/SnakeWorld-v0",
     entry_point="Snake_game.envs:SnakeWorldEnv",
     max_episode_steps=300,
)