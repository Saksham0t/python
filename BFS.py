def BFS(visited, MyGraph12, node):
    visited.append(node)
    queue.append(node)
    while queue:
      m = queue.pop(0)
      print (m, end=' ')
      for n in MyGraph12[m]:
        if n not in visited:
            visited.append(n)
            queue.append(n)
MyGraph12 = {
           'A': ['B', 'C'],
           'B': ['D', 'E', 'A'],
           'C': ['F', 'H', 'A'],
           'D': ['B', 'G'],
           'E': ['B'],
           'F': ['C'],
           'G': ['D', 'H'],
           'H': ['C', 'G']
}
visited = []
queue = []
print("Following is the Breadth-First Search: ")
BFS(visited, MyGraph12, 'A')


