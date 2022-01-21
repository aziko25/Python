"""
# 1) INTRO TO PYTHON
"""

"""
# 2) VARIABLES
name = "Aziz"
print("Hello "+name)
print(type(name)) #"type" shows the variable of the value
first_name = "Aziko"
last_name = "Abdujabbarov"
full_name = first_name +" "+ last_name
print("Hello "+full_name)

age = 17
age += 1
print(age)
print(type(age))
print("Your age is: "+str(age)) #we have to change all of the non-string variables into string to output 

height = 250.5
print(type(height))
print(height)
print("Your height is: "+str(height)+"cm")

human = True
notHuman = False
print(type(human))
print("Are you a human: "+str(human))
"""

"""
# 3) MULTIPLE ASSIGNMENT
name = "Aziz"
age = 21
attractive = True
height = 180.5

#OR

#name, age, attractive, height = "Aziz", 21, True, 180.5

print(name)
print(age)
print(attractive)
print(height)
"""

"""
# 4) STRING METHODS
name = "aziz"
print(len(name)) # SHOWS HOW MANY CHARACTERS IN THE STRING
print(name.find("a")) # SHOWS IN WHICH ORDER THE CHAR IS STAYING (STARTS WITH 0)
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha()) # CHECKS IF THERE IS ALPHABETICAL CHARS *DASHES ARE NOT ALPHABETICAL CHARS*
print(name.count("z"))
print(name.replace("z","a"))
print(name*3)
"""

"""
# 5) TYPE CASTING = CONVERT THE DATA TYPE OF A VALUE TO ANOTHER DATA TYPE
x = 1
y = 2.0
z = "3"

print(type(x))
print(type(y))
print(type(z))

z = float(z)

print(x)
print(int(y))
print(z*3)
"""


"""
# 6) USER INPUT
name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
age += 1
print()
print("Hello "+name)
print("You are "+str(age)+" years old")
print("Your height is: "+str(height)+" cm")
"""

"""
# 7) MATH FUNCTIONS
import math

num = 420
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi)) # IT WILL ALWAYS ROUND THE NUMBER UP
print(math.floor(pi)) # IT WILL ALWAYS ROUND THE NUMBER DOWN
print(abs(pi)) # IT WILL TURN A NEGATIVE NUMBER TO POSITIVE
print(pow(pi, 2)) 
print(math.sqrt(num))
print(max(x,y,z)) # FINDS THE LARGEST NUMBER BETWEEN VARIABLES
print(min(x,y,z)) # FINDS THE SMALLEST NUMBER BETWEEN VARIABLES
"""

"""
# 8) STRING SLICING = CREATE A SUBSTRING BY EXTRACTING ELEMENTS FROM ANOTHER STRING 

# INDEXING:
name = "Aziz Abdujabbarov"

first_name = name[0:4] # WE ARE SAYING TO THE COMPUTER, THAT WE NEED ONLY FIRST 5 CHARACTERS FROM A STRING
last_name = name[4:] # STARTS FROM THE DASH, BECAUSE DASH IS A 5 CHAR AND IF AFTER ":" EMPTY THEN IT WILL INCLUDE ALL 
funky_name = name[::2] # COUNTS EACH 2 CHARACTER
reversed_name = name[::-1] # REVERSES A STRING

print(first_name + last_name +" "+ funky_name +" "+ reversed_name)

# SLICING:
website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8,-4) # SO WE STARTED FROM THE 8TH CHARACTER WHICH IS "g" AND DELETED THE LAST 4 CHARS AFTER COMMA

print(website1[slice])
print(website2[slice])
"""

"""
# 9) IF STATEMENTS
age = int(input("How old are you?: "))

if age >= 18 and age <= 99:
    print("You are a teenager")
elif age < 0:
    print("You haven't born yet")
elif age == 100:
    print("You are a century old")
else:
    print("You are a baby")
"""

"""
# 10) LOGICAL OPERATORS
temp = int(input("What is temperature outside?: "))


if temp >= 15 and temp <= 30:
    print("It's normal weather outside")
elif (temp > 30 and temp < 90) or temp < 0:
    print("Stay at home")
elif not temp >= 91:
    print("ITS ok")

"""

"""
# 11) WHILE LOOPS
name = None
while not name:
    name = input("Enter Your name: ")

print("Hello "+name)

"""

"""
# 12) FOR LOOPS
import time
for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Azizkhuja Abdujabbarov":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy Eid")
"""

"""
# 13) NESTED LOOPS
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end = " ")
    print()
"""

# 14) BREAK, CONTINUE, PASS
"""
while True:
    name = input("Enter your name: ")
    if name != "":
        break 
"""

