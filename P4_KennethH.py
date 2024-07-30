import string

def task1():
    print("Task 1")
    wordCount = 0
    lineCount = 0
    fileAttempts = 0
    wordSet = set()
    wordDict = dict()
    sortedWordDict = dict()
    fileRead = False
    while fileAttempts < 3:
        try:
            inputFileName = input("Input file name: ") # Ex. sample.txt
            infile = open(inputFileName, "r")
            line = infile.readline()
            while line != "":
                lineCount += 1
                words = line.rsplit(" ")
                for word in words:
                    word = word.rstrip()
                    newWord = ""
                    for w in word:
                        if w.isdigit(): #if a word has a digit at all it is no longer considered a word
                            newWord = ""
                            break
                        if w not in string.punctuation: #remove punctuation
                            newWord += w.lower()
                    if newWord != "": #given that a word was present
                        wordCount += 1
                        if newWord not in wordSet: # if a new word
                            wordDict.update({newWord: 1})
                            wordSet.add(newWord)
                        else: #if word already existed
                            wordDict[newWord] = wordDict[newWord] + 1
                line = infile.readline()
            print("The file contained: " + str(wordCount) + " words.")
            print("The file contained: " + str(lineCount) + " lines.")
            #print(wordSet)
            for key in sorted(wordDict, key=wordDict.get, reverse = True): #sorts dictionary
                sortedWordDict[key] = wordDict[key]
            print(sortedWordDict)
            print()
            fileAttempts = 4
        except FileNotFoundError: #error for file not existing
            fileAttempts += 1
            print("File Not Found Error: This file does not exist.")
    if fileAttempts == 3:
        print("File not found exiting program.")

'''
Task 1
128
12
: 2, 'data': 2, 'into': 2, 'high': 1, 'level': 1, 'general': 1, 'purpose': 1, 'language': 1, 'design': 1, 'philosophy': 1, 'emphasizes': 1,
 'code': 1, 'readability': 1, 'consistently': 1, 'ranks': 1, 'as': 1, 'one': 1, 'most': 1, 'popular': 1, 'languages': 1, 'field': 1, 
 'science': 1, 'uses': 1, 'statistical': 1, 'techniques': 1, 'give': 1, 'programs': 1, 'ability': 1, 'past': 1, 'experiences': 1, 
 'improve': 1, 'how': 1, 'they': 1, 'perform': 1, 'specific': 1, 'tasks': 1, 'you': 1, 'will': 1, 'steps': 1, 'necessary': 1, 'create': 1, 
 'successful': 1, 'application': 1, 'with': 1, 'scikit': 1, 'library': 1, 'making': 1, 'studying': 1, 'statistics': 1, 'step': 1, 
 'direction': 1, 'artificial': 1, 'intelligence': 1, 'program': 1, 'analyses': 1, 'learns': 1, 'predict': 1, 'outcome': 1, 'get': 1, 
'ready': 1, 'dive': 1, 'world': 1, 'by': 1, 'using': 1}

Task 1
Input file name: sample.txt
The file contained: 150 words.
The file contained: 20 lines.
{'the': 14, 'is': 5, 'of': 5, 'and': 5, 'all': 4, 'has': 4, 'a': 3, 'in': 3, 'testing': 2, 'across': 2, 'to': 2, 'made': 2,
 'upon': 2, 'hat': 2, 'an': 2, 'by': 2, 'one': 1, 'two': 1, 'three': 1, 'todays': 1, 'forcast': 1, 'expecting': 1, 'heatwaves': 1,
 'california': 1, 'storms': 1, 'are': 1, 'likely': 1, 'appear': 1, 'whole': 1, 'east': 1, 'coast': 1, 'florida': 1, 'contact': 1,
'with': 1, 'atlantis': 1, 'declared': 1, 'independence': 1, 'pastafarianism': 1, 'resurgence': 1, 'italy': 1, 'jabberwock': 1, 
'did': 1, 'gyre': 1, 'gimble': 1, 'wabe': 1, 'mimsy': 1, 'were': 1, 'borogroves': 1, 'mome': 1, 'raths': 1, 'outgrabe': 1, 
'petter': 1, 'pann': 1, 'pickled': 1, 'peppers': 1, 'plum': 1, 'pudding': 1, 'came': 1, 'whiffling': 1, 'through': 1, 'tulgey': 1, 
'wood': 1, 'burbled': 1, 'way': 1, 'i': 1, 'am': 1, 'running': 1, 'out': 1, 'things': 1, 'say': 1, 'santa': 1, 'not': 1, 'real': 1, 
'kids': 1, 'queen': 1, 'england': 1, 'taken': 1, 'place': 1, 'beyond': 1, 'her': 1, 'throne': 1, 'bibble': 1, 'bramble': 1, 
'shrinkley': 1, 'shore': 1, 'cat': 1, 'wears': 1, 'harry': 1, 'potter': 1, 'ok': 1, 'fantasy': 1, 'at': 1, 'best': 1, 'lord': 1, 
'rings': 1, 'gatekept': 1, 'window': 1, 'shopping': 1, 'dungeons': 1, 'dragons': 1, 'occult': 1, 'game': 1, 'that': 1, 'should': 1, 
'be': 1, 'played': 1, 'ages': 1}'''


