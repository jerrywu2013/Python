for x in [1,2,3,4,5,6]:
    print(x)
###########################
#4 to 9 
nums = range(4, 9, 2)
print(list(nums))
#list(range(10, 0, -1))

###########################
for x in range(1, 10):
    for y in range(1, 10):
        print (x ,'*', y ,'=' ,x*y)

###########################
#\n about columns break.
for x in [1,2,3,4,5,6,7,8,9]:
    for y in [1,2,3,4,5,6,7,8,9]:
        print ('%s*%s=%s \n' % (x,y,x*y))
###########################
#\t about space.
for x in range(1,10):
    for y in range(1,10):
        print ('%s*%s=%s \t' % (x,y,x*y))
###########################

##Advance 9*9 problem
###########################
print ("\n".join(["\t".join(["%d*%d=%d" % (j,i,i*j) for i in range(1,10)]) for j in range(1,10)]))

###########################
a = "Free your mind."
print(a)
print("&".join(a))
##########################

