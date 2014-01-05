#WORKS

def slice_sort(p, cur_index):
	for i in range(cur_index, len(p)):
		if p[i] == cur_index + 1 or p[i] == -(cur_index +1):
			p[cur_index:i+1] = reversed(p[cur_index:i+1])
			for j in range(cur_index, i+1):
				p[j] = -p[j]
			break
	return p 

def print_p(p):
	string = "("	
	sep = " "
	for i in range(0, len(p) - 1):
		if p[i] > 0:
			string += "+" + str(p[i]) + sep
		else:
			string += str(p[i]) + sep

	if p[len(p) - 1] > 0:
		string += "+" + str(p[len(p) - 1]) + ")"
	else:
		string += str(p[len(p) - 1]) + ")"

	return string

def greedy_sort(p, f):
	rev_distance = 0

	for k in range(0, len(p)):
		if p[k] != k+1 and p[k] != -(k+1): 	
			p = slice_sort(p, k)
			rev_distance += 1
			f.write(print_p(p) + "\n")	

		if p[k] == -(k+1):
			rev_distance += 1
			p[k] = k+1
			f.write(print_p(p) + "\n")	


def get_p():
	g = open("greedy_sort.txt")
	lst = g.readline().strip('\n').split()
	lst[0] = lst[0][1:]
	lst[len(lst) - 1] = lst[len(lst) - 1].strip(")")
	for i in range(0, len(lst)):
		if "+" in lst[i]:
			lst[i] = int(lst[i][1:])
		else:
			lst[i] = int(lst[i])
	g.close()
	return lst

p = get_p()
f = open("greedy_out.txt", "w")
greedy_sort(p, f)

