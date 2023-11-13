import math

while True:
    part = input("Enter part: ")
    if int(part) == 1:
        code = float(input("Enter Answer Code: "))
        print(f"Correct answer: {round(math.pi/math.acos(code))}\n")
    elif int(part) == 3:
        code = int(input("Enter Answer Code: "))
        vol = float(input("Enter Vol: "))
        print(f"Correct answer: {round((code/(vol/10))/5)}\n")
    elif int(part) == 2:
        code = float(input("Enter Answer Code: "))
        print(f"Correct answer: {round(math.pi/math.asin(code))}\n")

