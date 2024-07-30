from random import randrange
import re

def task1():
    x = 1
    choice = -1
    usernames1 = ('lyang', 'kSimon', 'danny', 'tomatcpp', 'csDept', 'CoScpp', 'broncoWins', 'ponyExp', 'BldgAndRooms', 'helloKitty')
    passwords1 = ['sheCodes#123', 'catchAllGood1%', '@my2Choices', '123abc;;;', 'Hello2Monday$', 'GoodFriday@Cpp2', 'CS2520@Python',
                   'JavaIsHot2!', '2ManyRainingDays!', '1Startup@Starbucks']
    usernames2 = ('testMcgee', 'potatomato', 'MrKippling', 'radisHFe', 'Magica', 'Jessica', 'Anned', 'Meowsicle', 'Lunaom', 'Otomotone', 'Expreso', 'mawetao')
    passwords2 = ['hemIf#42', 'hemIf#32', 'hasdfsdemIf#4njv2', 'asdfhelkFf#12', 'claF%009', 'waefkjnFPEOK@4',
                  'Flemadi%23', 'miFkethk#5', 'Ketch$9asd', 'Yfeukn%k3', 'Eknawefi%93', 'aFEQopk#95']
    print("Task #1")

    # login method for user
    def login(data):
        check = False
        count = 0
        # 3 attempts, user enters username and password
        while ((check == False) or count == 3) :
            print("="*25)
            name = input("Input your username: ")
            password = input("Input your password: ")
            if name in data : #if username exists in dictionary
                if data.get(name) == password : # if password matches dictionary
                    print("Login successful! Welcome " + name)
                    check = True
                else : # password did not match dictionary
                    print("Incorrect password try again")
            else :#username did not match dictionary
                print("Username does not exist try again")
            count += 1
            if count == 3 : #too many tries
                print("Maximum tries exceeded exiting")
    
    # attempt to add user to dictionary
    def newUser(data):
        check = False
        passwordCheck = False
        while check == False :
            print("="*25)
            name = input("Enter a username: ") #take username
            while passwordCheck == False :
                passwordCheck == False
                print("")
                print("Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.")
                password = input("Enter a password: ")
                # regex, at least 8 chars, 
                # at least 1 lowercase
                # at least 1 uppercase
                # at least 1 number
                # at least 1 special character
                x = re.search(r"(?=^.{8,}$)((?=.*[0-9])(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", password)
                if x :
                    passwordCheck = True
                else :
                    #password did not pass check
                    print("Invalid passwords, please review password requirements.")
            # username checks
            y = re.search("^[a-zA-Z]+$", name)
            if name in data : #username already exists
                print("This username has already been chosen please choose another one.")
                break
            if y : #username accepted
                print("New user accepted")
                data[name] = password
                check = True
            #manual exit
            if (check == False):
                exit = int(input("Enter 0 if you wish to exit."))
                if (exit == 0) :
                    print("Returning to main prompt.")

    #changes password of a given username
    def passChange(name, data):
        check = False
        print("="*25)
        print("Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.")
        newPass = input("Enter a new password: ")
        # check password requirements
        x = re.search(r"(?=^.{8,}$)((?=.*[0-9])(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$", newPass)
        if x:
            if newPass == data.get(name): #password is the same as the one in the dictionary
                print("Password already in use.")
            else :
                data[name] = newPass
                check = True
        else : #password fails requirements
            print("Password does not meet requirements for the system.")
        return check
  
    while x < 2 :
        if (x == 1) :
            usernames = usernames2
            passwords = passwords2
        # if (x == 2) :
        #     usernames = usernames2
        #     passwords = passwords2
        data = {}
        for a, b in (list(zip(usernames, passwords))) :
            data.setdefault(a, b)
        while (choice != 4) :
            # print("="*25)
            # print(data)
            print("="*25)
            print("What would you like to do? Enter the corresponding number value.")
            print("1) Login")
            print("2) Create Account")
            print("3) Change Password")
            print("4) Exit")
            choice = int(input("Enter option: "))
            if choice == 1 :
                login(data)
            if choice == 2 :
                newUser(data)
            if choice == 3 :
                name = input("Enter your username: ")
                if name in data :
                    check = passChange(name, data)
                if check == False :
                    print("Failed to update password.")
                if check == True :
                    print("Password updated.")
            if choice == 4 :
                print("Exiting program.")
        
        x += 1