"""
phone_number = "123-456-7890" 

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
print()
"""

"""
for i in range(1,20+1):
    if i == 13:
        pass
    else:
        print(i)
"""

"""
# 15) LISTS
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food)
food[0] = "sushi"

print(food[0])

food.append("ice cream") # ADDS AN ITEM TO THE END OF THE LIST
food.remove("hotdog")
food.pop() # IT REMOVES THE LAST ELEMENT IN THE LIST
food.insert(0,"cake") # INSERTS AN ITEM TO THE LIST BY THE INDEX
food.sort() # SORTS A LIST BY ALPHABETICAL ORDER
# food.clear() # DELETES A LIST

for x in food:
    print(x) 
"""

"""
# 16) 2D LISTS = A LIST OF LISTS
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[2][1]) # FIRST ONE IS FOR THE LIST IN ORDER AND THE SECOND ONE IS FOR THE ORDER IN THE CASE

for x in food:
    print(x, end=" ")
    print()
"""

"""
# 17) TUPLES = COLLECTION WHICH IS ORDERED AND UNCHANGEABLE USED TO GROUP TOGETHER RELATED DATA
student = ("Azizkhuja",21,"male")

print(student.count("Azizkhuja")) # COUNTS HOW MANY TIMES THE NAME WAS USED
print(student.index("male")) # SHOWS IN WHICH ORDER IT HAS BEEN WRITTEN

for x in student:
    print(x)

if "Azizkhuja" in student:
    print("Aziko is here!")
"""

"""
# 18) SETS = COLLECTION WHICH IS UNORDERED AND UNINDEXED. NO DUPLICATE VALUES

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.clear()
utensils.update(dishes) # ADDS DISHES TO UTENSILS
dinner_table = dishes.union(utensils) # ADDS UTENSILS TO DISHES IN THE OTHER NEW SET


for x in utensils:
    print(x, end=" ")

print()

print(dishes.difference(utensils))
print(utensils.intersection(dishes)) # SHOWS AN ITEM THAT CONSISTS IN BOTH SETS
"""

"""
# 19) DICTIONARIES
capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
# capitals.clear()

print(capitals['Russia'])
print(capitals.get('Germany')) # CHECKS IF THERE EXISTS
print(capitals.keys()) # OUTPUTS ALL OF THE KEYS IN DICTIONARY
print(capitals.values())
print(capitals.items())
print()

for key, value in capitals.items():
    print(key,"-", value)
"""

"""
# 20) INDEXING
name = "aziz Abdujabbarov!"

if(name[0].islower()):
    name = name.capitalize()

first_name = name[0:4].upper()
last_name = name[4:].upper()
last_character = name[-1]

print(first_name + last_name)
print(last_character)
"""

"""
# 21) FUNCTIONS
def hello(name, age):
    print("hello! "+name+" "+str(age))
    print("have a nice day!")

hello("aziz", 21)
"""

"""
# 22) RETURN STATEMENT
def multiply(num1, num2):
    return num1 * num2

x = multiply(6, 10)
print(x)
"""

"""
# 23) KEYWORD ARGUMENTS
def hello(first, middle, last):
    print(first+" "+middle+" "+last)

hello(last="Aziz", first="Xasanovic", middle="Abdujabbarov")
"""

"""
# 24) NESTED FUNCTION CALLS
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

# OR

print(abs(round(float(input("Enter a whole positive number: ")))))
"""

"""
# 25) VARIABLE SCOPE = VARIABLES ARE AVAILABLE ONLY INSIDE THE FUNCTION
name = "Aziko" # GLOBAL SCOPE
def display_name():
    name = "Aziz" # LOCAL SCOPE
    print(name)

display_name()
print(name)
"""

"""
# 26) ARGS = PARAMETER THAT WILL PACK ALL ARGUMENTS INTO A TUPLE
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
        
print(add(1,2,3,4,5,6,7,8,9,10))

# OR IF WE WANT TO CHANGE THE NUMS LIKE IN THE LIST, THEN:

def add1(*args1):
    sum = 0
    args1 = list(args1)
    args1[0] = 50
    for i in args1:
        sum += i
    return sum
        
print(add1(1,2,3,4,5,6,7,8,9,10))
"""

"""
# 27) **KWARGS = PARAMETER THAT WILL PACK ALL ARGUMENTS INTO A DICTIONARY
def hello(**kwargs):
    print("Hello,", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(title="Mr.", first="Aziz", last="Xasanovic", middle="Abdujabbarov")
"""

