#WORKS

import itertools # Uses functions from the itertools library
import approx_pattern # Uses a modified version of approx_pattern, from chapter 2

def splt(string):
	lst = []
	for char in string:
		lst.append(char)
	return (lst)

def get_mutations(kmer, d, combo_positions, combinations):
	mutations = []

	for positions in combo_positions:
#		print("positions is ", positions)
		for combo in combinations:
#			print("combo = ", combo)
			mutation = splt(kmer)
			count = 0	
			for index in positions:
#				print("index is ", index)
				mutation[ index ] = combo[count]

				if mutation not in mutations:
					mutations.append(''.join(mutation))	

				count += 1

#	print(mutations)
	return (mutations)

def find_with_mutations(dnas, mutation, d):
	for dna in dnas:
		if ( len(approx_pattern.calc_indeces(dna, mutation, d)) == 0):
			return False 

	return True

def enumerate(dnas, d, k, combo_positions, combinations):
	dna1 = dnas[0]
	dnas.remove(dna1)
	corrects = []	
	for i in range(0, len(dna1) - k):
		kmer = dna1[i:i+k]
#		print(kmer)
		mutations = get_mutations(kmer, d, combo_positions, combinations)
		for mutation in mutations:
			if (find_with_mutations (dnas, mutation, d) and mutation not in corrects):
				corrects.append(mutation)

	return corrects	

g = open("dataset_enum.txt")
g.readline()
k = int(line1[0])
d = int(line1[2])

dnas = g.readlines()
print(dnas)

positions = range(0, k)
combo_positions = list(itertools.combinations(positions, d)) 
combinations = list(itertools.product(['A', 'T', 'G', 'C'], repeat = d))
mutations = enumerate(dnas, d, k, combo_positions, combinations)
mutations = [ x + " " for x in mutations]
print (''.join(mutations))
			
		
	
		
