# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(T):
    V,adj,s = create_variable(T)
    distance_dictionary = general_BFS(V,adj,s)
    final_list = [0]*(len(T) - 1)
    for city,distance in distance_dictionary.iteritems():
        if city != s:
            final_list[distance-1] += 1
    return final_list

# create a V,adj and s so I can use a more generalized familiar version of BFS
# that I have made 1000 times
def create_variable(T):
	V = range(len(T))
	adj = {}
	s = 0
	for vertex in V:
		adj[vertex] = []

	for P in range(len(T)):
		Q = T[P]
		if Q == P:
			s = Q
		adj[P].append(Q)
		adj[Q].append(P)
	
	return (V,adj,s)
	
def general_BFS(V,adj,s):
	level = {}
	level[s] = 0
	parent = {}

	for v in V:
		parent[v] = None
		if v != s:
			level[v] = float('inf')	

	search_queue = [s]

	while search_queue:
		current_vertex = search_queue.pop(0)
		for v in adj[current_vertex]:
			if level[v] == float('inf'):
				level[v] = level[current_vertex] + 1
				search_queue.append(v)
				parent[v] = current_vertex
			else:
				pass

	return level