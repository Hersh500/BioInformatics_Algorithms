#WORKS

def calc_indeces(dna, pattern, d):
	indexs = []

	for i in range(0,1+ len(dna) - len(pattern)):
		mismatch = 0
		j = 0 
		while j < len(pattern):
			if dna[i+j] != pattern[j]:	
				mismatch += 1
			if mismatch > d:
				break

			j += 1

		if mismatch <= d:
			indexs.append(i)
				

	return indexs

g = open("dataset_approx.txt")
pattern = g.readline()
dna = g.readline()
d = int (g.readline())
string = ""
for i in calc_indeces(dna, pattern, d):
	string += str(i) + " "
print (string)
