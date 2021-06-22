


import numpy as np

X= []
n = list(input())
for i in range(int(n[0])):
                                    # for size
    Array = list(map(int, input().split(' ')[:int(n[2])]))  # to input n elements
    X.append(Array)
#print(Array)
print(np.array(X))

print('-----------------------')
X_t =np.transpose(X)

for row in X_t:
    row = str(row).lstrip('[').rstrip(']')
    print(row)

#print(list(X_t))