import pyotp
totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
curr = totp.now()
print("Current OTP:",curr)

# user = int(input("Enter Number : "))

# if curr == user:
# 	print("User is Granted...")
# else:
# 	print("User is Denied...")


