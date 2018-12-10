from re import *

pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')

def get_address(x):
	address = input("Please type your email: ")
	is_valid = x.match(address)
	if is_valid:
		print("Valid Address: ",is_valid.group())
	else:
		print("Invalid Address! Please retry...\n")

get_address(pattern)


