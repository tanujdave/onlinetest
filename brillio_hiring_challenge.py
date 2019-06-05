lines = int(input())

extra_cols = ((lines * 2) - 1) - lines

l_triangle = int(extra_cols / 2)
r_triangle = (extra_cols % 2) + int(extra_cols / 2)

if l_triangle % 2 != 0:
    l_sum = l_triangle * (int(l_triangle / 2) + 1)
else:
    l_sum = (l_triangle * int(l_triangle / 2)) + int(l_triangle / 2)

if l_triangle == r_triangle:
    print(l_sum * 2)
else:
    if r_triangle % 2 != 0:
        r_sum = r_triangle * (int(r_triangle / 2) + 1)
    else:
        r_sum = (r_triangle * int(r_triangle / 2)) + int(r_triangle / 2)
    

    print(l_sum + r_sum)
