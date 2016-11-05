#Main Function
def main():
  print '==== MEAL CALCULATOR ===='
  print
  mealprice = input_meal()
  tip = calc_tip(mealprice)
  tax = calc_tax(mealprice)
  total = calc_total(mealprice, tax, tip)
  print_info(mealprice, tip, tax, total);
# Input Meal Price
def input_meal():
  mealprice = input('Enter the meal price $')
  mealprice = float(mealprice)
  return mealprice
# Calculate Tip @ 20%
def calc_tip(mealprice):
  tip = mealprice * .20
  return tip
# Calculate Tax @ 6%
def calc_tax(mealprice):
  tax = mealprice * .06
  return tax
# Calculate Total Cost
def calc_total(mealprice, tip, tax):
  total = mealprice + tip + tax
  return total
# Outputs calculated data in a readable form
def print_info(mealprice, tip, tax, total):
  print 'The meal price is $', mealprice
  print 'The tip is $', tip
  print 'The tax is $', tax
  print 'The total is $', total
#calls main
main()
