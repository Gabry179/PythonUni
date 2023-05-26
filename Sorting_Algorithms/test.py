from random import randint

def insertion_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while lista[j-1] > lista[j] and j > 0:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
    return lista

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
        return arr
    
def quicksort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    pivot=array[randint(0, len(array)-1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
        
    return quicksort(low) + same + quicksort(high)

def main():
    list = [5, 4, 6, 2, 7, 1]
    print(insertion_sort(list))
    print(merge_sort(list))
    print(quicksort(list))

if __name__ == "__main__":
    main()