"""
# 28) STRING FORMAT
animal = "cow"
item = "moon"
animal2 = "www"
item2 = "eee"

print("The "+animal+" jumped over the "+item)

# OR WE CAN USE STRING FORMAT:

print("The {} jumped over the {}".format("cow", "moon"))
print("The {1} jumped over the {0}".format("cow", "moon"))
print("The {animal1} jumped over the {item1}".format(animal1="cows", item1="moons"))

text = "The {} jumped over the {}"
print(text.format(animal2, item2))

name = "Aziz"

print("Hello, my name is {:>10} Abdujabbarov".format(name)) # WRITES THE NAME AFTER MAKING 10 DASHES TO RIGHT
print("Hello, my name is {:^10} Abdujabbarov".format(name)) # ALIGNS THE ITEM AT THE CENTER OF 10 DASHES
print("Hello, my name is {:<10} Abdujabbarov".format(name)) # ALLOCATES 10 SPACES TO RIGHT AFTER WRITING THE NAME

number = 3.14142
number1 = 1000

print("The number pi is {:.2f}".format(number)) # CHANGES THE NUM TO A FLOAT NUMBER
print("The number pi is {:.3f}".format(number)) # WRITES 3 DIGITS AFTER A COMMA
print("The number is {:,}".format(number1)) # PUTS A COMMA IN APPROPRIATE PLACE IN BIG NUMBERS
print("The number is {:b}".format(number1)) # CHANGES THE NUM TO A BINARY 
print("The number is {:o}".format(number1)) # CHANGES THE NUM TO OCTAL
print("The number is {:X}".format(number1)) # CHANGES THE NUM TO A HEXIDECIMAL NUM
print("The number pi is {:E}".format(number)) # CHANGES THE NUM TO A SCIENTIFIC NOTATION
"""

"""
# 29) RANDOM NUMBERS
import random

x = random.randint(1,6) # WHOLE NUMBER BETWEEN 1 AND 6
y = random.random() # FLOAT NUMBER

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(x)
print(y)
print(z)
print(cards)
"""

"""
# 30) EXCEPTION HANDLING
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("something went wrong!")
else:
    print(result)
finally:
    print("This will always execute!")
"""

"""
# 31) FILE DETECTION
import os

path = "C:\\Users\\User\\Pictures\\DATA STRUCTURES\\INTRO TO GRAPHS.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")
"""

"""
# 32) READ A FILE
try:
    with open('TextFile1.txt') as file:
       print(file.read())
except FileNotFoundError:
    print("That file was not found!")
"""

"""
# 33) WRITE A FILE
text = input("Write some text: ")

with open('TextFile1.txt', 'a') as file: # 'a' is to add a text for the existing and 'w' is to write a new one
    file.write(text)
"""

"""
# 34) COPY A FILE
import shutil

shutil.copyfile('TextFile1.txt', 'copytest.txt') # src, dst (*2 arguments could be*) 
# shutil.copy2('TextFile1.txt', 'C:\\blah\\blah\blahblah\\') 
"""

"""
# 35) MOVE A FILE
import os

source = "TextFile1.txt"
destination = "C:\\Users\\User\\Downloads\\TextFile1.txt"

try:
    if os.path.exists(destination):
        print("There is already file there!")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
"""

"""
# 36) DELETING A FILE
import os
import shutil

path = 'TextFile1.txt'

try:
    os.remove(path) # DELETE A FILE
    os.rmdir(path) # DELETE A FILE OR EMPTY FOLDER
    shutil.rmtree(path) # DELETES FILES OR FOLDERS
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have a permission to delete that!")
except OSError:
    print("That folder contains files!")
else:
    print(path+" DELETION WAS SUCCESSFUL!")
"""

"""
# 37) MODULES
from module1 import bye, hello
help("modules")

hello()
bye()
"""

"""
# 38) ROCK, PAPER, SCISSORS GAME]
import random

while True:

    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("TIE!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU LOSE!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("TIE!")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("TIE!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU LOSE!")
    elif player == "paper":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("TIE!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU LOSE!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("YOU WIN!")
    
    play_again = input("Play again? (Y/N): ").lower()

    if play_again != "y":
        break

print("Bye!")
"""

"""
# 39) QUIZ GAME
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ------------------------------------
def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# ------------------------------------
def display_score(correct_guesses, guesses):
    print("--------------------------")
    print("RESULTS:")
    print("--------------------------")
    print("Answers: ", end="|")
    for i in questions:
        print(questions.get(i), end="|")
    print()

    print("Guesses: ", end="|")
    for i in guesses:
        print(i, end="|")
    print()
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: "+str(score)+"%")

# ------------------------------------
def play_again():
    
    response = input("Do You Want To Play Again?: (Y/N)").upper()

    if response == "Y":
        return True
    else:
        return False

questions = { 
    "Who created Python?: " : "A",
    "What year Python was created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
    }

options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Bye!")
"""

