# Main Function recieves variables from input function
def main():
print '=== WELCOME ==='
age, weight, birthMonth = getInput() #returns 3 values to 3 variables
ansOutput(age, weight, birthMonth) #passes values to comparison function
# Gets input from user and returns 3 values
def getInput():
getAge = input('Enter Age: ')
getWeight = input('Enter Weight: ')
getMonth = raw_input('Enter Month: ')
return getAge, getWeight, getMonth
# Compares designated values and outputs data based on comparison
def ansOutput(age, weight, birthMonth):
if age <= 25:
print "Congratulations, the age is 25 or less"
if weight >= 128:
print "Congratulations, the weight is 128 or more"
if birthMonth == 'April':
print "Congratulations, the birth month is April"
#Main Function
main()
