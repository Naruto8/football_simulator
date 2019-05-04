import numpy as np
import pandas as pd

pass_pd = pd.read_csv("./pass_prob.csv").set_index('Position').T

player_ind = ['GK', 'RB', 'RCB', 'LCB', 'LB', 'CDM', 'RCM', 'LCM', 'RW', 'LW', 'ST']
short_pass_prob = np.array([0.5, 0.7, 0.9, 0.9, 0.7, 0.65, 0.6, 0.6, 0.8, 0.8, 0.9])
long_pass_prob = 1. - short_pass_prob
shoot_prob = np.array([0, 0, 0, 0, 0, 0.08, 0.13, 0.17, 0.25, 0.26, 0.6])
shoot_fail_prob = np.array([0, 0, 0, 0, 0, 0.9, 0.8, 0.8, 0.68, 0.7, 0.5])

def decide_action(player):
    pass_or_shoot = np.random.rand()
    if pass_or_shoot < shoot_prob[player]:
        return 'shoot'
    else:
        return 'pass'

def perform_pass(player):
    p = np.random.rand()
    cumulative_prob = 0
    for i, pass_p in enumerate(pass_pd[player]):
        cumulative_prob += pass_p
        if p > cumulative_prob:
            continue
        else:
            print(player + " passes to " + player_ind[i])
            return i
    print("fail")

def perform_shoot(player_id):
    p = np.random.rand()
    if p < shoot_fail_prob[player_id]:
        return 0
    return 1

def play(player):
    goal = 0
    next_player = player
    while goal == 0:
        action = decide_action(next_player)
        if action is 'pass':
            next_player = perform_pass(player_ind[next_player])
        else:
            print(player_ind[next_player] + " shoots!")
            shot = perform_shoot(next_player)
            if shot == 1:
                print("GOAL!")
                goal = 1
            else:
                print("And he misses it!")
                print("Play starts with the GK again....")
                next_player = 0

def simulate():
    player_index = 0
    play(player_index)

simulate()
