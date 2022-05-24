class Vertex:
    def __init__(self, value: str):
        self.value = value
        self.edges = {}
        print(f"created {value} vertex.")

    def add_edge(self, value: str, weight=0):
        self.edges[value] = weight
        print(f"added {value} to {self.value}. Weight is {weight}.")

    def get_edges(self):
        return list(self.edges.keys())
