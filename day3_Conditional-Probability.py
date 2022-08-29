#Objective
# In this challenge, we get started with conditional probability. Check out the Tutorial tab for learning materials!
# Task
# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

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
