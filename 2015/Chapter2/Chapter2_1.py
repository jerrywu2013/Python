#Title:Python chapter 2
#Date:2014/12/01
#Author:Jerry Wu
#E-mail:jerry@mail.ntust.edu.tw

#keywords
pass=1
with=1
return=1

#
for in (0,1,2,3,4,5):
	print("Hello")

#####Integer
x=10
y=2
z=4

x+y
x-y
x*y
x/y
x//y
x%y
x**y
-x
+x
abs(x)
divmod(x,y)
pow(x,y)
pow(x,y,z)
#pow(10,2,2) = (10*10) % 2
round(10.23333,2)

#Binary 
bin(1980)
#Hexadecimal
hex(1980)
#Octal
oct(1980)
#int
int(1.2456)
int(bytearray(b'123'), 20)

#Decimal(10)
14600926
#Binary(2) 
0b110111101100101011011110
#Octal(8)
0o67545336
#Hexadecimal(16)
0xDECADE

#Boolean
t= True
f=False
t and f
t and True


######Floating-point number
0.0,5.4,-2.5,8.9e-4

import math
math.acos(0.64)
math.acosh(1.64)
math.asin(1)
math.asinh(1)
math.atan(1)
math.atan2(1,2)
math.atanh(0.64)
math.ceil(0.64)
math.copysign(0.634,2)
math.cos(0.64)
math.cosh(0.64)
math.degrees(0.64)
math.e
math.exp(0.64)
math.fabs(x)
math.factorial(5) #階乘
math.floor(5.4)

#Decimal
import decimal
a = decimal.Decimal(9876)
b = decimal.Decimal("54321.012345678987654321")
a + b

23/1.05
print(23/1.05)
print(decimal.Decimal(23)/decimal.Decimal(1.05))

######Character

str(2.3)
#int(2.3)
#float(2.3)

#Slice
s = "Light ray"
s[-9]
s[0]

s[-1]
s[8]

s[0:2]
s[:]
s[0:len(s)]

x = "The waxwork man"
x[:12] + "wo" + x[12:]

x1 = "he ate camel food"
x1[::-2]
x1[::3]
x1[-1:2:-2]
x1[:2:-2]

treatises = ["A","C","D"]
" ".join(treatises)
"-<>-".join(treatises)
"".join(treatises)

##x.capitalize() #Return capital letter
x = "work"
print(x)
x.capitalize()


##x.center(width,char)
x = "This is a book."
print(x)
print(x.center(56, "="))
x.center(15,"=")

##x.count()
x = "This is a book."
print(x)
print(x.count("i"))
print(x.count("i",0,4))

##x.encode()
x = "This is a book."
x.encode(encoding="utf-8")

##x.endswith()
x.endswith(".")
x.endswith("i")

##x.expandtabs()
x = "b\t\t\tb"
print(x)
print(x.expandtabs())
print(x.expandtabs(0))
print(x.expandtabs(1))
print(x.expandtabs(4))

xx="a\ta"

##x.find() 
#index
x = "This is a book."
x.find("T")
#x.index()
x.index("T")

#x.isalnum() #Check number or character in vector
x = "66+88"
x1 = "book1234"
x2 = "This is a book."
x.isalnum()
x1.isalnum()
x2.isalnum()

#a.isalpha() #Check character in vector
x = "66+88"
x1 = "book1234"
x2 = "This is a book."
x3 = "Hi"
x.isalpha()
x1.isalpha()
x2.isalpha()
x3.isalpha()

#x.isdecimal() #Check Unicode number in vector
x = "66+88"
x1 = "1234567"
x.isdecimal()
x1.isdecimal()

#x.isdigit() #Check ASCII number in vector
x = "0sss566"
x1 = "0o127"
x2 = "6523"
x.isdigit()
x1.isdigit()
x2.isdigit()

#x.isidentifier()  #Check keywords
x = "if" 
x1 = "h appy"
x2 = "h_appy"
x.isidentifier()
x1.isidentifier()
x2.isidentifier()

#x.islower() #Return small letter
x1 = "Happy"
x2 = "happy"
x1.islower()
x2.islower()