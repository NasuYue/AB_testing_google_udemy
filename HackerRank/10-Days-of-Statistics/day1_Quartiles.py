#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import median 

# for python list[a:b] refer to 'a' inclued and 'b' not included
def quartiles(arr):
    sorted_arr=sorted(arr)
    cutoff=int(len(arr)/2)

    q1=median(sorted_arr[:cutoff])
    q2=median(sorted_arr)

    if len(arr)%2 == 0:        
        q3=median(sorted_arr[cutoff:])
    else:
        q3=median(sorted_arr[cutoff+1:])
    
    print(round(q1))
    print(round(q2))
    print(round(q3))


if __name__ == '__main__':
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(data)