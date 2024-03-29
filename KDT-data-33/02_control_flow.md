# 02_control_flow

## 제어문 (Control Statement)
1. 조건문
- `if`: 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용해야 한다.

    ```python
    if num % 2:
        print('홀수입니다.')
    else:
        print('짝수입니다.')
    ```
- `num % 2` 자리에는 일반적으로 참/거짓에 대한 조건식이 들어간다.
- 조건이 복수인 경우 `elif` 부를 사용한다.
  - 여러 개의 조건일 때는 위에서부터 순차적으로 조건이 검증되므로 순서에 유의해야 한다.
- 조건이 거짓인 경우 `else` 부를 선택적으로 사용한다.
- 조건문은 다른 조건문에 중첩될 수도 있다.
    ```python
    if money:
        print('부자')
        if time:
            print('금수저')
        else:
            print('자수성가')
    ```
- 조건 표현식(삼항 연산자)으로 활용 가능하다.
  - ex. `true_value if <조건식> else false_value`
  - ()항 연산자
    - 1항(단항) 연산자: `-3`
    - 2항 연산자: `1 + 2`
    - 3항 연산자: `1 if 2 else 3`
      - 상기 3항 연산자의 경우 `2`는 비어있거나 없는 값이 아니므로 `True`에 가깝기 때문에 결과값은 1이 된다.
  - 삼항 연산자 작성 방법
    1. <조건식> 양 옆에 if, else를 작성한다.
    2. 왼쪽 if 작성 후 True 일 때 도출하고 싶은 값을 작성한다.
    3. 오른쪽 else 작성 후 False 일 때 도출하고 싶은 값을 작성한다.
    4. <조건식>을 중심으로 퍼져나간다.
        ```python
        num = -5

        # if 문
        if num >= 0:
            value = num
        else:
            value = 0

        # 조건 표현식 (삼항 연산자)
        value = num if num >= 0 else 0
        ```

2. 반복문 (Loop Statement)
- `while` 반복문
  - 문법
    ```python
    while <조건식>:
        <코드 블럭>
    ```
  - 반복문의 수동 version 느낌
  - 조건식이 `True`인 경우 반복적으로 코드를 실행한다.
  - 반드시 종료 조건을 설정해야 한다.
  - 1부터 10까지 총합을 구하는 방법
    ```python
    num = 0
    total = 0

    while num <= 10:
        total += num
        num += 1
    print(total)
    ```
- `for` 문
  - 문법
    ```python
    for <임시변수> in <순회 가능한 데이터(iterable)>:
        <코드 블럭>
    ```
  - 반복문의 자동 version 느낌
  - 시퀀스(`string`, `tuple`, `list`, `range`)를 포함한 순회 가능한 객체(iterable)의 요소들을 순회한다.
  - `임시변수`란 `순회 가능한 데이터` 안의 수들이 돌아가면서 임시변수 자리에 자동으로 하나씩 적용되는 변수를 의미한다.
  - `순회 가능한 데이터`란 `container` 모두, 정확히는 `iterable`한 데이터, 순서가 있으면서 반복할 수 있는 변경 가능한 것(`str`, `list` 등)을 의미한다.
  - `str` 및 `list`의 요소들이 처음부터 끝까지 차례로 임시변수에 할당되며, 모든 요소들이 임시변수에 들어가면 종료된다.
  - `for` 문 안에서 임시변수에 다른 값을 할당해도, 다음 요소 값에 의해 덮어 씌워지기 때문에 반복 구문에 영향을 주지 않는다.
    ```python
    numbers = [1, 2, 3, 4, 5]

    for num in numbers:
        print(num)
        num = 100
    ```
  - 상기 예문과 같이 임시변수에 새로운 값을 할당하지 않고, `num *= 2`를 넣더라도 임시변수에 있는 값이 변할 뿐 원본 값은 변하지 않는다.
  - `list` 원본 값의 `idx`에 접근하는게 원본 값을 바꿀 수 있는 방법이기 때문에 아래와 같이 적용하면 원본도 바뀐다.
    ```python
    numbers = [1, 2, 3]

    for idx in range(len(numbers)):
        print(numbers[idx])
        numbers[idx] *= 2
    ```
### `for` 문 예시
- `list`의 길이만큼 범위를 순회하면서 `idx` 숫자를 출력하는 방법
    ```python
    lunch = ['짜장면', '초밥', '피자']

    for idx in range(len(lunch)):
        print(lunch[idx])
        # print(f'{idx + 1}번째 메뉴: {menu}')
    ```
- `enumerate(iterable, star='')`를 이용하는 방법
  - 내장함수의 하나로, `idx`와 `value`를 함께 활용할 수 있다.
  - `enumerate()` 사용 시 첫 번째 자리에 `idx`, 두 번째 자리에 임시변수 자리에서 순회하는 `요소`를 출력한다.
  - `star=''`를 사용하여 시작 `idx`를 지정할 수도 있다.

## 반복제어
1. `break`
- 반복문을 종료한다.
- 본래 `for` 문은 자동 종료, `while` 문은 조건이 있어야 종료되지만, `break`으로 반복문을 강제 종료시킬 수 있다.
- `for` 및 `while` 문의 `if` 조건 안에, 특정 조건 충족 시 `break`으로 강제 종료하는 방식으로 사용한다.
2. `continue`
- `continue` 이후의 코드를 수행하지 않고 다음 요소부터 계속하여 반복을 수행한다.
- `for` 및 `while` 문의 `if` 조건 안에, 특정 조건을 충족하면 다음 코드로 넘어가지 않고 다음 요소의 회차를 돌리는 방식으로 사용한다.
  - 즉, `if` 조건과 반대가 돼야만 다음 코드로 넘어갈 수 있다.
3. `for-else`
- 끝까지 반복문을 실행한 이후에 실행된다.
- 반복문이 `break` 키워드로 종료된다면 `else`는 실행되지 않는다. 즉 `break` 키워드로 인해 중간에 종료되지 않은 경우에만 실행된다.
  - `break`이 있는데도 끝까지 반복문이 실행되었다면 `else`가 실행된다.
  - `break`이 없어도 `else`가 무조건 실행되는 경우라면, `if`도 `else`도 필요 없다.
- (`for`의 경우) `list`의 소진이나, (`while`의 경우) 조건이 거짓이 돼서 종료될 때 `else`가 실행된다.
4. `pass`
- 아무 것도 하지 않는다.
- 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없고 error가 나오지 않도록 할 때 자리를 채우는 용도로 사용한다.