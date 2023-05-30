def conflict(place, pos):
    if pos in place:
        return True
    else:
        forbidden = []
        rows = len(place)
        for i in range(rows):
            r_d = place[i]+(rows-i)
            if r_d <= 7:
                forbidden.append(r_d)
            l_d = place[i]-(rows-i)
            if l_d >= 0:
                forbidden.append(l_d)
        if pos in forbidden:
            return True
    return False
    
def generator(size=8, place=()):
    for pos in range(size):
        if not conflict(place, pos):
            if len(place)==size-1:
                yield (pos,)
            else:
                for result in generator(size, place+(pos,)):
                    yield (pos,)+result

for i in list(generator()):
    print(i)