#Title:Python chapter 3
#Date:2014/12/01
#Author:Jerry Wu
#E-mail:jerry@mail.ntust.edu.tw

#Tuple

hair = "black","brown","blonde","red"
type(hair)
hair = ("black","brown","blonde","red")
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

