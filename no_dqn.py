import gym
from env import SpaceShooterEnv  

env = SpaceShooterEnv()

num_episodes = 5    
max_steps = 100     

for episode in range(num_episodes):
    state = env.reset()  
    done = False         #flag to check whether the episode is finished
    episode_reward = 0   
    step = 0             #for steps in each episode

    print(f"\nStarting episode {episode + 1}")

    while not done and step < max_steps:
        action = env.action_space.sample()  
        next_state, reward, done, _ = env.step(action)
        episode_reward += reward
        step += 1

        env.render()

        #print(f"Step: {step}, Action: {action}, Reward: {reward}, Done: {done}")

    print(f"Episode {episode + 1} finished with total reward: {episode_reward}")

env.close()

