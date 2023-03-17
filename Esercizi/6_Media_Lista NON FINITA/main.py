def weighted_average(values, weights=[]):
    if not weights:
        weights = [1] * len(values)
    if len(values) != len(weights):
        raise Exception("Lenght of values and weights must be the same")


values = [2, 5, 4, 9, 12]

print(weighted_average(values, weights=0))
