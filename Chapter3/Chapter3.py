#Title:Python chapter 3
#Date:2014/12/01
#Author:Jerry Wu
#E-mail:jerry@mail.ntust.edu.tw

#####Tuple

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

#####List

hair = ["black","brown","blonde","red"]
type(hair)

list()

L = [-17.5,"kilo",49,"V",["ram",5,"echo"],7]
L[0]==L[-6]==-17.5
L[1]==L[-5]


first, *rest = [9,2,-4,8,7]
first, rest

#####List Comprehension

leaps=[]
for year in range(1900,1940):
	if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
		leaps.append(year)
		
		
leaps = [y for y in range(1900,1940) if(y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)]



#####Set
S = {7,"veil",0,-29,("x",11),"sun",frozenset({8,4,7}),913}
Type(S)
S[0]
a = list(S)

set("pecan") | set("pie") == {'p','e','c','a','n','i'}
set("pecan") & set("pie") == {'p','e'}
set("pecan") - set("pie") == {'c','a','n'}
#set("pie") - set("pecan") == {"i"}
set("pecan") ^ set("pie") == {'c','a','n','i'}


0 in S
0 not in S
##
S.add(20)
##
S.clear()

##
a = {2}
S.difference(a)
##
S.difference_update(a)
##
S.discard(-29)
##
S = {7,"veil",0,-29,("x",11),"sun",frozenset({8,4,7}),913}
a = {913}
S.intersection(a)
##
S.intersection_update(a)
##
S = {7,"veil",0,-29,("x",11),"sun",frozenset({8,4,7}),913}
a = {27}
S.isdisjoint(a)
##
b = {20,21,30}
c = {20,21}
b.issubset(c)
c.issubset(b)
##
c.issuperset(b)
b.issuperset(c)
##
b.pop()
##
S.remove(-29)
##
b = {20,21,30}
c = {20,21}
b.symmetric_difference(c)
##
b = {20,21,30}
c = {20,21}
b.symmetric_difference_update(c)
##
b = {20,21,30}
c = {20,21,34,88}
b.union(c)
##
b.update(c)


#####dict
d1 = dict({"id":1948,"name":"washer","size":3})
d2 = dict(id=1948,name="washer",size=3)
d3 = dict([("id",1948),("name","Washer"),("size",3)])
d4 = dict(zip(("id","name","size"),(1948,"Washer",3)))
d5 = {"id":1948,"name":"Washer","size":3}

d1["id"]
d1["size"]=10

#items
for item in d1.items():
    print(item[0],item[1])

#keys
for key in d1:
    print(key)

#values
for value in d1.values():
    print(value)

##
d1.clear()
##
d2.copy()
##
d1 = dict.fromkeys("12345")
d1 = dict.fromkeys("12345",20)
##
d2.get("name")
##
d2.items()
##
d2.keys()
##
d2.values()
##
d2.pop("name")
##
d3.popitem()
##
d3.update(dict(ss=20))


#Tuple A = () 有順序、可重複、迭代只供讀取不能變動
#List B = ([]) 有順序、可重複、迭代允許改變
#set  C = set() 沒有順序、不可重複、迭代不允許改變
#dict S = {} 沒有順序、key不能重複




