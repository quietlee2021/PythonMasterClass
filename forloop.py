number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {0}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

for i in range(0,100,5):
    print("i is {0} ".format(i))

for i in range (1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}" .format(i, j, i*j))
    print("****************************************")

for i in range (1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}" .format(i, j, i*j), end='\t')
    print(' ')
    #print("****************************************")


quote = "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?/"

# Use a for loop and an if statement to print just the capitals in the quote above.
cleanedChar = ''
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cleanedChar = cleanedChar + char

print("The capitals in the string are {0}".format(cleanedChar))

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char, end='')
print(" ")
#Write a program to print out all the numbers from 0 to 100 that are divisible by 7
for i in range(0,100,7):
    print(i)
#Alternate using a slice
print("")
for i in range(100)[::7]:
    print(i)