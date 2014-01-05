import PROT_LIB #uses functions from the PROT program 
import RNA #uses functions to translate dna to rna 
import REVC_LIB # uses functions from the reverse complement program

def calc (dna, protein):
	dnas = []
	prot_len= len(protein) * 3  
	dna_len = len(dna)

	for i in range(0, 1 + dna_len - prot_len):
		substr = dna[i:i+prot_len] 
		if PROT_LIB.translate(RNA.RNA(substr)) == protein:
			dnas.append(substr)        # REVC_LIB.C() finds the complement of the substring
		elif PROT_LIB.translate(RNA.RNA(REVC_LIB.C(substr))) == protein:
			dnas.append(substr)		#^ function from RNA.py	

	return (dnas)

g = open("dataset_pep_2.txt")
dna = g.readline() 
prot = g.readline() 
lst = calc(dna, prot)
string = ""
for item in lst: 
	string = string + item + " "
print(string)
			
