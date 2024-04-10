import sys
input = sys.stdin.readline # 반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.

n = int(input())
arr = []

for i in range(n):
    N = int(input())
    arr.append(N)

for j in sorted(arr):
    print(j)