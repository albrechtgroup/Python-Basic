# In Programming, there are 3 types of control
# structures.
#   sequential execution - Everything learned 
#                          this far 
#   if then else decisions
#   looping back
##################
# Conditionals: the if then else control structure
##################

# if else statement:
myScore = 87
passingScore = 90
if myScore >= passingScore:
    print("Congradulations!")
    print("You have passed!!!")
else:
    print("We are sorry, you did not pass.")
    print("Please try again.")

print("Thank you for taking the exam.")

# The rule of thumb in Python is that on the 
# line preceding Any indented block of code
# that line must always end with a colon:

# Indented blocks of code must be consistent
# in your program because Python is a 
# whitespace sensitive programming language 
# and treats spaces and tabs Differently*
# Use consistent number of spaces or Tab
# 4 spaces is common

# if elif else statement:
myScore = 89
passingScore = 50
creditScore = 70
distinctionScore = 90
if myScore >= distinctionScore:
    print("Congrats!")
    print("You have passed with DISTINCTION!")
elif myScore >= creditScore:
    print("Congrats!")
    print("You have passed with CREDIT!")
elif myScore >= passingScore:
    print("Congradulations!")
    print("You have passed!!!")
else: 
    print("You did not pass..")
    print("Please try again.")
print("Thank you for taking the exam.")

# Nested if statements:
myScore = 89
passingScore = 50
creditScore = 70
distinctionScore = 90
if myScore >= distinctionScore:
    print("Congrats!")
    print("You have passed with DISTINCTION!")
elif myScore >= creditScore:
    print("Congrats!")
    print("You have passed with CREDIT!")
    if myScore >= distinctionScore - 5:
        print("You are only 5 points from Distinction score!")
elif myScore >= passingScore:
    print("Congrats!")
    print("You have passed!!!")
else:
    print("You did not pass..")
    print("Please try again.")
print("Thank you for taking the exam.")

#######################
# loops 
#######################
# Loops are control structures that loop
# back to repeat a block of code. Repeat

# while loop:
count = 1
while count <= 10:
    print(count)
    count = count + 1
# Output = 1,2,3,4,5,6,7,8,9,10

# input() &Nbreak keyword:
count = 1
while count <= 10:
    print(count)
    count = count + 1
    toExit = input("Enter e if you wish to exit.")
    if toExit == "e":
        break

# 'break' and 'continue' are used Inside while
#  and for loops
count = 0 
while count <= 9:
    count = count + 1
    if count%2:
        continue
    print(count)
# Here, when count divided by 2 gives a 
# non-zero remainder, the if condition 
# returns True, so it will Not print count,
# because of the 'continue' keyword, which
# immediately skips to the next iteration of 
# the while loop. Therefore, effectively, it 
# will only print the count when count 
# divided by 2 gives 
# zero remainder, which returns False, resulting
# in printing all Even numbers between 1-10

# for loop:
for count in range(10):
    print(count+1)

# The range() function is called the iterable,
# which means that it is something that can 
# be repeated and looped through a number 
# of times.
# Allows you to create a list of numbers 
# easily, and then use them for iterating
# the number of times, as specified by the 
# argument passed to the function

for count in range(10, 100):
    print(count)
# Output = 2-14

# passing a starting number, 2 arguments
# starting value and ending value
# Adding a 3rd value includes a incremeting
# value. 5
(10, 100, 5)

# negative 3rd number is the decrement value
(10, 100, -10)

# loop within another loop:
# also while loop in for, and reversed
for countA in range(1, 4):
    for countB in range(1, 4):
        for countC in range(1, 4):
            print(countA, countB, countC)

# Iterate a list using a for loop:
studentList = ["Mary", "John", "Mike", "Alice"]
for studentName in studentList:
    print(studentName)
# Each item inside studentList, will be 
# stored into the variable studentName
# and printed out, Voila!!

# Iterate a list using a while loop:
studentList = ["Mary", "John", "Mike", "Alice"]
index = 0
while index < len(studentList):
    print(studentList[index])
    index += 1
 # Same Output as for loop above, each
 # name printed out seperately.

 # for and while loops can also interate 
 # tuples, dictionaries and sets

# Finally: lists, tuples, dictionaries and 
# sets are called Iterables. Iterables have
# many values within itself.











