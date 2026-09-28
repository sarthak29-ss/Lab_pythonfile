num = int(input("enter an integer:"))

if num % 2 == 0:
  print(*f"{num} is even.")
else:
  print(f"{num} is odd.")