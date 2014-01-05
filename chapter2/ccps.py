#WORKS

import GTSP_LIB as sp #uses a modified version of gtsp.py 

table = sp.get_table()

def parse_input(spectrum):
	spectrum = spectrum.split()
	spectrum = [ int(x) for x in spectrum]
	return (spectrum)

def get_acids (spectrum, table):
	acids = []
	for mass in spectrum:
		if (mass > 0 and mass <= 186): 
			for acid in table:
				if table[acid] == mass:
					acids.append(acid)
					break
		elif (mass > 186):
			return (acids)

	return (acids)


def expand_list (acids, mega_lst, spectrum):
	new_lst = []

	for peptide in mega_lst:
		for acid in acids:
			expanded = peptide + acid	
			if spectra_equal(expanded, spectrum) and expanded not in new_lst:
				new_lst.append(expanded)
	return (new_lst) 
			
def spectra_equal(peptide, spectrum):

	sub_spectrum = sp.spectrum(peptide, False)
	for mass in sub_spectrum:
		if mass not in spectrum:
			return (False)
	return (True) 

def final_check(peptides, spectrum):
	for peptide in peptides:
		if (sp.spectrum(peptide, False) != spectrum):
			peptides.remove(peptide)

	return (peptides)	

def cyclosequence(acids, spectrum):
	mega_lst = acids	
	length = 1
	while length < len(acids):
		mega_lst = expand_list(acids, mega_lst, spectrum)
		length += 1

	return (mega_lst)
			 
def peptide_weights(peptide):
	string = ""
	for acid in peptide:
		if (string):
			string += "-"
		string += str(table[acid])

	return(string)
		
def format_output(mega_lst, table):
	output = []
	for peptide in mega_lst:
		string = ""
		for acid in peptide:
			if (string):
				string += "-"	
			string += str(table[acid])   
		output.append(string + " ")
	
	print(''.join(output))

def run(spectrum):
	table = sp.get_table()
	spectrum = parse_input(spectrum)
	acids = get_acids(spectrum, table)
	mega_lst = cyclosequence(acids, spectrum)
	format_output(mega_lst, table)

g = open("dataset_ccps.txt")
spectrum = g.read()
run(spectrum)	
	
		
		
		
		
