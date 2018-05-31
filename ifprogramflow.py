# name = input("Please enter your name:")
# # age = int(input("How old ar you, {0}?".format(name)))
# # limit = 21;
# # print(age)
# #
# # if age >= limit:
# #     print("You are old enough")
# # else:
# #     print("Please come back in {0} years".format(limit - age))
print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < 5:
    print("Please guess higher: ")
    guess = int(input())
    if guess == 5:
        print("Well done!")
    else:
        print("Whaa-whaa.  Wrong!")
elif guess > 5:
    print("Please guess lower: ")
    guess = int(input())
    if guess == 5:
        print("You got it champ!")
    else:
        print("Whaa-whaa.  Wrong!")
else:
    print("You got it on the first try!")


x = 5
y = 7

if x == y:
    print("x equals y")
elif x > y:
    print("x is greater than y")
else:
    print("x is smaller than y")



