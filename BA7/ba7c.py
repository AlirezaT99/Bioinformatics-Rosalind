def get_path(tree, src, dst, visited):  # DFS
    visited[src] = True
    for v, w in tree[src]:
        if visited[v]:
            continue

        if v == dst:
            return [(src, w), (dst, 0)]

        path = get_path(tree, v, dst, visited)
        if path is not None:
            return [(src, w)] + path

    return None


def delete_edge(tree, src, dst):
    i = -1
    for i, (neighbor, length) in enumerate(tree[src]):
        if neighbor == dst:
            break
    del tree[src][i]

    for i, (neighbor, length) in enumerate(tree[dst]):
        if neighbor == src:
            break
    del tree[dst][i]


def insert_new_node(tree, src, dst, distance, node_id):
    # Courtesy: this method is copied as it was not the subject presented in class
    path = get_path(tree, src, dst, [False] * (2 * N))

    curr = 0
    edge_length = path[0][1]
    remaining_length = distance

    while remaining_length >= edge_length:
        remaining_length -= edge_length
        curr += 1
        edge_length = path[curr][1]

    curr_node = path[curr][0]
    next_node = path[curr + 1][0]

    tree[curr_node].append((node_id, remaining_length))
    tree[next_node].append((node_id, edge_length - remaining_length))
    tree[node_id] = [(curr_node, remaining_length), (next_node, edge_length - remaining_length)]
    delete_edge(tree, curr_node, next_node)


def construct_tree(n, dist_matrix, node_id):
    if n == 2:
        return {0: [(1, dist_matrix[0][1])],
                1: [(0, dist_matrix[0][1])]}

    delta = min(dist_matrix[i][n - 1] + dist_matrix[k][n - 1] - dist_matrix[i][k]
                for i in range(n) for k in range(n) if i != n - 1 and k != n - 1) // 2

    for i in range(n - 1):
        dist_matrix[i][n - 1] -= delta
        dist_matrix[n - 1][i] = dist_matrix[i][n - 1]

    x = src = dst = -1
    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if dist_matrix[i][j] == dist_matrix[i][n - 1] + dist_matrix[j][n - 1]:
                x, src, dst = dist_matrix[i][n - 1], i, j
                break

    tree = construct_tree(n - 1, dist_matrix, node_id - 1)
    insert_new_node(tree, src, dst, x, node_id)
    tree[n - 1] = [(node_id, delta)]
    tree[node_id].append((n - 1, delta))

    return tree


def print_tree(tree):
    for src in tree:
        for dst, length in tree[src]:
            print('{}->{}:{}'.format(src, dst, length))


if __name__ == '__main__':
    N = int(input())
    adjacency_matrix = [list(map(int, input().split())) for _ in range(N)]
    print_tree(construct_tree(N, adjacency_matrix, (N-1 + N-2)))  # is called N_2 times