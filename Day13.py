"""
Day13.py

"""
balance = 180000
amount = int(input("Enter withdrawl amount: "))
if amount <= balance:
                  balance -= amount
                  print("withdrawal sucessfull")
                  print("Remaining balance:", balance)
else:
                  print("Insuficient balance:")