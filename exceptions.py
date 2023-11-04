#!/usr/bin/env python3

# Example 1

# Add an exception
try: 
	# Here we write the operation
	obj = 1.0/0

except ZeroDivisionError:
	# Add an exception warning
	print("Warning: you are dividing by zero")
	obj = 1.

print(obj)

# Example 2

# another example: trying to access a key that does not 
# exist in a dictionary

dictionary_1 = {"key1": 1., "key2": 2., "key3": 3.}

#print(dictionary_1["key4"]) # gives an error

# Add an exception
try:
	val = dictionary_1["key4"]

except KeyError:
	print("Warning: this key does not exist in\n a dictionary, reverting to key3")

	val = dictionary_1["key3"]

print(val)

# Example 3
# opening a file 

#file = open("file.txt", "r") # the file does not exist

try:

	file = open("file.txt", "r")

except FileNotFoundError:

	print("Error: that file does not exist")

	file = open("./text_files/file.txt", "r")

print(file)
