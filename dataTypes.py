""" Always remind ourselves that when coding,
    less code = less places to make mistakes,
    less places to make mistakes = less code
    to debug, less code to debug = less code 
    to read, and less code to read = that you 
    can see the whole picture much clearer. """

greeting = "Hello World"
print(greeting)

# Example 1:
num1 = 0
bool1 = bool(num1)
print(bool1)
# Output = False, ONlY empty strings and 0
#  are False

# Example 2:
num1 = 7
bool1 = bool(num1)
print(bool1)
# Output = True

# Example 3:
text1 = "0"
bool1 = bool(text1)
print(bool1)
# Output = True

# Python keywork 'None' is a null value
# Data type of 'None' is 'NoneType'
# Example:
i_am_None = None
print(i_am_None)
# Output = None
print(type(i_am_None))
# Output = NoneType


##########################
# String Manitpulation & Typecasting

print("Hi" * 3)
# Output = HiHiHi
print("*" * 10)
# Output = **********

text1 = "I am"
text2 = "here"
print(text1 + " " + text2)
# Output = I am here
print(text1, text2)
# Same Output as above, when 
# 'Concatinating' using the comma,
#  python auto adds the spaces

# Python's f-strings
print(f'Hello World')
# Output = Hello World
text1 = "I am"
text2 = "here"
print(f'Hi, {text1} {text2}')
# Output = Hi, I am here

print(f"Hello World")
# Output = Hello World

# Hello Andy
text = "Hello Andy"
print(text[:5])
# Output = Hello 
print(text[:4])
# Output = Hell
print(text[-4:])
# Output = Andy, -Negative numbers start 
# string from the Right going Left
# starting at -1, instead of 0

name = "Hello, My name is Andy"
print(name[18:22])
# Output = Andy
# Starting index is Inclusive,
# while the ending index is Exclusive.
print(name[6:])
# Output = My name is Andy

# Uppercase built-in function upper()
text = "Please convert me to all uppercase"
print(text.upper())
# Output = PLEASE CONVERT ME TO ALL UPPERCASE
# Does NOT Change the string, must save to a

# new variable(below)
upperText = text.upper()
print(upperText)
# Output is same, and value of variable 
# has been changed

# Lowercase built-in function lower()
lowerText = text.lower()
print(lowerText)

# count() function
text = "Count the number of u's in me."
print(text.count("u"))
# Output = 3

text = "Replace this with that"
print(text.replace("this", "that"))
# Output = Replace that with that

# len() for length of text
text = "What is the length of this text?"
print(len(text))
# Output = 31

""" strip() function to strip white space in
    beggining and end of a string
    lstrip() strip white space off front
    rstrip() strip white space off right """
text = "    Strip both ends   "  
print(text.strip())
# Output = Strip both ends

""" 'is' Methods to check True or False
    isalnum() - is Every character alphanumeric
    isalpha() - is Every character alphabetic
    isdigit() - is Every character numeric
    isupper() - is Every character uppercase
    islower() - is Every character lowercase """

# Example:
text = "abcdEf"
print(text.isalnum())
# Output = True
print(text.isdigit())
# Output = False, no numbers

# Typecasting allows you to convert one 
# variable type to another.

number = 5.32582
number_int = int(number)
print(number_int)
# Output = 5, f.p.n. turned into integer

number = 5
number_float = float(number)
print(number_float)
# Output = 5.0, integer turned into 
# a floating point number


#########################
# Data Structures

""" Basic Data structures:
   "strings"
   131 - numbers
   131.77 - floating point numbers
   True or False - booleans """


##########################
# Complex Data structures:

#   list = [], Very similar to arrays in JS
fruits = ["apples", "oranges", "strawberries", "pears"]
print(fruits[2])
# Output = strawberries
fruits[3] = "grapes"
# changes pears to grapes in the list
fruits.append("pineapple")
# Output = fruits = ["apples", "oranges", "strawberries", "pears", "pineapple"]
# append() will add to the End of list
fruits.insert(3, "insert me at index 3")
# insert() will insert into the list at 
# the given index
del fruits[3]
print(fruits)
# Output = list with the above str deleted

# .split() will split a string into a list
# .join() will join list items into a str

#  tuple = ()
""" tuples are like lists, but cannot be 
    changed
    Advantage: python processes tuples much
    aster than lists, also good for constant
    large data that do Not want to change
    this_is_a_tuple = () """


#   dictionary = {}
# Do not have index numbers, no order
# key: value pairs, like objects in JS
city_weather = {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15}
city_weather["Brooklyn"] = 77
# to add to dictionary or change exist value
# Output = {"Singapore": 30, "Paris": 15, "Sydney": 19, "Tokyo": 15, "Brooklyn": 77}
del city_weather["Singapore"]
# Output = {"Parris": 15, etc} minus Singapore
print(city_weather["Brooklyn"])
# Output = 77

#   set = {}
""" Similar rules to dictionaries
     does Not use key: value pairs
     add() method to add to set
    remove() method to remove from set
    cannot be changed, must be removed, then
    added
    No duplicate values allowed in sets """


##########################
# Operators:

# Mathmatical Operators:
""" + = add
    - = subtract
    * = multiply
    / = divide
    % = modulo- remainder after dividing 
    ** = exponentiation- num1 to the power of
         num2.
    // = floor- ignores decimals after division
         rounds down, 3.7 becomes 3
        negative numbers will instead round up 
        -3.7 becomes -4 """

# Assignment Operators:
"""  =
    +=
    -=
    *=
    /=
    %=
   //=
   **= """

number_2 = 5
number_2 += 3
print(number_2)
# Output = 8

# To assign multiple variable to multiple
#  values at same time:
num_1, num_2, text_1 = 3, 7, "multiple assignment"
print(num_1)
# Output = 3
print(num_2)
# Output = 7
print(text_1)
# Output = "multiple assignments"

""" Comparison Operators:
    > greater than
    < less than
    == equal
    != Not equal
    >= greater than or equal to 
    <= less than or equal to """

# Logical Operators:
# and -Both sides compared must be true
# or - One side or the other

# 'not'
num_1 = 3
num_2 = 7
print(not num_1 > num_2)
# Output = True, 3 is Not greater than 7,
# but using 'not' make it the opposite.
# Not false.

# Identity Operators:
# Used to determine if a var or value
# is of a certain class or data type

# 'is'
num_1 = 13
print(type(num_1) is int)
# Output = True
num_2 = 11.3
print(type(num_2) is float)
# Output = True

# 'is not'
print(type(num_2) is not str)
# Output = True

# Membership Operators:
# Use to check if a value is found within a
# sequence

# 'in' 
text_1 = "Hello World"
text_2 = "Hello"
text_3 = "hello"
print(text_2 in text_1)
# Output = True, Hello is 'in' Hello World

# 'not in'
print(text_2 not in text_1)
# Output = False, Hello is 'in' Hello World
print(text_3 in text_1)
# Output = False, lowercase hello is Not in

""" Rules of Operator Precedence
    () parenthesis
    ** exponentiation
    +x, -x unary plus, unary minus
    *, /, //, % multiplication, divisio,
                floor div, modulo
    +, - addition, subtraction
    ==,!=, >, >=, <. <=   comparisons, identity
    is, is not, in, not in      membership
    not  logical not
    and  logical and
    or   logical or """





 





