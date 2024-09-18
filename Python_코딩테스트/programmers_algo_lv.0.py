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


# 양꼬치
def solution(n, k):
    if n < 10:
        answer = (n*12000) + (k*2000)
    else:
        answer = (n*12000) + (k*2000) - (n//10)*2000
    return answer


# 양꼬치
def solution(n, k):
    if n < 10:
        answer = (n*12000) + (k*2000)
    else:
        answer = (n*12000) + (k*2000) - (n//10)*2000
    return answer


# 세균 증식
def solution(n, t):
    for i in range(1, t+1):
        n *= 2
    return n


# 편지
def solution(message):
    answer = len(message)*2
    return answer


# 피자 나눠 먹기 (3)
def solution(slice, n):
    if slice <= n:
        answer = n // slice
        if (n % slice) != 0:
            answer += 1
    else:
        answer = 1
    return answer


# 짝수 홀수 개수
def solution(num_list):
    e = 0
    o = 0
    for num in num_list:
        if num % 2 == 0:
            e += 1
        else:
            o += 1
        answer = [e, o]
    return answer


# 제곱수 판별하기
def solution(n):
    i = n**(1/2)
    if i % 1 == 0:
        answer = 1
    else:
        answer = 2
    return answer