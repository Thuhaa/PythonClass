# for loops and while loops
# Iterate = Run the program several times until a condition is met
# range(start, stop, step) # Returns a sequence start,  stop-1
# range(0,5) == 0,1,2,3,4
# Concatenation
# Iterable  = List, Sets, String, Tuples

our_list = ["TUK", "UON", "JKUAT", "KU", "Moi", 5, "g", "f"]
for x in our_list:
    # print(str(x) + " is in index " + str(our_list.index(x)))
    # print(f"{x} is in position {our_list.index(x)}")
    print("{} is in position {}".format(x, our_list.index(x)))
