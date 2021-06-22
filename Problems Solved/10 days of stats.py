import statistics

N = int(input())
X=[]

#for i in range(N):
 #   i = map(int, input()) 
#print(i)
#l = map(int, input().split()) 

a = [int(i) for i in input().split(' ')]
    

#print(a)

mean = sum(a)/len(a)
print(mean)

print(statistics.median(a))

#print(statistics.mode(a))





if statistics.mode(a) == a[0]:
    print(min(a))
#if statistics.mode(a)

