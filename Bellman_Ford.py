import time

class Graph:
	def __init__(self, vertices):
		self.V = vertices 
		self.graph = []

	def addEdge(self, u, v, wb, wt, ttv): 
		self.graph.append([u, v, wb, wt, ttv])
		

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print(i, "{:.2f}".format((dist[i])))
	

	def BellmanFord(self, src, initialB, initialT):

            bus = [float("Inf")] * self.V
            bus[src] = initialB
            train = [float("Inf")] * self.V
            train[src] = initialT
            dist = [float("Inf")] * self.V
            dist[src] = 0
    
            for _ in range(self.V - 1):
                for u, v, wb, wt, ttv in self.graph:
                    if bus[u] != float("Inf") and bus[u] + wb < bus[v]:
                            bus[v] = bus[u] + wb
                    if train[u] != float("Inf") and train[u] + wt + ttv < bus[v]:
                            bus[v] = train[u] + wt + ttv 
 
                    if train[u] != float("Inf") and train[u] + wt < train[v]:
                            train[v] = train[u] + wt
                    if bus[u] != float("Inf") and bus[u] + wb + ttv < train[v]:
                            train[v] = bus[u] + wb + ttv 
                    
                    if dist[v]>bus[v]:
                        dist[v]=bus[v]
                    if dist[v]> train[v]:
                        dist[v]=train[v]

            for u, v, wb, wt, ttv in self.graph:
                if (bus[u] != float("Inf") and bus[u] + wb < bus[v]) or (train[u] != float("Inf") and train[u] + wt + ttv < bus[v]) or (train[u] != float("Inf") and train[u] + wt < train[v]) or (bus[u] != float("Inf") and bus[u] + wb + ttv < train[v]):
                    print("Graph contains negative weight cycle")
                    return
                    
            self.printArr(dist)


"""
g= Graph(3)
g.addEdge(0, 1, 100, float("Inf"), float("Inf"))
g.addEdge(0, 2, float("Inf"), 180, 10)
g.addEdge(1, 2, 120, float("Inf"), 10)

start=time.time()
g.BellmanFord(0,0,30) 
"""

"""
g=Graph(2)
g.addEdge(0, 1, 4, 2, 2)
g.addEdge(1, 0, 4, 2, 1)

start=time.time()
g.BellmanFord(0,0,1)
end=time.time()
"""

"""
g= Graph(3)
g.addEdge(0, 1, 7, 8, 1)
g.addEdge(0, 2, float("Inf"), 2,  3)
g.addEdge(1, 2, 3, 2, 3)


g.addEdge(1, 0, 7, 8, 2)
g.addEdge(2, 0, float("Inf"), 2, 2)
g.addEdge(2, 1, 3, 2, 1)

start=time.time()
g.BellmanFord(0,0,2) 
end=time.time()
"""

"""
g= Graph(4)

g.addEdge(0, 1, 8, 6, 0.16)
g.addEdge(0, 2, 10, float("Inf"), 0.24)
g.addEdge(1, 2, 4, 1, 0.24)
g.addEdge(1, 3, float("Inf"), 5, float("Inf"))
g.addEdge(2, 3, float("Inf"), 3, float("Inf"))


g.addEdge(1, 0, 8, 6, 0.5)
g.addEdge(2, 0, 10, float("Inf"), 0.5)
g.addEdge(2, 1, 4, 1, 0.16)
g.addEdge(3, 1, float("Inf"), 5, 0.16)
g.addEdge(3, 2, float("Inf"), 3, 0.24)

start=time.time()
g.BellmanFord(0, 0, 0.5) 
end=time.time()
"""

