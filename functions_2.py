name = "John" # I declared the attribute here
def check_grade(marks, first_name, last_name): # 3 Arguments \\ Parameters # Python Script - One single file containing python code
    if marks <= 30:
        print(first_name+" "+last_name+" scored an F")
    elif marks > 30 and marks <= 40:
        print(first_name+" "+last_name+" scored an D")
    elif marks > 40 and marks <= 50:
        print(first_name+" "+last_name+" scored an C")
    elif marks > 50 and marks <= 60:
        print(first_name+" "+last_name+" scored an B")
    else:
        print(first_name+" "+last_name+" scored an A")

# Whatever data you pass through the function == "John"
# You can declare as many arguments as you want
#check_grade(56, "John", "Doe") # Moffat and Nancy

# Modular-- Importing Modules, Libraries, Framework
# GDAL - Geospatial Data Abstraction Library -
# Django - Web Framework
# stack -- Can't learn all of them
# Learn all the ones you need
# Once you learn a framework - Building
# Prewritten python that you can reuse.
# Write a library