# Objective: 
# In this challenge, we practice calculating probability. Check out the Tutorial tab for a breakdown of probability fundamentals!
# Task: 
# In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

import random
trials=10000
hits=0

for i in range(trials):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    if (d1+d2) <= 9:
        hits+=1
        
print('Probability at most 9 approximately is ',hits/trials) 
# Probability is close to the caculation result: 5/6