"""
g= Graph(5)
g.addEdge(0, 1, 4, 3, 1.05)
g.addEdge(1, 2, 2, 3, 5)
g.addEdge(2, 3, 5, 11, 1)
g.addEdge(3, 4, 12, 1.1, 2)
g.addEdge(0, 4, 8, 7, 2)

g.addEdge(1, 0, 4, 3, 2.06)
g.addEdge(2, 1, 2, 3, 1.05)
g.addEdge(3, 2, 5, 11, 5)
g.addEdge(4, 3, 12, 1.1, 1)
g.addEdge(4, 0, 8, 7, 2.06)

g.addEdge(0, 2, 6, 10, 5)
g.addEdge(0, 3, 20, 13, 1)
g.addEdge(1, 3, 13, 7, 1)
g.addEdge(1, 4, 1, 1.5, 2)
g.addEdge(2, 4, 4, 8, 2)

g.addEdge(2, 0, 6, 10, 2.06)
g.addEdge(3, 0, 20, 13, 2.06)
g.addEdge(3, 1, 13, 7, 1.05)
g.addEdge(4, 1, 1, 1.5, 1.05)
g.addEdge(4, 2, 4, 8, 5)

start=time.time()
g.BellmanFord(0,0,2.06) 
end=time.time()

"""
"""
g= Graph(6)

g.addEdge(0, 1, 4 , float("Inf"), 0.25)
g.addEdge(0, 2, 3 , 2 , 0.5)
g.addEdge(0, 3, 6 , float("Inf") , float("Inf"))
g.addEdge(0, 4, float("Inf"), 3, 1.06)
g.addEdge(1, 2, float("Inf"), 1, 0.5)
g.addEdge(1, 5, float("Inf"), 6, 3.04)
g.addEdge(2, 3, 4, float("Inf"), float("Inf"))
g.addEdge(3, 4, 2, float("Inf"), 1.06)
g.addEdge(3, 5, 4, float("Inf"), 3.04)
g.addEdge(4, 5, 3, 3, 3.04)


g.addEdge(1, 0, 4 , float("Inf"), 0.1)
g.addEdge(2, 0, 3 , 2 , 0.1)
g.addEdge(3, 0, 6 , float("Inf") , 0.1)
g.addEdge(4, 0, float("Inf"), 3, 0.1)
g.addEdge(2, 1, float("Inf"), 1, 0.25)
g.addEdge(5, 1, float("Inf"), 6, 0.25)
g.addEdge(3, 2, 4, float("Inf"), 0.5)
g.addEdge(4, 3, 2, float("Inf"), float("Inf"))
g.addEdge(5, 3, 4, float("Inf"), float("Inf"))
g.addEdge(5, 4, 3, 3, 1.06)

start=time.time()
g.BellmanFord(0,0.1,0) 
"""

g=Graph(7)

g.addEdge(0, 1, 3, 2, 0.25)
g.addEdge(1, 2, 4, 6, 2)
g.addEdge(2, 3, 8, 3, 1)
g.addEdge(3, 4, float("Inf"), 5, 0.5)
g.addEdge(4, 5, float("Inf"), 1, 0.06)
g.addEdge(5, 6, 6, float("Inf"), float("Inf"))
g.addEdge(0, 3, float("Inf"), 20, 1)
g.addEdge(1, 6, 4, float("Inf"), float("Inf"))
g.addEdge(1, 5, float("Inf"), 8, 0.06)
g.addEdge(2, 4, 4, 3, 0.5)
g.addEdge(2, 5, 6, 2, 0.06)
g.addEdge(3, 6, 15, float("Inf"), float("Inf"))
g.addEdge(0, 5, 9, float("Inf"), 0.06)


g.addEdge(1, 0, 3, 2, 0.3)
g.addEdge(2, 1, 4, 6, 0.25)
g.addEdge(3, 2, 8, 3, 2)
g.addEdge(4, 3, float("Inf"), 5, 1)
g.addEdge(5, 4, float("Inf"), 1, 0.5)
g.addEdge(6, 5, 6, float("Inf"), 0.06)

g.addEdge(3, 0, float("Inf"), 20, 0.3)
g.addEdge(6, 1, 4, float("Inf"), 0.25)
g.addEdge(5, 1, float("Inf"), 8, 0.25)
g.addEdge(4, 2, 4, 3, 2)
g.addEdge(5, 2, 6, 2, 2)
g.addEdge(6, 3, 15, float("Inf"), 1)
g.addEdge(5, 0, 9, float("Inf"), 0.3)

start=time.time()
g.BellmanFord(2,0,2)
end=time.time()

print(end-start)
