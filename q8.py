angle1 = float(input("enter first angle: "))
angle2 = float(input("enter second angle: "))
angle3 = float(input("enter third angle:"))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 100):
  print("these angles can form a valid trangle.")
else:
  print("these angles cannot form a valid triangle.")