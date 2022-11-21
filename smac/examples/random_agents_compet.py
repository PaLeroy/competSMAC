from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from absl import logging

from smac.env.starcraft2.compet_starcraft2 import CompetStarCraft2Env


def main():
    env = CompetStarCraft2Env(map_name="3m_compet")
    env_info = env.get_env_info()

    # Decide if a team plays the heuristic strategy
    team_1_heuristic = False
    team_2_heuristic = True

    n_agents_p1 = env_info["n_agents"]
    n_agents_p2 = env_info["n_enemies"]

    n_episodes = 8
    for e in range(n_episodes):
        env.reset()
        if e % 4 == 0:
            print("Team 1 plays the heuristic strategy.")
            env.setup_heuristic(True, False)
        elif e % 4 == 1:
            print("Team 2 plays the heuristic strategy.")
            env.setup_heuristic(False, True)
        elif e % 4 == 2:
            print("Team 1 and 2 play the heuristic strategy.")
            env.setup_heuristic(True, True)
        else:
            print("No team plays the heuristic strategy.")
            env.setup_heuristic(False, False)

        terminated = False
        episode_reward = np.zeros(n_agents_p1 + n_agents_p2)
        cpt = 0
        state = env.get_state()
        while not terminated:
            cpt += 1
            observations = env.get_obs()
            state = env.get_state()

            actions = []
            # Team 1
            obs_team_1 = observations[:n_agents_p1]
            for agent_id in range(n_agents_p1):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.choice(avail_actions_ind)
                actions.append(action)

            # Team 2
            obs_team_2 = observations[n_agents_p1:]
            for agent_id in range(n_agents_p1, n_agents_p1 + n_agents_p2):
                avail_actions = env.get_avail_agent_actions(agent_id)
                avail_actions_ind = np.nonzero(avail_actions)[0]
                action = np.random.choice(avail_actions_ind)
                actions.append(action)

            reward, terminated, s = env.step(actions)

            episode_reward += reward
        print("Rewards in episode {} = {}".format(e, episode_reward))
    env.close()


if __name__ == "__main__":
    logging.set_verbosity(logging.DEBUG)
    main()
