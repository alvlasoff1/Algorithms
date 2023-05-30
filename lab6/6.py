def filter(data, alpha):
    s = [0]*(len(data)+1)
    s[0] = data[0]
    for i in range(1, len(s)):
        s[i] = s[i-1] + alpha*(data[i-1] - s[i-1])
    return s
data = [1, 3, 4, 6, 5, 7, 9, 11]
print('Измерения: ', data)
print('Экспоненциальное сглаживание: ', filter(data, 0.5)[1:])