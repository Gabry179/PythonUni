input_filename = r'Esercizi\3_Converti_Parole\input.txt'
output_filename = r'Esercizi\3_Converti_Parole\output.txt'

with open(input_filename, 'r') as f:
    lines = f.readlines()

text = ""
for word in lines:
    text += word.lower()

with open(output_filename, 'w') as f:
    f.write(text)