import random
import numpy as np
import matplotlib.pyplot as plt
change_door = False

def play(switch):
    car = random.randint(0, 2)
    pick = 0                      # always pick door 0
    host = random.choice([d for d in range(3) if d != pick and d != car])
    if switch:
        pick = next(d for d in range(3) if d != pick and d != host)
    return pick == car




trials = 100_000

stay_wins = 0
switch_wins = 0

for _ in range(trials):
    if play(False):
        stay_wins += 1
    if play(True):
        switch_wins += 1

# plot the number of successes for each strategy
bars = plt.bar(["Stay", "Switch"], [stay_wins, switch_wins], color=["tab:red", "tab:green"])
plt.bar_label(bars)


plt.ylabel("Number of wins")
plt.title(f"Monty Hall: wins out of {trials:,} games")
plt.show()