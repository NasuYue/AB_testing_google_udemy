#Objective
# In this challenge, we get started with conditional probability. Check out the Tutorial tab for learning materials!
# Task
# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?

import random
trials=100000
num_at_least_one_boy=0
num_both_are_boy=0

for i in range(trials):
    d1=random.choice(['Boy','Girl'])
    d2=random.choice(['Boy','Girl'])
    if d1=='Boy' or d2=='Boy':
        num_at_least_one_boy+=1
    if d1=='Boy' and d2=='Boy':
        num_both_are_boy+=1

print('Conditional probability is approximately ',num_both_are_boy/num_at_least_one_boy) 
# Probability is close to the caculation result: 1/3