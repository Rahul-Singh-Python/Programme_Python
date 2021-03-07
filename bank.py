import sys

class Customer:
	'''
	customer class with bank related operations
	'''
	bankname = 'SBI'

	def __init__(self,name,balance=0):
		self.name=name
		self.balance=balance
	def deposit(self,amt):
		self.balance=self.balance+amt
		print('After deposite the balance: ',self.balance)
	def withdraw(self,amt):
		if amt > self.balance:
			print("Insufficient funds can not perform operations")
			sys.exit()
		self.balance=self.balance-amt
		print("After withdraw the balance: ",self.balance)
print("Wellcome to ",Customer.bankname)

name = input("Enter Your Name: ")
c = Customer(name)

while True:
	print('d-Deposit \n w-withdraw \n e-Exit')
	option = input("Choice Your Option: ")
	if option == 'd' or option == 'D':
		amt = float(input("Enter the amount to deposit: "))
		c.deposit(amt)
	elif option == 'w' or option == 'W':
		amt = float(input("Enter the amount to withdraw: "))
		c.withdraw(amt)
	elif option == 'e' or option == 'E':
		print("Thanks for Banking ")
		sys.exit()
	else:
		print("Choose Valid option ")