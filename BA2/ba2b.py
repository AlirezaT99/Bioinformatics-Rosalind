import itertools


def hamming_distance(str1, str2):
    return sum(1 if str1[j] != str2[j] else 0 for j in range(len(str1)))


k = int(input())
strings = []
while (text := input()) != '':
    strings.append(text)
alphabets = ['A', 'C', 'G', 'T']
k_mers = list(map(''.join, itertools.product(alphabets, repeat=k)))

result = None
result_value = 1e6
for k_mer in k_mers:
    d = 0
    for string in strings:
        d += min(hamming_distance(k_mer, string[i:i+k]) for i in range(len(string) - k + 1))
    if result_value > d:
        result_value = d
        result = k_mer
print(result)