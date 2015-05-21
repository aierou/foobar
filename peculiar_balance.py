# Boy am I happy about this solution.

import math

def answer(x):
	return [["-","R","L"][int(math.floor((x+.5*(3**i-1))/(3**i)))%3] for i in range(int(math.ceil(math.log(2*x,3))))]
	
print answer(1000000000)