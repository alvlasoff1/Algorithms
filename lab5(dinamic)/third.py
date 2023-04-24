print("Введите элементы массива через пробел")
arr = list(map(int, input().split()))
n = len(arr)
vsp = [0] * n
answer = 0
for chislo in arr:
    i, j = 0, answer
    while i != j:
        m = (i + j) // 2
        if vsp[m] < chislo:
            i = m + 1
        else:
            j = m
    vsp[i] = chislo
    answer = max(i + 1, answer)
print(answer)