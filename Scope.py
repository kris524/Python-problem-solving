class Difference:
    #maximumDifference = 0
    def __init__(self, a):
        
        self.__elements = a
        #self.maximumDifference = 0


    def computeDifference(self):
        self.maximumDifference = 0
        for i in range(0,len(a)):
            for j in range(0,len(a)):
                if a[i] == a[j]:
                    pass
                if a[i] != a[j]:
                    zeta = abs(a[i]-a[j])
                    if zeta > self.maximumDifference:
                
                        self.maximumDifference = zeta

        self.maximumDifference










_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)