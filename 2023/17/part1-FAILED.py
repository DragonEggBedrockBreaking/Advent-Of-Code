import heapq
import networkx as nx

with open("input.txt", "r", encoding="utf8") as f:
    lines = [[int(i) for i in line] for line in f.read().splitlines()]


def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    paths = {start: []}

    while queue:
        (distance, current) = heapq.heappop(queue)
        if current == end:
            return paths[end] + [end]
        for neighbor in graph.neighbors(current):
            if not check_restriction(current, neighbor, paths[current]):
                continue
            old_distance = distances[neighbor]
            new_distance = distance + graph.edges[current, neighbor]['weight']
            if new_distance < old_distance:
                distances[neighbor] = new_distance
                paths[neighbor] = paths[current] + [current]
                heapq.heappush(queue, (new_distance, neighbor))
    return None


def check_restriction(current, neighbour, path):
    if len(path) >= 3:
        five = (path[-3], path[-2], path[-1], current, neighbour)
        if len(set([node[0] for node in five])) == 1 and tuple(sorted(five, key=lambda node: node[1])) == five:
            return False
        if len(set([node[1] for node in five])) == 1 and tuple(sorted(five, key=lambda node: node[0])) == five:
            return False
    return True


G = nx.Graph()
for i, line in enumerate(lines):
    for j in range(len(line)):
        G.add_node((i, j))
for i, line in enumerate(lines):
    for j in range(len(line)):
        if i > 0:
            G.add_edge((i, j), (i-1, j), weight=lines[i-1][j])
        if i < len(lines[0]) - 1:
            G.add_edge((i, j), (i+1, j), weight=lines[i+1][j])
        if j > 0:
            G.add_edge((i, j), (i, j-1), weight=lines[i][j-1])
        if j < len(lines) - 1:
            G.add_edge((i, j), (i, j+1), weight=lines[i][j+1])

path = dijkstra(G, (0, 0), (len(lines) - 1, len(lines[0]) - 1))
print(sum([lines[node[0]][node[1]] for node in path])-lines[0][0])
