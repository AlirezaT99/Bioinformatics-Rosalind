import random


def find_profile(motifs):
    consensus = ''
    profile = []
    for idx in range(len(motifs[0])):
        count = {char: 1 for char in alphabet}
        for motif in motifs:
            count[motif[idx]] += 1
        consensus += max(alphabet, key=lambda nucleotide: count[nucleotide])
        profile.append(count)
    return consensus, profile


def score(motifs):
    result = 0
    _, profile = find_profile(motifs)
    for item in profile:
        result += sum(item.values()) - max(item.values())
    return result


def calc_prob(profile, item):
    prod = 1
    for idx in range(len(item)):
        prod *= profile[idx][item[idx]]
    return prod


def generate_random_motifs():
    for i in range(t):
        idx = random.randint(0, len(DNAs[i]) - k)
        yield DNAs[i][idx:idx + k]


def randomized_motif_search():
    motifs = list(generate_random_motifs())
    best_motifs = motifs
    while 1:
        _, profile = find_profile(motifs)
        motifs = []
        for i in range(t):
            motifs.append(max([DNAs[i][j:j + k] for j in range(len(DNAs[i]) - k + 1)]
                              , key=lambda item: calc_prob(profile, item)))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs


if __name__ == '__main__':
    k, t = map(int, input().split())
    DNAs = [input() for _ in range(t)]

    alphabet = ['A', 'C', 'G', 'T']
    epochs = 1000

    motifs = None
    for _ in range(epochs):
        new_motifs = randomized_motif_search()
        if not motifs or score(new_motifs) < score(motifs):
            motifs = new_motifs

    for motif in motifs:
        print(motif)