# Boy am I happy about this solution.

from math import floor,ceil,log

def answer(x):
	return [["-","R","L"][int(floor((x+.5*(3**i-1))/(3**i)))%3] for i in range(int(ceil(log(2*x,3))))]
	
print answer(1000000000)