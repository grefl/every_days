
N = 100
i = 0
while i < N:
    c = ' '
    if i % 10 == 9 or i == N-1:
        c = '\n'
    print(f"{i:{' '}{6}}{c}", end='')
    i +=1
