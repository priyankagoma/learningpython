# INDEXING AND SLICING#
#######################

     # 0123456789012345678901234567
test = "prepare yanki you are lovly"
      # 765432109876543210987654321-
#Indexing#
##########
print(test[22])
print(test[20])
print(test[18])
print(test[19])
print(test[10])
print(test[7])
print(test[0])
print(test[1])
print(test[12])
print(test[8])
print(test[9])
print(test[10])
print(test[11])
print(test[4])
# Negative indexing
###################
print(test[-5])
print(test[-15])
print(test[-16])
print(test[-7])
print(test[-6])
print(test[-13])
print(test[-12])
print(test[-11])
print(test[-8])
print(test[-10])
print(test[-27])
print(test[-26])
print(test[-23])
print(test[-17])
print(test[-16])

#SLICING
##########
     # 0123456789012345678901234567
test = "prepare yanki you are lovly"

print(test[:])
print(test[8:13])
print(test[22:27])
print(test[:7] + " " + test[8:13])
print(test[18:21] + " " + test[14:17] + " " + test[22:27])

# Slicing Backward.
####################
         # 01234567890123456789012345
Letters = "abcdefghijklmnopqrstuvwxyz"

# In order to perform backward slicing we have to put step of (-1) at the end of the code.
# so that it will gve us the revers value of the string.
# EX: if z is our start value and b is stop value so code should be [25:0:-1]
# Also it never includes the place of stop value in that case we can use the blank space
# so that we can get the last place of value.
# Ex:
print(Letters[25::-1])
print(Letters[::-1])

print(Letters[16:13:-1])
print(Letters[4::-1])
print(Letters[25:17:-1])

      # 012345678901234567890123456
test = "prepare yanki you are lovly"
      # 765432109876543210987654321-

print(test[26:0:-1])