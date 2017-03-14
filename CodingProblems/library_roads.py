n cities 1 to n
Cities are connected by m roads these 2-way (undirected graph)

The cost of repairing any road is costToMakeRoads dollars, and the cost to build a library in any city is costToMakeLibrary dollars.

You are given q queries, where each query consists of a map of HackerLand and value of costToMakeLibrary and costToMakeRoads.

PROBLEM: - For each query, find the minimum cost of making libraries accessible to all the citizens and print it on a new line.

q = 2
n = 3 m = 3 costToMakeLibrary = 2 costToMakeRoads = 1
(0, 1)

2
3 3 2 1
1 2
3 1
2 3

# End of first for looop
1: []
2: []
3: []
4: []
5: []
6: []
7: []
8: []

# End of second for looop
1: [7,3,2]
2: [1,3]
3: [1,2]
4: []
5: [6]
6: [5,8]
7: [1]
8: [6]




# 1 Solution: build all roads and 1 library
# 2 Solution: build libaries in every city

class LibariesAndRoads:
    def __init__(self, cities, libaries, cost_of_city, cost_of_library, graph):
        self.cities = cities
        self.libraries = libraries
        self.cost_of_road = cost_of_road
        self.cost_of_library = cost_of_library
        self.graph = graph
        self.num_of_verts = num_of_verts   
        self.subgraphs = self.find_subgraphs()    
        
    def min_cost_of(self, graph):
    # 1 Solution: build all roads and 1 library
       verts = #....
       soln1 = self.cost_of_road*verts + self.cost_of_library
        
    # 2 Solution: build libaries in every city
      cities = len(graph)
      soln2 = cities * self.cost_of_city
      
      return min(soln1, soln2)
      
    def find_subgraph(self):
        visited_already = set()
        subgraphs = []
        for node, verts in self.graph.item():
            if node not in visited_already:
                visited = set()
                sub = self.r_find_subgraph(visited, node)
                subgraph.append(sub)
                visited_already.add(visited)
        return subgraph

    def r_find_subgraph(self, visited, node):
        if node not in visited:
            verts = self.graph[node]
            visited.add(node)
            for v in verts:
                return r_find_subgraph(visited, node)
        return visited
        
    
    def calculate_min_cost(self):
        cost = 0
        for graph in self.subgraph:
             cost += min_cost_of(graph)  
        return cost
    
    
    
    
    
    

