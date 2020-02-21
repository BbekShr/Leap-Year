year = int(input("Enter a year: "))

if year>1582:
    if (year%4 is not 0):
        print("Common Year")
    elif (year%100 is not 0):
        print("Leap Year")
    elif (year%400 is not 0):
        print("Common Year")
    else:
        print("Leap year")
else:
    print("Not within the Gregorian calender period")
