# 05_data_structure_1

## 데이터 구조 
- 데이터 구조란 데이터에 편리하게 접근하고 변경하기 위해서 데이터를 저장하거나 조작하는 방법을 의미한다.
> Program = Data Structure + Algorithm
> 
> by Niklaus Wirth
- 알고리즘에 빈번히 활용되는 순서가 있는 (ordered) 데이터 구조
  - 문자열 (Str)
  - 리스트 (list)
- 데이터 구조에 적용 가능한 built-in function
- `method` 함수란 주어로 받는 변수의 행동을 의미한다고 이해하면 된다.
  - ex. (주어).(행동=method)()
> A.b = A에 들어있는 b속성을 찾으라는 의미


### 문자열 (string)
- 변경할 수 없고 `immutable`, 순서가 있고 `ordered`, 순회 가능한 `iterable`
1. `.find(x)` (조회/탐색)
    - x의 첫 번째 위치를 반환한다.
    - 없다면 `-1`을 반환한다.
2. `.index(x)` (조회/탐색)
    - x의 첫 번째 위치를 반환한다.
    - 없다면 오류 발생한다.
    - `.index(x)`를 이용해 오류 발생 이유를 알 수 있다는 게 장점이다.
3. 多 `.replace(old, new, count)` (문자열 변경)
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환한다.
    - `count` 지정 시 해당 수만큼만 시행한다.
4. `.strip([chars])` (문자열 변경)
    - 종류: `.strip()`, `.lstrip()`, `.rstrip()`
    - 특정한 문자들을 지정하면 양쪽 or 왼쪽 or 오른쪽을 제거한다.
    - 지정하지 않으면 공백을 제거한다.
5. 多 `.split([chars])` (문자열 변경)
    - 문자열을 특정한 단위로 나누어 `list`로 반환한다.
    - 문자열 사이에 기준으로 삼을만한 특정 단위가 없는 경우 `list`로 형변환하여 활용 가능하다.
        - cf. `.split()` => `list`
              `.join()` => `string`
6. 多 `'separator'.join(iterable)` (문자열 변경)
    - 특정한 문자열로 만들어 반환한다.
    - 반복 가능한 `iterable` 컨테이너의 요소들 사이에 구분자`separator`를 결합한 문자열로 반환한다.
        ```python
        word = '배고파'
        words = ['안녕', 'hello']
        '!'.join(word)   # 결과값: '배!고!파'
        ' '.join(words)  # 결과값: '안녕 hello'
        ```
7. `.capitalize()` (대소문자 변환)
   - 앞 글자를 대문자로 만들어 반환한다.
