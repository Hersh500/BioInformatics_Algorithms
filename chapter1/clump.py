#WORKS 

def clump(k, l, t, dna):
	kmers = []
	for i in range(0, (len (dna) - k)):
		kmer = dna[i:i+k]
		for j in range(0, (len(dna) - l)):
			L = dna[j:j+l]
			if L.count(kmer) >= t:
				if kmer not in kmers: 
					kmers.append(kmer)

	return (kmers)

g = open ("dataset.txt")
dna = g.readline()
klt = g.readline()
klt = klt.split()
k = int(klt[0])
l = int(klt[1])
t = int(klt[2])

print (clump (k, l, t, dna))

