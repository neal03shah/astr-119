import numpy as np

x = 1.0
y = 2.0

#exponents and logarithms
print(np.exp(x)) #e^x
print(np.log(x)) #ln x
print(np.log10(x)) # log_10 x
print(np.log2(x)) # log_2 x

#min/max/misc
print(np.fabs(x)) #absolute value of as a float
print(np.fmin(x,y)) #min of floats x and y
print(np.fmax(x,y)) #max of floats x and y

#populate arrays
n = 100 #define an int
z = np.arange(n,dtype=float) #array [0.0,float(n-1)]
z *= 2.0*np.pi/float(n-1)
sin_z = np.sin(z) #an aray sin(z)

#interpolate
print(np.interp(0.75,z,sin_z))
print(np.sin(0.75))



print(z)
print(sin_z)
