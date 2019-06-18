import  random
def quick_sort(arr, left, right):
    print(arr[left: right+1])
    pivot = arr[right]
    i = left
    j = right-1
    position = left
    changed = 0
    while i <= j:
        if arr[i] > pivot:
            changed = 1
            while j > i:
                if arr[j] <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    position = j
                    break
                j -= 1
        i += 1
    if changed == 0:
        position = right
    if changed == 1:
        arr[position], arr[right] = arr[right], arr[position]


    if len(arr[left:position]) > 1:
        quick_sort(arr, left, position-1)
    if len(arr[position:right]) > 1:
        quick_sort(arr, position+1, right)

    return arr, position



ls = [0, 8, 95, 87, 95, 34, 83, 7, 10, 65, 94, 99, 100]

print(quick_sort(ls, 0, 12))