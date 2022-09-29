def process_k_mers():
    for i in range(len(text) - k + 1):
        if text[i:i + k - 1] in graph.keys():
            graph[text[i:i + k - 1]] += ',' + text[i + 1:i + k]
        else:
            graph[text[i:i + k - 1]] = text[i + 1:i + k]


if __name__ == '__main__':
    k = int(input())
    text = input()

    graph = dict()
    process_k_mers()
    output = []
    for k, v in graph.items():
        output.append(k + ' -> ' + v)
        # print(k, '->', ','.join(v))
    for item in sorted(output):
        print(item)