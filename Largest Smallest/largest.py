n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
n4 = int(input("Enter fourth number: "))
n5 = int(input("Enter fifth number: "))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    largest = n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    largest = n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    largest = n3
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    largest = n4
else:
    largest = n5

print("The largest number is:", largest)
