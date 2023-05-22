#!/usr/bin/python3

import math, random

characters = [ ("Jack Boller", 50), ("Ali Baba", 35), ("Thief", 25) ]
explosives = [ "black", "blue", "green", "red" ]
stashes = "ABCDEF"

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

def calc_speed (is_male = True, intox = 0):
	num = 12 if is_male else 9
	num += intox
	num += doubly_open_ended_number()
	num = max(math.ceil(num), 0)
	return num

def doubly_open_ended_number ():
	return inv_cdf(binary_list_to_float())

# Choose explosives / detonators
def equipment ():
	choice = random.choice(explosives)
	print(characters[0][0] + ": " + choice)
	print(characters[1][0] + ":", end = "")
	for i in explosives:
		if i != choice:
			print(" " + i, end = "")
	print()
	print("Folder \"V\" starts in stash " + random.choice(stashes) + ".")

# Sums the second argument with the first argument number of doubly open-ended numbers. Useful for
# calculating the damage of firearms.
def firearm (x, y):
	sum = y
	for i in range(x):
		sum += doubly_open_ended_number()
	print(round(sum))

# Flip a coin x times
def gen_binary_list (x = 25):
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
	print("(Last " + characters[-1][0] + " gets +1 style point.)")

# Generate the distance a grenade can go
def get_grenade_distance (x = 5):
	print(max(0, math.floor(x + (doubly_open_ended_number() / 2))))

# Print out the speed a player can move in a turn.
def get_speed (is_male = True, intox = 0):
	speeds = []
	for i in range(2):
		speeds.append(calc_speed(is_male, intox))
	print(speeds)

# given a number between 0 and 1, return a number between -infinity and infinity
def inv_cdf (x):
	return -math.log(1 / x - 1, 2)
