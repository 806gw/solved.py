t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    for j in range(max(a, b), (a * b) + 1):
        if j % a == 0 and j % b == 0:
            print(j)
            break