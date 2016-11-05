# Main Function
def main():
print '==== Tax Calculator ===='
print #Blank Line
salesTotal = inputData()
countryTax = cTax(salesTotal)
stateTax = sTax(salesTotal)
totalTax = tTax (stateTax, countryTax)
outputData(salesTotal, stateTax, countryTax, totalTax);
# Input Total Sales
def inputData():
salesTotal = input('Enter Total Sales: $')
salesTotal = float(salesTotal)
return salesTotal
# Calculates Country Tax at 2%
def cTax(salesTotal):
countryTax = salesTotal * 0.02
return countryTax
#Calculates State Tax at 4%
def sTax(salesTotal):
stateTax = salesTotal * 0.04
return stateTax
# Calculates Total Tax
def tTax(stateTax, countryTax):
totalTax = stateTax + countryTax
return totalTax
# Outputs all data in a readable format
def outputData(salesTotal, stateTax, countryTax, totalTax):
print '==== OUTPUT ====',
print #Blank Line
print 'Total Sales: $', salesTotal
print 'Country Tax: $', countryTax
print 'State Tax: $', stateTax
print 'Total Tax: $', totalTax
main()
