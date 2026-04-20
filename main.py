class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, "->", self.adjacency_list[vertex])


# Misol:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")
graph.add_edge("D", "A")

graph.print_graph()
```

Kodni o'rganish uchun:

- `Graph` klassi yaratiladi.
- `adjacency_list` atributi yaratiladi, bu grafning adjacency ro'yxati bo'ladi.
- `add_vertex` metodi yaratiladi, u grafga yangi nuqtani qo'shadi.
- `add_edge` metodi yaratiladi, u grafga yangi qatorni qo'shadi.
- `print_graph` metodi yaratiladi, u grafni chiqaradi.
- Misol yaratiladi, grafga nuqtalar va qatorlar qo'shadi, keyin grafni chiqaradi.
