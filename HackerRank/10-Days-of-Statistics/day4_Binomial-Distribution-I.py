# Task
# The ratio of boys to girls for babies born in Russia is 1.09:1 . If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?
# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

# binomial distribution: b(x,n,p)=(n!/(n-x)!(x)!)*(p**x)*(q**(n-x))

import sys
import math

ratio = list(map(float, input().split()))
n=6
p=ratio[0]/(ratio[0]+ratio[1])
q=ratio[1]/(ratio[0]+ratio[1])

x=[3,4,5,6] # X>=3 equal to [3,4,5,6]

prob=0

for xx in x:
    prob += math.factorial(n)/(math.factorial(n-xx)*math.factorial(xx))*(p**xx)*(q**(n-xx))

sys.stdout.write(str(round(prob,3)))

"""
# Implementation by numpy

import numpy as np
n=6
p=float(1.09/(1+1.09))
size=1000
points=[]

for i in range(1000):
    prob=sum(np.random.binomial(n,p,size)>=3)/size
    points.append(prob)

print('The probability of 6 children with at least 3 boys in Russia is approximately ',np.mean(points))
"""