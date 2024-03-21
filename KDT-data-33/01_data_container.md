# 01_data_container

## 시퀀스형 *Sequence* 컨테이너
1. 순서를 가질 수 있다.
- 인덱스(idx)가 있다.
2. 특정 위치의 데이터를 가리킬 수 있다.
3. 기본적인 시퀀스 타입은 아래와 같다.
- list
  - 속성: mutable (값 수정 가능)
  - 생성 방법: `[]` 및 `list()`
  - 접근 방법: `list[i]`
  - 활용법:
    - list, tuple은 변수명을 복수형으로 만든다.
- tuple
  - 속성: immutable (값 수정 불가능)
  - 생성 방법: `()`
  - 활용법:
    - list, tuple은 변수명을 복수형으로 만든다.
      - 다만, tuple의 경우 직접 이름 작성할 일이 드물다.
    - 직접 사용하기보단, 파이썬 내부에서 다양하게 활용된다.
      - ex. 변수 생성 시 별도 명령 없으면 tuple이 기본값
      - ex. 소괄호가 없어도 콤마(,)가 있으면 자동으로 tuple로 묶인다.
    - 하나의 변수(좌항)에 여러 값(우항)을 넣으려고 한다면, tuple이다.
      - ex. `t = 1, 2`
    - 두 변수(좌항)에 각각 값(우항)을 넣는 것도 가능하다.
      - ex. `x, y = 1, 2` or `(x, y) = (1, 2)`
    - 하나의 요소(값)으로 구성된 tuple은 값 뒤에 쉼표를 붙인다.
      - `single = (1)` => `type = int`
      - `single = (1, )` => `type = tuple`
- range
  - 속성: immutable
  - 생성 방법: `range()`
  - 범위:
    - `range(n, m)` => `n부터 m-1까지 값`
    - `range(n, m, s)` => `n부터 m-1까지 +s만큼 증가`
  - 활용법: 
    - 연속된 정수만을 표현한다.
    - range를 list()로 감싸 형변환할 수 있다.
    - step이든 slice든, start 지점부터 end까지 step 방향 (+/-)으로 움직인다.
    - `r = range(3, 5)` 정의 후 `r[0] = 100`으로 덮어씌워 할당 불가능하다.
- string
  - 속성: immutable
  - 활용법:
    -  따옴표`''` 로 감싸서 출력한다.
- (binary)

---

## 시퀀스에서 활용할 수 있는 연산자/함수
> 시퀀스형: list, tuple, range, string
>
> range는 immutable 타입으로, 연결이나 반복이 불가능하다.

- `x in s`
- `x not in s`
- `s1 + s2` : concatenation (연결, 연쇄)
- `s * n` : n만큼 반복하여 더하기
- `s[i]` : indexing
- `s[i:j]` : slicing
- `s[i:j:k]` : k 간격으로 slicing
  - 값의 순서를 뒤집는 방법: `numbers[::-1]`
- `len(s)` : 길이
  - 길이 - 1 = 마지막 idx
- `min(s)` : 최솟값
- `max(s)` : 최댓값
- `s.count(x)` : x의 개수

---

## 비 시퀀스형 *Non-sequence* 컨테이너
1. 순서가 없다.
2. 기본적인 비시퀀스 타입은 아래와 같다.
- set
  - 속성: mutable
  - 생성 방법: `{}` 및 빈 세트를 만들 경우 `set()`
  - 활용법:
    - 순서가 없고 중복된 값이 없다.
    - 수학에서의 집합과 동일하게 처리된다.
    - 활용 가능한 연산자는 차집합(`-`), 합집합(`|`), 교집합(`&`)이다.
      - 경우에 따라 연산자의 역할 상이하므로, `| = 합집합` 등으로 생각하면 안된다.
    - `set{}`은 사용 불가능하며 아래와 같은 형식으로 만들어야 한다.
      - ex. set = {1, 2, 3}
        - set이라는 변수에 중괄호`{}`를 이용하여 값을 넣는 순간 집합 발생
        - ```python
          nums_list = 3, 1, 2, 2, 3, 1, '가'
          print(list(nums_list))
          print(nums_list)
          print()
          nums_set = {3, 1, 2, 2, 3, 1, '가'}
          print((list(nums_set)))
          print(nums_set)
          ```
          > 결과값
          > 
          > [3, 1, 2, 2, 3, 1, '가']
          > 
          > (3, 1, 2, 2, 3, 1, '가')
          > 
          > [1, 2, 3, '가']
          > 
          > {1, 2, 3, '가'}

    - set을 사용하여 list의 중복된 값을 손쉽게 제거할 수 있다.
    - set으로 변환하는 순간 순서를 보장할 수 없다.


- dictionary
  - 속성: mutable
  - 생성 방법: `{}` 및 `dict()`
  - 활용법:
    - `key`와 `value`가 쌍으로 이루어진다.
    - `key`는 변경 불가능(immutable)한 데이터만 가능하다.
    - `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.
    - `key`는 중복 불가능, `value`는 중복 가능하다.
      - `key`는 지문같은 역할을 하기 때문에 중복될 수 없지만, `value`는 마치 동명이인이 존재하듯 중복 가능하다.
      - ```python
        {'a' : 1, 'a' : 2}
        ```
        > 결과값
        > {'a' : 2}
        > key인 a가 중복될 수 없기 때문에, a가 마지막에 작성된 value 2로 변경되었다.
    - `dictionary`의 메서드 `.keys()` `.values()` `.items()`로 key, value, key + value 목록을 확인할 수 있다.
      - `.keys()` : key 값만 출력된다.
      - `.values()` : value 값만 출력된다.
      - `.items()` 결과만 보면 `(key, value)` 형태의 튜플이 여러 개 있는 형태로 출력된다.
      - ex. `dict_items([('서울', '02'), ('인천', '032'), ('광주', '062'), ('부산', '051')])`
    - `dictionary`에 존재하는 `key`의 `value`를 변경할 수 있다.
    - `dictionary`에 존재하지 않는 `key`를 추가할 수 있다.
---

## 컨테이너형 형변환
||str|list|tuple|range|set|dictionary|
|---|---|---|---|---|---|---|
|str||O|O|X|O|<center>X|
|list|O||O|X|O|<center>X|
|tuple|O|O||X|O|<center>X|
|range|O|O|O||O|<center>X|
|set|O|O|O|X||<center>X|
|dictionary|O|O (key만)|O (key만)|X|O (key만)||
- `range`는 형변환이 불가능하다.
- `dictionary`는 대응값이 필요하기 떄문에 다른 컨테이너형을 `dict`로 형변환하는 것은 불가능하지만 `dict`를 다른 컨테이너형으로 형변환하는 것은 가능하다.
- 형변환은 `list`를 `set`으로 바꿔서 중복 제거하거나, `range`를 `list`로 바꿔서 정수로 쓸 때 많이 사용한다.

---

## 데이터의 분류
1. 변경 불가능한(`immutable`) 데이터
    - Reference(참조) 할 뿐, 값이 복사되지 않는다.
    - 원본 값이 변하지 않고 새로운 객체를 생성한다.
    - 종류
      - literal
        - 숫자 (integer/float)
        - 글자 (string)
        - 참/거짓 (bool)
      - range()
      - tuple()
      - frozenset()
2. 변경 가능한(`mutable`) 데이터
    - Value 타입으로, 값이 실제로 넘어가기 때문에 실제 복사가 이루어진다. **근데 tutor에서는 값이 복사된 형태가 안 나타나고 참조 형태로 나타나는데??**
    -  원본 값이 변한다.
    -  종류
       -  list
       -  dict
       -  set
---

