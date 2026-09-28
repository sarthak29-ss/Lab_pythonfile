num = int(input("enter a number:"))
sign = -1 if num < 0 else 1
temp = abs(num)
reversed_num = 0

while temp > 0:
  reversed_num = (reversed_num * 10) + (temp % 10)
  temp //= 10
  print(f"reversed number: {sign * reversed_num}")