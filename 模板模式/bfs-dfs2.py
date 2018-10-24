def traverse(graph, start, end, action):
    path = []
    visited = [start, ]
    while visited:
        current = visited.pop(0)
        path.append(current)
        if current == end:
            return (True, path)  # 两个顶点之间没有连接，则跳过
        visited = action(visited, graph[current])
    return (False, path)


def extend_bfs_path(visited, current):
    return visited + current


def extend_dfs_path(visited, current):
    return current + visited


graph = {'Frankfurt': ['Mannheim', 'Wurzburg', 'Kassel'],
         'Mannheim': ['Karlsruhe'],
         'Karlsruhe': ['Augsburg'],
         'Augsburg': ['Munchen'],
         'Wurzburg': ['Erfurt', 'Nurnberg'],
         'Nurnberg': ['Stuttgart', 'Munchen'],
         'Kassel': ['Munchen'],
         'Erfurt': [],
         'Stuttgart': [],
         'Munchen': []}

bfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_bfs_path)
dfs_path = traverse(graph, 'Frankfurt', 'Nurnberg', extend_dfs_path)
print('bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
print('dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))
