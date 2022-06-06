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
			print(chr(i+ord("A")), "{:.2f}".format((dist[i])))
	

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
g.BellmanFord(0,0,2)
end=time.time()

#print(end-start)
"""



#INSTANCE 1

"""
all_cities = ['A','B','C','D','E','F','G']

cities_with_bus = ['A','B','C','D','F','G']

cities_with_train = ['A','B','E','F','G']

Time_btw_train_bus = [('A',5),('B',10),('F',10),('G',5)]

Time_btw_cities_by_bus = [('A','B',20),('B','C',20),('B','F',40),('C','D',15),('D','G',10),('F','G',10)]

Time_btw_cities_by_train = [('A','B',10),('A','E',20),('B','E',5),('E','F',10),('F','G',30)]

"""
"""
g=Graph(7)
g.addEdge(0, 1, 20, 10, 10)
g.addEdge(1, 2, 20, float("Inf"), float("Inf"))
g.addEdge(1, 5, 40, float("Inf"), 10)
g.addEdge(2, 3, 15, float("Inf"), float("Inf"))
g.addEdge(3, 6, 10, float("Inf"), 5)
g.addEdge(5, 6, 10, 30, 5)

g.addEdge(0, 4, float("Inf"), 20, float("Inf"))
g.addEdge(1, 4, float("Inf"), 5, float("Inf"))
g.addEdge(4, 5, float("Inf"), 10, 10)


g.addEdge(1, 0, 20, 10, 5)
g.addEdge(2, 1, 20, float("Inf"), 10)
g.addEdge(5, 1, 40, float("Inf"), 10)
g.addEdge(3, 2, 15, float("Inf"), float("Inf"))
g.addEdge(6, 3, 10, float("Inf"), float("Inf"))
g.addEdge(6, 5, 10, 30, 10)

g.addEdge(4, 0, float("Inf"), 20, 5)
g.addEdge(4, 1, float("Inf"), 5, 10)
g.addEdge(5, 4, float("Inf"), 10, float("Inf"))

g.BellmanFord(2, 0, float("Inf"))

"""

#INSTANCE 2

"""
all_cities = ['A','B','C','D','E','F']

cities_with_bus = ['A','B','C','E','F']

cities_with_train = ['A','B','C','D','F']

Time_btw_train_bus = [('A',5),('B',5),('C',25),('F',10)]

Time_btw_cities_by_bus = [('A','B',40),('B','C',5),('C','E',5),('E','F',5)]

Time_btw_cities_by_train = [('A','C',10),('C','D',5),('B','D',5),('D','F',40)]

"""
"""
g=Graph(6)
g.addEdge(0, 1, 40, float("Inf"), 5)
g.addEdge(1, 2, 5, float('Inf'), 25)
g.addEdge(2, 4, 5, float("Inf"), float("Inf"))
g.addEdge(4, 5, 5, float("Inf"), 10)

g.addEdge(0, 2, float("Inf"), 10, 25)
g.addEdge(2, 3, float("Inf"), 5, float("Inf"))
g.addEdge(1, 3, float("Inf"), 5, float("Inf"))
g.addEdge(3, 5, float("Inf"), 40, 10)

g.addEdge(1, 0, 40, float("Inf"), 5)
g.addEdge(2, 1, 5, float('Inf'), 5)
g.addEdge(4, 2, 5, float("Inf"), 25)
g.addEdge(5, 4, 5, float("Inf"), float("Inf"))

g.addEdge(2, 0, float("Inf"), 10, 5)
g.addEdge(3, 2, float("Inf"), 5, 25)
g.addEdge(3, 1, float("Inf"), 5, 5)
g.addEdge(5, 3, float("Inf"), 40, float("Inf"))

g.BellmanFord(2,0,25)

"""


#INSTANCE 3

"""
all_cities = ['A', 'B', 'C', 'D', 'E']

cities_with_bus = ['A', 'B', 'C', 'D']

cities_with_train = ['A', 'C', 'E']

Time_btw_train_bus = [('A',5), ('C',10)]

Time_btw_cities_by_bus = [('A','B',30), ('A','C',30), ('B','C',20), ('B','D',22), ('C','D',20)]

Time_btw_cities_by_train = [('A','C',20), ('A','E',75), ('C','E',40)]

"""
"""
g = Graph(5)

g.addEdge(0, 1, 30, float("Inf"), float("Inf"))
g.addEdge(0, 2, 30, 20, 10)
g.addEdge(1, 2, 20, float("Inf"), 10)
g.addEdge(1, 3, 22, float("Inf"), float("Inf"))
g.addEdge(2, 3, 20, float("Inf"), float("Inf"))

g.addEdge(0, 4, float("Inf"), 75, float("Inf"))
g.addEdge(2, 4, float("Inf"), 40, float("Inf"))


g.addEdge(1, 0, 30, float("Inf"), 5)
g.addEdge(2, 0, 30, 20, 5)
g.addEdge(2, 1, 20, float("Inf"), float("Inf"))
g.addEdge(3, 1, 22, float("Inf"), float("Inf"))
g.addEdge(3, 2, 20, float("Inf"), 10)

g.addEdge(4, 0, float("Inf"), 75, 5)
g.addEdge(4, 2, float("Inf"), 40, 10)

g.BellmanFord(0, 0, 5)

"""

#INSTANCE 4

"""
all_cities = ['A', 'B', 'C', 'D', 'E', 'F']

cities_with_bus = ['A', 'B', 'C', 'D', 'E']

cities_with_train = ['B', 'D', 'E', 'F']

Time_btw_train_bus = [('B',4), ('D',7), ('E',8)]

Time_btw_cities_by_bus = [('A','D',27), ('A','C',23), ('C','E',17), ('B','D',13), ('B','C',18), ('D','E',20)]

Time_btw_cities_by_train = [('D','E',12), ('D','F',22), ('E','F',17), ('B','F',11)]
"""
"""

g= Graph(6)

g.addEdge(0, 3, 27, float("Inf"), 7)
g.addEdge(0, 2, 23, float("Inf"), float("Inf"))
g.addEdge(2, 4, 17, float("Inf"), 8)
g.addEdge(1, 3, 13, float("Inf"), 7)
g.addEdge(1, 2, 18, float("Inf"), float("Inf"))
g.addEdge(3, 4, 20, 12, 8)

g.addEdge(3, 5, float("Inf"), 22, float("Inf"))
g.addEdge(4, 5, float("Inf"), 17, float("Inf"))
g.addEdge(1, 5, float("Inf"), 11, float("Inf"))


g.addEdge(3, 0, 27, float("Inf"), float("Inf"))
g.addEdge(2, 0, 23, float("Inf"), float("Inf"))
g.addEdge(4, 2, 17, float("Inf"), float("Inf"))
g.addEdge(3, 1, 13, float("Inf"), 4)
g.addEdge(2, 1, 18, float("Inf"), 4)
g.addEdge(4, 3, 20, 12, 7)

g.addEdge(5, 3, float("Inf"), 22, 7)
g.addEdge(5, 4, float("Inf"), 17, 8)
g.addEdge(5, 1, float("Inf"), 11, 4)

g.BellmanFord(1, 0, 4)

"""