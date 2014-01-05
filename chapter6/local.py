#WORKS

import sys
sys.setrecursionlimit(100000)

str1 = "" 
str2 = "" 

def print_matrix(matrix):
	for row in matrix:
		print(row)
	print()

acids = {"A": 0, "C": 1, "D":2, "E":3, "F":4, "G":5, "H":6, "I":7, "K":8, "L":9, "M":10, "N":11, "P": 12, "Q": 13, "R": 14, "S":15, "T":16, "V":17, "W":18, "Y":19}

def construct_backtrack(dna1, dna2, indel_penalty, blosum):
	maximum_value = 0
	max_i = 0
	max_j = 0
	s = [ [0 for i in range(0, len(dna2) + 1)] for j in range(0, len(dna1) + 1)]
	backtrack = [ [0 for i in range(0, len(dna2) + 1)] for j in range(0, len(dna1) + 1)]

	for i in range(0, len(dna1) + 1):
		s[i][0] = 0 
	for j in range(0, len(dna2) + 1):
		s[0][j] = 0 

	for i in range(1, len(dna1) + 1):
		for j in range(1, len(dna2) + 1):
			x = acids [ dna1[i - 1] ] 
			y = acids [ dna2[j - 1] ]
			s[i][j] = max (0, s[i-1][j] - indel_penalty, s[i][j-1] - indel_penalty, s[i-1][j-1] + blosum[x][y])
			if s[i][j] > maximum_value: 
				maximum_value = s[i][j]
				max_i = i
				max_j = j
			if s[i][j] == s[i-1][j] - indel_penalty:
				backtrack[i][j] = -1 #Vertical
			elif s[i][j] == s[i][j-1] - indel_penalty:
				backtrack[i][j] = 1   #Horizontal
			elif s[i][j] == s[i-1][j-1] + blosum[ acids[dna1[i - 1]]][acids[dna2[j - 1]]]:
				backtrack[i][j] = 2  #Diagonal
				

	print_matrix (s)
	return (backtrack, s[max_i][max_j], max_i, max_j)


def output_LCS (backtrack, dna1, dna2, i, j):
	global str1
	global str2

	print ("<",i,j,"> : ", backtrack[i][j])

	if i == 0 or j == 0:
		return 

	if backtrack[i][j] == -1:
		output_LCS (backtrack, dna1, dna2, i-1, j)
		str1 += dna1[i - 1]
		str2 += "-"
	elif backtrack[i][j] == 1:
		output_LCS(backtrack, dna1, dna2, i, j-1)
		str1 += "-"
		str2 += dna2[j - 1]
	elif backtrack[i][j] == 2:
		output_LCS(backtrack, dna1, dna2, i-1, j-1)
		str1 += dna1[i-1]
		str2 += dna2[j-1]
	else:
		output_LCS(backtrack, dna1, dna2, i-1, j-1)
		

def make_blosum():
	blosum_table = []
	g = open("pam.txt") #Uses the PAM250 scoring matrix
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

g = open("local.txt")	
#dna1 = "MEANLY" 
#dna2 = "PENALTY"
dna1 = g.readline().strip('\n')
dna2 = g.readline().strip('\n')
#dna1 = "ATGVWYYYYC"
#dna2 = "GYYCFFF"
#dna1 = "QTVHQIWMKRLASFFFSMMMRRLLQQSSSTTTFQQDWLLLLLSSSCCSPQPQPQTYTYTYTFFRRRSSMMMLNNNDNDKVWSKLLWPPPPQRMS"
#dna2 = "TQDFFSMLRRAAQFFMMRLCCDPPPATATATFPFPMMMDSNSSSDNSQRRQRQRQTFTDTSTCCQVVMNFRMNFRVDFPLLK"
dna1 = "ACDY"
dna2 = "CDY"
blosum_table = make_blosum() #Variable name is blosum, but it's actually the PAM matrix
print_matrix(blosum_table)
backtrack, score, i, j = construct_backtrack(dna1, dna2, 5, blosum_table)
print_matrix(backtrack)
output_LCS(backtrack, dna1, dna2,  i, j)
print(score)
print(str1)
print(str2)
