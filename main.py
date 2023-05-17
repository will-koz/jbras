#!/usr/bin/python3

import math, random

characters = [ ("Jack Boller", 50), ("Ali Baba", 35), ("Thief", 25) ]

# Convert a list of elements of the set {0, 1} into a floating point number
def binary_list_to_float (x = None):
	if x == None:
		x = gen_binary_list();
	sum = 0
	current_delta = 1
	for i in x:
		current_delta *= 0.5
		if i:
			sum += current_delta
	return sum

def doubly_open_ended_number ():
	return inv_cdf(binary_list_to_float())

# Flip a coin x times
def gen_binary_list (x = 10):
	l = []
	for i in range(x):
		l.append(math.floor(random.random() * 2))
	return l

def gen_characters (x = 3):
	idx = 0

	# Generate health points
	for i in range(x):
		s = characters[min(i, len(characters) - 1)]
		print(s[0] + ": " + str(math.ceil(s[1] + doubly_open_ended_number())))

# TODO comment this
def inv_cdf (x):
	return -math.log(1 / x - 1, 2)
