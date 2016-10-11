# Didn't find out why this failed one of five tests, went to bed, and was preoccupied during the rest of the time limit.

def answer(meetings):
	max=0;
	for i in meetings:
		schedule=[i]
		for j in meetings:
			add=True
			for k in schedule:
				if(j[0]<k[1] and j[1]>k[0]):
					add=False
			if add:
				schedule.append(j)
		if len(schedule)>max:
			print schedule
			max=len(schedule)
		
	return max
	
l=[[99-i,100-i] for i in range(0,100)]
print answer(l)