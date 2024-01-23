def imperativ_sort(arr):
    N = len(arr)
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def declarativ_sort(arr):
    imperativ_sort(arr)


my_array = [1, 6, 3, 6, 8, 0, 3, 6, 2, 9]
my_array2 = [1, 6, 3, 6, 8, 0, 3, 6, 2, 9]

imperativ_sort(my_array)
print("Результат работы сортировки в императивном стиле")
print(my_array)

declarativ_sort(my_array2)
print("Результат работы сортировки в декларативном стиле")
print(my_array2)