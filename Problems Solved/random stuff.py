def plusMinus(arr):
    # Write your code here
    count_positive=0
    count_negative = 0
    count_zero = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            count_positive+=1
        elif arr[i] <0:
            count_negative+=1
        elif arr[i] == 0:
            count_zero +=1
    print(format(count_positive/len(arr), '.6f'))
    print(format(count_negative/len(arr), '.6f'))
    print(format(count_zero/len(arr), '.6f')) 
    #return 
    #return 

plusMinus([1,-2,3,-5])

 


def cartesian(arr,arr2):
    for i in range(0,len(arr)):
        for j in range(0, len(arr2)):
            if arr[i] == ' ' or arr2[j] == ' ':
                continue 
            
            print((int(arr[i]),int(arr2[j])),end=' ')
            

arr = input()
arr2 = input()

cartesian(arr,arr2)



class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,firstName, lastName, idNumber,scores):
        Person.__init__(self, firstName, lastName,idNumber)
        
        self.scores = scores
        
    def calculate(self):
        sum = 0
        #values = list(self.scores)
        for score in scores:
            sum+=score
        average = sum/len(scores)
        if average>= 90 and average<=100:
            return 'O'

        elif average >=80 and average < 90:
            return 'E'
        elif average >=70 and average < 80:
            return 'A'

        elif average >= 55 and average < 70:
            return 'P'

        elif average >= 40 and average < 55:
            return 'D'

        elif average < 40:
            return 'T'



        
#print(sum([1,2,3])/len([1,2,3]))   
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
#print(sum(100,80)/)