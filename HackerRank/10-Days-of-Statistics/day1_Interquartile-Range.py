#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    
    # expand array of vales
    exp_val=[]
    for v in values:
        for i in range(freqs.pop(0)):
            exp_val.append(v)

    exp_val=sorted(exp_val)
    
# Using from d2 practice mean-mdian-mode
    cutoff=int(len(exp_val)/2)
    q1=median(exp_val[:cutoff])

    if len(exp_val)%2 == 0:        
        q3=median(exp_val[cutoff:])
    else:
        q3=median(exp_val[cutoff+1:])
        
    print(float(q3-q1))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
