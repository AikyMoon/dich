#coding:utf8

cache = {}
def can_win(a, b, depth):
    if (a, b) in cache.keys():
        return cache[(a, b)]

    if a+b >= 28:
        cache[(a, b)] = [False, [], 0, 0]
        return cache[(a, b)]

    wins = []

    a3b = can_win(a+3, b, depth + 1)
    if a3b[0] == False:
        wins.append([True, [f'(+3,) = ({a+3}, {b})'] + a3b[1], a3b[2] + 1, a3b[3] + 1])

    ab3 = can_win(a, b+3, depth + 1)
    if ab3[0] == False:
        wins.append([True, [f'(,+3) = ({a}, {b+3})'] + ab3[1], ab3[2] + 1, ab3[3] + 1])

    abb4 = can_win(a+4, b, depth + 1)
    if abb4[0] == False:
        wins.append([True, [f'(+4,) = ({a+4}, {b})'] + abb4[1], abb4[2] + 1, abb4[3] + 1])

    aab4 = can_win(a, b+4, depth + 1)
    if aab4[0] == False:
        wins.append([True, [f'(,+4) = ({a}, {b+4})'] + aab4[1], aab4[2] + 1, aab4[3] + 1])

    abb2 = can_win(a*2, b, depth + 1)
    if abb2[0] == False:
        wins.append([True, [f'(*2,) = ({a*2}, {b})'] + abb2[1], abb2[2] + 1, abb2[3] + 1])

    aab2 = can_win(a, b*2, depth + 1)
    if aab2[0] == False:
        wins.append([True, [f'(,*2) = ({a}, {b*2})'] + aab2[1], aab2[2] + 1, aab2[3] + 1])


    if len(wins) > 0:
        minlen_i = 0
        for i in range(len(wins)):
            if wins[minlen_i][2] > wins[i][2]:
                minlen_i = i
        cache[(a, b)] = wins[minlen_i]
        return cache[(a, b)]

    cache[(a, b)] = [False, [f'и даже если (+2,) = ({a+2},{b}), то будет ответ ', a3b[1],
                             f'и даже если (,+2) = ({a},{b+2}), то будет ответ ', ab3[1],
                             f'и даже если (+4,) = ({a+4},{b}), то будет ответ ', abb4[1],
                             f'и даже если (,+4) = ({a},{b+4}), то будет ответ ', aab4[1],
                            f'и даже если (*2,) = ({a*2},{b}), то будет ответ ', abb2[1],
                            f'и даже если (,*2) = ({a},{b*2}), то будет ответ ', aab2[1]],
                     min(a3b[2], ab3[2],aab4[2], abb4[2], aab2[2], abb2[2]) + 1,
                     max(a3b[3], ab3[3],aab4[3], abb4[3], aab2[3], abb2[3]) + 1]
    return cache[(a, b)]

for i in range(1, 24):
    print(i, can_win(i, 4, 0))
    #cache = {}
    print()
