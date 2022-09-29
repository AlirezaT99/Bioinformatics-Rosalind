class Node:
    def __init__(self, char=''):
        self.children = {}
        self.value = char

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


def print_edges(node, edge=''):
    if len(node.children) > 1:
        if edge != '':
            print(edge)
        for char in node.children.keys():
            print_edges(node.children[char], char)
    elif len(node.children) == 1:
        print_edges(node.children[list(node.children.keys())[0]], edge + list(node.children.keys())[0])
    else:
        print(edge)


def insert(word):
    node = root
    for idx in range(len(word)):
        if word[idx] not in node.children.keys():
            node.children[word[idx]] = Node(word[idx])
        node = node.children[word[idx]]


if __name__ == '__main__':
    text = input()
    suffixes = [text[i:] for i in range(len(text))]
    root = Node()
    for suffix in suffixes:
        insert(suffix)
    print_edges(root)