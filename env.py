import gym
from gym import spaces
import numpy as np

class SpaceShooterEnv(gym.Env):
    def __init__(self):
        super(SpaceShooterEnv, self).__init__()
        self.action_space = spaces.Discrete(4)  # 0: stay, 1: left, 2: right, 3: shoot
        # Observations: position, enemy position, health, score
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        
        self.bot_position = 0.5  
        self.enemy_position = np.random.uniform(0, 1)  
        self.health = 1.0  
        self.score = 0
    
    def reset(self):
        self.bot_position = 0.5
        self.enemy_position = np.random.uniform(0, 1)
        self.health = 1.0
        self.score = 0
        return np.array([self.bot_position, self.enemy_position, self.health, self.score])
    
    def step(self, action):
        done = False
        reward = 0
        
        if action == 1:  # Move left
            self.bot_position = max(0, self.bot_position - 0.1)
        elif action == 2:  # Move right
            self.bot_position = min(1, self.bot_position + 0.1)
        elif action == 3:  # Shoot
            if abs(self.bot_position - self.enemy_position) < 0.1:
                reward = 10  # Hit enemy
                self.enemy_position = np.random.uniform(0, 1)  # Respawn enemy

        self.enemy_position -= 0.05
        if self.enemy_position < 0:
            self.health -= 0.1  # Lose health if enemy reaches you
            self.enemy_position = np.random.uniform(0, 1)  # Respawn enemy
        
        if self.health <= 0:
            done = True
        
        return np.array([self.bot_position, self.enemy_position, self.health, self.score]), reward, done, {}

    def render(self, mode='human'):
        print(f"Bot Position: {self.bot_position}, Enemy Position: {self.enemy_position}, Health: {self.health}, Score: {self.score}")
