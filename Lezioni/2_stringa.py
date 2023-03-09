table = "temperature;humidity;city\n16;80;Messina"
print(table)

separator = ';'
rows = table.splitlines()

for row in rows:
    cells = row.split(separator)
    print(cells)