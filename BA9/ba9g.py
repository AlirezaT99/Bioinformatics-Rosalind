text = input()
suffixes = [(i, text[i:]) for i in range(len(text))]
print(', '.join(str(item[0]) for item in sorted(suffixes, key=lambda k: k[1])))