def process_input():
    while edges := input():
        parts = edges.split(' -> ')
        src, dest_arr = int(parts[0]), list(map(int, parts[1].split(',')))
        adjacent[src] = dest_arr
        out_degree[src] = len(dest_arr)
        for dest in dest_arr:
            if dest not in in_degree.keys():
                in_degree[dest] = 0
            in_degree[dest] += 1


def find_start_finish():
    start_node = finish_node = -1
    for node in out_degree.keys():
        if node not in in_degree.keys():
            in_degree[node] = 0
        if out_degree[node] > in_degree[node]:
            start_node = node
    for node in in_degree.keys():
        if node not in out_degree.keys():
            out_degree[node] = 0
        if in_degree[node] > out_degree[node]:
            finish_node = node
    return start_node, finish_node


def find_euler_path():
    current_node = start
    result = []

    current_path = [start]
    while current_path:  # isn't empty
        if out_degree[current_node]:
            current_path.append(current_node)
            out_degree[current_node] -= 1
            current_node = adjacent[current_node].pop()
        else:
            result.append(current_node)
            current_node = current_path.pop()
    return '->'.join(map(str, result[::-1]))


if __name__ == '__main__':
    adjacent, out_degree, in_degree = {}, {}, {}
    process_input()
    start, finish = find_start_finish()
    print(find_euler_path())