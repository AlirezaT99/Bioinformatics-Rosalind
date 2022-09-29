def preprocess():
    occurrence_dict = {}
    chars = ['A', 'C', 'G', 'T']
    for char in chars:
        arr = []
        counter = 0
        for i in range(len(BWT)):
            if BWT[i] == char:
                counter += 1
            arr.append(counter)
        occurrence_dict[char] = arr
    return occurrence_dict, {'A': sorted_BWT.find('A'), 'C': sorted_BWT.find('C'), 'G': sorted_BWT.find('G'),
                             'T': sorted_BWT.find('T')}, {'A': sorted_BWT.rfind('A'), 'C': sorted_BWT.rfind('C'),
                                                          'G': sorted_BWT.rfind('G'), 'T': sorted_BWT.rfind('T')}


def count_match(word):
    old_low = char_first[word[-1]]
    old_high = char_last[word[-1]]
    high = low = -1
    for i in range(len(word) - 2, -1, -1):
        low = char_first[word[i]] + char_count[word[i]][old_low - 1]
        high = low + (char_count[word[i]][old_high] - char_count[word[i]][old_low - 1]) - 1
        old_low, old_high = low, high
        if high < low:
            return 0
    return high - low + 1


if __name__ == '__main__':
    BWT = input()
    sorted_BWT = ''.join(sorted(BWT))
    queries = input().split()
    char_count, char_first, char_last = preprocess()

    result = []
    for query in queries:
        result.append(count_match(query))
    print(*result)