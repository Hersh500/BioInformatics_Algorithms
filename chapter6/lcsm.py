#WORKS
#DIFFERENT THAN ROSALIND PROBLEM 

import sys
sys.setrecursionlimit(100000)

def print_matrix(matrix):
	for row in matrix:
		print(row)
	print()

def lcs(dna1, dna2):
	s = [ [0 for i in range(0, len(dna2) + 1)] for j in range(0, len(dna1) + 1)]
	backtrack = [ [0 for i in range(0, len(dna2) + 1)] for j in range(0, len(dna1) + 1)]

	for i in range(1, len(dna1) + 1):
		for j in range(1, len(dna2) + 1):
			#print("<",i,j,">")

			if dna1[i-1] == dna2[j - 1]:
				s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + 1)
			else:
				s[i][j] = max(s[i-1][j], s[i][j-1])
			
			
			if s[i][j] == s[i-1][j]:
				backtrack[i][j] = -1 #Vertical
			elif s[i][j] == s[i][j-1]:
				backtrack[i][j] = 1   #Horizontal
			elif s[i][j] == s[i-1][j-1] + 1:
				backtrack[i][j] = 2  #Diagonal

	print_matrix (s)
	print_matrix(backtrack)
	return (s[len(dna1) - 1][len(dna2) - 1], backtrack)

def output_LCS(backtrack, dna1, i, j):
	if i == 0 or j == 0:
		return
	if backtrack[i][j] == -1:
		output_LCS(backtrack, dna1, i-1, j)
	elif backtrack[i][j] == 1:
		output_LCS(backtrack, dna1, i, j-1)
	else:
		output_LCS(backtrack, dna1, i-1, j-1)
		print( dna1[i-1], end = "" )

g = open("lcsm.txt")
dna1 = g.readline()
dna2 = g.readline()

result, backtrack = lcs(dna1, dna2)
output_LCS(backtrack, dna1, len(dna1), len(dna2))
print()
