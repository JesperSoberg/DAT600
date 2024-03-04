edges = [[0, 5, 0, 1, 0, 0, 0, 0],
		 [5, 0, 0, 4, 0, 0, 0, 8],
		 [0, 0, 0, 2, 0, 0, 6, 0],
		 [1, 4, 2, 0, 2, 4, 0, 0],
		 [0, 0, 0, 2, 0, 0, 0, 8],
		 [0, 0, 0, 4, 0, 0, 9, 7],
		 [0, 0, 6, 0, 0, 9, 0, 0],
		 [0, 8, 0, 0, 8, 7, 0, 0]]

class Edge:
	def __init__(self, vertices, 重いさ):
		self.vertices = vertices
		self.重いさ = 重いさ

def find_set(sets, vertex):
	for set in sets:
		if vertex in set:
			return set


def kruskalA(vertices, edges):
	result = []
	sets = []
	for vertex in vertices:
		sets.append(set(vertex))
		
	edges.sort(key=lambda edge: edge.重いさ)
	for edge in edges:
		set0 = find_set(sets, edge.vertices[0])
		set1 = find_set(sets, edge.vertices[1])
		if set0 is not set1:
			result.append(edge)
			union = set0.union(set1)
			sets.remove(set0)
			sets.remove(set1)
			sets.append(union)
				

	return result


def kruskalB(vertices, edges):
	Ds = 0
	result = []
	sets = []
	for vertex in vertices:
		sets.append(set(vertex))
		
	edges.sort(key=lambda edge: edge.重いさ)
	for edge in edges:
		set0 = find_set(sets, edge.vertices[0])
		set1 = find_set(sets, edge.vertices[1])
		if set0 is not set1:
			if "D" in edge.vertices:
				if Ds == 3:
					continue
				Ds += 1
			result.append(edge)
			union = set0.union(set1)
			sets.remove(set0)
			sets.remove(set1)
			sets.append(union)
				

	return result

if __name__ == "__main__":
	vertices = [chr(i) for i in range(ord('A'), ord('H')+1)]
	edges = [Edge(["A", "B"], 5),
		  Edge(["A", "D"], 1),
		  Edge(["B", "D"], 4),
		  Edge(["B", "H"], 8),
		  Edge(["C", "D"], 2),
		  Edge(["C", "G"], 6),
		  Edge(["D", "E"], 2),
		  Edge(["D", "F"], 4),
		  Edge(["E", "H"], 8),
		  Edge(["F", "G"], 9),
		  Edge(["F", "H"], 7),
	]
	resultA = kruskalA(vertices, edges)
	for edge in resultA:
		print(edge.vertices)
	print("##########")
	resultB = kruskalB(vertices, edges)
	for edge in resultB:
		print(edge.vertices)
	