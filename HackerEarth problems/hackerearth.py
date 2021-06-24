#THE PROBLEM THAT WAS SOLVED: https://www.hackerearth.com/practice/codemonk/
T = int(input())

#Number of elements 

for i in range(T):
#numer of steps of rotation, very important number
    NK = list(map(int,input().rstrip().split()))

#the array
    A = list(map(int, input().rstrip().split()))

    for i in range(NK[1]):
    #print(A[-1])
        last_element = A.pop(-1)
        A.insert(0,last_element)
    #print(A)

#A =','.join(A)
print(*A)