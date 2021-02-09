'''
02/01/2021


Review:
--------------
if/elif/else statement

if (Condition):
  Body Statement1

elif (Condition):
  Body Statement2
.
.
.

else:
  Body Statement3

Nested Conditional Statement
-------------------------------------
-A conditional statement inside another conditional statement

Indentation
-The header/clause of a nested conditional statement must be indented from the outer header

- A conditional statement inside another conditional statement

if (Condition):
  Body Statement1
  if (Condition):       <-- Starting a nested statement
    Body statement 1a   <-- Ending a nested statement

elif (Condition):
  Body Statement2
  if (Condition):       <-- Starting a nested statement
    Body statemeent 2a 

  elif (Condition):
    Body Statemeent 2b

  else:
    Body statement 2c   <--- Ending a nested statement

.
.
.

else:
  BodyStatement3


Example
-------------
x = y = 10

if(x < y):
  print("x is less than y")

else:
  if(x > y):
    print("x is greater than y")
  else:
    print("x and y must be equal")
'''

# Exercise: Evaluate if your number is positive/ negative/ zero and odd/even


userNum = int(input("Enter a number:\n"))

#Positive
if (userNum > 0):
  if (userNum % 2 == 0):
    print("This number is even and positive")
  else:
    print("This is an odd and positive number")


#Negative
elif (userNum < 0):
  print("This number is negative")
  if (userNum % 2 == 0):
    print("This number is even and negative")
  else:
    print("This is an odd and negative number")
#zero
else:
  print("This number is zero")
