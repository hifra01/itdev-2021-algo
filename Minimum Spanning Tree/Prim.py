def Prim(graph: dict, root_node):
    # Isi list unvisited didapat dari keys yang ada pada dictionary graph
    unvisited = list(graph.keys())
    visited = []
    solution = []

    # Memindahkan node akar dari unvisited ke visited
    visited.append(root_node)
    unvisited.remove(root_node)

    # Iterasi dilakukan selama di dalam unvisited masih ada node
    while unvisited:
        start = ''  # untuk menampung node asal edge solusi
        end = ''    # untuk menampung node tujuan edge solusi
        min_cost = float('inf') # untuk menampung biaya edge solusi

        for start_node in visited:  # Lakukan iterasi terhadap setiap node yang sudah dikunjungi
            for end_node, cost in graph[start_node].items():    # terhadap node yang terhubung
                
                # Catat bila edge memiliki biaya yang lebih rendah dari sebelumnya
                # dan node tujuan belum pernah dikunjungi
                if cost < min_cost and end_node not in visited:
                    start = start_node
                    end = end_node
                    min_cost = cost

        # Memasukkan solusi ke list solusi
        solution.append([start, end, min_cost])

        # Memindahkan node tujuan dari unvisited ke visited
        visited.append(end)
        unvisited.remove(end)

    return solution




if __name__ == '__main__':
    graph = dict()

    # Untuk setiap edge, tambahkan node tujuan
    # beserta beratnya.
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

    # Node akar
    root_node = 'S'

    result = Prim(graph, root_node)

    for solution in result:
        print(solution)
