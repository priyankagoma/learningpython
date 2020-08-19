# Using a step in slice, it can be step 2,3,4,5,etc...
Numbers = "12345678901234567890"
Ex: print(Numbers[0:6:2])
# so we can see the slice starts at index position 0 and it extends up to (not included) position 6.
# now we are stepping through the sequence in steps of 2.

Numbers = "12345678901234567890"
Seperators = Numbers[1:20:1]
print(Seperators)
Seperators = Numbers[1::3]
print(Seperators)
Seperators = Numbers[:18:2]
print(Seperators)

          #1234567890123456789012345678901
Letters = "a b c d e f g h i j k l m n o p"

print(Letters[:20:1])
print(Letters[::2])
print(Letters[2:10:2])

Letters = "abcdefghijklmnopqrstuvwxyz"
         # 54321098765432109876543210-
Characters = Letters
print(Characters[1:21:2])

# Step in Slicing Backward.
##########################
# In Step in backward slicing we will step through the sequence in steps of (-)Negative.
# It will give us the revers value.
# Ex:

test = "1 2 3 4 5 6 7 8 9 0"
      # 9876543219876543210-
print(test[19:0:-2])
print(test[19::-1])

Letters = "abcdefghijklmnopqrstuvwxyz"
         # 54321098765432109876543210-
print(Letters[25:0:-2])