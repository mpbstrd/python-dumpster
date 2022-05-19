import random
import numpy as np

words = np.loadtxt("5LW.txt",dtype=str)

word = random.choice(words)

user_input = input(": ")
while user_input != word:
    print(word)
    user_input = input(": ")
    if 