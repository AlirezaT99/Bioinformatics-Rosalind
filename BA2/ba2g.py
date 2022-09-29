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


def sample_motif(profile, items):
    return random.choices(items, [calc_prob(profile, item) for item in items])[0]


def generate_random_motifs():
    for i in range(t):
        idx = random.randint(0, len(DNAs[i]) - k)
        yield DNAs[i][idx:idx + k]


def gibbs_sampler():
    motifs = list(generate_random_motifs())
    best_motifs = motifs
    for time in range(N):
        i = random.randint(0, t - 1)
        _, profile = find_profile(motifs[:i] + motifs[i + 1:])
        motifs[i] = sample_motif(profile, [DNAs[i][j:j + k] for j in range(len(DNAs[i]) - k + 1)])

        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


if __name__ == '__main__':
    k, t, N = map(int, input().split())
    DNAs = [input() for _ in range(t)]

    alphabet = ['A', 'C', 'G', 'T']
    epochs = 20

    motifs = None
    for _ in range(epochs):
        new_motifs = gibbs_sampler()
        if not motifs or score(new_motifs) < score(motifs):
            motifs = new_motifs

    for motif in motifs:
        print(motif)