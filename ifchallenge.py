# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.
name = input("Please provide your name: ")
age = int(input("Pleae provide your age {0}: ".format(name)))

if (18 <= age < 31):
    print("Welcome {0} to your holiday!" .format(name))
else:
    print("Sorry {0} but you're not able to go.".format(name))

# For loop.  Print out numbers from 0 to 9.
for x in range(0, 10):
        print("%d"% (x))