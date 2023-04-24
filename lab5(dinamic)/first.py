def take(k, things):
    table = []
    maximum = 0
    res = ''
    for _ in range(len(things)):
        table.append([[0, '']]*(k+1))
    first = list(things.keys())[0]
    for i in range(1, k+1):
        if k - things[first][0] >= 0:
            table[0][i] = [things[first][1], first]
            if table[0][i][0] > maximum:
                res = table[0][i][1]
    for i, item in enumerate(list(things.keys())[1:], start=1):
        for j in range(1, k+1):
            if i == 2 and j == 3:
                pass
            free = j - things[item][0]
            if free >= 0:
                if table[i-1][j][0] >= things[item][1] + table[i-1][free][0]:
                    table[i][j] = table[i-1][j]
                elif table[i-1][j][0] < things[item][1] + table[i-1][free][0]:
                    table[i][j] = [things[item][1] + table[i-1][free][0], table[i-1][free][1] + ' ' + item]
            else:
                table[i][j] = table[i-1][j]
            if table[i][j][0] > maximum:
                res = table[i][j][1]
    return res
k = 4 # емкость рюкзака
things = {'Гитара': (1, 1500), 'Магнитофон': (4, 3000), 'Ноутбук': (3, 2000)}
kthings = {'Гитара': (1, 1500), 'Магнитофон': (4, 3000), 'Ноутбук': (3, 2000)}
m = 2
n = 2
d = float('inf')
overall = []
for i in range(m):
    taken = take(k, things).split()
    for j in taken:
        del things[j]
    overall += taken
    if n - len(overall) < 0:
        while n - len(overall) < 0:
            for el in overall:
                if kthings[el][1] < d:
                    d = kthings[el][1]
                    el_d = el
            overall.remove(el_d)
            d = float('inf')
        break
print(overall)