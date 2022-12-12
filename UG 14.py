class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()

    def vertex(self): #mencetak seluruh vertex
        print("Seluruh Node dibawah = ", end= "")
        for key, value in self._data.items():
            print(key,end="")
        print()
    
    def edge(self): #mencetak seluruh edge
        print("Seluruh Edge = ", end = "")
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        for item in listEdge:
            print(item, end = ' ')
        print()

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        print("Traversing BFS = ",end="")
        visited = [] 
        visited.append(node)
        listQueue = []
        listQueue.append(node)

        while listQueue:
            node = listQueue.pop(0)
            print(node, end=" ")
            for i in self._data[node]:
                if i not in visited:
                    visited.append(i)
                    listQueue.append(i)

graph = Graph()
graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('C')
graph.addVertex('D')
graph.addVertex('E')
graph.addVertex('F')
graph.addVertex('G')

graph.addEdge('A', 'B')
graph.addEdge('B','C')
graph.addEdge('B', 'D')
graph.addEdge('C', 'G')
graph.addEdge('C', 'E')
graph.addEdge('D','E')
graph.addEdge('E', 'F')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs("A")