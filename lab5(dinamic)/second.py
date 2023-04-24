stuff = [5, 4, 6, 2, 7]

def matrix_brackets(mats):
    ln = len(mats)
    ans = [[-float('inf') for i in range(ln - 1)] for j in range(ln - 1)]
    table = [[float('inf') for i in range(ln-1)] for j in range(ln-1)]
    for i in range(ln - 1):
        table[i][i] = 0
    for loop in range(1, ln - 1):
        for i in range(ln - loop - 1):
            j = i + loop
            table[i][j] = float('inf')
            for k in range(i, j):
                new = min(table[i][j],
                                  table[i][k] + table[k+1][j] + mats[i]*mats[k+1]*mats[j+1])
                if new != table[i][j]:
                    ans[i][j] = max(k, ans[i][j])
                table[i][j] = new
    return table[0][ln - 2], ans


def print_parenthesization(s, start, end):
    if start == end:
        print('A[{}]'.format(start + 1), end='')
        return

    k = s[start][end]

    print('(', end='')
    print_parenthesization(s, start, k)
    print_parenthesization(s, k + 1, end)
    print(')', end='')


num, s = matrix_brackets(stuff)

print_parenthesization(s, 0, len(s[0])-1)