#Title:Python chapter 3
#Date:2014/12/01
#Author:Jerry Wu
#E-mail:jerry@mail.ntust.edu.tw

#Tuple

hair = "black","brown","blonde","red"
type(hair)


type(hair)

hair[2]
hair[-3]

x = hair[:2],"gray",hair[2:]
x[0]
x[0][1]

things = (1,-7.5,("pea",(5,"Xyz"),"queue"))
things[2][1][1][2]

manufacturer, model, seating = (0,1,2)
min,max=(0,1)
aircraft = ("airbus","a320-200",(100,220))
aircraft[seating][max]

import math

for x,y in ((-3,-4),(5,12),(28,-45)):
	print(math.hypot(x,y))
	
x = (-3**2)+(-4**2)	
math.sqrt(abs(x))

#List

hair = ["black","brown","blonde","red"]
type(hair)

list()

L = [-17.5,"kilo",49,"V",["ram",5,"echo"],7]
L[0]==L[-6]==-17.5
L[1]==L[-5]


first, *rest = [9,2,-4,8,7]
first, rest

#List Comprehension

leaps=[]
for year in range(1900,1940):
	if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		leaps.append(year)
		
		
leaps = [y for y in range(1900,1940) if(y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]



#Set
S = {"black","brown","blonde","red"}
Type(S)

set("pecan") | set("pie") == {'p','e','c','a','n','i'}
set("pecan") & set("pie") == {'p','e'}
set("pecan") - set("pie") == {'c','a','n'}
#set("pie") - set("pecan") == {"i"}
set("pecan") ^ set("pie") == {'c','a','n','i'}




