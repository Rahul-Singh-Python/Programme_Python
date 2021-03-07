import random

otp = random.randrange(100000,1000000)
print(otp)


user = int(input("Enter the Otp : "))
if otp == user:
	print('Access Granted!!!')
else:
	print("Access Denied!!!")