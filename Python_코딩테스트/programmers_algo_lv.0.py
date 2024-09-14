# 숫자 비교하기
def solution(num1, num2):
    if num1 != num2:
        answer = -1
    else:
        answer = 1
    return answer


# 나이 출력
def solution(age):
    answer = 2022 - age + 1
    return answer


# 두 수의 차
def solution(num1, num2):
    answer = num1 - num2
    return answer


# 몫 구하기
def solution(num1, num2):
    answer = num1 // num2
    return answer


# 나머지 구하기
def solution(num1, num2):
    answer = num1 % num2
    return answer


# 두 수의 곱
def solution(num1, num2):
    answer = num1 * num2
    return answer


# 두 수의 나눗셈
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer


# 각도기
def solution(angle):
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer


# 짝수의 합
def solution(n):
    answer = 0
    for i in range(0, n+1, 2):
        answer += i
    return answer


# 두 수의 합
def solution(num1, num2):
    answer = num1 + num2
    return answer