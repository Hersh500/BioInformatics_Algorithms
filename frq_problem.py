#WORKS

def count(str, k): 
	most_frq = {};	
	max_count = 0; 
	for i in range(0, len(str) - k):
		count = 0; 
		for j in range(0, len(str) - k):	
			if str[j:j+k] == str[i:i+k]:
				count = count + 1; 

		if count >= max_count:
			print (count)
			if (count in most_frq):
				if str[i:i+k] not in most_frq[count]:
					most_frq[count].append(str[i:i+k])
			else:
				most_frq[count] = [str[i:i+k]]
			max_count = count
	return (most_frq)

def get_data():
	g = input("enter the string") 
	r = int(input("enter k")) 
	return (g,r)

string, k = get_data() 
most_frq = count(string, k)
max = 0; 
for count in most_frq: 
	if count > max: 
		max = count
for i in most_frq[max]: 
	print (i)
