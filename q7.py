import math
x1 = float(input("enter x1: "))
y1 = float(input("enter y1: "))
x2 = float(input("enter x2: "))
y2 = float(input("enter x2: "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"the euclidean distance is: {distance:.2f}")
