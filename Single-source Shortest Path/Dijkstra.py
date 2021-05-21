def Dijkstra(graph: dict, origin):
    # Konstanta pembantu
    INFINITE = float('inf')
    DISTANCE = 0    # Index kolom Distance pada tabel Jarak Terpendek
    PREVIOUS_NODE = 1   # Index kolom Previous Node pada tabel Jarak Terpendek

    # Men-generate tabel Jarak Terpendek
    shortest_table = dict()
    for node in graph.keys():
        if node == origin:
            shortest_table[node] = [0, None]
        else:
            shortest_table[node] = [INFINITE, None]

    # Fungsi-fungsi pembantu
    def get_shortest_distance(node):
        # Fungsi untuk mengambil distance sebuah node dari tabel Jarak Terpendek
        return shortest_table[node][DISTANCE]

    def set_shortest_distance(node, new_distance):
        # Fungsi untuk mengubah distance sebuah node dari tabel Jarak Terpendek
        shortest_table[node][DISTANCE] = new_distance

    def set_previous_node(node, previous_node):
        # Fungsi untuk mengubah Previous Node sebuah node dari tabel Jarak Terpendek
        shortest_table[node][PREVIOUS_NODE] = previous_node

    def get_distance(first_node, second_node):
        # Fungsi untuk mengambil nilai jarak node 1 ke node 2 dari tabel Graph
        return graph[first_node][second_node]

    def get_next_node(visited):
        # Fungsi untuk mencari unvisited node dengan nilai distance terkecil dari tabel Jarak Terpendek
        unvisited = []

        for key, value in shortest_table.items():
            # Untuk setiap node pada tabel Jarak Terpendek,
            # jika node tidak terdapat pada visited, masukkan ke unvisited
            if key not in visited:
                unvisited.append([key, value])

        # Urutkan unvisited berdasarkan kolom Distance dari yang terkecil ke yang terbesar
        unvisited.sort(key=lambda node: node[1][DISTANCE])

        # Kembalikan nama node dengan distance urutan pertama pada list unvisited
        return unvisited[0][0]

    def find_shortest_path():
        visited = []
        # Pencarian dimulai dari node origin
        current_node = origin

        while True:
            # Mencatat node-node tetangga dari node yang dicek saat ini
            neighbor = graph[current_node]

            if set(neighbor).issubset(set(visited)):
                # Jika semua node tetangga sudah pernah dikunjungi, maka lewati node ini
                pass

            else:
                unvisited = set(neighbor).difference(set(visited))

                for next_node in unvisited:
                    # Dapatkan jarak antara node origin dengan node yang belum dikunjungi
                    distance_from_origin = get_shortest_distance(next_node)

                    # Jika current_node masih pada node asal dan jarak neighbor pada tabel Jarak Terpendek masih infinite
                    if distance_from_origin == INFINITE and current_node == origin:
                        total_distance = get_distance(current_node, next_node)

                    else:
                        total_distance = get_shortest_distance(
                            current_node) + get_distance(current_node, next_node)

                    # Ubah nilai pada tabel Jarak Terpendek jika total_distance saat ini lebih kecil
                    if total_distance < distance_from_origin:
                        set_shortest_distance(next_node, total_distance)
                        set_previous_node(next_node, current_node)

            # Menandai current node sebagai visitedS
            visited.append(current_node)

            # Mengecek apakah algoritma sudah selesai atau belum
            if len(visited) == len(shortest_table.keys()) or get_shortest_distance(get_next_node(visited)) == INFINITE:
                break

            # Mengubah nilai current_node menjadi node untuk dicek berikutnya
            current_node = get_next_node(visited)

        return shortest_table

    return find_shortest_path()


if __name__ == '__main__':
    graph = dict()
    graph['S'] = {
        'A': 7,
        'C': 8
    }

    graph['A'] = {
        'S': 7,
        'B': 6,
        'C': 3
    }

    graph['B'] = {
        'A': 6,
        'C': 4,
        'D': 2,
        'T': 5
    }

    graph['C'] = {
        'S': 8,
        'A': 3,
        'B': 4,
        'D': 3
    }

    graph['D'] = {
        'B': 2,
        'C': 3,
        'T': 2
    }

    graph['T'] = {
        'B': 5,
        'D': 2
    }

    origin = 'S'

    print(Dijkstra(graph, origin))
