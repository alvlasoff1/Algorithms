print('Введите количество ступенек')
n = int(input())
arr = [1, 1, 2] + [0]*(n-2)
for i in range(3,n+1):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
print(arr)
print(arr[n])
    
