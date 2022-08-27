# Objective
# In this challenge, we practice calculating probability. We recommend you review the previous challenge's Tutorial before attempting this problem.
# Task
# In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

import random
trials=100000
hits=0

for i in range(trials):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    if (d1+d2) == 6 and (d1!=d2):
        hits+=1
        
print('Probability with two different values and sum of 6 approximately is ',hits/trials) 
# Probability is close to the caculation result: 1/9
