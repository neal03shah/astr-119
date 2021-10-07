#string

s = "I am a string."
print(type(s))	##returns str

#Boolean
yes = True
print(type(yes))	## boolean

no = False
print(type(no))

# List -- ordered and changeable
alpha_list = ["a", "b", "c"]	#list initalization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#Tuple -- ordered and unchangeable
alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't change elements of a tuple.")
print(alpha_tuple)
