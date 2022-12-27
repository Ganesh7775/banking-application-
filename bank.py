import sys
class Customer:
	"""customer class with bank operations"""
	bankname="GANESH BANK"
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=balance

	def deposit(self,amt):
		self.balance=self.balance+amt
		print("Balance after deposit :",self.balance)

	def withdraw(self,amt):
		if amt>self.balance:
			print("insufficient funds cant perform this operation ")
			sys.exit()
		self.balance=self.balance-amt
		print("Remaining amount :",self.balance)

print("Welcome to : ",Customer.bankname)
name=input("Enter your name :")
c=Customer(name)
while True:
	print("d-Deposit \n w-Withdraw \n e-Exit ")
	option=input("Choose your option :")
	if option=="d" or option=="D":
		amt=float(input("Enter amount"))
		c.deposit(amt)

	elif option=="w" or option=="W":
		amt=float(input("Enter amount :"))
		c.withdraw(amt)

	elif option=="e" or option=="E":
		print("Thanks for Banking ")
		sys.exit()
	else:
		print("Invalid option .. choose correct option ")















