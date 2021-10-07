#python exceptions demonstrated

try:
	print(a) #but note that a is not defined
except:
	print("a is not defined")

#specific errors to help with cases
try:
	print(a) #this will fail
except NameError:
	print("a is still not defined")
except:
	print("Something else went wrong")

#this will break out program
print(a)