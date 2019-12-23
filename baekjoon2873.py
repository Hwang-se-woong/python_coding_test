import sys
sys.setrecursionlimit(10**6)


def read(): return sys.stdin.readline().strip()


n, m = map(int, read().split())
q = []
matrix = [list(map(int, read().split())) for _ in range(m)]
check = [[False for i in range(n)] for j in range(m)]

x = 0
y = 0
dir = 1
if(m % 2 == 1):
    while(True):
        if(x == n - 1 and y == m - 1):
            break

        if(x != n - 1 and dir == 1):
            x += dir
            print('(', x, ',', y, ')')
            q.append('D')
        elif(x == n - 1 and dir == 1):
            y += 1
            dir = dir * -1
            print('(', x, ',', y, ')')
            q.append('R')
        elif(x != 0 and dir == -1):
            x += dir
            print('(', x, ',', y, ')')
            q.append('U')
        elif(x == 0 and dir == -1):
            y += 1
            dir = dir * -1
            print('(', x, ',', y, ')')
            q.append('R')


print(q)

for i in range(n):
    for j in range(m):
        print('matrix[', i, '][', j, '] = ', matrix[i][j])
