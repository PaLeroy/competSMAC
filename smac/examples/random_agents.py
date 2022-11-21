from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging

from smac.env import StarCraft2Env
import numpy as np


def main():
    env = StarCraft2Env(map_name="3m")

    env_info = env.get_env_info()

    n_actions = env_info["n_actions"]
    n_agents = env_info["n_agents"]

    n_episodes = 10

    for e in range(n_episodes):
        env.reset()
        terminated = False
        episode_reward = 0

        while not terminated:
            obs = env.get_obs()
            state = env.get_state()

            actions = []
            for idx, agent_id in enumerate(range(n_agents)):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.choice(avail_actions_ind)
                actions.append(action)

            reward, terminated, info = env.step(actions)
            episode_reward += reward
        print("Total reward in episode {} = {}".format(e, episode_reward))

    env.close()


if __name__ == "__main__":
    logging.set_verbosity(logging.DEBUG)

    main()
