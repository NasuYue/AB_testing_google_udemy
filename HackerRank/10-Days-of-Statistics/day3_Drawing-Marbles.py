# Objective
#In this challenge, we're reinforcing what we've learned today. In case you've missed them, today's tutorials are on Conditional Probability and Combinations and Permutations.
# Task
#A bag contains 3 red marbles and 4 blue marbles. Then, 2 marbles are drawn from the bag, at random, without replacement. If the first marble drawn is red, what is the probability that the second marble is blue?

# Caculation:
# P(A|B) = P(A&B)/P(B) = P(two draw is read and blue)/P(first draw is red) = (3/7)*(4/6)/(3/7) = 2/3

import random
trials=100000
bag=['R','R','R','B','B','B','B']
num_R=0
num_RB=0

for i in range(trials):
    random.shuffle(bag)
    if bag[0] == 'R':
        num_R+=1
        if bag[1] == 'B':
            num_RB+=1

print('Conditional probability is approximately ',num_RB/num_R)
# Probability is close to the caculation result: 2/3 ~= 0.666 