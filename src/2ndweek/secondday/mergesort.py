def mergesort(arr):
    if len(arr)==1:
        return arr

    mid = len(arr) //2

    left_half = arr[:mid]
    right_half= arr[mid:]

    left_sorted=mergesort(left_half)
    right_sorted =mergesort(right_half)

    i=j=0
    result =[]
    while i< len(left_sorted) and j< len(right_sorted):
        if left_sorted[i]< right_sorted[j]:
            result.append(left_sorted[i])
            i=i+1
        else:
            result.append(right_sorted[j])
            j=j+1
    result = result+ left_sorted[i:]
    result = result+right_sorted[j:]
    return result

print(mergesort([3,5,2,6,34,1]))