"""
# 40) OOP
from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print()

car_1.drive()
car_1.stop()

print()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

print()

car_2.drive()
car_2.stop()
"""

"""
# 41) CLASS VARIABLES
from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

car_1.wheels = 2
Car.wheels = 6

print(car_1.wheels)
print(car_2.wheels)

print(Car.wheels)
"""

"""
# 42) INHERITANCE
class Animal:

    alive = True
    
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()
"""

"""
# 43) MULTI-LEVEL INHERITANCE
class Organism:
    alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()
"""

"""
# 44) MULTIPLE INHERITANCE
class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
"""

"""
# 45) METHOD OVERRIDING
class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()

rabbit.eat()
"""

"""
# 46) METHOD CHAINING
class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive this car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()

car.turn_on().drive()

car.brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
"""

"""
# 47) SUPER FUNCTION
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def Area(self):
        return self.length*self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.length*self.width*self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.Area())
print(cube.Volume())
"""

"""
# 48) ABSTRACT CLASSES
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stopped this motorcycle")

car = Car()
moto = Motorcycle()

car.go()
car.stop()

moto.go()
moto.stop()
"""

"""
# 49) OBJECTS AS ARGUMENTS
class Car:
    color = None

class Moto:
    color = None

def change_color(car, color):
    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Moto()

change_color(car_1, "red")
change_color(car_2, "green")
change_color(car_3, "blue")

change_color(bike_1, "white")

print(car_1.color)
print(car_2.color)
print(car_3.color)

print(bike_1.color)
"""

"""
# 50) DUCK TYPING

class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
person.catch(duck)
"""

"""
# 51) WALRUS OPERATOR

print(happy := True)

food = list()
while food := input("What food do you like?: ") != "quit":
    food.append(food)
"""

"""
# 52) FUNCTIONS TO VARIABLES
def hello():
    print("Hello")

print(hello)
hi = hello
print(hi)

hello()
hi()

say = print

say("Hi")
"""

"""
# 53) HIGHER ORDER FUNCTION
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))
"""

"""
# 54) LAMBDA
def double(x):
    return x * 2

print(double(5))

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5, 6))
print(add(5, 6, 7))
print(full_name("Aziz", "Abdujabbarov"))
print(age_check(18))
"""

"""
# 55) SORT
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

students.sort(reverse=True) # IT WILL SORT FROM THE END OF THE ALPHABETICAL. 
students.sort() # WILL SORT BY ALPHABETICAL ORDER
sorted_students = sorted(students)
sorted_students = sorted(students, reverse = True) # WILL REVERSE

for i in students:
    print(i, end=" ")

print()

for i in sorted_students:
    print(i, end=" ")

print()
print()

students1 = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

students2 = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

grade = lambda grades: grades[1] # WE GIVE THE INDEX OF THE ITEMS. GRADES ARE 2 ITEM AFTER NAMES, SO INDEX 1
students1.sort(key=grade)
students2.sort(key=grade, reverse=True)

# OR

sorted_students = sorted(students, key=grade)

for i in students1:
    print(i)

print()
print()

for i in students2:
    print(i)
"""

"""
# 56) MAP
store = [("shirts", 20.00),
         ("pants", 25.00),
         ("jackets", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
to_sum = lambda data: (data[0], data[1]*10700)

store_euros = list(map(to_euros, store))
store_sum = list(map(to_sum, store))

for i in store_euros:
    print(i)

for i in store_sum:
    print(i)
"""

"""
# 57) FILTER
friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 20)]

age = lambda age: age[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
"""

"""
# 58) REDUCE
import functools

letters = ["H", "E", "L", "L", "O", " ", "A", "Z", "I", "K", "O"]
word = functools.reduce(lambda x, y:x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
"""

"""
# 59) LIST COMPREHENSIONS
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# OR

squares = [i * i for i in range(1, 11)]
print(squares)
# ...

students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda x: x >= 60, students))

print(passed_students)

# OR

passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)
"""

"""
# 60) DICTIONARY COMPREHENSIONS
cities_in_F = {'New York' : 32, 
               'Boston' : 75,
               'Los-Angeles' : 100,
               'Chicago' : 50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

weather = {'New York' : "snowing",
           'Boston' : "sunny",
           'Los-Angeles' : "sunny",
           'Chicago' : "cloudy"}

sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
print(sunny_weather)

cities = { 'New York' : 32, 
           'Boston' : 75,
           'Los-Angeles' : 100,
           'Chicago' : 50 }

desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print(desc_cities)

#...

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities1 = { 'New York' : 32, 
           'Boston' : 75,
           'Los-Angeles' : 100,
           'Chicago' : 50 }

desc_cities1 = {key: check_temp(value) for (key,value) in cities1.items()}
print(desc_cities1)
"""

