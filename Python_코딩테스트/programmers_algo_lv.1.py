# [해시] 폰켓몬
# n/2개를 선택 가능합니다. 즉 선택할 수 있는 기회를 설정하는 단계입니다.
# 선택할 때 종을 최대한 다앙하게 선택해야 합니다. 종류의 수이므로 중복을 취급하지 않습니다.(set)
# 선택 기회(n/2))가 종의 수보다 크면 종의 수만큼 선택, 종의 수보다 작다면 n/2를 출력합니다.
def solution(nums):
    answer = min(len(nums)//2, len(set(nums)))
    return answer


# [정렬] K번째수
def solution(array, commands):
    answer = []
    for a, b, c in commands:
        tmp_arr = array[a-1:b]
        tmp_arr.sort()
        answer.append(tmp_arr[c-1])
    return answer


# [완전탐색] 최소직사각형
# 두 개의 모서리를 비교하여 큰 값은 전부 가로, 작은 값은 전부 세로로 두고 가장 큰 값을 곱하기
def solution(sizes):
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(max(sizes[i]))
        height.append(min(sizes[i]))
    answer = max(width)*max(height)
    return answer


# [스택/큐] 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for i in range(len(arr)):
        if answer[-1] != arr[i]:
            answer += [arr[i]]
    return answer