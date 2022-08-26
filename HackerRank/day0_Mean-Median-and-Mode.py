import numpy as np
from scipy import stats

N=input()
NN=list(map(int,input().split()))

print(np.mean(NN))
print(np.median(NN))
print(int(stats.mode(NN)[0]))

# stats.mode return array of ndarray
# Force ndarray to int