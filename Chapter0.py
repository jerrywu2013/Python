#Chapter0
"$(FULL_CURRENT_PATH)"

print (3, -1, 3.14159, -2.8)


print (type(3))
print (type(3.14159))
print (type(3.0))



print (int(3.14159), int(-2.8))
print (float(3), float(-1))



print (3.1415926535897932384626433832795028841971)



print (1.4142135623730950488016887242096980785696)

# arithmetic operators
# +		plus		addition
# -		minus		subtraction
# *		times		multiplication
# /		divided by 	division
# **    power		exponentiation

print (1 + 2, 3 - 4, 5 * 6, 2 ** 5)


print (1.0 / 3, 5.0 / 2.0, -7 / 3.0)


print (1 / 3, 5 / 2, -7 / 3)


# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression
# 先乘除後加減
print (1 + 2 * 3, 4.0 - 5.0 / 6.0, 7 * 8 + 9 * 10)

print (1 * 2 + 3 * 4)
print (2 + 12)


# always manually group using parentheses when in doubt


print (1 * (2 + 3) * 4)
print (1 * 5 * 4)



# valid variable names - consists of letters, numbers, underscore (_)
# starts with letter or underscore
# case sensitive (capitalization matters)

# legal names - ninja, Ninja, n_i_n_j_a
# illegal names - 1337, 1337ninja

# Python convention - multiple words joined by _
# legal names - elite_ninja, leet_ninja, ninja_1337
# illegal name 1337_ninja


# assign to variable name using single equal sign =
# (remember that double equals == is used to test equality)

# examples 

my_name = "Joe Warren"
print (my_name)

my_age = 51
print (my_age)

# birthday - add one

#my_age += 1
#my_age = my_age +1
print (my_age)


# the story of the magic pill

magic_pill = 30
print (my_age - magic_pill)

my_grand_dad = 74

print (my_grand_dad - 2 * magic_pill)





# Temperature examples
#華氏(Fahrenheit)轉攝氏(Celsius)臺灣
# convert from Fahrenheit to Celsuis
# c = 5 / 9 * (f - 32)
# use explanatory names

#攝氏(Celsius) = (Fahrenheit-32)*5/9
#華氏(Fahrenheit) = Celsius*(9/5)+32 


temp_Fahrenheit = 200
#華氏212度，攝氏是多少
temp_Celsius = 5.0 / 9.0 * (temp_Fahrenheit - 32)
print (temp_Celsius)

#Test!

#Data Type
#Font
"Hard Times"[5]
"giraffe"[0]

#Object Reference
#Variable
x = "blue"
y = "green"
z = x

print (x, y, z)
z = y 
print (x, y, z)
x = z 
print (x, y, z)

route = 866
print (route, type(route))

route = "North"
print (route, type(route))

#Collection Data Type

"Denmark","Finland","Norway","Sweden"
"one",
x = [1,4,9,16,25,36,49]
type(x)
x[1]
x[0]

y = ["Denmark","Finland","Norway","Sweden"]
z=y[0]
type(z)

#Len()
len("one")
len("one",)
len(("one",))
len([3,5,1,2,"pause",5])
len("automatically")

#append()
x = ["zebra",49,-879,"aardvark",200]
x.append("more")
print (x)
type(x)
#list.append()
list.append(x, "extra")
print (x)
type(x)

#Switch data
x[1] = "kk"
x

#Explorer data
x[0:3]

##Logic 
a = ["R", 3, None]
b = ["R", 3, None]
a is b
b = a
a is b

a = "something"
b = None
a is not None
b is not None
a is not None, b is not None

#<, <=, ==, !=, >=, >
a = 2
b = 6
a == b
a <= b, a != b, a >= b, a > b

a = "many paths"
b = "many paths"
a is b
a == b

a = 9
0 <= a <= 10

"3" > 4
3 > 4
int("3") > 4

##Membership
p = (4, "frog", 9, -33, 9, 2)
2 in p
"dog" not in p




