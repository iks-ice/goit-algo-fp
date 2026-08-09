import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adjacency_list[u].append((v, weight))
        
    def add_undirected_edge(self, u, v, weight):
        self.add_edge(u, v, weight)
        self.add_edge(v, u, weight)

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[start_vertex] = 0

        min_heap = [(0, start_vertex)]

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

if __name__ == "__main__":
    g = Graph()
    
    g.add_undirected_edge('A', 'B', 4)
    g.add_undirected_edge('A', 'C', 2)
    g.add_undirected_edge('B', 'C', 1)
    g.add_undirected_edge('B', 'D', 5)
    g.add_undirected_edge('C', 'D', 8)
    g.add_undirected_edge('C', 'E', 10)
    g.add_undirected_edge('D', 'E', 2)
    g.add_undirected_edge('D', 'F', 6)
    g.add_undirected_edge('E', 'F', 3)

    start = 'A'
    print(f"Обчислення найкоротших шляхів від вершини '{start}':\n")

    shortest_paths = g.dijkstra(start)
    
    print(f"{'Вершина':<10} | {'Найкоротша відстань від ' + start:<25}")
    print("-" * 42)
    for vertex, dist in sorted(shortest_paths.items()):
        print(f"{vertex:<10} | {dist:<25}")
