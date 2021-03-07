
SECURE = (('s','$'),('and','&'),('a','@'),('0','*'),('i','1'))

def securePassword(password):
	for a,b in SECURE:
		password = password.replace(a,b)
	return password

if __name__ == '__main__':
	password = input("Enter Your Password: ")
	password = securePassword(password)
	print(f"Your Secure Password is: {password}")