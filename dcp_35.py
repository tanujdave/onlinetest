S = list(['B','B','G','B','R','G', 'R','B','R','G','R', 'B', 'B', 'B', 'R', 'R', 'G', 'G', 'R', 'B', 'R', 'B'])
v = 0

def moveEl(idx, i, v):
    v = v + 1
    if 'R' == i:
        del S[idx]
        S.insert(0, i)
        if 'R' == S[idx] or 'B' == S[idx]:
            moveEl(idx, S[idx], v)

    if 'B' == i:
        del S[idx]
        S.insert(len(S), i)        
        if 'R' == S[idx] or ('B' == S[idx] and idx != v):
            moveEl(idx, S[idx], v)

for idx, i in enumerate(S):
    moveEl(idx, i, v)

print(S)