def bfs(V,adj,s):
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

V = ['a','b','c','d']
adj = {'a':['c','b'],'b':['c','d'],'c':['a','b','d'],'d':['b','c']}
# adj = {'a':['b'],'b':['c'],'c':['d'],'d':[]}
s = 'c'

print bfs(V,adj,s)
