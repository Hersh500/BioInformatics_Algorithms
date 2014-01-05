#WORKS

def splt(protein):
    lst = []
    for letter in protein:
        lst.append(letter)
    return lst

def get_combos(protein):
    mega_list = [protein]
    protein = splt(protein)
    for a in range(0, len(protein)):
        base = protein[a]
        sub_list = []
        index = a
        while len(base) < len(protein): #generates all cyclic combinations of the protein
            sub_list.append(base)
            print(base)
            print( index )
            index = (index+1) % len(protein)
            base += protein[index]

        mega_list += sub_list

    return (mega_list)

def get_table():
	g = open("integer_mass_table.txt")
	table = {}
	f = g.readlines()
	for element in f:
		x = element.split()
		table[x[0]] = int(x[1])
	return (table)

def calc_mass (protein, table):
	weight = 0
	for acid in protein:
		weight += table[acid]
	return weight

def find_weights (subprots, table):
	weights = [0] 
	for pro in subprots:
		weights.append(calc_mass (pro,table)) 
	return (sorted(weights))	

protein = "CTLWHRNIPNCR"
table = get_table()
prots = get_combos(protein)
print(prots)
weights = find_weights(prots, table)
string = ""
for weight in weights:
	string += str(weight) + " "
print(string) 
