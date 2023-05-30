def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def matrix_search(matrix: list, x: int):
    for i in range(len(matrix)):
        res = binary_search(matrix[i], x)
        if res != -1:
            return i, res
    return -1, -1

matrix = [[15, 20, 70, 85],
          [20, 35, 80, 95],
          [30, 55, 95, 105],
          [40, 80, 100, 120]]
print(matrix_search(matrix, 105))