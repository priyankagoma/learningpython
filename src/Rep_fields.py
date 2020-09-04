#Replacement Fields

#first we will see the string function.
#Basically str() function helps us to coerce an integer into a string.
#EX:
age = 24
print("My age is " + str(age) + " years old")
#As this can be rapidly become tedious
#So we can use replacement fields and the (dot format) method
#The value in the parentheses after .format will be replased with the values in our code.
#So the replacement fields is number inside the curly braces that determines which value to be used.
#EX:
print("My age is {0} years old" .format(age))

print("There are {0} days in {1} , {2} , {3} , {4}".format(31, "Jan", "march", "may", "july"))

print("I have {0} Children in my home ".format(4))

print("There are {0} days in a week, {2} days in a month and {1} days in a year."
      .format("seven", "three sixty five", "thirty"))

print("{0} {1} {2}".format("I", "Love", "You"))

print("How many hours it will take ")

