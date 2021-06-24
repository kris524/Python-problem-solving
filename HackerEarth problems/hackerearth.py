'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
#number of cases
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