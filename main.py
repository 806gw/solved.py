s = input()
a = int(input())
found = False  # 발견 여부를 나타내는 변수

for i in range(a):
    b = input()
    c = input()
    if b + c == s:
        print("1")
        found = True
        break

if not found:  # 발견하지 못한 경우에만 실행됨
    print("0")
