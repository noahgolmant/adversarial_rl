""" constants for all the programs """
from baselines import deepq, trpo_mpi, ppo2, a2c  # home of modified learn fns 
from cleverhans.attacks import FastGradientMethod
ATTACKS = {
    'fgsm': FastGradientMethod,
}

# unfortunately, the  baselines ddpg implementation is too buggy to use,
# even out-of-the-box
ALG_LEARN_FNS = {
    'deepq': deepq.learn,
    # 'deepq': deepq.learn,
    # 'trpo_mpi': trpo_mpi.learn,
    # 'ppo2': ppo2.learn,
    # 'a2c': a2c.learn
}

VALID_ALGS = list(ALG_LEARN_FNS.keys())

POLICY_GRAD_ALGS = [
    'trpo_mpi',
    'ppo2',
    'a2c'
]