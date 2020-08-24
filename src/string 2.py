# INDEXING AND SLICING#
#######################
# In order to do the indexing in string we will put the position of sequence in square bracket in our code.
# So that we can get the value of the number of sequence.
# And the position of sequence will always starts from 0 instead of 1.
#Ex:    012345678901234567890123456
test = "prepare yanki you are lovly"

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
# In Negative indexing we have to use the index position from the end of the string.
# where the last character is at position -1.
#Ex:
test = "prepare yanki you are lovly"
      # 765432109876543210987654321-

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
# In slicing we will put the start and stop value of sequence in string.
# So that we will get the position of sequence according to the code.
# As it will give us the position of up to but not included of stop value.
# We should always put the stop value one step ahead in code from what we want.
      # 012345678901234567890123456
test = "prepare yanki you are lovly"

print(test[:])           #(start:stop value)
print(test[8:13])
print(test[22:27])
print(test[:7] + " " + test[8:13])
print(test[18:21] + " " + test[14:17] + " " + test[22:27])

#Slicing with negative numbers.
###############################
#In Negative indexing we will count from the end of the string, instead of from the begining.
#Ex:
test ="prepare yanki you are lovly"
     # 765432109876543210987654321-

print(test[-15:-14] + " " + test[-5:-2] + test[-7:-6] + " " + test[-13:-10])
print(test[-15:-1])

print(test[-5:27])
print(test[-27:2] + test[12:-14] + test[8:-15] + test[-18:10])

# Slicing Backward.
####################
         # 01234567890123456789012345
Letters = "abcdefghijklmnopqrstuvwxyz"
         # 65432109876543210987654321-

# In order to perform backward slicing we have to put step of (-1) at the end of the code.
# so that it will give us the revers value of the string.
# EX: if z is our start value and b is stop, so code should be [25:0:-1]
# because it never includes the position of stop value, so we will use the blank space
# to get the last value of position.
# Ex:
print(Letters[25::-1])    #(start:stop:step value)
print(Letters[::-1])
#
print(Letters[16:13:-1])
print(Letters[4::-1])
print(Letters[25:17:-1])
#
print(Letters[:-9:-1])

      # 012345678901234567890123456
test = "prepare yanki you are lovly"
      # 765432109876543210987654321-

print(test[26:0:-1])

#Slicing Idioms
###############
         # 01234567890123456789012345
Letters = "abcdefghijklmnopqrstuvwxyz"
         # 65432109876543210987654321-
print(Letters[-4:])
print(Letters[-1:])
print(Letters[-2:-1])
print(Letters[:1])
print(Letters[0])