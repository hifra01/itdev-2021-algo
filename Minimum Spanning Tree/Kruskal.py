def Kruskal(graph: list):
    # Konstanta pembantu (index elemen pada graph)
    FIRST_NODE = 0
    SECOND_NODE = 1
    COST = 2

    # Generate daftar edge yang terurut dari cost rendah ke tinggi
    sorted_graph = sorted(graph, key=lambda edge: edge[COST])

    # Tabel Parent dan Rank yang digunakan untuk algoritma Find-Union
    parent = dict()
    rank = dict()

    node_list = set([edge[0] for edge in sorted_graph])

    # Memberi nilai awal pada tabel parent dan rank
    for node in node_list:
        parent[node] = node
        rank[node] = 0

    def find(node):
        # Fungsi untuk mencari absolute parent dari sebuah node
        if parent[node] == node:
            return node
        return find(parent[node])

    def union(first_node, second_node):
        # Fungsi untuk menggabungkan dua set tree yang terpisah menjadi satu
        first_node_parent = find(first_node)
        second_node_parent = find(second_node)

        if rank[first_node_parent] < rank[second_node_parent]:
            parent[first_node_parent] = second_node_parent

        elif rank[first_node_parent] > rank[second_node_parent]:
            parent[second_node_parent] = first_node_parent

        else:
            parent[second_node_parent] = first_node_parent
            rank[first_node_parent] += 1

    def find_minimum_spanning_tree():
        total_edge = 0
        result = []

        for edge in sorted_graph:
            first_node = edge[FIRST_NODE]
            second_node = edge[SECOND_NODE]
            first_node_parent = find(first_node)
            second_node_parent = find(second_node)

            # Tambahkan edge ke solusi jika absolute parent kedua node tidak sama
            if first_node_parent != second_node_parent:
                total_edge += 1
                result.append(edge)
                union(first_node, second_node)

            # Algoritma dapat berhenti jika jumlah edge solusi sudah mencapai (jumlah_node - 1)
            if total_edge >= len(node_list):
                break

        return result

    return find_minimum_spanning_tree()


if __name__ == '__main__':
    graph = []

    graph.append(['S', 'A', 7])
    graph.append(['S', 'C', 8])

    graph.append(['A', 'S', 7])
    graph.append(['A', 'B', 6])
    graph.append(['A', 'C', 3])

    graph.append(['B', 'A', 6])
    graph.append(['B', 'C', 4])
    graph.append(['B', 'D', 2])
    graph.append(['B', 'T', 5])

    graph.append(['C', 'S', 8])
    graph.append(['C', 'A', 3])
    graph.append(['C', 'B', 4])
    graph.append(['C', 'D', 3])

    graph.append(['D', 'B', 2])
    graph.append(['D', 'C', 3])
    graph.append(['D', 'T', 2])

    graph.append(['T', 'B', 5])
    graph.append(['T', 'D', 2])

    print(Kruskal(graph))
