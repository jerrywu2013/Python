s = input("enter an integer:")
try:
    i = int(s)
    print("valid integer entered:", i)
except ValueError as err:
    print(err)

#https://docs.python.org/2/tutorial/errors.html
	