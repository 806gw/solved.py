import sys

n = int(input())
arr = []

N = input().split()

for i in N:
    arr.append(int(i))
print(max(arr) - min(arr))