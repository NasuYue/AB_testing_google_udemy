#!/bin/python3

import math
import os
import random
import re
import sys


def stdDev(arr):
    arr_mean=sum(arr)/len(arr)
    SD=float(0)
    Dev=float(0)
    
    for i in range(len(arr)):
        Dev+=(arr[i]-arr_mean)**2
    
    SD=math.sqrt(Dev/len(arr))
        
    print(SD)
    
    
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
