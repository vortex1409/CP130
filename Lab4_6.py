#The main function
def main():
meal = getData()
tip, tax, total = calcData(meal)
outputData(meal, tip, tax, total)
#This function gets the meals price
def getData():
meal = input ("Enter Price: $")
meal = float(meal)
return meal
#Calculates all data (tip, tax & total)
def calcData(meal):
if meal >= 0.01 and meal <= 5.99:
tip = meal * 0.1
elif meal <= 12:
tip = meal * 0.13
elif meal <= 17:
tip = meal * 0.16
elif meal <= 25:
tip = meal * 0.19
else:
tip = meal * 0.22
tax = meal * .06
total = meal + tip + tax
return tip, tax, total
#Prints out calculated and recived data
def outputData (meal, tip, tax, total):
print "Meal: $", meal
print "Tip: $", tip
print "Tax: $", tax
print "Total: $", total
#Main Function
main()
