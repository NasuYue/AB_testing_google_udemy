# Objective
# In this challenge, we're getting started with combinations and permutations. Check out the Tutorial tab for learning materials!
# Task
# You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?

# Caculation:
# Every suits have 13 cards out of 52 cards deck
# The first draw can be any card with any suit, the probability is 1 (52 out of 52)
# The second draw should have same suit as first draw, the probability is 12/51
# P = 1 * (12/51) = 12/51

import random

trials=100000
hits=0
cards=[]

for suit in ['spades', 'hearts', 'clubs', 'diamonds']:
    for i in range(13):
        cards.append(suit)

for i in range(trials):
    random.shuffle(cards)
    if cards[0] == cards[1]:
        hits+=1
        
print('Probability is approximately ',hits/trials) 
# Probability is close to the caculation result: 0.234 ~= 12/51