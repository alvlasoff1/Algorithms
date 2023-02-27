f = open('D:\\ИТМО\\АЛГОСЫ\\Весна\\lab2\\wiki.txt', 'r', encoding='utf-8')
wiki = (list(map(lambda x: x.replace('\n', ' '), f.readlines())))
wikistr = ''
for i in wiki:
    wikistr += str(i)
f.close()
f = open('D:\\ИТМО\\АЛГОСЫ\\Весна\\lab2\\not_wiki.txt', 'r', encoding='utf-8')
doc = (list(map(lambda x: x.replace('\n', ' '), f.readlines())))
docstr = ''
for i in doc:
    docstr += str(i)
f.close()

for i in ['-', '—', '.', ',', '\t']:
    wikistr.replace(i, '')
    docstr.replace(i, '')

wikistr.lower()
docstr.lower()

wiki = wikistr.split()
doc = docstr.split()

def Match(a, t):
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
                return True
        else:
            if j > 0:
                j = p[j-1] # если находится несовпадения сдвигаем на длинну максимального суффикса
            else:
                i += 1
                j = 0
    return False

i = 0
l = 3
symbols_in_text = 19716

symbols = 0
while i < len(doc):
    while True:
        k = doc[i:i+l]
        if Match(wiki, doc[i:i+l]):
            l += 1
        else:
            break
    if l != 3:
        for j in doc[i:i+l]:
            symbols += len(j)
        i += l
        l = 3
    else:
        i += 1

print('Процентное содержание плагиата: {}'.format((symbols/symbols_in_text) * 100))