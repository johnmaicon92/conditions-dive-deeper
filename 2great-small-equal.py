# Identify the Greatest

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if num1>=num2 and num1>=num3:
    large=num1
elif num2>=num1 and num2>=num3:
    large=num2
else:
    large=num3
print("The largest number is: ",large)
         
# Identify the Smallest

num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
if num1<=num2 and num1<=num3:
    small=num1
elif num2<=num1 and num2<=num3:
    small=num2
else:
    small=num3
print("The smallest number is: ",small)


# Equality Check
a = []
n = int(input("Number of elements = "))
for i in range(n):
    a.append(int(input("Value = ")))

counter = 0
repeated = []

for i in a:
    if i not in repeated:
        if a.count(i) > 1:
            print(f'{i} appears {a.count(i)} times')
            counter += 1
            repeated.append(i)

print(f'{counter} numbers repeated')