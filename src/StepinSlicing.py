# Using a step in slice, it can be step 2,3,4,5,etc...
Numbers = "12345678901234567890"
Ex: print(Numbers[0:6:2])
# so we can see the slice starts at index position and it extends up to (not included) position 6.
# so we are stepping through the sequence in steps of 2.

Numbers = "12345678901234567890"
Seperators = Numbers[1::3]
print(Seperators)

# Step in Slicing Backward.
test = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
      # 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1-
print(test[18:1:-1])

Letters = "abcdefghijklmnopqrstuvwxyz"
        # 765432109876543210987654321-
print(test[18:2:-2])