'''
Test #1
Task #1
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 1
=========================
Input your username: lyang
Input your password: motley
Incorrect password try again
=========================
Input your username: lyang
Input your password: sheCodes#123
Login successful! Welcome lyang
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 2
=========================
Enter a username: kimperly

Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a password: jckef
Invalid passwords, please review password requirements.

Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a password: Myasdfi$23
New user accepted
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 3
Enter your username: kimperly
=========================
Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a new password: Myasdfi$23
Password already in use.
Failed to update password.
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 3
Enter your username: mofe
Failed to update password.
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 3
Enter your username: lyang
=========================
Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a new password: TheyCod#321
Password updated.
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 4
Exiting program.

Test #2
Task #1
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 1
=========================
Input your username: testasdfpo
Input your password: awepokf
Username does not exist try again
=========================
Input your username: testMcgee
Input your password: hemIf#42
Login successful! Welcome testMcgee
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 2
=========================
Enter a username: testMcgee

Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a password: PLEFK%k3mf
This username has already been chosen please choose another one.
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 2
=========================
Enter a username: mcGeesTest

Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a password: FEPOkfkler$2
New user accepted
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 3
Enter your username: mcGeesTest
=========================
Passwords must be at least 8 characters long, contain at least 1 uppercase letter, lowercase letter, number, and special character.
Enter a new password: Simple%23
Password updated.
=========================
What would you like to do? Enter the corresponding number value.
1) Login
2) Create Account
3) Change Password
4) Exit
Enter option: 4
Exiting program.
'''

def task2():
    print("Task #2")
    x = 1
    L1 = []
    L2 = []

    def prime_generator():
        n=2
        while True:
            if isPrime(n):
                yield(n)
            n += 1

    def isPrime(n):
        # iterate from 2 to n/2
        for d in range(2, int(n/2)+1):
            # if n is divisible by any number between 2 and n/2 it is not prime
            if (n % d) == 0:
                return False
        return True
    
    while x < 3:
        print()
        print("Test#" + str(x))
        p = prime_generator()
        # generate list numbers
        for i in range(50) :
            L1.append(next(p))
            L2.append(randrange(0, 101))
            next(p)

        #convert lists to sets
        S1 = set(L1) 
        S2 = set(L2)
        print("S1 length: ") 
        print(len(S1))
        print("S2 length: ") 
        print(len(S2))

        # merge sets
        R1 = S1.intersection(S2)
        print("R1 length: ") 
        print(len(R1))
        # unique = union - intersection
        temp = S1.union(S2)
        R2 = temp.difference(R1)
        print("R2 length: ") 
        print(len(R2))
        x += 1
        # clear for next test
        S1.clear()
        S2.clear()
        R1.clear()
        R2.clear()
        temp.clear()
        L1.clear()
        L2.clear()
'''
Task #2

Test#1
S1 length:
50
S2 length:
40
R1 length:
5
R2 length:
80

Test#2
S1 length:
50
S2 length:
40
R1 length:
1
R2 length:
88
'''   

def task3():
    print("Task #3")

    def tryTuple(*args):
        resultuple = (min(args), max(args), len(args))
        return resultuple
    
    print(tryTuple(3, 5, 12, 9, 1, 2))
    print(tryTuple("hi", "bye", "happy"))
    print(tryTuple(["cat", 3], ["dog", 2]))

'''
Task #3
(1, 12, 6)
('bye', 'hi', 3)
(['cat', 3], ['dog', 2], 2)
'''


def main():
    #task1();
    #task2();
    task3();

if __name__ == '__main__':
    main()