#WORKS

import sys
gpath = []

def print_path(path):
	print (path[0], end = "")
	for i in range(1, len(path)):
		print("->"+str(path[i]), end = "")
	print()
		
def get_graph():
	graph = {}
	g = open("dag.txt")
	source = int(g.readline())
	sink = int(g.readline())
	line = g.readline()	
	while line:
		x = line.split("->")
		node = int( x[0] )
		y = x[1].split(":")
		if node in graph:
			graph[node].append( (int(y[0]), int(y[1])))
		else:
			graph[ int(x[0]) ] = [ (int(y[0]), int(y[1])) ]		
		line = g.readline()
	return source, sink, graph	

def adj_list(node, graph):
	lst = []
	try: 
		for n in graph[node]:
			lst.append(n[0])
		return lst
	except KeyError:
		return lst

def weight(src, dst, graph):
	try:
		for n in graph[src]:
			if n[0] == dst:
				return n[1]
		return -1
	except KeyError:
		return -1 
	return -1

def save_path(path):
	global gpath
	gpath = list(path)

def find_path (node, sink, path, graph):
	curmax = 0

	path.append(node)

	if node == sink:
		return 0

	dlist = adj_list(node, graph)

	for n in dlist:
		length = find_path (n, sink, path, graph) + weight (node, n, graph)	
		if length > curmax:
			curmax = length
			if path[len(path) -1] == sink:
				save_path(path);
		path.pop() 
	return curmax 

source, sink, graph = get_graph()
print(source)
print(sink)
print(graph)
curmax = find_path (source, sink, [], graph) 
print(curmax)
print_path(gpath)
