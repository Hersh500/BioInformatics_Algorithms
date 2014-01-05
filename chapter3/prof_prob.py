#WORKS 

def get_matrix():
	g = open("dataset_prob.txt")
	dna = g.readline()
	k = int( g.readline()[0] ) 
	g.readline()
	profile = g.readlines()
	matrix = []

	for row in profile:
		row = row.split()
		print(row)
		sub_matrix = {'A': float(row[0]), 'C': float(row[1]), 'G': float(row[2]), 'T': float(row[3])}
		matrix.append(sub_matrix)

	return (dna, k, matrix)

def calc_prob(matrix, kmer):
	prob = 1
	for n in range(0, len(kmer)):
		prob = prob * matrix[n][kmer[n]]
	return prob
		
		
def most_prob(dna, matrix, k):
	max_prob = ["",0]
	for i in range(0, len(dna) - k):
		kmer = dna[i:i+k]
		prob = calc_prob(matrix, kmer)
		if prob > max_prob[1]:
			max_prob[0] = kmer
			max_prob[1] = prob

	return max_prob[0]

dna, k, matrix = get_matrix()

print (most_prob(dna, matrix, k)) 
	
