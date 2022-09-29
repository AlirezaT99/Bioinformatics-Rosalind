def find_profile(motifs):
    consensus = ''
    profile = []
    for idx in range(len(motifs[0])):
        count = {char: 0 for char in alphabet}
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
        prod *= profile[idx][item[idx]]  # / count ?
    return prod


def greedy_motif_search():
    best_motifs = [dna[:k] for dna in DNAs]
    first_dna_k_mers = [DNAs[0][i:i + k] for i in range(len(DNAs[0]) - k + 1)]
    for k_mer in first_dna_k_mers:
        motifs = [k_mer, ]
        for i in range(1, t):
            consensus, profile = find_profile(motifs)
            motifs.append(max([DNAs[i][j:j + k] for j in range(len(DNAs[i]) - k + 1)]
                              , key=lambda item: calc_prob(profile, item)))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


if __name__ == '__main__':
    k, t = map(int, input().split())
    DNAs = [input() for _ in range(t)]
    alphabet = ['A', 'C', 'G', 'T']
    for motif in greedy_motif_search():
        print(motif)