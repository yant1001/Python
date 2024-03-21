# 03_function_2

## 함수와 스코프 (scope)
- `scope`: 범위 혹은 영역
- 지역 스코프(함수 스코프)는 함수가 종료되면 사라진다.
- 함수 내부가 아니면 모두 글로벌 영역에 위치해 있다.
- 전역 스코프와 지역 스코프에 같은 이름의 변수를 만들 수 있다.
- 종류:
  - 전역 스코프 (global scope): 코드 어디에서든 참조할 수 있는 공간
    - 전역 스코프에서 지역 스코프의 변수를 참조할 수 없다.
  - 지역 스코프 (local scope): 함수가 만든 스코프로 함수 내부에서만 참조할 수 있는 공간
    - 지역 스코프에서 전역 스코프의 변수를 참조할 수 있다.
  - 전역 변수 (global variable): 전역 스코프에 정의된 변수
  - 지역 변수 (local variable): 지역(로컬) 스코프에 정의된 변수
    - 기본적으로 지역 스코프에서 전역 스코프의 변수를 바꿀 수는 없으나, 아래와 같이 `선언 키워드`인 `global` `nonlocal`를 사용하면 가능하다. (권장X)
      ```python
      a = 10
      b - 20

      def func():
        global a
        a = 100
        b = 200
        print(a, b)

      func()
      print(a, b)
      ```
- 특징:
    1. 코드가 함수 정의 외부에 있다. == global
    2. 코드가 함수 정의 내부에 있다. == local
    3. 함수는 호출하면 scope를 만들며, 종료되면 scope는 사라진다.
    4. local => global 참조는 가능하다. 반대는 불가능
    5. local과 global에 같은 이름(변수, 함수 등)이 있다면, 함수 내부에서는 local을 더 우선시 한다.
---
**예시**
```python
a = 10
def func(b):
    c = 20
    print(a, b, c)

# a = 전역 변수 (글로벌)
# b, c = 지역 변수 (로컬)
```
- 변수의 수명주기 (life cycle)
  - 종류:
    - 빌트인 스코프 (built-in scope): 파이썬이 실행된 이후부터 영원히 유지
    - 전역 스코프 (global scope): 모듈이 호출된 시점 이후 혹은 이름이 선언된  이후부터 인터프리터가 끝날 때까지 유지
        - cf. `interpreter`: 코드를 한 줄씩 읽어 내려가며 실행하는 프로그램
    - 지역(함수) 스코프 (local scope): 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지 (함수 내에서 처리되지 않은 예외를 일으킬 때 삭제됨)
    - 참고:
      - 안 만들었는데 쓸 수 있는 것 = 빌트인
      - 만들었는데 함수 밖에 있는 것 = 글로벌
      - 만들었는데 함수 안에 있는 것 = 로컬


  - 이름 검색 (resolution) 규칙
    - 이름(식별자)들은, 파이썬 예약어를 제외, 우리가 지정했고 바꿀 수 있는 것들을 의미한다.
    - 파이썬에서 사용되는 이름(식별자)들은 이름 공간(name space)에 저장되어 있으며, 아래와 같은 순서로 이름을 찾아나간다.
    - LEGB Rule:
      1. Local scope: 함수
      2. Enclosed scope: 특정 함수의 상위 함수
      3. Global scope: 함수 밖의 변수 혹은 import된 모듈
      4. Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성

## 재귀 함수 (Recursive Function)
- 함수 내부에서 자기 자신을 호출하는 함수
- 팩토리얼 계산
  - 반복문을 이용한 팩토리얼 계산
    ```python
    def fact(n):
      result = 1
      while n > 1:
        result *= n
        n -= 1
      
      return result
    
    fact(5)  # 결과값: 120

    # n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소한다. n이 1이 되면 반복문이 더 이상 돌지 않는다.
    ```
  - 재귀를 이용한 팩토리얼 계산
    ```python
    def factorial(n):
      if n == 1:
        return 1
      return n * factorial(n-1)

    factorial(5)  # 결과값: 120

    # 재귀 함수를 호출하며, n은 1씩 감소한다. n이 1이 되면 추가 함수를 더 이상 호출하지 않는다.
    ```
  - 재귀함수를 작성할 때는 반드시, 점점 범위가 줄어들어 반복되지 않고 최종적으로 도달하게 되는 `base case`가 존재해야 한다.
    - ex. n이 1일 때, 함수가 아닌 정수를 반환하는 `base case`
  - 알고리즘 구현 시 많이 사용되나, 함수가 호출될 때마다 메모리 공간이 쌓이기 때문에 프로그램 실행 속도가 늘어지는 단점이 발생한다. (stack overflow)
    - 이를 방지하기 위해, 파이썬에서는 1,000번이 넘어가면 더 이상 함수를 호출하지 않고 종료한다. (최대 재귀 깊이, RecursionError)
  - 피보나치 수열
    - 재귀를 사용하는 대표적인 방식이다.
    - 첫째 및 둘째 항이 1이며, 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열 (1, 1, 2, 3, 5, 8 ...)
    - 피보나치 수열을 리턴하는 두 가지 방식
      - 재귀함수 `fib(n)`
        ```python
        def fib(n):
          if n == 0:
            return 0
          elif n == 1:
            return 1
          else:
            return fib(n-1) + fib(n-2)

        fib(10)  # 결과값: 55

        # fib(10)에서 시작해서 fib(0)까지 갔다가, 주어진 fib(0), fib(1) 값과 연산식들을 이용해 다시 fib(10)까지 구해 올라온다.
        ```
      - 반복문을 활용한 함수 `fib_loop(n)`
        ```python
        # for문 이용
        def fib_loop(n):
          result = [0, 1]
          for _ in range(n-1):
            result.append(result[-1] + result[-2])
          return result[n]

        fib_loop(10)  # 결과값: 55

        # result[-1]+result[-2]는 현존하는 result list의 뒤에서 첫째, 둘째 항의 합을 list에 더해주는 방식이다.
        ```
        ```python
        # while문 이용
        def fib_loop2(n):
          a, b = 0, 1
          while n > 1:
            a, b = b, a+b
            n -= 1
          return b

        fib_loop2(10)  # 결과값: 55
        ```
  - 반복문과 재귀 함수의 차이
    - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용한다.
    - 재귀 호출은 `변수 사용`을 줄여줄 수 있으나, 입력 값이 커질수록 연산 속도가 오래 걸린다는 단점이 있다.
    - 반복문은 재귀로 구현된 함수보다 연산 속도가 빠른 편이다.