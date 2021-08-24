#We are using the (for loof) with (.format) to see the effect of the formattin in the replacement fields.
#1. We will put :2 in first replacement field and :3, :4 for the other two.
#to increase the size of the width of replacement fields.
#2. Similerly we can chose the width accordingly by using this method.
#3. Another example of change the wodth accordingly.
#4. We can also aling the values field width
#so for left aling the values we place a (<) symbol after the colon.

#Ex: 1
for x in range(1, 6):
    print("No. {0:2}  squared is {1:3} and cubed is {2:4}" .format(x, x ** 2, x ** 3))
print()
#Ex: 2
for y in range(1, 6):
    print("No. {0:2}  squared is {1:4} and cubed is {2:4}" .format(y, y ** 2, y ** 3))
print()
#Ex: 3
for z in range(1, 6):
    print("No. {0:2}  squared is {1:3} and cubed is {2:3}" .format(z, z ** 2, z ** 3))
print()
#Ex: 4
for x in range(1, 6):
    print("No. {0:2}  squared is {1:<3} and cubed is {2:<4}" .format(x, x ** 2, x ** 3))

