from itertools import combinations, product


def visible_k_mers(seq, k):
    result = list()
    for i in range(len(seq) - k + 1):
        result.append(seq[i:i + k])
    return result


def approximate_matches(k_mer):
    result = set()
    res_ls = list()
    for indices in combinations_indices:
        for chars in permutations_chars:
            k_mer_copy = k_mer
            for index, char in zip(indices, chars):
                k_mer_copy = k_mer_copy[:index] + char + k_mer_copy[index + 1:]
            result.add(k_mer_copy)
            res_ls.append(k_mer_copy)
    return result


def k_mers_approximate_occurrences(text, k):
    k_mers = dict()
    all_k_mers = visible_k_mers(text, k)
    all_k_mers_rev = list(map(reverse_complement, all_k_mers))

    for k_mer in all_k_mers + all_k_mers_rev:
        for match in approximate_matches(k_mer):
            if match in k_mers.keys():
                k_mers[match] += 1
            else:
                k_mers[match] = 1
    return k_mers


def results_argmax(results):
    maximum = max([value for value in results.values()])
    return filter(lambda key: results[key] == maximum, results.keys())


def reverse_complement(nucleotide):
    return ''.join(complements_dict[i] for i in nucleotide[::-1])


complements_dict = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
nucleobases = ''.join(['T', 'C', 'A', 'G'])

if __name__ == '__main__':
    dna_string = input()
    pattern_length, max_mismatch = list(map(int, input().split()))
    combinations_indices = list(combinations(range(pattern_length), max_mismatch))
    permutations_chars = list(product(nucleobases, repeat=max_mismatch))
    res = k_mers_approximate_occurrences(dna_string, pattern_length)
    print(*results_argmax(res))