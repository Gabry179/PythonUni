def merge_sort(arr):
    if len(arr) > 1:
        # Splitting the array in half
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # Recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge
        i = 0 # left_arr index
        j = 0 # right_arr index
        k = 0 # merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k+=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
        return arr

list = [5, 4, 6, 2, 7, 1]
print(merge_sort(list))