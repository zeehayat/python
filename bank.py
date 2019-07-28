bank_name="MCB"
amount=0
def deposit(account_no,amount):
	if(is_available(account_no)):
		addamount(amount)
	else:
		print("Account does not exist")


def is_available(account_no):
	#Look into the list
	return True

def addamount(amount):
	amount=amount+amount
	
deposit(100,10000)
print(amount)
