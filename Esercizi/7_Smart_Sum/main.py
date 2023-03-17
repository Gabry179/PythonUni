def smart_sum(list):
    sum = 0
    for i in list:
        try:
            sum += i
        except TypeError:
            print("Il valore inserito non e' un numero")
    return sum

list = [2, 5, 3]
print(smart_sum(list))