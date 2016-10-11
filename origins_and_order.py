import itertools, datetime

def getDate(test):
	try:
		return datetime.date(*test) # * converts list to arguments
	except ValueError:
		return None

def answer(x,y,z):
	results = filter(lambda a: a != None, map(getDate, set(itertools.permutations([x,y,z]))))
	if(len(results) > 1): return "Ambiguous"
	return str(results[0].month).zfill(2) + "/" + str(results[0].day).zfill(2) + "/" + str(results[0].year).zfill(2)
	
print answer(2,13,31)