number = int(input("Enter your number: "))
count = 0
while (number>0):
    number = number//10
    count = count+1
print('Number of digits:', count)