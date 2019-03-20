##P E M D A S
# Parentheses
# Exponents
# Multiplication
# Division
# Addition
# Subtraction

operand1 = 65
operand2 = 83.22

#addition
print(operand1 + operand2)

#subtraction
print(operand1 - operand2)

#multiplication
print(operand1 * operand2)

#division
print(operand1 / operand2)


print(9 % 3) # % just shows the remainder
print(10 % 3)
print(15 % 6)

print(16 % 2) #even
print(17 % 2) #odd

print(3 ** 3) #exponent
print(10 ** 2) #exponent

print(10 // 3) #floor division
print(15 // 6) #floor division


#Order of Operations
print(5-6*2)
print((5-6)*2)

print(3**3*5)
print(3**(3*5))


# In python integers and floating point numbers when compared if they have an equal value are "True"
print(10==10)
print(10.0==10)
# != means does not equal
print(10 != 10)
print(10 != 13)

# > greaterthan < Less than <= lessthan or equal to >= greaterthan or equal to.

print(5>2)
print(5<2)

# in "and" logical operator both sides must be true in "or" only one needs to be true.

print(5==5 and 10==10)
print(5==5 or 10==5)
print(5==5 and 10==5) #false

# "not" negates logical operator

print(5==5)
print (not 5==5)