####
#'''Function definition and invocation.'''

def happyBirthdayEmily():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")

happyBirthdayEmily()
#########################
##Function		
age = get_int('enter your age:')
print('Age: %s' % age)	

def get_int(msg):
    while True:
	    try:
		    i = int(input(msg))
			return i
		except ValueError as err:
		    print(err)
			
#########################			
age = get_int("enter your age:")