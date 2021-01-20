import random

random.seed()

random_lines = random.choices(open('Mutations_I.tsv').readlines(),k=29)

outfile=open('MutationsI_sample.tsv','w')
outfile.write('Gene name'+'\t'+'Transcript ID'+'\t'+'Mutation CDS'+'\t'+'Chromosomic Position'+'\n')

for i in random_lines:
    outfile.write(i)
    print(i)

outfile.close()

