#Main Function Declared
def main():
# GLOBAL VARIABLES
#=====================================
endProgram = "no"
endOrder = "no"
totalBurger = 0
totalFry = 0
totalSoda = 0
total = 0
tax = 0
subtotal = 0
option = 0
burgerCount = 0
fryCount = 0
sodaCount = 0
#=====================================
# END PROGRAM WHILE LOOP
while endProgram == "no":
# GLOBAL RESET VARIABLES
#=================================
totalBurger = 0
totalFry = 0
totalSoda = 0
total = 0
tax = 0
subtotal = 0
#================================
# END ORDER WHILE LOOP
while endOrder == "no":
print "Enter 1 (Yum Yum Burgers)"
print "Enter 2 (Grease Yum Fries)"
print "Enter 3 (Soda Yum)"
option = input("Enter Option: ")

Starting Out with Programming Logic and Design 27
# OPTION SELECTION IF/ELSEIF
if option == 1:
totalBurger = getBurger(totalBurger, burgerCount)
elif option == 2:
totalFry = getFry(totalFry, fryCount)
elif option == 3:
totalSoda = getSoda(totalSoda, sodaCount)
else:
print "Invalid Input"
endOrder = raw_input("End Order? (yes/no): ")
total = calcTotal(totalBurger, totalFry, totalSoda)
printReceipt(total)
endProgram = raw_input("End Program? (yes/no): ")
# GETS BURGER INPUT
def getBurger(totalBurger, burgerCount):
burgerCount = input("# of Burgers: ")
totalBurger = totalBurger + burgerCount * 0.99
return totalBurger
# GETS FRY INPUT
def getFry(totalFry, fryCount):
fryCount = input("# of Fries: ")
totalFry = totalFry + fryCount * 0.79
return totalFry
# GETS SODA INPUT
def getSoda(totalSoda, sodaCount):
sodaCount = input("# of Sodas: ")
totalSoda = totalSoda + sodaCount * 1.09
return totalSoda
# CALCULATES TOTAL
def calcTotal(totalBurger, totalFry, totalSoda):
subtotal = totalBurger + totalFry + totalSoda
tax = subtotal * 0.06
total = subtotal + tax
return total

Starting Out with Programming Logic and Design 28
# PRINTS TOTAL
def printReceipt(total):
print "Total: $", total
# CALLS MAIN
main()
