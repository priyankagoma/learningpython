#SEQUENCE IN OPERATORS.
######################

#We can not concatinate str to int only string to string.
#We can also concatinate strings without using (+).

string1 = "Priyanka "
string2 = "Nishtha "
string3 = "Bobby "
string4 = "Tavishi "
string5 = "Kanika "
print(string1 + string4 + string5)

print("Priyanka " "Tavishi " "Kanika ")

#Strings can be multiplied by integers.
#In line 19 Acoording to the BODMAS string ("5") is multiplied with int 4 then its concatinating with str (Hello).
#In line 20 becouse of the parentheses, evaluates 5+4 to get 9.
#So it will repeat the string 9 times.
print("Hello " * 5)
print("Hello " * 4)
print("Hello " + 4 * "5")
print("Hello " * (4 + 5))

#Now we will check one thing is in another.
#So here, the IN operator evaluates to True or False if the first thing exixts in the second or not.
Butterfly = "Red Blue Green Purple"
print("Red" in Butterfly)
print("Blue" in Butterfly)
print("Orange" in Butterfly)
print()
today = "Tuesday"
print("day" in today)
print("Fri" in today)