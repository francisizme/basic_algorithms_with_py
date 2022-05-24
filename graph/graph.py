from vertex import Vertex

vertex_tuple = tuple[str, list[str]]


class Graph:
    def __init__(self, directed=False):
        self.graph_dict: dict[str, Vertex] = {}
        self.directed = directed
        print("created", "directed" if directed else "bi-directional", "graph", end=" ")

    def add_vertex(self, vertex: Vertex):
        self.graph_dict[vertex.value] = vertex
        print(f"added {vertex.value} to the graph")

    def add_edge(self, from_vertex: str, to_vertex: str, weight=0):
        self.graph_dict[from_vertex].add_edge(to_vertex, weight)
        if not self.directed:
            self.graph_dict[to_vertex].add_edge(from_vertex, weight)

    def find_path(self, from_vertex: str, to_vertex: str, visited=None):
        if visited is None:
            visited: set[str] = set()
        visited.add(from_vertex)
        if from_vertex == to_vertex:
            return visited
        for neighbor in self.graph_dict[from_vertex].get_edges():
            if neighbor not in visited:
                path = self.find_path(neighbor, to_vertex, visited)
                if path:
                    return path

    def find_shorted_path(self, from_vertex: str, to_vertex: str):
        start_vertex_and_path: vertex_tuple = (from_vertex, [from_vertex])
        queue: list[vertex_tuple] = [start_vertex_and_path]
        visited: set[str] = set()

        while queue:
            current_vertex, path = queue.pop(0)
            visited.add(current_vertex)
            for neighbor in self.graph_dict[current_vertex].get_edges():
                if neighbor not in visited:
                    if neighbor == to_vertex:
                        return path + [neighbor]
                    else:
                        queue.append((neighbor, path + [neighbor]))
