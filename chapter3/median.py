#WORKS

import itertools

def generate_kmers(k):
	return ( list(itertools.product(['A', 'T', 'G', 'C'], repeat = k) ) )	

def difference(kmer, string):
	diff = 0
	for i in range(0, len(kmer)):
		if kmer[i] != string[i]:
			diff += 1
	return diff

def distance(kmer, dna_strand):
	min_distance = len(dna_strand)
	k = len(kmer)

	for i in range(0, len(dna_strand) - k):
		string = dna_strand[i:i+k]
		distance = difference(kmer,string)
		if distance < min_distance:
			min_distance = distance

	return min_distance
  
def d(kmer, dna):
	total_distance = 0
	min_distance = len(dna[0]) * len(dna)
	for strand in dna: 
		total_distance += distance(kmer, strand)
	
	return total_distance

def MedianString(dnas, k):
	kmers = generate_kmers(k)
	best_pattern = kmers[0]
	for kmer in kmers:
		print("kmer is", kmer, "and d is", d(kmer, dnas))
		if d(kmer, dnas) < d(best_pattern, dnas):
			best_pattern = kmer	

	return best_pattern

g = open("dataset_median.txt")
line = g.readline()
k = int(line)
dnas = g.readlines()

print( MedianString(dnas, k) ) 
