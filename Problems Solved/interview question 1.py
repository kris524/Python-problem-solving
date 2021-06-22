
import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    count,pairs = Counter(ar),0
    for i in count:
        pairs += count[i]/2
    return pairs



n = int(input())
a = [int(i) for i in input().split(' ')]
print(a)
print(a.pop(3))
print(sockMerchant(n,a))

print(7//2)
        
     
print(5/4
)        
print( round(3.33))