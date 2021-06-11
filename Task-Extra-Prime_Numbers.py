'''
Code to find Prime Numbers
in given Interval.

'''

# function to find Prime Numbers
def findPrime(num):
  for i in range(2, (num//2)+1):
    if num % i == 0:
      return 0
  return 1

# Declare the variables
flag = 0

# Ask user to enter lower value of interval
print("Enter lower limit")
# Take input
lLim = int(input("Input: "))

# Ask user to enter upper value of interval
print("Enter Upper limit")
# Take input
uLim = int(input("Input: "))

if lLim < uLim and lLim > 0:
# print display message
  print(f'Prime Numbers between {lLim} and {uLim} are:')

  # Traverse each number in the interval
  # with the help of for loop
  for i in range(lLim, uLim+1):
    if i < 2:
      continue
    elif i == 2:
      flag = 1
    else:
      flag = findPrime(i)
    if flag == 1:
      print(i, end = '| ')

else:
  print('Invalid Input, Please Try Again')