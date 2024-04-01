T = input()
T = int(T)

for case in range(T) :
    A, B = input().split()
    A = int(A)
    B = int(B)
    print("Case #" + str(case+1) + ": " + str(A) + " + " + str(B) + " = " + str(A + B))