def array_operations(arr):
    product = 1
    sum = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            product *= arr[i]
        else:
            sum += arr[i]
    return product, sum


arr = [1, 2, 3, 4, 5, 6]
print(array_operations(arr))
