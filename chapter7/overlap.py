#WORKS
#Follows the same template as Global, Local, Edit distance, and fitting alignment

import sys
sys.setrecursionlimit(100000)

str1 = "" 
str2 = "" 

def print_matrix(matrix):
	for row in matrix:
		print(row)
	print()

acids = {"A": 0, "C": 1, "D":2, "E":3, "F":4, "G":5, "H":6, "I":7, "K":8, "L":9, "M":10, "N":11, "P": 12, "Q": 13, "R": 14, "S":15, "T":16, "V":17, "W":18, "Y":19}

def construct_backtrack(dna1, dna2, indel_penalty):
	maximum_value = 0
	max_i = 0
	max_j = 0
	s = [ [0 for i in range(0, len(dna2) + 1)] for j in range(0, len(dna1) + 1)]
	backtrack = [ [0 for i in range(0, len(dna2) + 1)] for j in range(0, len(dna1) + 1)]

#	for i in range(0, len(dna1) + 1):
#		s[i][0] = s[i-1][0] - indel_penalty 
#	for j in range(1, len(dna2) + 1):
#		s[0][j] = s[0][j-1] - indel_penalty  

	for i in range(1, len(dna1) + 1):
		for j in range(1, len(dna2) + 1):
			x = acids [ dna1[i - 1] ] 
			y = acids [ dna2[j - 1] ]
			if x == y:
				s[i][j] = max ( s[i-1][j] - indel_penalty, s[i][j-1] - indel_penalty, s[i-1][j-1] + 1)
			else:
				s[i][j] = max ( s[i-1][j] - indel_penalty, s[i][j-1] - indel_penalty, s[i-1][j-1] - 2) 


			if s[i][j] == s[i-1][j] - indel_penalty:
				backtrack[i][j] = -1 #Vertical
			elif s[i][j] == s[i][j-1] - indel_penalty:
				backtrack[i][j] = 1   #Horizontal
			elif s[i][j] == s[i-1][j-1] + 1 or s[i][j] == s[i-1][j-1] - 1:  
				backtrack[i][j] = 2  #Diagonal
	max_score = 0
	for i in range(0, len(dna1) +1):
		if s[i][len(dna2)] >= max_score:
			max_score = s[i][len(dna2)]
			max_i = i
			max_j = len(dna2)
	for j in range(0, len(dna2) + 1):
		if s[len(dna1)][j] >= max_score:
			max_score = s[len(dna1)][j]
			max_j = j
			max_i = len(dna1)

	print_matrix (s)
	return (backtrack, max_score, max_i, max_j) #Requires a max index from both strings


def output_LCS (backtrack, dna1, dna2, i, j):
	global str1
	global str2

	print ("<",i,j,"> : ", backtrack[i][j])

	if i == 0 or j == 0:
		return 

	if backtrack[i][j] == 1:
		output_LCS(backtrack, dna1, dna2, i, j-1)
		str1 += "-"
		str2 += dna2[j - 1]
	elif backtrack[i][j] == -1:
		output_LCS (backtrack, dna1, dna2, i-1, j)
		str1 += dna1[i - 1]
		str2 += "-"
	else:
		output_LCS(backtrack, dna1, dna2, i-1, j-1)
		str1 += dna1[i-1]
		str2 += dna2[j-1]
		

def make_blosum():
	blosum_table = []
	g = open("pam.txt")
	g.readline()
	line = g.readline().split()
	while line:
		line = [int(line[x]) for x in range(1, len(line))]
		blosum_table.append(line)
		line = g.readline().split()
	return blosum_table


def score(str1, str2, blosum):
	score = 0
	for i in range(0, len(str1)):
		if str1[i] == "-" or str2[i] == "-":
			score -= 5
		else:
			score += blosum[ acids[str1[i]]][acids[str2[i]]]
	return score

g = open("overlap.txt")	
dna1 = g.readline().strip('\n')
dna2 = g.readline().strip('\n')
#dna1 = "TAGGCTTA"
#dna2 = "TAGATA"
#dna1 = "AAAAAAAAAAAATTATAA"
#dna2 = "TTT"
#dna1 = "AAATTTAAA"
#dna2 = "TATA"
#dna1 = "PAWHEAE"
#dna2 = "HEAGAWGHEE"
#blosum_table = make_blosum()
#print_matrix(blosum_table)
backtrack, score,i, j = construct_backtrack(dna1, dna2, 2)
print(i)
print(j)
print_matrix(backtrack)
output_LCS(backtrack, dna1, dna2, i, j)
print(score)
print(str1)
print(str2)
