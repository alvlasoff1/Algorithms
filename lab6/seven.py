def find_missing(nums, mn):
    st = set(nums)
    i = mn
    while i in st:
        i += 1
    return i
print('Введите список чисел через пробел')
arr = list(map(int, input().split()))
print(find_missing(arr, min(arr)))
