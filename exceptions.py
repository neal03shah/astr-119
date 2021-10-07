#python exceptions let you deal
#with unexpected results

try:
	print(a) #this will throw an exception because a is not defined
except:
	print("a is not defined!")

#there are specific errors

try:
	print(a)	#will throw an exception
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong")

#this will break our program
print(a)