def task2(runs = 1):
    print("Task 2")
    class Pair:
        def __init__(self, nx = 0, ny = 0):
            self.x = nx
            self.y = ny
        def __str__(self):
            return "<" + str(self.x) + ", " + str(self.y) + ">"
        def __add__(self, point):
            return Pair(self.x + point.x, self.y + point.y)
        def __mul__(self, point):
            return Pair(self.x * point.x, self.y * point.y)
        def __truediv__(self, point):
            return Pair(self.x * self.y - point.x * point.y, self.x * point.x - self.y * point.x)
    
    if runs == 1:
        print("Run 1")
        p1 = Pair(3, 2)
        p2 = Pair(1, 5)
        p3 = Pair(4, 3)
        print(p1)
        print(p2)
        print(p3)
        print("p1 + p2 = " + str(p1 + p2))
        print("p1 * p2 = " + str(p1 * p2))
        print("p2 / p2 = " + str(p2 / p2))
        print("p1 + p2 * p3 = " + str(p1 + p2 * p3))
        print("p1 * p2 / p3 + p1 = " + str(p1 * p2 / p3 + p1))
    if runs == 2:
        print("Run 2")
        p1 = Pair(4, -3)
        p2 = Pair(-6, 4)
        print(p1)
        print(p2)
        print("p1 + p2 = " + str(p1 + p2))
        print("p1 * p2 = " + str(p1 * p2))
        print("p2 / p2 = " + str(p2 / p2))
        print("p1 + p1 / p2 = " + str(p1 + p1 / p2))
        print("p1 * p2 + p1 = " + str(p1 * p2 + p1))
    print()

'''
Task 2
Run 1
<3, 2>
<1, 5>
<4, 3>
p1 + p2 = <4, 7>
p1 * p2 = <3, 10>
p2 / p2 = <0, -4>
p1 + p2 * p3 = <7, 17>
p1 * p2 / p3 + p1 = <21, -26>

Task 2
Run 2
<4, -3>
<-6, 4>
p1 + p2 = <-2, 1>
p1 * p2 = <-24, -12>
p2 / p2 = <0, 60>
p1 + p1 / p2 = <16, -45>
p1 * p2 + p1 = <-20, -15>
'''
        
def task3():
    print("Task 3")
    class Bicycle:
        def __init__(self, nGear = 10, nSpeed = 0):
            self.gear = nGear
            self.speed = nSpeed
        def applyBrake(self, decrement = 0):
            self.speed -= decrement
        def speedUp(self, increment = 0):
            self.speed += increment
        def __str__(self):
            return "Number of gears are " + str(self.gear) + "\n" + "Speed of bicycle is " + str(self.speed) + "\n"
        def sound(self):
            print("Honk Honk")
        def stop(self):
            self.speed = 0

    class MountainBike(Bicycle):
        def __init__(self, nGear, nSpeed, startHeight = 5, light = False):
            super().__init__(nGear, nSpeed)
            self.seatHeight = startHeight
            self.lightOn = light
        def setHeight(self, newHeight):
            self.seatHeight = newHeight
        def __str__(self):
            if self.lightOn == True:
                return super().__str__() + "Seat height is " + str(self.seatHeight) + "\n" + "Light is on\n"
            else:
                return super().__str__() + "Seat height is " + str(self.seatHeight) + "\n" + "Light is off\n"
        def sound(self):
            print("VRRRRRRR")
        def headLightButton(self):
            if self.lightOn == False:
                self.lightOn = True
                print("Light is turned on")
            else:
                self.lightOn = False
                print("Light is turned off")
    
    mb = MountainBike(3, 100, 25)
    b = Bicycle(8, 50)
    print(mb)
    mb.sound()
    mb.applyBrake(20)
    mb.headLightButton()
    print(mb)
    mb.speedUp(10)
    print(mb)
    mb.stop()
    mb.headLightButton()
    print(mb)

    print(b)
    b.sound()
'''
Task 3
Number of gears are 3
Speed of bicycle is 100
Seat height is 25
Light is off

VRRRRRRR
Light is turned on
Number of gears are 3
Speed of bicycle is 80
Seat height is 25
Light is on

Number of gears are 3
Speed of bicycle is 90
Seat height is 25
Light is on

Light is turned off
Number of gears are 3
Speed of bicycle is 0
Seat height is 25
Light is off

Number of gears are 8
Speed of bicycle is 50

Honk Honk
'''
        


def main():
    task1();
    #task2(1);
    #task2(2);
    #task3();

if __name__ == '__main__':
    main()