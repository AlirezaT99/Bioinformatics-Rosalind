def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)

    lps = [0] * m
    compute_lps_array(pattern, m, lps)
    # print(lps)

    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:  # found a match
            yield i - j
            j = lps[-1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def compute_lps_array(pattern, m, lps):
    prev_length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[prev_length]:
            prev_length += 1
            lps[i] = prev_length
            i += 1
        else:
            if prev_length != 0:
                prev_length = lps[prev_length - 1]
            else:
                lps[i] = 0
                i += 1


print(*list(kmp_search(input(), input())))