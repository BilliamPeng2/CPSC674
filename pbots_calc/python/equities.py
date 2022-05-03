import pbots_calc
import sys
import pandas as pd
import numpy as np
import json
import pickle
from poker.hand import Hand, Combo, Range

def main(): #for generating the dictionary with the handvhand EVs (cashe)
    equities = {}
    hands = [str(hand) for hand in list(Hand)]
    for hand1 in hands:
        for hand2 in hands:
            equities[(hand1, hand2)] = pbots_calc.calc(f"{hand1}:{hand2}", "", "", 100000).ev[0]
            print(hand1, hand2, equities[(hand1, hand2)])
    f = open("equities.pickle", "wb")
    pickle.dump(equities, f)
    f.close()

if __name__ == "__main__":
    main()
