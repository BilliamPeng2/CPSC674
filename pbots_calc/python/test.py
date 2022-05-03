import exploit_poker_bot
import pbots_calc
import sys
import pandas as pd
import numpy as np
import pickle
import random
from poker.hand import Hand, Combo, Range
import matplotlib.pyplot as plt

def main(pot, stack, rounds):
    call_range, assumed_jam_range = exploit_poker_bot.gto(pot, stack, 100) #gto ranges to begin with
    print(exploit_poker_bot.range_ev(pot, stack, call_range, assumed_jam_range))
    print("percent", exploit_poker_bot.percentage(assumed_jam_range))
    exploits = [1.1, 1.2, 1.3, 1.4, 1.5] #exploit percentages
    #exploits = [.9, .8, .7, .6, .5]

    colors = ["blue", "black", "orange", "green", "red"] #for the graphs

    for i in range(5): #simulate play and graph range ev
        opponent_percentage = exploit_poker_bot.percentage(assumed_jam_range) * exploits[i]
        jam_range = exploit_poker_bot.build_random_range(opponent_percentage)
        ev_data, range_ev_data = exploit_poker_bot.play_as_caller(pot, stack, call_range.copy(), jam_range, assumed_jam_range.copy(), rounds)
        plt.plot(range_ev_data, label = f"{exploits[i]}", color = colors[i])
        plt.axhline(y=exploit_poker_bot.range_ev(pot, stack, call_range, jam_range), linestyle = '--', color = colors[i])
        plt.axhline(y=exploit_poker_bot.range_ev(pot, stack, exploit_poker_bot.optimal_call(pot, stack, jam_range), jam_range), linestyle = '--', color = colors[i])
    plt.title('Caller\'s Range EV over Hands Played')
    plt.xlabel('Hands Played')
    plt.ylabel('Expected Value of Exploitative Strategy')
    plt.legend(title = "Deviation of Jammer", loc = "upper left", bbox_to_anchor=(1.04, 1))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        pot = float(sys.argv[1])
        stack = float(sys.argv[2])
        rounds = int(sys.argv[3])

    main(pot, stack, rounds)
