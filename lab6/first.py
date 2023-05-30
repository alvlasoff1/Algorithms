arr = [[1,1,2],
       [1,0,2],
       [2,1,1]]
def count_null():
    global arr
    k = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 0:
                k += 1
    return k
def correct_result():
    k1 = 0
    k2 = 0
    global arr
    for i in range(3):
        for j in range(3):
            if arr[i][j] == 1:
                k1 += 1
            if arr[i][j] == 2:
                k2 += 1
    neob_summ = 9 - count_null()
    if neob_summ % 2 == 0:
        if k1 == k2:
            return True
    if neob_summ % 2 != 0:
        if abs(k1 - k2) == 1:
            return True
    return False
    
def first():
    global arr
    if arr[0][0] == arr[0][1] == arr[0][2] == 1:
        return True
    if arr[1][0] == arr[1][1] == arr[1][2] == 1:
        return True
    if arr[2][0] == arr[2][1] == arr[2][2] == 1:
        return True
    if arr[0][0] == arr[1][1] == arr[2][2] == 1:
        return True
    return False
def second():
    global arr
    if arr[0][0] == arr[0][1] == arr[0][2] == 2:
        return True
    if arr[1][0] == arr[1][1] == arr[1][2] == 2:
        return True
    if arr[2][0] == arr[2][1] == arr[2][2] == 2:
        return True
    if arr[0][0] == arr[1][1] == arr[2][2] == 2:
        return True
    return False
def nichya():
    if not first() and not second() and count_null() == 0:
        return True
    return False
if correct_result():
    if first():
        print('Выиграл первый')
    elif second():
        print('Выиграл второй')
    elif nichya():
        print('Ничья')
    else:
        print('Игра не закончена')
else:
    print('Введен некорректный результат игры')
