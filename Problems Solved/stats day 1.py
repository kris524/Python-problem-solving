
import math
import os
import random
import re
import sys
from statistics import median
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
 
n = int(input())
arr = list(map(int, input().rstrip().split()))

print(int(median(arr[:n//2])))
print(int(median(arr)))
print(int(median(arr[(n+1)//2:])))

print(10//2)

arr1 = [1,2,3,4,5,6,7,8,9]
print(arr1[5:])


import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#
from statistics import median


def interQuartile(values, freqs):
    empty = []
    # Print your answer to 1 decimal place within this function

    #first pick the index of the list of freqs
    for i in range(0,len(freqs)):
        #then pick the number itself
        for j in range(freqs[i]):
            empty.append(values[i])
    sorted_empty = sorted(empty)
    Q1 = int(median(sorted_empty[:len(sorted_empty)//2]))
    Q3 = int(median(sorted_empty[(len(sorted_empty)+1)//2:]))

    print(float(Q3 - Q1))
    #return Q1, Q3

interQuartile([6, 12, 8, 10, 20, 16],[5, 4, 3, 2, 1, 5])
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(n,val, freq)
 