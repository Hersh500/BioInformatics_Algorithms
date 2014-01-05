#WORKS
def splt(lst):
	splt = []
	for i in range(0, len(lst)):
		if (i+1)%3 == 0:
			splt.append(lst[0:3])
			lst = lst[3:]
	return (splt)	

g = open("table.txt", 'r') #Uses a given translation table
f = g.readlines() 
for i in range(0, len(f)):
	f[i] = f[i].split() 

def translate(s):
	s = splt(s)
	pro = []
	for i in range(0, len(s)):
		for j in range(0, len(f)):
			if s[i] in f[j]:
				if f[j][0] != 'Stop':
					pro.append(f[j][0]) 
	return (pro)

g = open("PROT.txt") #Dataset
s = g.readline().strip('\n')
c = ''.join(translate(s))
print (c)
