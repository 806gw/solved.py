H, M = input().split()  # Take input and split into two strings
H = int(H)  # Convert the first string to an integer
M = int(M)  # Convert the second string to an integer

timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24

print(H, M)