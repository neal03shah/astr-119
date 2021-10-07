x = [0.0, 3.0, 5.0, 2.5, 3.7]	#define an array
print(type(x))

#print x
print("Originally x = ",x)

#remove the third element
x.pop(2)
print(x)

#remove the element equal to 2.5
x.remove(2.5)
print(x)

#get a copy
y = x.copy()
print(y)

#how many elements equal 0.0
print(y.count(0.0))

#print the index with value 3.7
print(y.index(3.7))

#sort the list
print("Inserting 5.9 at the beginning of y")
y[0] = 5.9
print(y)
print("Sorting y in ascending order...")
y.sort()
print(y)

#reverse sort
y.reverse()
print(y)

#remove all elements
y.clear()
print(y)