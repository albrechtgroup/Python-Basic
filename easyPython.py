greeting = "Hello World"
print(greeting)

# Example 1:
num1 = 0
bool1 = bool(num1)
print(bool1)
# Output = False, ONlY empty strings and 0
#          are False

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

# Python keywork None is a null value
# Data type of None is NoneType

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
# concatinating using the comma,
# python auto adds the spaces

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

# strip() function to strip white space in
# beggining and end of a string
# lstrip() strip white space off front
# rstrip() strip white space off right
text = "    Strip both ends   "
print(text.strip())
# Output = Strip both ends

# is Methods to check True or False
#  isalnum() - is Every character alphanumeric
#  isalpha() - is Every character alphabetic
#  isdigit() - is Every character numeric
#  isupper() - is Every character uppercase
#  islower() - is Every character lowercase
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







