#Lab 7.4 - Py - Michael Dorfman
#11/23/2016
# Displays random math equations and grades them

# External Libraries
#=====================================
import random
#=====================================

# Main Function Declared
def main():

    # DECLARE VARIABLES
    #=====================================
    counter = 0
    studentName = "No Name"
    averageRight = 0.0
    right = 0
    number1 = 0
    number2 = 0
    answer = 0.0
    percentage = 0
    #=====================================
    studentName = inputNames()

    # While loop to call functions and send values
    while counter < 10:
        number1, number2 = getNumbers()
        answer = getAnswer(number1, number2)
        right = checkAnswer(answer, number1, number2, right, counter)
        counter = counter + 1

    averageRight, percentage = results(right, averageRight, percentage)
    displayInfo(right, averageRight, studentName, percentage)

# Accepts Student Name
def inputNames():
    studentName = raw_input("Enter Student Name: ")
    return studentName

# Generates Random Numbers
def getNumbers():
    number1 = random.randint(1, 500)
    number2 = random.randint(1, 500)
    return number1, number2

# Allows user to enter answer
def getAnswer(number1, number2):
    print "What is the answer to the following equation?"
    print number1," + ",number2
    answer = input("Answer: ")
    return answer

# Checks if the answer is right and displays if it is correct or not
# also displays the question number
def checkAnswer(answer, number1, number2, right, counter):

    question = counter + 1
    
    if answer == (number1+number2):
        print "#", question, " Correct Answer"
        right = right + 1
    else:
        print "#", question, " Incorrect Answer"
    return right

# Figures out the average and percentage and returns values  
def results(right, averageRight, percentage):
    averageRight = right / 10
    averageRight = float(averageRight)
    percentage = averageRight * 100
    return averageRight, percentage

# Displays final information to user
def displayInfo(right, averageRight, studentName, percentage):
    print "Student Name: ", studentName
    print "Correct: #", right
    print "Average Correct: ", averageRight
    print "Percentage: ", percentage, "%"

main()
