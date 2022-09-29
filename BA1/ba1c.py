complements_dict = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
nucleotide = input()
print(''.join(complements_dict[i] for i in nucleotide[::-1]))