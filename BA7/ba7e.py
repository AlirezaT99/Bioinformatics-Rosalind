def remove_col_row(matrix, i):
    result = []
    for j in range(len(matrix)):
        if j != i:
            result.append([matrix[j][k] for k in range(len(matrix[j])) if k != i])
    return result


def build_d_prime(total_distance, dist_matrix, n):
    d_prime = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d_prime[i][j] = (n - 2) * dist_matrix[i][j] - total_distance[i] - total_distance[j]
            d_prime[j][i] = d_prime[i][j]
    return d_prime


def get_arg_min(matrix, n):
    i = j = -1
    current_min = float('inf')
    for k in range(n):
        for m in range(k, n):
            if matrix[k][m] < current_min:
                i, j = k, m
                current_min = matrix[i][j]
    return i, j


def create_delta(total_distance, n):
    delta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            delta[i][j] = (total_distance[i] - total_distance[j]) / (n - 2)
            delta[j][i] = delta[i][j]
    return delta


def neighbour_joining(dist_matrix, n, nodes):
    if n == 2:
        return {nodes[0]: [(nodes[1], dist_matrix[0][1])],
                nodes[1]: [(nodes[0], dist_matrix[0][1])]}

    total_distance = [sum(row) for row in dist_matrix]
    i, j = get_arg_min(build_d_prime(total_distance, dist_matrix, n), n)

    delta = create_delta(total_distance, n)
    limb_length_i = (dist_matrix[i][j] + delta[i][j]) / 2
    limb_length_j = (dist_matrix[i][j] - delta[i][j]) / 2

    new_row = [(dist_matrix[k][i] + dist_matrix[k][j] - dist_matrix[i][j]) / 2 for k in range(n)] + [0]  # 0.5 *
    dist_matrix.append(new_row)
    for k in range(n):
        dist_matrix[k].append(new_row[k])

    new_node = nodes[-1] + 1
    nodes.append(new_node)

    dist_matrix = remove_col_row(dist_matrix, max(i, j))  # to avoid exception
    dist_matrix = remove_col_row(dist_matrix, min(i, j))  # and remove correctly

    node_i = nodes[i]
    node_j = nodes[j]
    nodes.remove(node_i)
    nodes.remove(node_j)

    tree = neighbour_joining(dist_matrix, n - 1, nodes)
    if node_i not in tree.keys():
        tree[node_i] = []
    if node_j not in tree.keys():
        tree[node_j] = []
    if new_node not in tree.keys():
        tree[new_node] = []

    tree[node_i].append((new_node, limb_length_i))
    tree[new_node].append((node_i, limb_length_i))
    tree[node_j].append((new_node, limb_length_j))
    tree[new_node].append((node_j, limb_length_j))

    return tree


def print_tree(tree):
    for src in range(len(tree)):
        for dst, length in tree[src]:
            print('{}->{}:{:.3f}'.format(src, dst, length))  # 3 or 2 ?


if __name__ == '__main__':  # Courtesy: Implementing D-Prime is adapted from github (was not in slides)
    N = int(input())
    distance_matrix = [list(map(int, input().split())) for _ in range(N)]
    print_tree(neighbour_joining(distance_matrix, N, list(range(N))))