"""
# 61) ZIP FUNCTION
usernames = ["Aziz", "Aziko", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = dict(zip(usernames, passwords))
users1 = zip(usernames, passwords, login_date)

for (key,value) in users.items():
    print(key+" : "+value)

for i in users1:
    print(i)
"""

"""
# 62) IF _NAME_ == '__MAIN__'
import module1
print(__name__)
print(module1.__name__)

if __name__ == '__main__':
    print("running this module directly")
else:
    print("running other module indirectly")

def hello():
    print("Hello")
"""

"""
# 63) TIME MODULE
import time

print(time.ctime(100000000))
print(time.time()) # RETURN CURRENT SECONDS SINCE EPOCH
print(time.ctime(time.time())) # SHOWS CURRENT TIME

time_object = time.localtime()
# time_object = time.gmtime()

print(time_object) # SHOWS TIME OBJECTS
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y") # TIME STRUCTURE
print(time_object)

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0) # year, month, day, hours, minutes, secs, day of the week, year, dst
time_string = time.asctime(time_tuple)
print(time_string)
time_string1 = time.mktime(time_tuple)
print(time_string1)
"""

"""
# 64) THREADING
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")

def drink_coffee():
    time.sleep(4)
    print("You drank coffee")

def study():
    time.sleep(5)
    print("You finished studying")
    
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

eat_breakfast()
drink_coffee()
study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
"""

"""
# 65) DAEMON THREADS
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

x.setDaemon(True)

answer = input("Do you want to exit?")
"""

"""
# 66) MULTIPROCESSING
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(cpu_count()) # 12

    a = Process(target=counter, args=(12.5, ))
    b = Process(target=counter, args=(12.5, )) # I ACCELERATED THE PROCESSING
    c = Process(target=counter, args=(12.5, ))
    d = Process(target=counter, args=(12.5, ))
    e = Process(target=counter, args=(12.5, ))
    f = Process(target=counter, args=(12.5, )) # I ACCELERATED THE PROCESSING
    g = Process(target=counter, args=(12.5, ))
    h = Process(target=counter, args=(12.5, ))
    i = Process(target=counter, args=(12.5, ))
    j = Process(target=counter, args=(12.5, )) # I ACCELERATED THE PROCESSING
    k = Process(target=counter, args=(12.5, ))
    l = Process(target=counter, args=(12.5, ))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    i.start()
    j.start()
    k.start()
    l.start()
    
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()
    i.join()
    j.join()
    k.join()
    l.join()

    print("finished in:", time.perf_counter(), "seconds")

if __name__ == '__main__':
    main()
"""

"""
# 67) GUI WINDOWS
from tkinter import *

# WIDGETS = GUI ELEMENTS: BUTTONS, TEXTBOXES, LABELS, IMAGES
# WINDOWS = SERVES AS A CONTAINER TO HOLD OR CONTAIN THESE WIDGETS

window = Tk() # INSTANTIATE AN INSTANCE OF A WINDOW
window.geometry("840x840") # WIDTH, HEIGHT
window.title("FIRST GUI PROGRAM")

# icon = PhotoImage(file='5509317.jpg')
# window.iconphoto(True, icon) # FOR THE ICON
window.config(background="#5cfcff")

window.mainloop() # PLACE WINDOW ON COMPUTER SCREEN, LISTEN FOR EVENTS
"""

"""
# 68) LABELS FOR WINDOWS
from tkinter import *

window = Tk()

photo = PhotoImage(file='Momoshiki1.png')

window.geometry("840x840") # WIDTH, HEIGHT
window.title("FIRST GUI PROGRAM WITH LABEL")

label = Label(window, text="Hello World",
                      font=('Arial', 40, 'bold'), 
                      fg='#00FF00', 
                      bg='black',
                      relief=RAISED,
                      bd=15,
                      padx=20,
                      pady=20,
                      image=photo,
                      compound='bottom') # PUTS THE PHOTO BOTTOM IN THE LABEL
                       
label.pack() # PUTS A LABEL IN TOP AT THE CENTER
# label.place(x=0, y=0)

window.config(background="#5cfcff")

window.mainloop()
"""

