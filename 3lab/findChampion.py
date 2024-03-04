class Vertex:
	def __init__(self, navn):
		self.navn = navn
		self.colour = "white"
		self.Discovered = 0
		self.Finished = 0

class Graph:
	def __init__(self, vertices, edges):
		self.vertices  = [Vertex(i) for i in vertices]
		self.edges = self.initEdges(edges)

	def initEdges(self, edges):
		result = {}
		for vertex in self.vertices:
			result[vertex] = []
		for edge in edges: 
			for vertex in self.vertices:
				if vertex.navn == edge[0]:
					fra = vertex
					break
			for vertex in self.vertices:
				if vertex.navn == edge[1]:
					result[fra].append(vertex)
					break
		return result

	def DFS(self):
		for vertex in self.vertices:
			vertex.colour = "white"
		self.time = 0
		forest = []
		for vertex in self.vertices:
			if vertex.colour == "white":
				tree = self.DFSVisit(vertex, [])
				forest.append(tree)
		return forest


	def DFSVisit(self, vertex, tree):
		self.time += 1
		vertex.Discovered = self.time
		vertex.colour = "gray"
		for dst in self.edges[vertex]:
			if dst.colour == "white":
				tree = self.DFSVisit(dst, tree)
		vertex.colour = "black"
		self.time += 1
		vertex.Finished = self.time

		tree.append(vertex)
		return tree

	def stronglyConnectedComponents(self):
		self.DFS()
		self.vertices.sort(key=lambda vertex: vertex.Finished, reverse=True)
		self.transpose_edges()
		scc = self.DFS()
		return scc

	def transpose_edges(self):
		new_edges = {}
		for vertex in self.vertices:
			new_edges[vertex] = []
		for fra in self.edges.keys():
			for til in self.edges[fra]:
				new_edges[til].append(fra)
		self.edges = new_edges


if __name__ == "__main__":
	vertices = [chr(i) for i in range(ord('A'), ord('G')+1)]
	edges = [("A", "B"), ("A", "D"),
		  ("B", "A"), ("B", "C"),
		  ("C", "E"), ("C", "F"),
		  ("D", "B"), ("D", "C"),
		  ("E", "G"),
		  ("F", "E"),
		  ("G", "F")]
	graph = Graph(vertices, edges)
	scc = graph.stronglyConnectedComponents()
	for tree in scc:
		for vertex in tree:
			print(vertex.navn, end="")
		print("\n#######################")