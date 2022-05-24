rna = []
with open('miRNA_interactions.txt', 'r') as f:
    for line in f:
        rna += [line.rstrip().split("\t")]
dict = {'Gene.Symbol':'miRNA'}
for i in range(1,len(rna)):
    if rna[i][1] in dict.keys():
        if rna[i][4] not in dict[rna[i][1]]:
            dict[rna[i][1]].append(rna[i][4])
    else:
        dict[rna[i][1]] = [rna[i][4]]
print(dict)