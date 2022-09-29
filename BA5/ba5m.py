import numpy as np


def score(x, y, z):
    return int(x == y and y == z and x != '-')


def msa():
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            for k in range(1, len(str3) + 1):
                best_move = max(
                    ((0, 0, -1), s[i][j][k - 1] + score('-', '-', str3[k - 1])),
                    ((0, -1, 0), s[i][j - 1][k] + score('-', str2[j - 1], '-')),
                    ((0, -1, -1), s[i][j - 1][k - 1] + score('-', str2[j - 1], str3[k - 1])),
                    ((-1, 0, 0), s[i - 1][j][k] + score(str1[i - 1], '-', '-')),
                    ((-1, 0, -1), s[i - 1][j][k - 1] + score(str1[i - 1], '-', str3[k - 1])),
                    ((-1, -1, 0), s[i - 1][j - 1][k] + score(str1[i - 1], str2[j - 1], '-')),
                    ((-1, -1, -1), s[i - 1][j - 1][k - 1] + score(str1[i - 1], str2[j - 1], str3[k - 1])),
                    key=lambda m: m[1]
                )
                s[i][j][k] = best_move[1]
                direction[(i, j, k)] = best_move[0]


def print_msa():
    x, y, z = len(str1), len(str2), len(str3)

    out1 = ''
    out2 = ''
    out3 = ''

    while x > 0 and y > 0 and z > 0:
        dx, dy, dz = direction[(x, y, z)]
        x += dx
        y += dy
        z += dz
        if dy == 0 and dz == 0:
            out1 = str1[x] + out1
            out2 = '-' + out2
            out3 = '-' + out3
        elif dx == 0 and dz == 0:
            out1 = '-' + out1
            out2 = str2[y] + out2
            out3 = '-' + out3
        elif dx == 0 and dy == 0:
            out1 = '-' + out1
            out2 = '-' + out2
            out3 = str3[z] + out3
        elif dx == 0:
            out1 = '-' + out1
            out2 = str2[y] + out2
            out3 = str3[z] + out3
        elif dy == 0:
            out1 = str1[x] + out1
            out2 = '-' + out2
            out3 = str3[z] + out3
        elif dz == 0:
            out1 = str1[x] + out1
            out2 = str2[y] + out2
            out3 = '-' + out3
        else:
            out1 = str1[x] + out1
            out2 = str2[y] + out2
            out3 = str3[z] + out3
    while x > 0:
        x -= 1
        out1 = str1[x] + out1
        out2 = '-' + out2
        out3 = '-' + out3
    while y > 0:
        y -= 1
        out1 = '-' + out1
        out2 = str2[y] + out2
        out3 = '-' + out3
    while z > 0:
        z -= 1
        out1 = '-' + out1
        out2 = '-' + out2
        out3 = str3[z] + out3

    print(out1)
    print(out2)
    print(out3)


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    str3 = input()

    s = [np.zeros((len(str2) + 1, len(str3) + 1)) for _ in range(len(str1) + 1)]
    direction = dict()

    msa()
    print(int(s[len(str1)][len(str2)][len(str3)]))
    print_msa()