"""
# 69) BUTTONS
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)
    print("You clicked the button")

window = Tk()

photo = PhotoImage(file='Momoshiki1.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black", # EVEN IF WE CLICK THE BACKGROUND WILL CHANGE TO THE COLOR WE GAVE
                state=ACTIVE,  # IT CAN BE DISABLED TO
                image=photo,
                compound='bottom') 

button.pack()

window.mainloop()
"""

"""
# 70) ENTRYBOX
from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED) # DISABLES AFTER WE SUMBIT THE TEXT

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*") # USEFUL FOR PASSWORDS

entry.insert(0, 'Example')
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
"""

"""
# 71) CHECKBOX
from tkinter import *

def display():
    if(x.get()):
        print("You agree")
    else:
        print("You don't agree")

window = Tk()

x = BooleanVar()

photo = PhotoImage(file="Momoshiki1.png")

check_button = Checkbutton(window, 
                           text="I agree",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=LEFT)

check_button.pack()

window.mainloop()
"""

"""
# 72) RADIO BUTTONS
from tkinter import *

window = Tk()

momoshiki_photo = PhotoImage(file="Momoshiki1.png")
juubidara_photo = PhotoImage(file="Juubidara.png")
isshiki_photo = PhotoImage(file="Isshiki1.png")

strongest_images = [momoshiki_photo, isshiki_photo, juubidara_photo]

food = ["Momoshiki", "Isshiki", "Madara"]

def choose():
    if(x.get()==0):
        print("You choosed Momoshiki as strongest in Naruto Verse")
    elif(x.get()==1):
        print("You choosed Isshiki as strongest in Naruto Verse")
    elif(x.get()==2):
        print("You choosed Madara as strongest in Naruto Verse")
    else:
        print("WRONG CHOOSE!")

x = IntVar()

label = Label(window, text="WHO IS STRONGEST?",
                      font=('Arial', 20, 'bold'), 
                      fg='#00FF00', 
                      bg='black',
                      relief=RAISED,
                      bd=15,
                      padx=20,
                      pady=20)

for index in range(len(food)):
    radio_button = Radiobutton(window, 
                               text=food[index],
                               variable=x,
                               value=index,
                               padx=25,
                               pady=3,
                               font=("Impact",20),
                               image=strongest_images[index],
                               compound=RIGHT,
                               indicatoron=0, # IT WILL MAKE PUSH BUTTON INSTEAD A BULLET
                               width=375, # SETS A WIDTH FOR RADIO BUTTONS
                               command=choose) # SET COMMAND OF RADIO BUTTON TO FUNCTION 


    label.pack()
    radio_button.pack(anchor=W) # WEST
    
window.mainloop()
"""

"""
# 73) SLIDING SCALE
from tkinter import *

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window = Tk()

flame_photo = PhotoImage(file="flame.png")
flame_Label = Label(image=flame_photo)
flame_Label.pack()

scale = Scale(window, from_=100, to=0,
              length=600,
              orient=VERTICAL, # CAN BE HORIZONTAL TOO
              font=("Consolas",20),
              tickinterval=10, # NUMERIC INDICATORS ON THE SCALE
              #showvalue=0, # HIDE CURRENT VALUE
              resolution=5, # INCREMENT OF A SLIDER
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black") 

scale.set((scale['from']-scale['to'])/2+scale['to']) # SETTING THE DEFAULT POSITION (MIDDLE)
scale.pack()

button = Button(window,
                text='submit',
                command=submit)

cold_photo = PhotoImage(file="cold.png")
cold_Label = Label(image=cold_photo)
cold_Label.pack()

button.pack()

window.mainloop()
"""

"""
# 74) LISTBOX
from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ")
    
    for index in food: 
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantio", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()
"""

"""
# 75) MESSAGEBOX
from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='This is an info message box', message='You are a robot')
    messagebox.showwarning(title='WARNING!', message='You have a VIRUS!!!')
    messagebox.showerror(title='ERROR!', message='Something went wrong')

    if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
        print('You did a thing!')
    else:
        print('You canceled a thing')

        ###

    if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry the thing?'):
        print('You retried a thing!')
    else:
        print('You canceled a thing')

        ###

    if messagebox.askyesno(title="ask yes or no", message='Do you like a cake?'):
        print('You like a cake!')
    else:
        print('You doesnt like a cake')

        ###

    answer = messagebox.askquestion(title='ask question', message='Do you like a pie?')
    if (answer == 'yes'):
        print('I like pie too')
    else:
        print('Why do you not like a pie?')

        ###

    answer1 = messagebox.askyesnocancel(title=' Yes no cancel', message='Do you like to code?', icon='warning') # info or error
    if(answer1 == True):
        print("You like to code")
    elif(answer1 == False):
        print("Then why are you coding?")
    else:
        print("You have dodged the question")

window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
"""

