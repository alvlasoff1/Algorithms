def div_hash(string):
    arr = string.split()
    l = len(arr)
    if l & (l-1) == 0: #проверка на степень двойки
        m = l + 1
    else:
        m = l
    key_len = len(str(m))
    keys = set()
    vals = {} #словарь с ключами
    res = ''
    for i in arr:
        val = 0
        for j in i:
            val += ord(j)
        val = val % m
        val = '0' * (key_len - len(str(val))) + str(val) #чтобы все ключи были одинаковой длинны
        vals[i] = val
        res += str(val)
    return res