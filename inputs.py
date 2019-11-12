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
	data = []
	choices = ["s", "c", "i", "d", "x", "X", "%", "u"]

	width = ""
	size = ""
	flags = ""

	type = random.choice(choices)
	if (random.random() > .5):
		if (random.random() > .8):
			width = "*"
			data.append(str(random.randint(-10, 10)))
		else:
			width = str(random.randint(1, 20))
	if (random.random() > .5):
		if (random.random() > .8):
			size = ".*"
			if (type != "%" and type != "c"):
				data.append(str(random.randint(-10, 10)))
		else:
			size = "." + str(random.randint(0, 5))
	choice = random.choice([0, 1, 2])
	if (choice == 0):
		flags = ""
	elif (choice == 1):
		flags = "-"
	else:
		flags = "0"
	if (type == "s"):
		format += flags.replace("0", "")
		format += width
		format += size
		data.append(input_string())
	if (type == "c"):
		format += flags.replace("0", "")
		format += width
		data.append(input_char())
	if (type == "i" or type == "d"):
		format += flags
		format += width
		format += size
		data.append(input_int())
	if (type == "x"):
		format += flags
		format += width
		format += size
		data.append(input_int())
	if (type == "X"):
		format += flags
		format += width
		format += size
		data.append(input_int())
	if (type == "%"):
		data = []
		data.append("")
	if (type == "u"):
		format += flags
		format += width
		format += size
		data.append(input_int())
	format += type
	return (format, data)
