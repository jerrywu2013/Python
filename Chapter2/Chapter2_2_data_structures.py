x = [22, 56.3, 23, 1, 34.5]
##x.count()
#Return the number of times x appears in the list.
print(x.count(22), x.count(56.3), x.count('x'))

#Insert an item at a given position. 
x.insert(3, -1)

#Add an item to the end of the list.
x.append(222)

#Remove the first item from the list whose value is x
x.remove(222)

#Reverse the elements of the list in place.
x.reverse()

#Sort the items of the list in place.
x.sort()

#Remove the item at the given position in the list, and return it.
x.pop()
x.pop(2)

###List Comprehensions
#List comprehensions provide a concise way to create lists.

squares = []
for x in range(10):
squares.append(x**2)
#squares.append(pow(x,2))

#which is more concise and readable.
squares = [x**2 for x in range(10)]

#R language
#squares<-(0:9)^2

#A list comprehension consists of brackets containing 
#an expression followed by a for clause, then zero or more for or if clauses.
# 
xx =[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]



