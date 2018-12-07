"""
Created on Fri Dec  7 23:33:25 2018

@author: simon

Project: FuturaeNetcom/4chan
"""

import gym


# main part of the programm
def main():
    env = gym.make('CartPole-v0')
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break
    return


main()
