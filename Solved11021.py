# 테스트 케이스의 개수를 입력받음
T = input()
T = int(T)

# 테스트 케이스 개수만큼 반복
for case in range(T):
    # 각 테스트 케이스에서 A와 B를 공백을 기준으로 입력받음
    A, B = input().split()
    # 입력받은 문자열을 정수로 변환
    A = int(A)
    B = int(B)
    # 현재 테스트 케이스 번호를 나타내는 문자열과 A와 B를 더한 값을 출력   x
    print("Case #" + str(case+1) + ": " + str(A + B))

# 숫자 자료형 변수와 문자열 자료형 변수는 +를 이용한 연산이 되지 않음.
# 이 경우에는 str()을 이용해 정수형 자료형을 문자열 자료형으로 변환 시켜서 출력해야함