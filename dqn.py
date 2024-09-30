import gym
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import DummyVecEnv
from env import SpaceShooterEnv  

env = DummyVecEnv([lambda: SpaceShooterEnv()])
model = DQN('MlpPolicy', env, verbose=1)

model.learn(total_timesteps=10000)

model.save("dqn_space_shooter_env")

#model = DQN.load("dqn_space_shooter_env")
#for later loading if needed

for episode in range(5):
    state = env.reset()
    done = False
    episode_reward = 0
    
    while not done:
        action, _ = model.predict(state)
        
        # Take the action in the environment
        next_state, reward, done, _ = env.step(action)
        
        # Accumulate the reward
        episode_reward += reward
        env.render(mode='None')
    
    print(f"Episode {episode + 1}: Total Reward = {episode_reward}")

