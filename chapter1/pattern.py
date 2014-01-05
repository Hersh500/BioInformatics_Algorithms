#WORKS

def find_pattern(String, p):
	x = 0; 
	line = ""

	while (x != -1): 
		x = String.find(p, x+1) 
		line = line + str(x) + " "

	print(line)

g = open ("dataset_3_5.txt")
p = g.readline().strip('\n') 
String = g.readline().strip('\n') 
find_pattern(String, p); 	
