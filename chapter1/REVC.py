#WORKS

def splt(string):
	lst = []
	for item in string:
		lst.append(item)
	return (lst)

def REV(dna):
	dna = dna[::-1] #Reverses the DNA sequence
	return dna

def C(dna):
	dna = splt(dna)
	print (dna)
	x = len(dna)
	for i in range(0, x):
		if dna[i] == "T":
			dna[i] = "A"
		elif dna[i] == "A":
			dna[i] = "T"
		elif dna[i] == "C":
			dna[i] = "G"
		elif dna[i] == "G":
			dna[i] = "C"
	return (''.join(dna))

g = open("dataset_3_2.txt")
dna = g.read(); 
dna = REV(dna)
dna = C(dna) 	
print(dna); 
