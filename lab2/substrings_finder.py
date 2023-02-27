import timeit

def fibonacci(a, b, i, s='1'):
    if i == 500:
        return s
    if i == 0:
        s += '1'
        return fibonacci(1, 1, i+1, s)
    else:
        s += str(a+b)
        return fibonacci(b, b+a, i+1, s)

def Rabin_Karp_Matcher(text, pattern, d=10, q=9973): # d - мощность алфавита
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q # значение на первой букве
    p = 0 # значение хэша в паттерне
    t = 0 # значение хэша в тексте
    result = 0
    for i in range(m): # прогон первой строки длинны паттерна в тексте
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result += 1
        if s < n-m:
            t = (t-h*ord(text[s]))%q # убрать s-ую букву
            t = (t*d+ord(text[s+m]))%q # добавить s+m-ую букву
            t = (t+q)%q # делаем t больше нуля
    return result

def Boyer_Moor_Matcher(a, t):
    res = 0
    s = set() # множество неповторяющихся символов
    m = len(t) # длинна образа
    n = len(a) # длинна данных
    d = {} # словарь со смещениями

    for i in range(m-2, -1, -1): # формирование смещений для всех элементов кроме последенего
        if t[i] not in s:
            d[t[i]] = m-i-1
            s.add(t[i])
    if t[m-1] not in s: # смещение для последенего элемента
        d[t[m-1]] = m
    d['*'] = m

    if n >= m:
        i = m-1
        while i < n:
            k = 0 # индекс для прохода сравнения
            flbreak = False
            for j in range(m-1, -1, -1):
                if a[i-k] != t[j]: # несовпадение
                    if j == m-1:
                        if d.get(a[i], False):
                            off = d[a[i]]
                        else:
                            off = d['*']
                    else:
                        off = d[t[j]]
                    i += off
                    flbreak = True
                    break
                k += 1
            if not flbreak: # если не встретилось несовпадений на строке, то найден шаблон
                res += 1
                i += m-1
    return res

def KMP_Match(a, t):
    p = [0] * len(t) # массив с максимальными значениями длинн префиксов
    m = len(t) # длинна строки шаблона
    n = len(a) #длинна строки данных
    res = 0
    j, i = 0, 1
    while i < len(t): # формирование массива пи
        if t[j] == t[i]:
            p[i] = j+1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j-1]
    i, j = 0, 0
    while i < n: # прооход по данным и сдвиги
        if a[i] == t[j]:
            i += 1
            j += 1
            if j == m:
                res += 1
                j = 0
        else:
            if j > 0:
                j = p[j-1] # если находится несовпадения сдвигаем на длинну максимального суффикса
            else:
                i += 1
                j = 0
    return res

def Naive(a, t):
    n = len(a)
    m = len(t)
    res = 0
    i = 0
    while i <= n-m:
        for j in range(m):
            if t[j] == a[i+j]:
                if j == m-1:
                    res += 1
            else:
                break
        i += 1
    return res

    
s = fibonacci(1, 1, 0)
res = {i: 0 for i in range(10, 100)}

timer1 = timeit.default_timer()
for i in range(10, 100):
    res[i] = Boyer_Moor_Matcher(s, str(i))
print('Time for Boyer-Moor: ' + str(timeit.default_timer() - timer1))
print(str(max(res, key=res.get)) + '\n')

timer2 = timeit.default_timer()
for i in range(10, 100):
    res[i] = Rabin_Karp_Matcher(s, str(i))
print('Time for Rabin-Karp: ' + str(timeit.default_timer() - timer2))
print(str(max(res, key=res.get)) + '\n')

timer3 = timeit.default_timer()
for i in range(10, 100):
    res[i] = KMP_Match(s, str(i))
print('Time for KMP: ' + str(timeit.default_timer() - timer3))
print(str(max(res, key=res.get)) + '\n')

timer4 = timeit.default_timer()
for i in range(10, 100):
    res[i] = Naive(s, str(i))
print('Time for Naive: ' + str(timeit.default_timer() - timer4))
print(str(max(res, key=res.get)) + '\n')