"""
# 76) COLORCHOOSER
from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")

button = Button(text='click me', command=click)
button.pack()

window.mainloop()
"""

"""
# 77) TEXT AREA
from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple")
text.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
"""

"""
# 78) OPEN A FILE (FILE DIALOG)
from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text="Open",command=openfile)
button.pack()

window.mainloop()
"""

"""
# 79) SAVE A FILE (FILEDIALOG)
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\User\\Pictures\\PYTHON\\PYTHON",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                        ])
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    #filetext = input("Enter some text: ") # ITS OPTIONAL, IF WE WRITE THIS INSTEAD OF THE TOP ONE, THEN WE FIRST SAVE THE FILE AND THEN WRITE A TEXT IN THE CONSOLE 
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save',command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
"""

"""
# 80) MENUBAR
from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

window = Tk()

openImage = PhotoImage(file="Momoshiki1.png")
saveImage = PhotoImage(file="Isshiki1.png")
exitImage = PhotoImage(file="Juubidara.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound='left')
fileMenu.add_separator() # SEPARATES SECTIONS
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()
"""

"""
# 81) FRAMES
from tkinter import *

window = Tk()

frame = Frame(window, bg="pink", bd=5,relief=SUNKEN)
frame.pack(x=0, y=0)

button = Button(frame, text="W", font=("Consolas",25), width=3).pack(side=TOP)
button = Button(frame, text="A", font=("Consolas",25), width=3).pack(side=LEFT)
button = Button(frame, text="S", font=("Consolas",25), width=3).pack(side=LEFT)
button = Button(frame, text="D", font=("Consolas",25), width=3).pack(side=LEFT)

window.mainloop()
"""

"""
# 82) NEW WINDOWS
from tkinter import *

def create_window():
    new_window = Tk()     # TK() IS INDEPENDENT WINDOW, AND THE TOPLEVEL() IS  LINKED TO THE MAIN WINDOW
    old_window.destroy()

old_window = Tk()

Button(old_window, text="create a new window", command=create_window).pack()

old_window.mainloop()
"""

"""
# 83) WINDOW TABS
from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is Tab 1", width=50, height=25).pack()
Label(tab2, text="Good bye, this is Tab 2", width=50, height=25).pack()

window.mainloop()
"""

"""
# 84) GRID
from tkinter import *

window = Tk()

titleLabel = Label(window, text="Enter your info", font=("Arial", 25)).grid(row=0,column=0, columnspan=2)

firstNameLabel = Label(window, text="First name: ", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1, column=1)

lastNameLabel = Label(window, text="Last name: ", bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)

emailNameLabel = Label(window, text="First name: ", bg="blue", width=30).grid(row=3, column=0)
emailNameEntry = Entry(window).grid(row=3, column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)

window.mainloop()
"""

"""
# 85) PROGRESS BAR
from tkinter import *
from tkinter.ttk import *
import time

def start():   
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB'S downloaded")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
"""

"""
# 86) CANVAS

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
canvas.create_line(0, 500, 500, 0, fill="red", width=5)

canvas.create_rectangle(50, 50, 250, 250, fill="purple", width=5)

points = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(points, fill="yellow", outline="red", width=3)

canvas.create_arc(0,0, 500,500, fill="green", style=PIESLICE, start=180, extent=180)

canvas.create_arc(0,0, 500,500, fill="red", extent=180, width=10)
canvas.create_arc(0,0, 500,500, fill="white", extent=180, start=180, width=10)
canvas.create_oval(190,190, 310,310, fill="white", width=10)
canvas.create_oval(210,210, 290,290, fill="white", width=10)
canvas.create_oval(230,230, 270,270, fill="white", width=10)
canvas.create_oval(250,250, 250,250, fill="white", width=10)

canvas.pack()

window.mainloop()
"""

"""
# 87) KEYBOARD EVENTS
from tkinter import *

def doSomething(event):
    # print("You pressed: "+ event.keysym) 
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomething) # <Return> is Enter, <q> is Quit, <Key> is For All.

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()
"""

"""
# 88) MOUSE EVENTS
from tkinter import *

def doSomething(event):
    print("Mouse Coordinates: " +str(event.x)+","+str(event.y))

window = Tk()

window.bind("<Button-1>", doSomething) # JUST A CLICK FROM MOUSE'S LEFT SIDE
window.bind("<Button-2>", doSomething) # JUST A CLICK FROM MOUSE'S SCROLL
window.bind("<Button-3>", doSomething) # JUST A CLICK FROM MOUSE'S RIGHT SIDE
window.bind("<ButtonRelease>", doSomething) # IF WE PRESS THE MOUSE AND HOLD, IT WILL NOT WRITE UNTIL WE FREE THE MOUSE
window.bind("<Enter>", doSomething) # JUST ENTER THE WINDOW (SHOWS COORDINATES)
window.bind("<Leave>", doSomething) # SHOWS THE COORDINATES IF WE LEAVE THE WINDOW (WITH MOUSE)
window.bind("<Motion>", doSomething) # WHERE THE MOUSE MOVED

window.mainloop()
"""

