#Main Function Declared
def main():
# GLOBAL VARIABLES
#=====================================
counter = 0
endProgram = "no"
totalScores = 0.0
averageScores = 0.0
score = 0
number = 0
#=====================================
# END PROGRAM WHILE LOOP
while endProgram == "no":
# GLOBAL RESET VARIABLES
#=================================
counter = 0
endProgram = "no"
totalScores = 0.0
averageScores = 0.0
score = 0
number = 0
#=================================
number = getNumber()
totalScores= getScores(number, totalScores)
averageScores = getAverage(totalScores, number)
printAverage(averageScores)
endProgram = raw_input("End Program?: ")
PASTE CODE HERE

Starting Out with Programming Logic and Design 24
# getNumber gets number of students
# returns number
def getNumber():
number = input("How many students took the test?: ")
return number
# getScores loops until all grades are entered
# for the number of students given
# returns totalScores
def getScores(number, totalScores):
for counter in range(0,number):
score = input("Enter Score: ")
totalScores = totalScores + score
return totalScores
# getAverage recieves totalScores and number
# calculates the average score and
# returns averageScores
def getAverage(totalScores, number):
averageScores = totalScores/number
return averageScores
# printAverage recieves averageScores
# prints averageScores to screen
def printAverage(averageScores):
print "The average score is: ", averageScores
#Calls Main
main()
