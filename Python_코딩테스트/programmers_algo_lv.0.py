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


# 배열의 평균값
def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer


# 삼각형의 완성조건(1)
def solution(sides):
    if max(sides) < (sum(sides) - max(sides)):
        answer = 1
    else:
        answer = 2
    return answer


# 중복된 숫자 개수
def solution(array, n):
    list = []
    for i in array:
        if i == n:
            list.append(i)
    answer = len(list)
    return answer


# 머쓱이보다 키 큰 사람
def solution(array, height):
    list = []
    for i in array:
        if i > height:
            list.append(i)
    answer = len(list)
    return answer


# 배열 두배 만들기
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(num*2)
    return answer


# 중앙값 구하기
import math

def solution(array):
    array.sort()
    center = math.trunc(len(array)/2)
    answer = array[center]
    return answer


# 짝수는 싫어요
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer


# 피자 나눠 먹기 (1)
def solution(n):
    if n >= 7:
        answer = n // 7
        if n % 7 != 0:
            answer = (n // 7) + 1
    else:
        answer = 1
    return answer


# 옷가게 할인 받기
def solution(price):
    if price >= 500000:
        answer = price * (1 - 0.2)
    elif price >= 300000:
        answer = price * (1 - 0.1)
    elif price >= 100000:
        answer = price * (1 - 0.05)
    else:
        answer = price
    return int(answer)


# 아이스 아메리카노
def solution(money):
    answer = []
    if money >= 5500:
        answer.append(money // 5500)
        answer.append(money % 5500)
    else:
        answer.append(0)
        answer.append(money)
    return answer


# 개미 군단
def solution(hp):
    answer = 0
    if hp >= 5:
        if hp % 5 == 0:
            answer = hp // 5
        elif hp % 5 <= 2:
            answer = (hp // 5) + (hp % 5)
        elif hp % 5 == 3:
            answer = (hp // 5) + 1
        elif hp % 5 == 4:
            answer = (hp // 5) + 2
    else:
        if hp % 3 == 0:
            answer = hp // 3
        else:
            answer = (hp // 3) + (hp % 3)
    return answer