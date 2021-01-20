import sys

# importamos el fichero con el que vamos a trabajar
file = sys.argv[1]

# importamos el nombre de la carpeta de salida por pantalla
folder = sys.argv[2]

# abrir fichero para lectura
infile = open(file)

# ficheros de salida para los diferentes tipos de mutaciones
folder = folder.replace('\\','/')

file1 = folder + '/Mutations_I.tsv'
file2 = folder + '/Mutations_II.tsv'
file3 = folder + '/Mutations_III.tsv'
file4 = folder + '/Mutations_extra.tsv'

outfile1 = open(file1,"w") # tipo I/IV
outfile2 = open(file2,"w") # tipo II
outfile3 = open(file3,"w") # tipo III/V
outfile4 = open(file4,"w") # mutaciones que tienen nomenclatura extraña

# escribir nombres de las columnas
outfile1.write('Gene name'+'\t'+'Transcript ID'+'\t'+'Mutation CDS'+'\t'+'Chromosomic Position'+'\n')
outfile2.write('Gene name'+'\t'+'Transcript ID'+'\t'+'Mutation CDS'+'\t'+'Chromosomic Position'+'\n')
outfile3.write('Gene name'+'\t'+'Transcript ID'+'\t'+'Mutation CDS'+'\t'+'Chromosomic Position'+'\n')
outfile4.write('Gene name'+'\t'+'Transcript ID'+'\t'+'Mutation CDS'+'\t'+'Chromosomic Position'+'\n')

def RepresentsInt(s):
   try:
       int(s)
       return True
   except ValueError:
       return False

i = 1
# para cada linea del fichero
for line in infile:
    # quitamos el salto de línea y separamos las columnas delimitadas por tabuladores
    columns = line.strip('\n').split('\t')
    # tomamos el primer campo, que es el nombre del gen
    genname = columns[0]
    # tomamos el campo 2, que es el identidficador del transcrito
    transcript = columns[1]
    # tomamos el campo 20, que es la anotación
    anotation = columns[19]
    # tomamos el campo 26, que es la posición cromosómica
    position = columns[25]

    # si es un cambio de nucleótidos, tendrá '>'
    if '>' in anotation:
        # si empieza por 'c.-', no nos interesa
        if ('c.-' in anotation):
            # dejarla pasar
            continue
        # si no empieza por 'c.-'
        else:
            # si tiene '+' será mutación intrónica downstream
            if ('+' in anotation):
                # separamos por el '>' y tomamos la parte de la izquierda
                # separamos por el '+' y tomamos la parte de la derecha
                # nos desacemos de la letra caracter para quedarnos con el número
                number = anotation.split('>')[0].split('+')[1][:-1]
                
                if not RepresentsInt(number):
                   print ("Warning: " + number + 'in line' + str(i) + " not an integer.")
                   outfile4.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')
                   continue
                
                # si el número es mayor a 6
                if (int(number) > 6):
                    # será una variable deep intronic (tipo II)
                    outfile2.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')
                # si no
                else:
                    # será una variable intrónica cercana al exón (tipo I o IV)
                    outfile1.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')

            # si tiene tiene '-' será mutacion intrónica upstream
            elif ('-' in anotation):
                # separamos por el '>' y tomamos la parte de la izquierda
                # separamos por el '-' y tomamos la parte de la derecha
                # nos desacemos de la letra para quedarnos con el número
                number = anotation.split('>')[0].split('-')[1][:-1]
                
                if not RepresentsInt(number):
                   print ("Warning: " + number + 'in line' + str(i) + " not an integer.")
                   outfile4.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')
                   continue
                
                # si el número es mayor a 6
                if (int(number) > 6):
                    # será una variable deep intronic (tipo II)
                    outfile2.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')
                # si no
                else:
                    # será una variable intrónica cercana al exón (tipo I o IV)
                    outfile1.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')
                    
            # si no tiene ni '+' ni '-', será una mutación exónica
            else:
                # será una mutación de tipo III o IV
                outfile3.write(genname+'\t'+transcript+'\t'+anotation+'\t'+position+'\n')
    # si no es un cambio nucleotídico
    else:
        # dejar pasar la linea
        continue
    print(i)
    i+=1
