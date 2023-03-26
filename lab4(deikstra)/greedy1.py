n = 77

m1, m2, m3, m4 = [10]*4
s1, s2, s3, s4 = (50, 10, 5, 1)

d = {s1: m1, s2: m2, s3: m3, s4: m4}
res = {s1: 0, s2: 0, s3: 0, s4: 0}

sorted_d = {i[0]: i[1] for i in sorted(d.items(), key=lambda x: x[0], reverse=True)}

for s in sorted_d:
    if n > 0:
        while n - s >= 0 and sorted_d[s] > 0:
            n -= s
            sorted_d[s] -= 1
            res[s] += 1
    else:
        break
print(res)