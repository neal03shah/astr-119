import numpy as np
import sys

#define a function that returns a value

def expo(x) :
	return np.exp(x)	#return e^x 

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call expo

#define a main function
def main():
	n = 10 #default value for n

	#check if there is a command line
	#argument that has been passed?
	if(len(sys.argv)>1):
		n - int(sys.argv[1])	#reset n

	show_expo(n)

#run the main function
if __name__=="__main__":
	main()