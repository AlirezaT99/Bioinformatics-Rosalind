import numpy as np
from math import inf


def get_score(i, j):
    return BLOSUM62[indices.index(str1[i])][indices.index(str2[j])]


def lcs():
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            t[i][j] = max((gap_open + s[i][j - 1]), (gap_extend + t[i][j - 1]))  # ,  (gap_open + b[i][j - 1]))
            b[i][j] = max((gap_open + s[i - 1][j]), (gap_extend + b[i - 1][j]))  # , (gap_open + t[i - 1][j]))
            s[i][j] = max(get_score(i - 1, j - 1) + s[i - 1][j - 1], t[i][j], b[i][j])
            dir_char = 'm' if str1[i - 1] == str2[j - 1] else 'f'
            best = max((dir_char, get_score(i - 1, j - 1) + s[i - 1][j - 1]), ('i', t[i][j]), ('d', b[i][j]),
                       key=lambda k: k[1])
            s[i][j] = best[1]
            direction[i][j] = best[0]


def print_lcs():
    m, n = len(str1), len(str2)

    out1 = ''
    out2 = ''
    while m > 0 or n > 0:
        if direction[m][n] == 'd':
            out1 = str1[m - 1] + out1
            out2 = '-' + out2
            m -= 1
        elif direction[m][n] == 'm' or direction[m][n] == 'f':
            out1 = str1[m - 1] + out1
            out2 = str2[n - 1] + out2
            m -= 1
            n -= 1
        else:
            out2 = str2[n - 1] + out2
            out1 = '-' + out1
            n -= 1
    print(out1)
    print(out2)


def init_matrices():
    for idx in range(1, len(str2) + 1):  # TODO ??
        direction[0][idx] = 'i'
    for idx in range(1, len(str1) + 1):
        direction[idx][0] = 'd'
    # init middle
    s[1:, 0] = -1e6
    s[0, 1:] = -1e6
    # init top
    t[1:, 0] = -1e6
    t[0, 1:] = gap_open
    for idx in range(2, len(str2) + 1):
        t[0][idx] += gap_extend * (idx - 1)
    # init bottom
    b[0, 1:] = -1e6
    b[1:, 0] = gap_open
    for idx in range(2, len(str1) + 1):
        b[idx][0] += gap_extend * (idx - 1)


gap_open = -11
gap_extend = -1
indices = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
BLOSUM62 = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
            [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
            [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
            [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
            [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
            [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
            [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
            [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
            [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
            [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
            [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
            [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
            [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
            [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
            [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
            [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
            [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
            [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
            [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
            [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]

if __name__ == '__main__':
    str1 = input()
    str2 = input()

    s = np.zeros((len(str1) + 1, len(str2) + 1))
    t = np.zeros((len(str1) + 1, len(str2) + 1))  # top
    b = np.zeros((len(str1) + 1, len(str2) + 1))  # bottom
    direction = [['-' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    init_matrices()

    lcs()
    print(int(s[len(str1)][len(str2)]))
    print_lcs()

    # for row in s:
    #     print('\t'.join(map(str, row)))
    # print()
    # for row in direction:
    #     print('\t'.join(row))