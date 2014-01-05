#WORKS

def prints(s):
	for row in s:
		print(row)

def manhattan(n, m, down, right): 
	s = [ [0 for i in range(0, m+1)] for j in range(0, n+1)]
	for i in range(1, n+1):
		print("i is ", i)
		s[i][0] = s[i-1][0] + down[i][0]
	for j in range(1, m+1):
		s[0][j] = s[0][j-1] + right[0][j]
	for i in range(1, n + 1):
		print("i is ", i)
		for j in range(1, m + 1):
			s[i][j] = max(s[i-1][j] + down[i][j], s[i][j-1] + right[i][j])
	return (s[n][m])

g = open("tourist.txt")
n = int(g.readline())
m = int(g.readline())
down = [ [0 for x in range(0, m+1)] ]
right = []
for i in range(0, n):
	lst = [int(x) for x in (g.readline()).split()]
	down.append(lst)

g.readline()

for i in range(0, n+1):
	lst = [0] + [int(x) for x in (g.readline()).split()] 
	right.append(lst)
prints(down)
print()

prints(right)
print (manhattan(n, m, down,right))
