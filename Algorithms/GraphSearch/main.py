class Graph:
    def __init__(self):
        self.graph = {
                'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': [],
                'E': ['F'],
                'F': ['C']
                }
        self.frontiere = []
        self.explored = []
    

    def BFS(self, start, end):
        explored = []
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if neighbour == end:
                        return new_path
                explored.append(node)
        return None

    def DFS(self,start, end):
        explored = []
        stack = [[start]]
        while stack:
            path = stack.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    stack.append(new_path)
                    if neighbour == end:
                        return new_path
                explored.append(node)
        return None

    def IncrementalDFS(self, minDepth):
        pass

    def UnifomCostSearch(self):
        pass


print(Graph().DFS('A','D'))

