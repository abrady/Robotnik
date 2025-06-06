"""
TO EDIT: Some miscellaneous utility functions

Functions to edit:
    1. sample_trajectory (line 19)
    2. sample_trajectories (line 67)
    3. sample_n_trajectories (line 83)
"""
import numpy as np
import time

############################################
############################################

MJ_ENV_NAMES = ["Ant-v4", "Walker2d-v4", "HalfCheetah-v4", "Hopper-v4"]
MJ_ENV_KWARGS = {name: {"render_mode": "rgb_array"} for name in MJ_ENV_NAMES}
MJ_ENV_KWARGS["Ant-v4"]["use_contact_forces"] = True

def sample_trajectory(env, policy, max_path_length, render=False):
    """
    Rolls out a policy and generates a trajectories

    :param policy: the policy to roll out
    :param max_path_length: the number of steps to roll out
    :render: whether to save images from the rollout
    """
    # Initialize environment for the beginning of a new rollout
    ob = TODO # HINT: should be the output of resetting the env

    # Initialize data storage for across the trajectory
    # You'll mainly be concerned with: obs (list of observations), acs (list of actions)
    obs, acs, rewards, next_obs, terminals, image_obs = [], [], [], [], [], []
    steps = 0
    while True:

        # Render image of the simulated environment
        if render:
            if hasattr(env.unwrapped, 'sim'):
                if 'track' in env.unwrapped.model.camera_names:
                    image_obs.append(env.unwrapped.sim.render(camera_name='track', height=500, width=500)[::-1])
                else:
                    image_obs.append(env.unwrapped.sim.render(height=500, width=500)[::-1])
            else:
                image_obs.append(env.render())

        # Use the most recent observation to decide what to do
        obs.append(ob)
        ac = TODO # HINT: Query the policy's get_action function
        ac = ac[0]
        acs.append(ac)

        # Take that action and record results
        ob, rew, done, _ = env.step(ac)

        # Record result of taking that action
        steps += 1
        next_obs.append(ob)
        rewards.append(rew)

        # TODO end the rollout if the rollout ended
        # HINT: rollout can end due to done, or due to max_path_length
        rollout_done = TODO # HINT: this is either 0 or 1
        terminals.append(rollout_done)

        if rollout_done:
            break

    return Path(obs, image_obs, acs, rewards, next_obs, terminals)

def sample_trajectories(env, policy, min_timesteps_per_batch, max_path_length, render=False):
    """
        Collect rollouts until we have collected `min_timesteps_per_batch` steps.

        TODO implement this function
        Hint1: use sample_trajectory to get each path (i.e. rollout) that goes into paths
        Hint2: use get_pathlength to count the timesteps collected in each path
    """
    timesteps_this_batch = 0
    paths = []
    while timesteps_this_batch < min_timesteps_per_batch:

        # TODO
        pass

    return paths, timesteps_this_batch

def sample_n_trajectories(env, policy, ntraj, max_path_length, render=False):
    """
        Collect `ntraj` rollouts.

        TODO implement this function
        Hint1: use sample_trajectory to get each path (i.e. rollout) that goes into paths
    """
    paths = []
        
    TODO

    return paths

############################################
############################################

def Path(obs, image_obs, acs, rewards, next_obs, terminals):
    """
        Take information (separate arrays) from a single rollout
        and return it in a single dictionary
    """
    if image_obs != []:
        image_obs = np.stack(image_obs, axis=0)
    return {"observation" : np.array(obs, dtype=np.float32),
            "image_obs" : np.array(image_obs, dtype=np.uint8),
            "reward" : np.array(rewards, dtype=np.float32),
            "action" : np.array(acs, dtype=np.float32),
            "next_observation": np.array(next_obs, dtype=np.float32),
            "terminal": np.array(terminals, dtype=np.float32)}


def convert_listofrollouts(paths):
    """
        Take a list of rollout dictionaries and return separate arrays,
        where each array is a concatenation of that array from across the rollouts
    """
    observations = np.concatenate([path["observation"] for path in paths])
    actions = np.concatenate([path["action"] for path in paths])
    next_observations = np.concatenate([path["next_observation"] for path in paths])
    terminals = np.concatenate([path["terminal"] for path in paths])
    concatenated_rewards = np.concatenate([path["reward"] for path in paths])
    unconcatenated_rewards = [path["reward"] for path in paths]
    return observations, actions, next_observations, terminals, concatenated_rewards, unconcatenated_rewards

############################################
############################################

def get_pathlength(path):
    return len(path["reward"])
