# 00_python_intro

## 1. 기초 문법
- 주석은 `#` 또는 `'''` 및 `"""`로 표현한다.
- 1줄에 1문장이 원칙이다.
- 한 줄로 표기할 떄는 `;`을 작성하여 표기할 수 있다.
- 여러줄의 문자열을 작성 시에는 역슬래시`\`를 사용하여 표기할 수 있다.
- `[]` `{}` `()`는 역슬래시`\` 없이도 표현할 수 있다.

---

## 2. 변수
- 할당 연산자: `=`
  - 변수는 `=`를 통해 할당된다.
  - 해당 데이터 타입을 확인하기 위해 `type()`을 활용한다.
  - 해당 값의 메모리 주소를 확인하기 위해 `id()`를 활용한다.
  - 같은 값 동시 할당 가능, 다른 값도 동시 할당 가능하다.
    - ex. `x, y = 1, 2`
  - **할당**이란 `dust = 60`일 때 dust가 60이 아닌, **dust에 60을 저장한다.** 를 의미한다.
  - 변수에 새로운 값을 할당하면, 기존의 값은 사라진다.
- 식별자
  - 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름을 의미한다.
  - 첫 글자에 숫자가 올 수 없다.
  - 대소문자를 구별할 수 있다.
  - 파이썬 예약어, 내장함수*(built-in function)*, 모듈 등의 이름은 식별자로 사용할 수 없다.

---
  
## 3. 데이터 타입
- 숫자 타입 (int/float)
  - `int` (정수, integer)
    - 8진수: `0o` / 2진수: `0b` / 16진수: `0x`
  - `float` (부동소수점, 실수, float)
    - 실수를 컴퓨터가 2진수를 통해 표현하는 과정에서 부동소수점을 사용하기 때문에, 항상 같은 값으로 일치되지 않고 근사값으로 표기될 수 있다.
      - 이 경우 반올림 `round(값, 소수점 자릿수)` 함수를 이용하여 해결 가능하다.
      - `math` 모듈을 통해 값이 같은지 확인할 수 있다.
        ```python
        import math
        math.isclose(3.5 - 3.12, 0.38)
        ```
    - 컴퓨터식 지수 표현 방식으로 `e` 및 `E`를 사용할 수 있다.
  - `complex` (복소수)
    - 실수와 정수 외에 복소수도 있으나, 거의 사용하지 않으므로 나중에 등장하면 찾아봐야 한다.
- 문자열 타입 (str)
  - `''` 및 `""`을 활용하여 표현 가능하다.
    - `''`를 사용한 문자열 안에 `''`을 사용할 경우 문장 기호 앞에 이스케이프 문자`\`를 활용하여 표기 `\'` 하거나,
    - 서로 다른 문장 부호 구성 `'철수가 "안녕?"이라고 말했다.'` 를 사용할 수 있다.
  - 문자열을 묶을 때 하나의 문장 부호를 선택하여 유지해야 한다. *pick a rule and stick to it*
  - 문자열은 `+` 연산자로 이어붙이고, `*` 연산자로 반복시킬 수 있다.
  - `input()`은 무조건 `str`을 출력한다.
  - 이스케이프 시퀀스

    |<center>예약문자</center>|내용(의미)|
    |:--------:|:--------:|
    |\n|줄 바꿈|
    |\t|탭|
    |\r|캐리지리턴|
    |\0|널(Null)|
    |\\\\ |`\`|
    |\\'|단일인용부호(`'`)|
    |\\"|이중인용부호(`"`)|
    ---
  - 아랫줄과 연결되도록 `end=''`을 사용할 수 있다.
  - `str.format()` 및 `f-string`을 활용하여 문자열에 변수를 넣어 출력할 수 있다.
    - ex1. `'제 이름은 {}, 점수는{}입니다.'.format(name, score)`
    - ex2. `f'제 이름은 {name}, 점수는 {score}입니다.'`
- 참/거짓 (boolean) 타입
  - `True` 및 `False`를 출력한다.
    - `True = 1` `False = 0`
  - 비어있거나 없다는 뉘앙스의 값은 모두 `False`, 나머지는 모두 `True`를 출력한다.
    - `0`, `0.0`, `()`, `[]`, `{}`, `''`, `None`은 `False`를 출력한다.
  - `None` 타입은 값이 없음을 표현한다.
- 형 변환 타입
  - 암시적 형변환
    - 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동 형변환하는 경우이다.
    - `bool`과 `Numbers(int/float/complex)`에만 가능하다.
      - `int + bool = int` `int + float = float`로 자동 계산된다.
      - `complex > float > int > bool` 순서로 덮어씌워진다.
      - ex. `1 + True = 2`
  - 명시적 형변환
    - 암시적 형변환 상황을 제외하고는 모두 명시적 형변환이 필요하다.
    - 암시적 형변환이 되는 모든 경우도 명시적 형변환이 가능하다.
      - `int()`: `str`, `float`를 `int`로 변환
      - `float()`: `str`, `int`를 `float`로 변환
      - `str()`: `int`, `float`, `list`, `tuple`, `dict`를 `str`로 변환
    - `str => int`는 글자가 정수인 숫자일 경우에만 변환 가능하다.
    - `int => str`은 모두 가능하다.

---

## 4. 연산자
- 산술 연산자

  |연산자|내용|
  |----|---|
  |+|덧셈|
  |-|뺄셈|
  |\*|곱셈|
  |/|나눗셈|
  |//|몫|
  |%|나머지(modulo)|
  |\*\*|거듭제곱|
  ---
  - `(-3 ** 2) == ((-3) ** 2)`이므로 `-3`의 2제곱을 구하기 위해서는 `(-3) ** 2`로 표기해야 한다.
  - 나눗셈`/`은 항상 `float`를 돌려준다.
  - 정수 결과를 얻으려면 `//` 연산자를 사용해야 한다.
