year = int(input("Enter The Year : "))

if year % 100 == 0:
    if year % 400 == 0:
        print("The Entered Year ", year, " is a Leap Year")
    else:
        print("The Entered Year ", year, " is not a Leap Year")
else:
    if year % 4 == 0:
        print("The Entered Year ", year, " is a Leap Year")
    else:
        print("The Entered Year ", year, " is not a Leap Year")