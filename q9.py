cp = float(input("enter cost price:"))
sp = float(input("enter selling price:"))
if sp > cp:
  print(f"profit of: {sp-cp}")
elif cp > sp:
  print(f"loss of: {cp-sp}")
else:
  print("no profit, no loss.")