- 비교 연산자

  |연산자|내용|
  |----|---|
  |`<`|미만|
  |`<=`|이하|
  |`>`|초과|
  |`>=`|이상|
  |`==`|같음|
  |`!=`|같지않음|
  |`is`|객체 아이덴티티|
  |`is not`|부정된 객체 아이덴티티|
  ---
  - 계산된 결과값인 `3 > 5 = False`는 단순히 연산의 결과가 틀렸음을 의미하는 것이 아니라, `False`라는 새로운 값이 생성됨을 의미한다.
- 논리 연산자

  |연산자|<center>내용|
  |---|---|
  |a and b|a와 b 모두 True시만 True|
  |a or b|a 와 b 모두 False시만 False|
  |not a|True => False, False => True|
  ---
  - `and` 연산자는 모두 `True`여야 `True` 출력
  - `or` 연산자는 모두 `False`여야 `False` 출력
  - 단축 평가 (short circuit evaluation)
    - 첫 번째 값이 확실할 때, 두 번째 값은 확인하지 않는다.
    - `and`: 모두 `True`인 경우만 `True`이므로 첫 번째 값이 `True`이더라도 두 번째 값을 확인한다.
      - `'a' and 'b'` => `'b'`
      - `Fasle`를 발견하면 뒷 부분을 확인하지 않고 해당 값 바로 출력
    - `or`: 하나만 `True`이더라도 `True`이므로 `True`를 만나면 해당 값을 바로 반환한다.
      - `'a' or 'b'` => `'a'`
      - `True`를 발견하면 뒷 부분을 확인하지 않고 해당 값 바로 출력
- 복합 연산자
  - 연산과 대입이 함께 이루어진다.
  - 반복문을 통해 갯수를 셀 때 많이 활용된다.
    - ex.
      ```python
      cnt = 0
      while cnt < 5:
        print(cnt)
        cnt += 1
      
      0으로 할당된 변수 cnt를 반복문 while을 통해 5회 반복하는 동안, cnt에 1씩 더하는 구문
      ```

    |연산자|내용|
    |----|---|
    |a += b|a = a + b|
    |a -= b|a = a - b|
    |a \*= b|a = a \* b|
    |a /= b|a = a / b|
    |a //= b|a = a // b|
    |a %= b|a = a % b|
    |a \*\*= b|a = a ** b|
    ---
  - 할당 시에는 우항을 먼저 확인한다.
- 기타 연산자
  - 숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다. *(concatenation 연결)*
  - `in` 연산자를 통해 요소가 속해있는지 여부를 확인할 수 있다.
  - `is` 연산자를 통해 동일한 객체(object)인지 확인할 수 있다.
  - `[]`를 통해 값에 접근할 수 있다. (indexing)
  - `[:]`을 통해 슬라이싱할 수 있다. (slicing)
- 연산자 우선순위
  1. `()`을 통한 grouping
  2. Slicing
  3. Indexing
  4. 제곱연산자
      `**`
  5. 단항연산자 
      `+`, `-` (음수/양수 부호)
  6. 산술연산자
      `*`, `/`, `%`
  7. 산술연산자
      `+`, `-`
  8. 비교연산자, `in`, `is`
  9. `not`
  10. `and` 
  11. `or`

> 참고 내용
> 
> RAM(Random Access Memory) 특성상 변수에 값(value)을 저장하면 이름(identifer)이라는 곳에 데이터가 들어오고, 값의 랜덤 위치에 데이터가 생성된다.
> 
> 값(value)이 같더라도 위치가 다르기 때문에 id(주소)도 달라야 하지만, 파이썬에서 예외적으로 -5 ~ 256 까지의 수는 특별 취급하여 id가 동일하도록 설정하였다.
> 
> 이 때문에 257부터는 id(주소)가 달라진다.