num = int(input("enter an integer:"))
temp = abs(num)
digit_sum = 0

while temp > 0:
   digit_sum += temp % 10
   temp //= 10
   print(f"the sum of digits is: {digit_sum}")

