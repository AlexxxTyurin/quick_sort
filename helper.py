
def quick_sort(arr, left, right):
    if left >= right:
        return arr
    i = left
    j = right
    pivot = arr[(i + j) // 2]
    print(arr[left:right + 1], pivot)
    while i <= j:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j -= 1
    position = i
    print(arr)
    if len(arr[left:position]) > 1:
        quick_sort(arr, left, position-1)
    if len(arr[position:right+1]) > 1:
        quick_sort(arr, position, right)


ls = [1, 4, 9, 0, 7, 6, 2, 5, 9, 78, 90, 76, 34, 89, 25, 95, 100, 300, 56, 10, 0, 38, 10]
quick_sort(ls, 0, len(ls)-1)
print(ls)
