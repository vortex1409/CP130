#Lab 8.5 - Py - Michael Dorfman
#11/29/2016

# Main Function
def main():
    
    endProgram = "no"

    while(endProgram == "no"):

        # Declare Variables
        minutesAllowed = 0
        minutesUsed = 0
        totalDue = 0
        minutesOver = 0

        # Call Functions
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)
        totalDue, minutesOver = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)

        # End Program (Input Validation)
        endProgram = raw_input("End Program?")
        while(endProgram != "yes" or endProgram != "no"):
            print "Invalid Input"
            endProgram = raw_input("End Program?")

# Gets Allowed Minutes
# Recieves one variable and returns one variable
def getAllowed(minutesAllowed):
    minutesAllowed = input("Minutes Allowed: ")

    # Input Validation
    while(minutesAllowed < 200 or minutesAllowed > 800):
        minutesAllowed = input("Invalid - Enter Again")

    return minutesAllowed

# Gets Used Minutes
# Recieves one variables and returns one variable
def getUsed(minutesUsed):
    minutesUsed = input("Minutes Used: ")

    # Input Validation
    while(minutesUsed < 0):
        minutesUsed = input("Invalid - Enter Again")

    return minutesUsed

# Calculates total cost due and minutes over
# Recieves four variables and returns two variables
def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):

    extra = 0

    if(minutesUsed <= minutesAllowed):
        totalDue = 74.99
        minutesOver = 0
        print "Acceptable Usage"
    else:
        minutesOver = minutesUsed - minutesAllowed
        extra = minutesOver * 0.20
        totalDue = 74.99 + extra
        print "Over by: ", minutesOver

    return totalDue, minutesOver

# Displays the Data
# Recieves 4 variables and returns no variables
def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print "=== Montly Report ==="
    print "Allowed: ", minutesAllowed
    print "Used: ", minutesUsed
    print "Over: ", minutesOver
    print "Total Cost Due: $", totalDue

# Calls and Executes Main Function
main()
