while True:
    try:
        width = float(input("Please enter the width "))
        break
    except ValueError:
        print("It's not a number, please enter the number")


while True:
    try:
        height = float(input("Please enter the height "))
        break
    except ValueError:
        print("It's not a number, please enter the number")


print(f"Area of the rectangle = {width * height: .4f}")
print(f"Circumference of the rectangle = {2*width + 2*height: .4f}")
