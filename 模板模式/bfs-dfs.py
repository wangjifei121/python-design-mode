"""
sorted()这样的函数属于理想的案例。现实中，我们没法始终写出100%通用的代码。许多算法都有一些（但并非全部）通用步骤。
广度优先搜索（Breadth-First Search，BFS）和深度优先 搜索（Depth-First Search，DFS）是其中不错的例子.
"""

def bfs(graph, start, end):
    """
    广度优先搜索（Breadth-First Search，BFS）
    :param graph: 城市列表
    :param start: 出发地 Frankfurt
    :param end: 目的地 Nurnberg
    """
    path = []
    visited = [start, ]
    while visited:
        current = visited.pop(0)
        path.append(current)
        if current == end:
            return (True, path)  # 两个顶点不相连，则跳过
        visited = visited + graph[current]
    return (False, path)


# 函数bfs()和dfs()在start和end之间存在一条路径时返回一个元组(True, path)；
# 如果路径不存在，则返回(False, path)（此时， path为空）。

def dfs(graph, start, end):
    """
    和深度优先搜索（Depth-First Search，DFS）
    :param graph: 城市列表
    :param start: 出发地
    :param end: 目的地
    """
    path = []
    visited = [start, ]
    while visited:
        current = visited.pop(0)
        path.append(current)
        if current == end:
            return (True, path)  # 两个顶点不相连，则跳过
        visited = graph[current] + visited
    return (False, path)


def main():
    """
    为了简化，假设该图是有向的。这意味着只能朝一个方向移动，我们可以检测如何从Frankfurt到Mannheim，而不是另一个方向。
    可以使用列表的字典结构来表示这个有向图。每个城市是字典中的一个键，列表的内容是从该城市始发的所有可能目的地。
    叶子顶点的城市（例如，Erfurt）使用一个空列表即可（无目的地）。
    """
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

    bfs_path = bfs(graph, 'Frankfurt', 'Nurnberg')
    dfs_path = dfs(graph, 'Frankfurt', 'Nurnberg')
    print('bfs Frankfurt-Nurnberg: {}'.format(bfs_path[1] if bfs_path[0] else 'Not found'))
    print('dfs Frankfurt-Nurnberg: {}'.format(dfs_path[1] if dfs_path[0] else 'Not found'))

    bfs_nopath = bfs(graph, 'Wurzburg', 'Kassel')
    print('bfs Wurzburg-Kassel: {}'.format(bfs_nopath[1] if bfs_nopath[0] else 'Not found'))
    dfs_nopath = dfs(graph, 'Wurzburg', 'Kassel')
    print('dfs Wurzburg-Kassel: {}'.format(dfs_nopath[1] if dfs_nopath[0] else 'Not found'))


if __name__ == '__main__':
    main()
