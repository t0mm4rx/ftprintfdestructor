import random
import string

def random_string(length):
	letters = string.ascii_letters + string.digits + " "
	return ''.join(random.choice(letters) for i in range(length))

def input_string():
	choice = random.choice([0, 1, 2])
	if (choice == 0):
		return '"{}"'.format(random_string(random.randint(1, 100)))
	if (choice == 1):
		return "NULL"
	if (choice == 2):
		return '""'

def input_uint():
	return str(random.randint(0, 2147483647))

def input_short_uint():
	return str(random.randint(0, 100))

def input_int():
	choice = random.choice([0, 1, 2, 3])
	if (choice == 0):
		return str(random.randint(-2147483648, 2147483647))
	if (choice == 1):
		return str(2147483647)
	if (choice == 2):
		return str(-2147483647)
	if (choice == 3):
		return str(0)

def input_char():
	choice = random.choice([0, 1])
	if (choice == 0):
		return "'" + random.choice(string.ascii_letters + string.digits) + "'"
	if (choice == 1):
		return "'\\0'"

def random_arg():
	format = "%"
	data = ""
	choices = ["s", "c", "p", "i", "d", "x", "X", "%", "u"]

	type = random.choice(choices)
	if (type == "s"):
		data = input_string()
	if (type == "c"):
		data = input_char()
	if (type == "p"):
		value = random.random()
		if (value < .33):
			data = "&a"
		elif (value < .66):
			data = "&b"
		else:
			data = "&c"
	if (type == "i" or type == "d"):
		data = input_int()
	if (type == "x"):
		data = input_int()
	if (type == "X"):
		data = input_int()
	if (type == "%"):
		data = ""
	if (type == "u"):
		data = input_uint()
	format += type
	return (format, data)
