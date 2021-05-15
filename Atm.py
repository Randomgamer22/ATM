class ATM(object):
	def __init__(self, card_number, pin):
		self.card_number = card_number
		self.pin = pin
		self.balance = 1000

	def check_balance(self):
		print("You balance is ",self.balance)

	def withdraw_money(self, amount):
		if amount <= self.balance:
			print("Withdrawal successful, Your balance is", self.balance-amount)
		else: 
			print("Insufficient funds.")

def main():
	card_number = input("Card Number: ")
	pin = input("Pin: ")
	atm = ATM(card_number, pin)

	choose_action = int(input("What action to perform (1 = balance enquiry, 2 = withdraw_money): "))

	if choose_action == 1:
		atm.check_balance()
	elif choose_action == 2:
		amount_to_withdraw = int(input("Amount to withdraw: "))
		atm.withdraw_money(amount_to_withdraw)
	else:
		print("Invalid number try re-running the program.")

main()
