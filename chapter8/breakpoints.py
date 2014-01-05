#WORKS

import greedy #Uses the greedy sorting code to get the data in an appropriate format

def calc_breakpoints(p):
	p.insert(0, 0)
	p.insert(len(p), len(p)) 
	print(p)
	numpoints = 0	

	for i in range(1, len(p)):
		if p[i] != p[i-1] + 1: 
			numpoints += 1

	return numpoints			

p = greedy.get_p()
print (calc_breakpoints(p))
