def dfs(Graph, start, meet):
    meet.add(start)
    print(start)

    for n in Graph[start]:
        if n not in meet:
            dfs(Graph, n, meet)

MyGraph12 = {
    'A':['B','C'],
    'B':['A','D'],
    'C':['A','E','F'],
    'D':['B','G'],
    'E':['C','H'],
    'F':['C'],
    'G':['D'],
    'H':['E']
}
meet = set()
dfs(MyGraph12,'A',meet)
