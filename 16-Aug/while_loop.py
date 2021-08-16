# While loop == Until a condition is met
# Runs until a condition is True
# pep 8 standards == Python standards
# DRY principle == Don't Repeat yourself # Programming standards
x = 10  # Assigned x to 10
while x < 100:
    x += 1
    if x == 30:
        continue
    print(x)


"""
x is 10
adding 1 to x making x 11,
x is 11
adding 1 to x making x 12,
checking if x is 30 == True: # Ignore when x is 30

continue
x is 30 # Ignoring this
Adding 1 to x making x 31
print x
... repeat until x is 99
x<100 == True
"""



"""
x is 0
print x
then add 1 to x making x = 1
x is 1
print x
then add 1 to x making x 2
x is 2
print x
then add 1 to x making x 3
print x
...
...
stop when x is 99
"""

# https://github.com/Thuhaa/PythonClass