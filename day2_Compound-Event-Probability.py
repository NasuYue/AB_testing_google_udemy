#Objective
# In this challenge, we practice calculating the probability of a compound event. We recommend you review today's Probability Tutorial before attempting this challenge.
#Task
#There are 3 urns labeled X, Y, and Z.
# Urn X contains 4 red balls and 3 black balls.
# Urn Y contains 5 red balls and 4 black balls.
# Urn Z contains 4 red balls and 4 black balls.
# One ball is drawn from each of the  urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

import random
trials=10000
hits=0

# return 1 if red
def urn_draw(red,black):
    dice=random.randint(1,red+black)
    return 1 if (dice<=red) else 0

# 2 red and 1 black in 3 urn_draw pattern is RRB, RBR, BRR

for i in range(trials):
    d1=urn_draw(4,3)
    d2=urn_draw(5,4)
    d3=urn_draw(4,4)

    if (d1+d2+d3)==2:
        hits+=1

print('Probability is approximately ',hits/trials) 
# Probability is close to the caculation result: 17/42