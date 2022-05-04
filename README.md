# Exploitative Jam/Fold Poker Agent
William Peng's Project for CPSC 674: Advanced Computational Intelligence for Games

## Code in Respository
In this repository is the [pbots_calc library](https://github.com/mitpokerbots/pbots_calc), [poker-eval library](https://github.com/atinm/poker-eval), and code written for the poker bot.

The code I've written for this project are in 3 different files located in pbots_calc/python and are detailed below

The equities.py file uses the pbots_calc library to generate the equities.pickle file that contains a pre-computed dictionary containing poker hand versus hand equities

The exploit_poker_bot.py file contains all the code, logic, and functions for the exploitative poker agent

The test.py file contains code written to use the exploit poker bot for experimentation and fictitious play and generates readable plots

## Usage
```bash
python3 test.py pot stack rounds
```

Pot is a number for the amount of bb in the middle. Stack is a number for the amount of bb each player has in their stack. Rounds is a number for the number of rounds of fictitious play.

To edit the ranges tested for the opponent, changes must be made in the test.py file

To edit the amount of rounds simulated in fictitious play to get the game theory optimal strategy, change the rounds number in the gto function in the test.py file

## Installation
The exploitative poker agent has no pre-requirements before running, however the pbots_calc library does. Follow the instructions in the pbot_calc respository linked above or in the ReadMe in the pbots_calc folder


