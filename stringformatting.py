age = 62
print("my age is " + str(age) + " years")

#replacement fields
print("my age is {0} years".format(age))

meal1 = "spam" + "eggs" + "beans"
meal2 = "spam\neggs\nbeans"
meal3 = "spam, eggs, beans"
meal4 = """spam
eggs
beans"""

print(meal1)
print(meal2)
print(meal3)
print(meal4)

print("Terry\tJohn\tGraham\tMichael\tEric\tTerry")

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5
Total = total + tax
print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[::5])
print(data[:12:5])

