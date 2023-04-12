n = 2**1000
str = str(n)
sum = 0
for i in range(len(str)):
    sum += int(str[i])
print(sum)