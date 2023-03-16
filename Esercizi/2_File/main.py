#Leggere il file input2.txt che contiene i seguenti numeri floating point:
# 32.0
# 54.0
# 67.5
# 80.25
# 115.0
# Calcolare il valor medio e la somma e scrivere i numeri dati, il valor medio e la somma
# sul file output.txt

input_filename = r'Esercizi\2_File\input2.txt'
output_filename = r'Esercizi\2_File\output.txt'

with open(input_filename, 'r') as f:
    lines = f.readlines()

summation = 0
for line in lines:
    summation += float(line)
mean = summation / len(lines)

with open(output_filename, 'w') as f:
    f.write("%s,%s" % (summation,mean))