"""
# 89) DRAG & DROP
from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0,y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()
"""

"""
# 90) MOVE IMAGES W/KEYS
from tkinter import *

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)

def move_left(event):
    label.place(y=label.winfo_y(), x=label.winfo_x()-10)

def move_right(event):
    label.place(y=label.winfo_y(), x=label.winfo_x()+10)

window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<d>", move_right)
window.bind("<a>", move_left)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

momoshiki = PhotoImage(file='Momoshiki1.png')
label = Label(window, image=momoshiki, bg="red")
label.place(x=0,y=0)


window.mainloop()
"""

"""
# 90 - CONTINUE [MOVE IMAGES ON CANVAS]
from tkinter import *

def move_up(event):
    canvas.move(MyIsshiki,0,-10)

def move_down(event):
    canvas.move(MyIsshiki,0,10)

def move_left(event):
    canvas.move(MyIsshiki,-10,0)

def move_right(event):
    canvas.move(MyIsshiki,10,0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


canvas = Canvas(window, width=500, height=500)
canvas.pack()

Isshiki = PhotoImage(file='Isshiki1.png')
MyIsshiki = canvas.create_image(0,0,image=Isshiki, anchor=NW)

window.mainloop()
"""

"""
# 91) 2D ANIMATIONS
from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

SpaceX = PhotoImage(file='space1.png')
Space = canvas.create_image(0,0, image=SpaceX, anchor=NW)

Juubidara = PhotoImage(file='Juubidara.png')
Madara = canvas.create_image(0,0, image=Juubidara, anchor=NW)

Madara_width = Juubidara.width()
Madara_height = Juubidara.height()

while True:
    coordinates = canvas.coords(Madara)
    print(coordinates)

    if(coordinates[0]>=(WIDTH-Madara_width) or coordinates[0]<0):
        xVelocity = -xVelocity

    if(coordinates[1]>=(HEIGHT-Madara_height) or coordinates[1]<0):
        yVelocity = -yVelocity

    canvas.move(Madara, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)
    
window.mainloop()
"""

"""
# 92) MULTIPLE ANIMATIONS
from tkinter import *
from balls92 import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0,0, 100, 1,1, "yellow")
tennis_ball = Ball(canvas, 0,0, 50, 4,3, "green")
basket_ball = Ball(canvas, 0,0, 125, 8,7, "orange")


while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()

    window.update()
    time.sleep(0.01)

window.mainloop()
"""

"""
# 93) CLOCK PROGRAM
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black", relief=RAISED, bd=15, padx=10, pady=5)
time_label.pack()

day_label = Label(window, font=("Ink Free", 25), relief=RAISED, bd=15, padx=10, pady=5)
day_label.pack()

date_label = Label(window, font=("Ink Free", 30), relief=RAISED, bd=15, padx=10, pady=5)
date_label.pack()

update()

window.mainloop()
"""


"""
# 95) RUN WITH COMMAND PROMPT

# WE CHANGE THE ADDRESS OF THE COMMAND PROMPT TO A FILE DIRECTORY AND THEN TYPE:
# python "filename".py

# 96) PIP
# WE JUST CHECK THE INSTALLATION OF THE PACKAGES FROM COMMAND PROMPT

# 97) PY TO EXE
# IN THE COMMAND PROMPT WE WRITE: 
# pyinstaller -F -w -i Isshiki1_UON_icon.ico clockprogram.py AND IT WILL CONVERT TO EXE
"""

"""
# 98) CALCULATOR PROGRAM
from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()
"""

"""
# 99) TEXT EDITOR PROGRAM
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program", "This is a program written by YOUUUUU!!!")


def quit():
    window.destroy()


window = Tk()
window.title("Text editor program")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()
"""

"""
# 100) TIC TAC TOE GAME
from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))

        else:
            buttons[row][column]['text'] = player
            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0], 
           [0,0,0], 
           [0,0,0]]

label = Label(text=player+" turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
"""

"""
# 100) SNAKE GAME
from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 60
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction

    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction

    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, 
                       font=('consolas',70), 
                       text="GAME OVER", fill="red", tag="gameover")

window = Tk()

window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
""" 




