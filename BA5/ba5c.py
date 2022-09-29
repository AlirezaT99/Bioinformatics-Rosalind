str1 = input()
str2 = input()
s = [['' for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            s[i][j] = s[i-1][j-1] + str1[i - 1]
        else:
            s[i][j] = s[i][j-1] if len(s[i][j-1]) > len(s[i-1][j]) else s[i-1][j]
print(s[len(str1)][len(str2)])