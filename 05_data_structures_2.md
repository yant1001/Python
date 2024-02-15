# 05_data_structures_2

> 알고리즘에 많이 활용되는 `unordered` 데이터 구조
> - 세트(set)
> - 딕셔너리(dictionary)



## 세트(Set)
- 변경 가능하고 `mutable`, 순서가 없고 `unordered`, 순회 가능한 `iterable`
1. `.add(elem)` (추가 및 삭제)
	- elem을 세트에 추가한다.
   - `.apend()`와 달리 `.add()`는 순서 없이 더하기만 한다.
   - 집합(set)은 중복을 허용하지 않기 때문에 여러번 실행해도 반복적으로 값이 적용되지 않는다.

2. `.update(*others)` (추가 및 삭제)
	- 여러 값을 추가한다.
	- 인자로는 반드시 `iterable` 데이터 구조를 전달해야 한다.\
		ex. a.update({'tomato', 'tomato', 'strawberry'}, {'grape', 'lemon'})

3. `.remove(elem)` (추가 및 삭제)
	- elem을 세트에서 삭제하고, 없으면 keyerror를 발생시킨다.

4. `.discard(elem)` (추가 및 삭제)
	- elem을 세트에서 삭제하고, 없어도 keyerror를 발생시키지 않는다.

5. `.pop()` (추가 및 삭제)
	- 임의의 원소를 제거해 반환한다.
   - 집합(set)은 순서가 없기 때문에 `list`의 `.pop()`과 달리, 아무것도 입력하지 않아도 맨 마지막이 나오지 않는다.
   - 랜덤으로 제거하여 반환하고, 더 이상 나올게 없으면 keyerror가 발생한다.



## 딕셔너리(Dictionary)
- 변경 가능하고 `mutable` 순서가 없고 `unordered` 순회 가능한 `iterable`
- `key: value` 페어의 자료 구조
1. `.get(key[, default])` (조회)
	- key를 통해 value를 가져온다.
	- 절대로 keyerror가 발생하지 않는다. default는 기본적으로 none이다.
	- key가 딕셔너리에 있는 경우 key 값을 돌려주고, 그렇지 않으면 default를 돌려준다.
2. `.pop(key[, default])` (추가 및 삭제)
	- key가 딕셔너리에 있으면 제거하고 그 값을 돌려준다. 그렇지 않으면 default를 반환한다.
	- default가 없는 상태에서 딕셔너리에 없으면 keyerror가 발생한다.
3. `.update()` (추가 및 삭제)
	- 값을 제공하는 key, value를 덮어쓴다.


### 딕셔너리 순회 (for 반복문 활용)
- 딕셔너리의 key에 접근할 수 있으면, value에도 접근할 수 있다.
- `iterable`에서 딕셔너리를 생성하여 `dictionary comprehension`을 만들 수 있다.
   ```py
   # dictionary comprehension
   # 활용법: {키: 값 for 요소 in iterable}
   cubic = {x: x ** 3 for x in range(1, 8)}
   print(cubic)

   # dictionary comprehension + 조건
   # 활용법: {키: 값 for 요소 in iterable if 조건식}
   dusts = {'seoul': 72, 'incheon': 82, 'jeju': 29, 'donghae': 45}
   {k: ('bad' if v > 70 else 'normal') for k, v in dusts.items()}
   ```
- 딕셔너리에서 `for`문을 활용하는 4가지 방법
	1. dictionary 순회 (key 활용)
   ```py
   for key in dict:
      print(key)
      print(dict[key])
   ```

	2. `.keys()` 활용
   ```py
   for key in dict.keys():
      print(key)
      print(dict[key])
   ```

	3. `.values()` 활용
   ```py
   for val in dict.values():
      print(val)
   ```

	4. `.items()` 활용
   ```py
   for key, val in dict.items():
      print(key, val)
   ```

- `list`가 주어질 때, 각각의 요소의 개수를 `value` 값으로 갖는 딕셔너리를 만드는 방법
   ```py
   book_title - ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock' 'holmes', 'the', 'great', 'gasby', 'hamlet', 'huckleberry', 'fin']

   # dict[key]로 접근하는 방법
   # a in dict => key a가 존재하는지를 검증
   # if 등장한 적 있는 경우, else 한번도 등장한 적 없는 경우
   counter = {}
   for title in book_title:
      if title in counter:
         counter[title] += 1
      else:
         counter[title] = 1
   print(counter)

   # .count() 메서드로 접근하는 방법
   counter = {}
   for title in book_title:
      counter[title] = book_title.count(title)
   print(counter)

   # .get() 메서드로 접근하는 방법
   counter = {}
   for title in book_title:
      counter[title] = counter.get(title, 0) + 1
   print(counter)
   ```
