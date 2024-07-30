#Author: Kenneth Hung
#Assignment: Programming Assignment 1
#Last revision: 02/2/2024

# Task 1
# FV = PV * (1 + (INT/100))**YRS
# prompt users to enter
# float value present value (PV) as a dollar amount ex: 1530.50
# float value interest rate (INT) ex: 3.5 representing 3.5%
# integer value years (YRS)
print("Task 1: Practicing arithmetic expressions. Please enter inputs according to specifications given. ")
print("-" * 25) # divider

# Make it clear for user what inputs are required
PV = float(input("Enter a present value, represented as a floating point number with two decimal places: "))
INT = float(input("Enter an interest value as a percent, such as '3.2', the value can be a floating point number: "))
YRS = int(input("Enter a integer value, for example '13', to represent a set amount of years, round to the nearest whole number:"))

# equation
# INT is first divided by 100 and the result is added with 1
# it is then put to the power of YRS and finally multiplied by PV
# the result is stored in FV
print()
print("Performing calculations...")
FV = PV * ((1 + (INT/100)) ** YRS)

# print out text and dollar sign and also specify the amount of decimal placements
print("Future Value: $%.2f" % FV)
print("-" * 25) # divider
'''
Test 1
Enter a present value, represented as a floating point number with two decimal places: 1000.0
Enter an interest value as a percent, such as '3.2', the value can be a floating point number: 5.0
Enter a integer value, for example '13', to represent a set amount of years, round to the nearest whole number:30

Performing calculations...
Future Value: $4321.94

Test 2
Enter a present value, represented as a floating point number with two decimal places: 1530.50
Enter an interest value as a percent, such as '3.2', the value can be a floating point number: 3.5
Enter a integer value, for example '13', to represent a set amount of years, round to the nearest whole number:15

Performing calculations...
Future Value: $2564.12

Test 3
Enter a present value, represented as a floating point number with two decimal places: 48
Enter an interest value as a percent, such as '3.2', the value can be a floating point number: 16
Enter a integer value, for example '13', to represent a set amount of years, round to the nearest whole number:8

Performing calculations...
Future Value: $157.36
'''

# Task 2
# take 2 user inputted numbers and store them in two separate variables
# swap the values of the two variables in 1 line of code
print("Task 2: Practice assignments, Swapping two numbers")
print("-" * 25) # divider
firstNum = int(input("Enter the first number, the value must be an integer: "))
secondNum = int(input("Enter the second number, the value should also be an integer: "))

# the swap must be done in one line
print("Peforming Swap...")
firstNum, secondNum = secondNum, firstNum

# print out results
print("The value of the first variable is now: " + str(firstNum))
print("THe value of the second variable is now: " + str(secondNum))
print("-" * 25) # divider
'''
Test 1
Enter the first number, the value must be an integer: 7
Enter the second number, the value should also be an integer: 9
Peforming Swap...
The value of the first variable is now: 9
THe value of the second variable is now: 7

Test 2
Enter the first number, the value must be an integer: 21
Enter the second number, the value should also be an integer: 4
Peforming Swap...
The value of the first variable is now: 4
THe value of the second variable is now: 21

Test 3
Enter the first number, the value must be an integer: 2
Enter the second number, the value should also be an integer: 150
Peforming Swap...
The value of the first variable is now: 150
THe value of the second variable is now: 2
'''


# Task 3
# Convert java code into python
# compare and contrast
print("Task 3: Compare and Contrast, convert given Java code to python")
print("-" * 25) # divider

#what took 15 lines in java took 6 in python
print("Enter the value of num1 and num2 ")
num1, num2 = int(input("")), int(input(""))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient when " + str(num1) + "/" + str(num2) + " is: " + str(quotient))
print("Remainder when " + str(num1) + " is divided by " + str(num2) + " is: " + str(remainder))
'''
Test 1
Enter the value of num1 and num2
12
35
Quotient when 12/35 is: 0
Remainder when 12 is divided by 35 is: 12

Test 2
Enter the value of num1 and num2
35
13
Quotient when 35/13 is: 2
Remainder when 35 is divided by 13 is: 9

Test 3
Enter the value of num1 and num2
35
0
Traceback (most recent call last):
  File "c:\Users\kenhu\Desktop\python\P1_KennethH.py", line 107, in <module>
    quotient = num1 // num2
               ~~~~~^^~~~~~
ZeroDivisionError: integer division or modulo by zero
'''

# Task 4
# Practice if statement, BMI for Metric or USA/English
print("Task 4: Practice if statement, BMI for Metric and USA")
print("-" * 25) # divider
system = input("To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': ")
if system == "USA" or system == "Metric" :
    if system == "USA" :
        weight = float(input("Please enter your weight in pounds (lb): "))
        height = float(input("Please enter your weight in inches (in): "))
        BMI = 703 * (weight / (height ** 2))
    else :
        weight = float(input("Please enter your weight in kilograms (kg): "))
        height = float(input("Please enter your weight in meters (m): "))
        BMI = (weight / (height ** 2))
    if BMI > 25 :
        print("Your BMI is: %.2f" % BMI)
        print("You are medically considered overweight.")
    elif BMI < 16 :
        print("Your BMI is: %.2f" % BMI)
        print("You are medically considered underweight.")
    else :
        print("Your BMI is: %.2f" % BMI)
        print("You are medically considered average weight.")
print("End of program")

'''
Test 1
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': USA
Please enter your weight in pounds (lb): 155
Please enter your weight in inches (in): 70
Your BMI is: 22.24
You are medically considered average weight.
End of program

Test 2
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': USA
Please enter your weight in pounds (lb): 172
Please enter your weight in inches (in): 68
Your BMI is: 26.15
You are medically considered overweight.
End of program

Test 3
Please enter your weight in kilograms (kg): 75
Please enter your weight in meters (m): 1.83
Your BMI is: 22.40
You are medically considered average weight.
End of program

Test 4
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': Metric
Please enter your weight in kilograms (kg): 51.5
Please enter your weight in meters (m): 1.68
Your BMI is: 18.25
You are medically considered average weight.
End of program

Test 5
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': USA
Please enter your weight in pounds (lb): 100
Please enter your weight in inches (in): 60
Your BMI is: 19.53
You are medically considered average weight.
End of program

Test 6
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': Metric
Please enter your weight in kilograms (kg): 42
Please enter your weight in meters (m): 1.3
Your BMI is: 24.85
You are medically considered average weight.
End of program

Test 7
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': USA
Please enter your weight in pounds (lb): -52 
Please enter your weight in inches (in): 48 
Your BMI is: -15.87
You are medically considered underweight.
End of program

Test 8
To calculate your BMI please specify which measurement system. Enter 'USA' or 'Metric': Metric
Please enter your weight in kilograms (kg): 64 
Please enter your weight in meters (m): 0
Traceback (most recent call last):
  File "c:\Users\kenhu\Desktop\python\P1_KennethH.py", line 19, in <module>
    BMI = (weight / (height ** 2))
           ~~~~~~~^~~~~~~~~~~~~~~
ZeroDivisionError: float division by zero

'''
