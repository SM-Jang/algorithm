def func2(arr, n):
    for i in range(n):
        target = 100-arr[i]
        for j in range(n):
            if target == arr[j] and j!=i:
                return 1
    return 0
