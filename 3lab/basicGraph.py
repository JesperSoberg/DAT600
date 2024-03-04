from collections import deque as deck

class Vertex:
	def __init__(self, navn):
		self.navn = navn
		self.colour = "white"

class Graph:
	def __init__(self, vertices, edges):
		self.vertices  = [Vertex(i) for i in vertices]
		self.edges = self.initEdges(edges)

	def initEdges(self, edges):
		result = {}
		for vertex in self.vertices:
			result[vertex.navn] = []
		for edge in edges: 
			fra = edge[0]
			for vertex in self.vertices:
				if vertex.navn == edge[1]:
					result[fra].append(vertex)
					break
		return result
	
	def removeCycles(self):
		queue = deck()
		self.vertices[0].colour = "gray"
		queue.append(self.vertices[0])
		while len(queue) != 0:
			curVertex = queue.popleft()
			i = 0
			while i < len(self.edges[curVertex.navn]):
				vertex = self.edges[curVertex.navn][i]
				if vertex.colour == "white":
					vertex.colour = "gray"
					queue.append(vertex)
				elif vertex.colour == "black":
					self.edges[curVertex.navn].remove(vertex)
					continue
				i += 1
			curVertex.colour = "black"

if __name__ == "__main__":
	vertices = [chr(i) for i in range(ord('A'), ord('J')+1)]
	edges = [("A", "B"), 
		    ("B", "C"), ("B", "D"), 
			("C", "A"), ("C", "E"), ("C", "F"), 
			("D", "E"), ("D", "F"),
			("E", "F"), ("E", "G"),  ("E", "J"),
			("F", "B"), ("F", "G"), ("F", "H"), ("F", "J"),
			("H", "I"), 
			("I", "C"), 
			("J", "I"),
	]
	graph = Graph(vertices, edges)
	graph.removeCycles()
	for key, edges in graph.edges.items():
		print(f"Key: {key}: Edges: {[i.navn for i in edges]}")
