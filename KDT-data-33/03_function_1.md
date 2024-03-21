# 03_function_1

## 1. 함수의 정의
- 정의: 특정한 기능(function)을 하는 코드의 묶음
- 특징:
  - 하나의 함수는 하나의 작업을 한다.
  - 가독성, 재사용성, 유지보수에 용이하다.
- 활용법:
    ```python
    def <함수이름> (parameter1, parameter2):
        return value
    ```
- 선언과 호출:
  - 함수의 선언은 `def` 키워드를 활용한다.
  - 함수는 동작 후에  `return`을 통해 결과값을 전달한다.
    - `return` 값이 없으면, `None`을 반환한다.
  - 소괄호`()`가 붙은 코드는 함수를 호출한다.
  - 내장함수(built-in functions) 및 예약어는 절대 변수명으로 사용할 수 없다.
    - `dir(__builtins__)`을 이용하여 내장함수 목록을 확인할 수 있다.

---

## 2. 함수의 Output
- 함수의 `return`
  - 함수는 **반환되기 위해 존재**한다.
  - 함수는 오직 한 개의 객체만 반환한다.
  - `return`은 `def`로 정의된 함수 안에서만 사용 가능하다.
  - `return`이 없으면 끝까지 실행되고, `None`을 반환한다.
  - `return`이 있으면, 그 자리에서 종료된다. 함수가 종료된다.
  - 함수는 `return` 값으로 평가받기 떄문에, `함수 + 4` 또한 계산할 수 있다.
    - ex. `sum([1, 2, 3]) + 4`

---

## 3. 함수의 Input
- 매개변수(parameter)
    ```python
    def func(x):
        return x + 2
    ```
  - `x`는 매개변수이다.
  - 임력을 받아 함수 내부에서 활용할 `변수`이다.
  - 함수의 정의 부분에서 확인할 수 있다.

- 전달인자(argument)
    ```python
    func(2)
    ```
  - `2`는 (전달)인자(argument)이다.
  - 실제로 전달되는 `입력값`이다.
  - 함수의 호출 부분에서 확인할 수 있다.

- 함수의 인자
  - 함수는 입력값(input)으로 인자(argument)를 넘겨줄 수 있다.
  - 위치 인자
    - 기본적으로 인자는 위치에 따라 함수 내에 전달된다.
      - 순서에 따라 다른 값이 `return`될 수 있다.
  - 기본 인자 값
    - 호출 시 인자가 없으면 기본 인자 값이 활용된다.
      ```python
      def greeting(name='익명'):
        print(f'{name}, 안녕?')

      greeting()
      greeting('철수')
      ```
      > 함수의 소괄호 안에서는 띄어쓰기 생략해도 된다.
      > 
      > ex. greeting(name='익명')
      > 
      > `return` 값이 없으면 `none type`으로 평가됨에 유의해야 한다.
	- 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수 없다.
      ```python
      # 오류 발생하는 경우
      def greeting(name='john', age):
        return f'{name}은 {age}살입니다.'

      # 오류 발생하지 않는 경우
      def greeting(age, name='john'):
        return f'{name}은 {age}살입니다.'
      ```
  - 키워드 인자
    - 함수를 호출할 때 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달할 수 있다.
    - 키워드 인자의 암묵적, 명시적 위치 지정
      ```python
      # 암묵적 위치 지정
      greeting(10, 'john')

      # 명시적 위치 지정
      greeting(name='jack', age=20)
      ```
    - 키워드 인자를 활용한 다음, 그 뒤에 위치 인자를 활용할 수는 없다. 즉 정의할 때도, 실행할 때도 `=`가 붙은 인자는 뒤로 가야 한다.
  - 가변(임의) 인자 리스트 (Arbitrary Argument Lists)
    ```python
    def func(a, b, *args):
    ```
  	- `*args`: 임의의 개수의 위치 인자를 받음을 의미하며, 보통 매개변수 목록의 마지막에 온다.
  	- `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해, 함수를 정의할 때 가변 인자 리스트 `*args`를 활용한다.
  	- 가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현한다.
  	- 가변 인자 리스트를 사용하여, 여러 개의 정수 중 가장 큰 값을 반환하는 함수 만드는 법
      ```python
      def my_max(*args):
        maximum = args[0]
        for arg in args:
          if arg > maximum:
            maximum = arg
        return maximum

      my_max(1, 2, 3, 4)
      # 결과값: 4
      ```

  - 가변(임의) 키워드 인자 (Arbitrary Keyword Arguments)
    ```python
    def func(**kwargs):
    ```
  	- `**kwargs`: 임의의 개수의 키워드 인자를 받음을 의미한다.
  	- 정해지지 않은 키워드 인자들은 함수를 정의할 때 가변 키워드 인자 `**kwargs`를 활용한다.
  	- 가변 키워드 인자는 `dict` 형태로 처리되며, 매개변수에 `**`로 표현한다.
  	- `dictionary` 생성 함수를 만들 때, 키워드 인자로 넘기면 함수 안에서 식별자로 쓰이기 때문에 식별자를 숫자만으로 적을 수 없음에 유의한다
      ```python
      # key가 숫자인 dict를 만들 수 없는 경우
      dict(1 = 1, 2 = 2)

      # key가 숫자인 dict를 만들 수 있는 경우
      dict([(1, 1), (2, 2)])
      dict(((1, 1), (2, 2)))
        # 결과값: {1: 1, 2: 2}
      ```
  	- 가변 키워드 인자를 활용하여, URL 생성하는 법
      ```python
      def my_url(**kwargs):
        prefix = 'https://api.go.kr?'
        for k, v in kwargs.items():
          prefix += f'{k}={v}&'
        return prefix

      print(my_url(sidoname = '서울', key = 'asdf'))
      # 결과값: https://api.go.kr?sidoname=서울&key=asdf&
      ```
    