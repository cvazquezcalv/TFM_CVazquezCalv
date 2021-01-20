import random

random.seed()

random_lines = random.choices(open('Mutations_III.tsv').readlines(),k=29)

outfile=open('MutationsIII_sample.tsv','w')
outfile.write('Gene name'+'\t'+'Transcript ID'+'\t'+'Mutation CDS'+'\t'+'Chromosomic Position'+'\n')

for i in random_lines:
    outfile.write(i)
    print(i)

outfile.close()