8. `.tile()` (대소문자 변환)
    - 어퍼스트로피(')나 공백 이후를 대문자로 만들어 반환한다.
9. `.upper()`
    - 모두 대문자로 만들어 반환
10. `.lower()`
    - 모두 소문자로 만들어 반환
11. `.swapcase()`
    - 대소문자를 변경하여 반환
12. 기타 문자열 관련 검증 메소드: 참/거짓 반환
    - .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower()
13. 기타 참고할만한 함수
    - `dir('')`: 문자열이 가지고 있는 메소드를 확인할 수 있다.
    - `help('')`


### 리스트 (List)
- 변경 가능하고 `mutable`, 순서가 있고 `ordered`, 순회 가능한 `iterable`
1. 多 `.append(x)` (값 추가/삭제)
    - 리스트에 값을 추가할 수 있다.
    - 원본 값을 바꿀 수 없는 immutable 값인 str은 변경 불가능하다.
2. `.extend(iterable)` (값 추가/삭제)
    - `.extend()` 메서드를 활용하여 리스트에 iterable(list, range, tuple, string) 값을 붙일 수 있다.
    ```python
    cafe = ['starbucks', 'droptop']

    # .append() 메서드로 리스트를 추가할 경우
    cafe.append(['coffeenie'])
    ['starbucks', 'droptop', ['coffeenie']]

    # .extend() 메서드로 리스트를 추가할 경우
    cafe.append(['twosome'])
    ['starbucks', 'droptop', ['coffeenie'], 'twosome']

    # .extend() 메서드로 문자열을 추가할 경우
    cafe.extend('ediya')
    ['starbucks', 'droptop', ['coffeenie'], 'twosome', 'e', 'd', 'i', 'y', 'a']
    **문자열은 한 글자씩 나눠서 추가된다.**
    **대부분의 경우 .extend()보다는 += 연산자를 많이 사용한다.**
    ```
3. `.insert(i, x)` (값 추가/삭제)
   - 정해진 위치 `i`에 `x` 값을 추가한다.
```python
cafe = ['starbucks', 'droptop', ['coffeenie'], 'twosome', 'e', 'd', 'i', 'y', 'a']

# 변수 cafe 첫번째에 문자열 삽입
cafe.insert(0, 'start')
['start', 'starbucks', 'droptop', ['coffeenie'], 'twosome', 'e', 'd', 'i', 'y', 'a']

# 변수 cafe 마지막에 문자열 삽입
cafe.insert(len(cafe), 'end')
['start', 'starbucks', 'droptop', ['coffeenie'], 'twosome', 'e', 'd', 'i', 'y', 'a']
# -1로 표현할 경우, 맨 뒤가 아닌 그 앞자리에 문자열 삽입된다. 맨 뒤에 있는 문자열을 하나 밀고 그 자리에 들어오기 때문.
cafe.insert(-1, 'end')

# 변수 cafe 길이보다 큰 인덱스에 문자열 삽입
# 리스트 길이보다 큰 인덱스는 마지막에 문자열이 추가된다.
cafe.insert(100, '!')

```
4. `.remove(x)` (값 추가/삭제)
    - 리스트에서 값이 x인 것을 삭제한다.
    - return이 없으므로 원본을 바꾼다.
5. 多 `.pop(i)` (값 추가/삭제)
    - 정해진 위치 `i`에 있는 값을 삭제 후 그 항목을 반환한다.
    - `i`가 지정되지 않으면 마지막 항목을 삭제하고 되돌린다.
    - return이 있으므로 원본을 바꾸지 않는다.
6. `.clear()`
    - 리스트의 모든 항목을 삭제한다.
7. `.index(x)` (탐색 및 정렬)
    - x값을 찾아 해당 index 값을 반환한다.
8. `.count(x)` (탐색 및 정렬)
    - 원하는 값의 개수를 반환한다.
    ```python
    # .count(x)를 활용해 원하는 값을 모두 삭제하는 방법
    for _ in range(a.count(1)):
        a.remove(1)
    
    # for문을 작성할 때, 한 번 쓰고 이후 다시 쓰지 않을 임시변수에 대해 _로 대체한다.
    ```
9. 多 `.sort()` (탐색 및 정렬)
    - 리스트의 값을 정렬한다.
    - 내장함수 `sorted()`와 다르게, 원본 list를 변형시키고 `none`을 리턴한다.
    ```python
    # .sort() 메서드의 reverse 옵션
    lotto.sort(reverse=True)
    
    # random을 이용한 .sort() 활용법
    import random
    lotto = random.sample(range(1, 46), 6)
    s_lotto = sorted(lotto)

    # .sort() => return 없음, 원본 바꿈
    # sorted() => return 있음, 원본 안바꿈
    # sorted()는 내장함수, .sort()는 list만 할 수 있는 method이다.
    ```
10. `.reverse()` (탐색 및 정렬)
    - 리스트를 반대로 뒤집는다.
    - 정렬이 아님에 유의한다.


#### 리스트의 복사
```python
original_list = [1, 2, 3]

copy_list = original_list
# 복사가 아니라, 대상은 하나지만 같은 대상을 지칭하는 이름이 2개가 된 형태이다.

copy_list[0] = 5
print(original_list)
=> [5, 2, 3]

original_list is copy_list True
```

#### 데이터 타입별 복사
1. 변경 불가능한 immutable 데이터 **(value type)**
   1. literal
      1. number
      2. string
      3. bool
   2. range()
   3. tuple()
   4. frozenset()

=> 복사가 가능하다.
```python
a = 20 ; b = a ; b = 10

print(a) ; print(b)
  #20        #10
```

2. 변경 가능한 mutable 데이터 **(ref type)**
   1. list
   2. dict
   3. set

=> 복사되지 않고, 같은 대상을 함께 지칭하기 때문에 a와 b 값이 동일하게 출력된다.
```python
a = [1, 2, 3, 4] ; b = a ; b[0] = 100

print(a) ; print(b)
#[100, 2, 3, 4]
```

#### 리스트 복사 방법
**얕은 복사 (shallow copy)**
1. slice 연산자 사용 [:]
   1. slice 연산자로 리스트 a의 모든 요소를 변수 b에 저장
   ```python
   b = a[:]
   a[0] = 5
   a is b, a, b

   # (False, [5, 2, 3], [1, 2, 3])
   ```
2. .copy() 활용
   1. .copy() 메서드로 리스트 a를 복사하여 변수 b에 저장
   ```python
   b = a.copy()
   b[0] = 5
   a is b, a, b

   # (False, [1, 2, 3], [5, 2, 3])
   ```
3. 2원 리스트의 복사
   1. 가장 밖에 있는 리스트는 복사되지만, 리스트 안의 리스트(중첩된 리스트)는 복사되지 않고 참조된다.
```python
b = a[:]
a[0] = 5
a[2][0] = 100

a, b
# ([5, 2, [100, 2]], [1, 2, [100, 2]])
```
**깊은 복사(deep copy)**
- 중첩된 상황에서 복사 가능하다.
- 내부에 있는 모든 객체까지 새롭게 값이 변경된다.
- copy 모듈 활용
```py
from copy import deepcopy
aa = deepcopy(a)
a[2][0] = 100

a, aa
# ([5, 2, [100, 2]], [5, 2, [100, 2]])
```

#### List Comprehension
- 표현식과 제어문을 통해 리스트 생성
- 여러 줄의 코드를 한 줄로 축소 가능
```py
[expression for 변수 in iterable if 조건식]
list(expression for 변수 in iterable if 조건식)

# example 1
numbers = range(1, 11)
cubic_list = []
for num in numbers:
    cubic_list.append(num ** 3)
# list comprehension
cubic_list = [num ** 3 for num in range(1, 11)]



# example 2
words = 'Life is too short, you need python!'
vowels = 'aeiou'

new_words = ''
for char in words:
    if char not in vowels:
        new_words += char
# list comprehension
result = [char for char in words if char not in vowels]
print(''.join(result))
```

## 데이터 구조에 적용 가능한 Built-in Function
- 순회 가능한 `iterable` 데이터 구조에 적용 가능한 `Built-in Function`
- `iterable` 타입: `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

1. `map(function, iterable)`
- 순회 가능한 데이터 구조의 모든 요소에 `function`을 적용한 후 그 결과를 돌려준다.
- 주어진 여러 개의 `iterable` 요소에 특정 `function` 함수를 적용하여 다른 것으로 매핑한다.
- 첫번째 인자 `function`은 사용자 정의 함수도 가능하다.
- 입력값을 처리할 때 자주 활용된다.
```py
# 변수 numbers를 정수로 구성된 리스트로 만들기
numbers = ['1', '2', '3']
list(map(int, numbers))
```

2. `filter(function, iterable)`
- `iterable`에서 `function`의 반환된 결과가 `True`인 것들만 반환한다.
```py
def is_odd(n):
    return bool(n % 2)

list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))
```

3. `zip(*iterables)`
- 복수의 `iterable` 객체를 모아 `zip()`을 구성한다.
- 튜플의 모음으로 구성된 값을 반환한다.
```py
# zip() 사용
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']
list(zip(girls, boys))
# [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]


# map(), zip() 사용
l1 = [1, 2, 3]
l2 = [4, 5, 6]
list(map(sum, zip(l1, l2)))
# [5, 7, 9]
```


### Lambda 표현식
- 간단한 함수의 경우 람다표현식으로 짧게 줄여 쓸 수 있다.
- 새로 정의하여 만들게 되는 함수가 다시 사용할 것 같지는 않을 때 간단하게 쓰기 위해 람다표현식을 사용하기도 한다.
- Lambda 표현 가능한 조건
  1. 매개변수가 1개 이상
  2. `return` 구문 포함 한줄
- Lambda 표현식 만드는 방법
  1. 맨 앞에 `lambda` 작성
  2. `def`와 함수 이름과 소괄호 지우기
  3. `enter`와 `return` 키워드 지우기
```py
# 기명 함수
def cube(n):
    return n ** 3
cube(10)
# 기명 리스트
n = [1, 2, 3]

# 익명 함수
(lambda n: n ** 3)(10)
# 익명 리스트
[1, 2, 3]
```