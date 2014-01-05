#WORKS

import PROB_PROF_LIB as pf #uses a modified version of Probability Profile Problem 

def profile(motifs, profile):

	if len(motifs) == 1:
		profile = {'A': [], 'C': [], 'G': [], 'T': []}
		for n in motifs[0]:
			for key in profile:
				if key == n:
					profile[key].append(1)
				else:
					profile[key].append(0)

	
	else:
#		print("motifs passed into profile is", motifs)
		motif = motifs[ len(motifs) - 1 ]
		for key in profile:
			profile[key] = [x*(len(motifs) -1) for x in profile[key]]

		for i in range(0, len(motif)):
			for key in profile:
				if key == motif[i]:
					profile[key][i] += 1 
		
		for key in profile:
			profile[key] = [x/len(motifs) for x in profile[key]]
				
	return profile

def calc_prob(prof, kmer):
	#print("prof passed into calc_prob is ", prof)
	prob = 1
	for n in range(0, len(kmer)):
		#print("kmer[n] is ", kmer[n])
		prob = prob * prof[kmer[n]][n]
	return prob

def most_prob(dna, profile, k):
	max_prob = [dna[0:k], 0]	
	#print("profile passed into most prob is", profile)
	for i in range(0, len(dna) - k):
		kmer = dna[i:i+k]
		prob = calc_prob(profile, kmer)
		if prob > max_prob[1]:
			max_prob[0] = kmer
			max_prob[1] = prob
	
	return max_prob[0]
	
				 	
def consensus(motifs, prof, k):
	consensus = ""
	for i in range(0, k):
		mx = ["", -1] 
		for nucleotide in prof:
			if prof[nucleotide][i] > mx[1]:
				mx[0] = nucleotide
				mx[1] = prof[nucleotide][i] 

		consensus += mx[0]
	print("consensus for", motifs, "is", consensus)	
	return (consensus)

def score(motifs, k, prof):
	score = 0
	cons = consensus(motifs,prof,k) 
	#print("length of motifs is ", len(motifs))
	#print(motifs)
	for motif in motifs:
	#	print(motif)
		for i in range(0, k):
	#		print("i is ", i)
			if motif[i] != cons[i]:
				score += 1
	
	return (score)

def print_profile(prof):
	for nucleotide in prof:
		print(nucleotide, ": ", prof[nucleotide])

def greedy(dnas, k):
	dna = dnas[0]
	best_motifs = []
	best_profile = {} 

	for i in range(0, len(dnas)):
		best_motifs.append (dnas[i][0:k])	
		best_profile = profile (best_motifs, best_profile)
		

	for i in range(0, len(dna) - k):
		kmer = dna[i:i+k]
		#print(kmer)
		motifs = [kmer]
		prof = profile(motifs, {}) 
		for j in range(1, len(dnas)):
			#print("profile for kmer", kmer, "is", prof)
			#print("kmer", kmer, "comes from ", dnas[j-1])
			kmer = most_prob(dnas[j], prof, k)
	#		print("most prob kmer", kmer)
			motifs.append(kmer)
			#print("motifs in greedy after: ", motifs)
			prof = profile(motifs, prof) 
			#print_profile(prof)
	
		#print("profile for motifs", motifs)
		#print(prof)
		#print()
		if score(motifs, k, prof) < score(best_motifs, k, best_profile):
			best_motifs = list(motifs)
	#		print("best motifs is updated to ", best_motifs)
			best_profile = dict(prof)
	
	return (best_motifs)
g = open("dataset_greedy.txt")
line = g.readline()
line = line.split()
k = int(line[0])
print(k)
dna = g.readlines()
dna = [x.strip('\n') for x in dna]
lst = greedy(dna,k)
for item in lst:
	print(item)

