class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if shortest_path is None or len(sp) < len(shortest_path):
                    shortest_path = sp

        return shortest_path

    def dfs(self, visited, root):
        if root not in visited:
            print(root)
            visited.add(root)

        for node in self.graph_dict[root]:
            if node not in visited:
                self.dfs(visited, node)

    def bfs(self, visited, root):
        q = [root]
        while len(q) > 0:
            root = q.pop(0)
            if root not in visited:
                print(root)
                visited.add(root)
                for node in self.graph_dict[root]:
                    if node not in visited:
                        q.append(node)


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Paris", "Mumbai"),
        ("Mumbai", "Dubai"),
        ("Dubai", "Mumbai"),
        ("Paris", "Dubai"),
        ("Dubai", "Paris"),
        ("Paris", "New York"),
        ("New York", "Paris"),
        ("Dubai", "New York"),
        ("New York", "Dubai"),
        ("New York", "Toronto"),
        ("Toronto", "New York"),
    ]
    route_graph = Graph(routes)
    startPoint = "Mumbai"
    endPoint = "New York"
    isVisited = set()
    route_graph.bfs(isVisited, "Toronto")
    print(route_graph.get_shortest_path(startPoint, endPoint))
