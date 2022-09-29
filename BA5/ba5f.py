import numpy as np


def lcs():
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            dir_char = 'm' if str1[i - 1] == str2[j - 1] else 'f'
            move1 = (dir_char, s[i - 1][j - 1] + PAM250[indices.index(str1[i - 1])][indices.index(str2[j - 1])])
            move2, move3 = ('i', s[i][j - 1] - 5), ('d', s[i - 1][j] - 5)
            move4 = ('t', 0)
            best = max(move1, move2, move3, move4, key=lambda k: k[1])
            s[i][j] = best[1]
            direction[i][j] = best[0]


def print_lcs():
    max_idx = np.argmax(s)
    m, n = (max_idx // s.shape[1]), (max_idx % s.shape[1])

    out1 = ''
    out2 = ''
    while m > 0 or n > 0:
        if direction[m][n] == 't':
            break
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


str1 = input()
str2 = input()
# s = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
s = np.zeros((len(str1) + 1, len(str2) + 1))
direction = [['-' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
for idx in range(1, len(str2) + 1):
    direction[0][idx] = 't'
    s[0][idx] = 0
for idx in range(1, len(str1) + 1):
    direction[idx][0] = 't'
    s[idx][0] = 0

indices = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
PAM250 = [[2, -2, 0, 0, -3, 1, -1, -1, -1, -2, -1, 0, 1, 0, -2, 1, 1, 0, -6, -3],
          [-2, 12, -5, -5, -4, -3, -3, -2, -5, -6, -5, -4, -3, -5, -4, 0, -2, -2, -8, 0],
          [0, -5, 4, 3, -6, 1, 1, -2, 0, -4, -3, 2, -1, 2, -1, 0, 0, -2, -7, -4],
          [0, -5, 3, 4, -5, 0, 1, -2, 0, -3, -2, 1, -1, 2, -1, 0, 0, -2, -7, -4],
          [-3, -4, -6, -5, 9, -5, -2, 1, -5, 2, 0, -3, -5, -5, -4, -3, -3, -1, 0, 7],
          [1, -3, 1, 0, -5, 5, -2, -3, -2, -4, -3, 0, 0, -1, -3, 1, 0, -1, -7, -5],
          [-1, -3, 1, 1, -2, -2, 6, -2, 0, -2, -2, 2, 0, 3, 2, -1, -1, -2, -3, 0],
          [-1, -2, -2, -2, 1, -3, -2, 5, -2, 2, 2, -2, -2, -2, -2, -1, 0, 4, -5, -1],
          [-1, -5, 0, 0, -5, -2, 0, -2, 5, -3, 0, 1, -1, 1, 3, 0, 0, -2, -3, -4],
          [-2, -6, -4, -3, 2, -4, -2, 2, -3, 6, 4, -3, -3, -2, -3, -3, -2, 2, -2, -1],
          [-1, -5, -3, -2, 0, -3, -2, 2, 0, 4, 6, -2, -2, -1, 0, -2, -1, 2, -4, -2],
          [0, -4, 2, 1, -3, 0, 2, -2, 1, -3, -2, 2, 0, 1, 0, 1, 0, -2, -4, -2],
          [1, -3, -1, -1, -5, 0, 0, -2, -1, -3, -2, 0, 6, 0, 0, 1, 0, -1, -6, -5],
          [0, -5, 2, 2, -5, -1, 3, -2, 1, -2, -1, 1, 0, 4, 1, -1, -1, -2, -5, -4],
          [-2, -4, -1, -1, -4, -3, 2, -2, 3, -3, 0, 0, 0, 1, 6, 0, -1, -2, 2, -4],
          [1, 0, 0, 0, -3, 1, -1, -1, 0, -3, -2, 1, 1, -1, 0, 2, 1, -1, -2, -3],
          [1, -2, 0, 0, -3, 0, -1, 0, 0, -2, -1, 0, 0, -1, -1, 1, 3, 0, -5, -3],
          [0, -2, -2, -2, -1, -1, -2, 4, -2, 2, 2, -2, -1, -2, -2, -1, 0, 4, -6, -2],
          [-6, -8, -7, -7, 0, -7, -3, -5, -3, -2, -4, -4, -6, -5, 2, -2, -5, -6, 17, 0],
          [-3, 0, -4, -4, 7, -5, 0, -1, -4, -1, -2, -2, -5, -4, -4, -3, -3, -2, 0, 10]]

lcs()
print(int(np.max(s)))

# for row in s:
#     print('\t'.join(map(str, row)))
# print()
# for row in direction:
#     print('\t'.join(row))

print_lcs()