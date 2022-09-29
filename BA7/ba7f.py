class Node:
    def __init__(self, tag, label, node_id):
        self.tag = tag
        self.label = label
        self.node_id = node_id
        self.children = []
        self.children_chars = dict()

    @staticmethod
    def reset_tags():
        for node in nodes.values():
            node.tag = int(len(node.node_id) == labels_len)

    @staticmethod
    def get_ripe_nodes():
        result = []
        for node in nodes.values():
            if node.tag == 0 and len(node.children) == 2 and node.children[0].tag + node.children[1].tag == 2:
                result.append(node)
        return result

    @staticmethod
    def get_leaves():
        result = []
        for node in nodes.values():
            if len(node.children) == 0:
                result.append(node)
        return result

    def __str__(self):
        return 'Node ' + self.node_id

    def __repr__(self):
        return 'Node ' + self.node_id


def assign_label(node, char):  # Backtrace
    if not node.children:
        return
    node.label += char
    assign_label(node.children[0], node.children_chars[char][0])
    assign_label(node.children[1], node.children_chars[char][1])


def small_parsimony(idx):
    s = dict()
    for leaf in leaves:
        s[leaf] = {'A': 1e5, 'C': 1e5, 'G': 1e5, 'T': 1e5}
        s[leaf][leaf.label[idx]] = 0
    ripe_node = None
    while ripe_nodes := Node.get_ripe_nodes():
        ripe_node = ripe_nodes.pop()
        ripe_node.tag = 1

        child1 = ripe_node.children[0]
        child2 = ripe_node.children[1]
        s[ripe_node] = {'A': None, 'C': None, 'G': None, 'T': None}

        for symbol in alphabet:  # BUG
            child1_char, min_score = '', 1e5
            for k in alphabet:
                value = s[child1][k] + int(symbol != k)
                if value < min_score:
                    min_score = value
                    child1_char = k

            s[ripe_node][symbol] = min_score

            child2_char, min_score = '', 1e5
            for j in alphabet:
                value = s[child2][j] + int(symbol != j)
                if value < min_score:
                    min_score = value
                    child2_char = j

            ripe_node.children_chars[symbol] = (child1_char, child2_char)
            s[ripe_node][symbol] += min_score

            # s[ripe_node][symbol] = min(list(s[child1][k] + int(symbol != child1.label[idx]) for k in alphabet)) \
            #                          + min(list(s[child2][j] + int(symbol != child2.label[idx]) for j in alphabet))
    smallest_char, smallest_value = '', 1e5
    for k, v in s[ripe_node].items():
        if v < smallest_value:
            smallest_value = v
            smallest_char = k
    assign_label(ripe_node, smallest_char)


def calculate_score():
    score = 0
    for node in nodes.values():
        for child in node.children:
            score += hamming_dist(node.label, child.label)
    return score


def hamming_dist(s1, s2):
    return sum([1 if s1[j] != s2[j] else 0 for j in range(len(s1))])


def get_edges():
    edges = []
    for node in nodes.values():
        for child in node.children:
            dist = hamming_dist(node.label, child.label)
            edges.append(node.label + '->' + child.label + ':' + str(dist))
            edges.append(child.label + '->' + node.label + ':' + str(dist))
    return edges


if __name__ == '__main__':
    n = int(input())
    nodes = dict()

    labels_len = -1
    alphabet = ['A', 'C', 'G', 'T']

    while (edge := input()) != '':
        src, dst = edge.split('->')
        if dst not in nodes.keys():
            if dst.isdigit():
                nodes[dst] = Node(0, '', dst)
            else:
                nodes[dst] = Node(1, dst, dst)
                labels_len = len(dst)

        if src not in nodes.keys():
            nodes[src] = Node(0, '', src)
        nodes[src].children.append(nodes[dst])

    leaves = Node.get_leaves()
    for i in range(labels_len):
        small_parsimony(i)
        Node.reset_tags()

    print(calculate_score())
    for edge in get_edges():
        print(edge)