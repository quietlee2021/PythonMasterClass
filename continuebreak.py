shopping_list = ["milk","pasta","eggs","spam","bread","rice"]
for item in shopping_list:
    if item == "spam":
        #continue
        break
    print("Buy " + item)

# Modify this loop to stop when i is exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i%11 == 0:
        break

print(" ")
for i in range (0,20,1):
    if (i ==0)or(i%3==0) or (i%5==0):
        continue
    print(i)

#other solution 1
print(" ")
# using continue
for x in range(20):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)

#other solution 2
print(" ")
# without continue
for x in range(20):
    if x % 3 != 0 and x % 5 != 0:
        print(x)

