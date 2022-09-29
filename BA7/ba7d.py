class Cluster:
    clusters = []

    @staticmethod
    def calculate_distance(cluster1, cluster2):
        return sum(distance_matrix[i][j] for i in cluster1.nodes for j in cluster2.nodes) / float(
            len(cluster1.nodes) * len(cluster2.nodes))

    def __init__(self, cluster_id, age, nodes):
        self.cluster_id = cluster_id
        self.age = age
        self.nodes = nodes

    def __str__(self):
        return 'Cluster ' + str(self.cluster_id)


def UPGMA():
    Cluster.clusters = [Cluster(i, 0, [i]) for i in range(N)]
    clusters_ids = set(range(N))

    from collections import defaultdict
    tree = defaultdict(list)
    new_node = N

    while len(clusters_ids) > 1:
        cluster1, cluster2 = min(
            [(Cluster.clusters[c1], Cluster.clusters[c2]) for c1 in clusters_ids for c2 in clusters_ids if c1 != c2],
            key=lambda tpl: Cluster.calculate_distance(tpl[0], tpl[1]))

        new_cluster = Cluster(new_node, 0.5 * Cluster.calculate_distance(cluster1, cluster2),
                              cluster1.nodes + cluster2.nodes)
        Cluster.clusters.append(new_cluster)
        new_node += 1

        tree[new_cluster.cluster_id].append((cluster1.cluster_id, new_cluster.age - cluster1.age))
        tree[new_cluster.cluster_id].append((cluster2.cluster_id, new_cluster.age - cluster2.age))
        tree[cluster1.cluster_id].append((new_cluster.cluster_id, new_cluster.age - cluster1.age))
        tree[cluster2.cluster_id].append((new_cluster.cluster_id, new_cluster.age - cluster2.age))

        clusters_ids.remove(cluster1.cluster_id)
        clusters_ids.remove(cluster2.cluster_id)
        clusters_ids.add(new_cluster.cluster_id)

        distances = [Cluster.calculate_distance(new_cluster, cluster) for cluster in Cluster.clusters]
        for i in range(len(distance_matrix)):
            distance_matrix[i].append(distances[i])
        distance_matrix.append(distances + [0])  # distances[:-1]

    return tree


def print_tree(tree):
    for src in range(len(tree)):
        for dst, length in tree[src]:
            print('{}->{}:{:.3f}'.format(src, dst, length))


if __name__ == '__main__':
    N = int(input())
    distance_matrix = [list(map(int, input().split())) for _ in range(N)]
    print_tree(UPGMA())