number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {0}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
    print("This parrot is " + state)

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
cleanedChar = ''
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        cleanedChar = cleanedChar + quote
newChar = cleanedChar
print("The capitals in the string are {0}".format(newChar))