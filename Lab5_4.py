#The main function
def main():
endProgram = "no"
while endProgram == "no":
totalBottles = getBottles()
totalPayout = calcPayout(totalBottles)
printInfo(totalBottles, totalPayout)
endProgram = raw_input("End the program? (yes/no): ")
# Returns total bottles after 7 day user input
def getBottles():
totalBottles = 0
todayBottles = 0
counter = 1
while counter <= 7:
todaysBottles = input("Enter # of Bottles: ")
totalBottles = totalBottles + todaysBottles
counter = counter + 1
return totalBottles
# Calculates payout
def calcPayout(totalBottles):
totalPayout = 0
totalPayout = totalBottles*0.10
return totalPayout
# Outputs data from previous functions
def printInfo(totalBottles, totalPayout):
print "# of Bottles: ", totalBottles
print "Payout: $", totalPayout
#Calls main
main()
