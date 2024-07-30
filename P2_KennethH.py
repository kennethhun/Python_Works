import math
import time

def task1():
    x = 1
    i = 1
    print("Task #1")
    while x < 7:
        print("Test#" + str(x))
        val = float(input("To calculate the value of sin(x) please enter a float value for x: "))
        # recursion function 
        def sinRecursion(n, currentTerm, total, i):
            mathVal = math.sin(n) #value from imported math
            difference = abs(mathVal - total) # difference between imported math and calced math
            if (mathVal == total) or ((difference / abs(mathVal)) < 0.000001):
                # print out iterations, calced and imported math outputs, and difference
                print("It takes %d rounds of iterations to calculate sin(%f)" % (i, n))
                print("Estimated result: " + str(total))
                print("Sin(%f) from math library: " % n + str(total))
                print("Difference: " + str(difference))
            elif (i > 99):
                print("-=Error terminating at 100 iterations=-")
                print("It takes %d rounds of iterations to calculate sin(%f)" % (i, n))
                print("Estimated result: " + str(total))
                print("Sin(%f) from math library: " % n + str(total))
                print("Difference: " + str(difference))
            else:
                # generate next term and add to collective total, then go to next iteration
                nextTerm = (-1) * (n**2) / (2*i*(2*i+1)) * currentTerm
                total += nextTerm
                sinRecursion(n, nextTerm, total, i+1)
        # recursion function call
        sinRecursion(val, val, val, i)
        print()
        x += 1

'''
Task #1
Test#1
To calculate the value of sin(x) please enter a float value for x: 0.0
It takes 1 rounds of iterations to calculate sin(0.000000)
Estimated result: 0.0
Sin(0.000000) from math library: 0.0
Difference: 0.0

Test#2
To calculate the value of sin(x) please enter a float value for x: 1.5709
It takes 6 rounds of iterations to calculate sin(1.570900)
Estimated result: 0.9999999383187816
Sin(1.570900) from math library: 0.9999999383187816
Difference: 5.630715160798161e-08

Test#3
To calculate the value of sin(x) please enter a float value for x: -3.14
It takes 10 rounds of iterations to calculate sin(-3.140000)
Estimated result: -0.0015926523931608435
Sin(-3.140000) from math library: -0.0015926523931608435
Difference: 5.233259847605559e-10

Test#4
To calculate the value of sin(x) please enter a float value for x: -0.7854
It takes 4 rounds of iterations to calculate sin(-0.785400)
Estimated result: -0.7071077682415541
Sin(-0.785400) from math library: -0.7071077682415541
Difference: 3.116179194684321e-07

Test#5
To calculate the value of sin(x) please enter a float value for x: 6.28
It takes 15 rounds of iterations to calculate sin(6.280000)
Estimated result: -0.0031853011537927045
Sin(6.280000) from math library: -0.0031853011537927045
Difference: 6.393452859146387e-10

Test#6
To calculate the value of sin(x) please enter a float value for x: -4.32
It takes 10 rounds of iterations to calculate sin(-4.320000)
Estimated result: 0.9239985765513766
Sin(-4.320000) from math library: 0.9239985765513766
Difference: 4.1782818871460847e-07
'''
# takes a user inputted string, finds its length returns string
def get_input():
    userString = input("Enter a sentence or phrase: ")
    print(len(userString))
    return(userString)
# finds the total number of letters in a given string not counting whitespace
def get_num_of_letters(userString):
    charCount = 0
    for x in userString:
        if x.isalpha():
            charCount += 1
    print("Total number of characters: " + str(charCount))
# removes all whitespace in a string
def output_without_whitespace(userString):
    tempString = ''
    for x in userString:
        if x.isalpha():
            tempString += x
    print("String with no whitespace: " + tempString)
# finds the first letter of every word in a string and generates a fully uppercase string
def get_first(userString):
    prevVal = ''
    tempString = userString[0].upper()
    for x in userString:
        if (prevVal == ' ') or (prevVal == '\t'):
            if (x != ' ') and (x != '\t'):
                tempString += x.upper()
        prevVal = x
    print("The first letters the string's words in uppercase: " + tempString)

def task2():
    print("Task #2")
    x = 1
    while x < 4:
        # function calls
        print("Test#" + str(x))
        userString = get_input()
        print("You entered: " + userString)
        get_num_of_letters(userString)
        output_without_whitespace(userString)
        get_first(userString)
        x += 1
        print()
'''
Task #2
Test#1
Enter a sentence or phrase: The only thing we have to fear is fear itself
45
You entered: The only thing we have to fear is fear itself
Total number of characters: 36
String with no whitespace: Theonlythingwehavetofearisfearitself
The first letters the string's words in uppercase: TOTWHTFIFI

Test#2
Enter a sentence or phrase: Double tab          testing for errors.
31
You entered: Double tab         testing for errors.
Total number of characters: 25
String with no whitespace: Doubletabtestingforerrors
The first letters the string's words in uppercase: DTTFE

Test#3
Enter a sentence or phrase: Double  space  test  for  incorrect  outputs.
45
You entered: Double  space  test  for  incorrect  outputs.
Total number of characters: 34
String with no whitespace: Doublespacetestforincorrectoutputs
The first letters the string's words in uppercase: DSTFIO
'''
# generates a prime number
def prime_generator():
    n=2
    while True:
        if isPrime(n):
            yield(n)
        n += 1
# checks if a number is prime or not
def isPrime(n):
    # iterate from 2 to n/2
    for d in range(2, int(n/2)+1):
        # if n is divisible by any number between 2 and n/2 it is not prime
        if (n % d) == 0:
            return False
    return True

def task3():
    p = prime_generator()
    print("Print the first 50 prime numbers followed by 101st and 1100nth.")
    # generate 1100 prime numbers
    for i in range(1100):
        if i < 51: #print first 50
            print(str(i + 1) + ": " + str(next(p)))
        elif i == 100: # print 101st and start timer
            print("...")
            print(str(i + 1) + ": " + str(next(p)))
            t0 = time.time()
        elif i == 1099: # print 1100th and print out execution time in seconds
            print(str(i + 1) + ": " + str(next(p)))
            t = time.time() - t0
            print("The execution time in seconds between the 101st prime number and 1100nth prime number is: " + str(t))
        else: # generate next prime number
            next(p)
'''
Print the first 50 prime numbers followed by 101st and 1100nth.
1: 2
2: 3
3: 5
4: 7
5: 11
6: 13
7: 17
8: 19
9: 23
10: 29
11: 31
12: 37
13: 41
14: 43
15: 47
16: 53
17: 59
18: 61
19: 67
20: 71
21: 73
22: 79
23: 83
24: 89
25: 97
26: 101
27: 103
28: 107
29: 109
30: 113
31: 127
32: 131
33: 137
34: 139
35: 149
36: 151
37: 157
38: 163
39: 167
40: 173
41: 179
42: 181
43: 191
44: 193
45: 197
46: 199
47: 211
48: 223
49: 227
50: 229
51: 233
...
101: 547
1100: 8831
The execution time in seconds between the 101st prime number and 1100nth prime number is: 0.19955730438232422
'''    

def main():
    task1();
    #task2();
    #task3();

if __name__ == '__main__':
    main()