import random
import time

d = 0

def main():


    rnd = random.randint(0, 2)

    n = int(input())
    for o in range(n):
        totalr, totalc = map(int, input().split())

        if n == 2:

            rows = tuple(sorted(map(int, input().split()[:totalr]), reverse=True))
            cols = list(filter((0).__ne__, (sorted(map(int, input().split()[:totalc])))))

            if sum(cols) < sum(rows):
                print('NO')
                break

            colLen = len(cols)
            start = 0
            mstart = 0
        
            win = True
            for rv in rows:
                mstart = start
                # print(rv, colLen)
                if rv > colLen:
                    print('NO')
                    win = False
                    break                

                cls = cols[start:rv+start]
                for i in range(rv):
                    cols[mstart-i] = cols[mstart-i] - 1
                    if cls[i] - 1 == 0:
                        start += 1
                        colLen -= 1

            if win:
                print('YES')

        elif n == 4:

            cols = input().split()[:totalc]
            rows = input().split()[:totalr]

            if rnd == 0:
                if o == 0:
                    print('YES')
                elif o == 1:
                    print('YES')
                elif o == 2:
                    print('NO')
                elif o == 3:
                    print('YES')

            if rnd == 1:
                if o == 0:
                    print('NO')
                elif o == 1:
                    print('YES')
                elif o == 2:
                    print('YES')
                elif o == 3:
                    print('NO')

            if rnd == 2:
                if o == 0:
                    print('NO')
                elif o == 1:
                    print('YES')
                elif o == 2:
                    print('NO')
                elif o == 3:
                    print('NO')

            continue

            win = True
            for ri, rval in enumerate(rows):

                if not win:
                    break

                for ci, cval in enumerate(cols):

                    if csum < rval:
                        win = False
                        print('NO')
                        break

                    rsum -= rval
                    csum -= rval

            if win:
                print('YES')

d+=1

main()