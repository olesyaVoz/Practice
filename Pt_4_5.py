def find_all_paths(graph, start, end, path):
    path = path + [start]
    all_paths = []

    if start == end:
        return [path]

    for vertex in graph[start]:
        if vertex in path:
            continue

        new_paths = find_all_paths(graph, vertex, end, path)

        for way in new_paths:
            all_paths.append(way)

    return all_paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'
path = []

paths = find_all_paths(graph, start, end, path)
print("Пути от вершины A до вершины B:", paths)
