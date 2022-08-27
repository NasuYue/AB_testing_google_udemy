#!/bin/python3
import math
import os
import random
import re
import sys

def weightedMean(X, W):
    product=float(0)
    for i in range(len(X)):
        product += X[i] * W[i]

    print('{0:.1f}'.format(product/sum(W)))
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
