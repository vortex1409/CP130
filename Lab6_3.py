#the main function
def main():
#A Basic For loop
print "I will display the numbers 1 through 5."
for num in [1, 2, 3, 4, 5]:
print (num)
#The Second Counter code
print "Second Counter"
for sec in range(1,61):
print "The Second Is: ", sec
#The Accumulator code
total = 0
for counter in range(5):
number = input("Enter Number: ")
total = total + number
print "The total is", total
#The Average Age code
totalAge = 0
averageAge = 0
number = input("How many ages: ")
for counter in range(0, number):
age = input("Enter Age: ")
totalAge = totalAge + age
averageAge = totalAge/number
print "Average Age: ", averageAge
#calls main
main()
