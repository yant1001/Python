# 06_module

|용어|정의|
| --------| ------------------- |
|모듈| 특정 기능을 `.py` **파일 단위**로 작성한 것.|
|패키지| 특정 기능과 관련된 여러 **모듈들의 집합**. 패키지 안에는 또다른 서브 패키지를 포함 할수도 있음.|
|파이썬 표준 라이브러리| 파이썬에 **기본적으로 설치된 모듈과 내장 함수**를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 불림.|
|패키지 관리자(**`pip`**)| `PyPI` 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지.|


### 모듈(Module)
- 파이썬 파일을 의미한다.
- 특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)이다.
- 활용법:
  1. `import` 문을 통해 내장 모듈을 이름 공간으로 가져온다.
  2. `dir()`을 통해 해당 모듈로 활용할 수 있는 모든 기능을 보여준다.
```py
# 하기 정의한 두 개의 함수를 check.py 파일로 저장
def odd(n):
    return bool(n % 2)
def even(n):
    return not bool(n % 2)


import check
check.odd(10)   # FALSE
check.even(10)  # TRUE
```


### 패키지(Package)
- 파이썬 폴더를 의미한다.
- 점(`.`)으로 구분된 모듈 이름(`package.module`)을 써서 모듈을 구조화하는 방법니다.
- 예를 들어, 모듈 이름 `my_package.math`는 `my_package`라는 이름의 패키지에 있는 `math`라는 이름의 하위 패키지를 가리킨다.
- 활용법:
  1. (생성) `__init__.py` 파일을 생성하며, 모든 `__init__.py` 파일은 비워둔다.
    - python 3.3ver 부터는 `__init__.py` 파일이 없어도 패키지로 인식하지만, 하위 버전 호환 및 일부 프레임워크에서의 올바른 동작을 위해 해당 파일 생성을 권장한다. 
  2. (활용) 모듈과 동일하게 `from`과 `import` 키워드를 통해 코드를 가져와 활용한다.
     1. `from` 패키지 `import` 모듈
     2. `from` 패키지.모듈 `import` 데이터
        - 특정한 함수 혹은 어트리뷰트만 활용하고 싶을 때 사용한다.
     3. `from` 모듈 `import` `*`
        - 해당하는 모듈 내 모든 변수, 함수, 클래스를 가져온다.
        - 모든 정보를 불러오며 많은 메모리를 차지하기 때문에, 권장하지 않는 방법이다.
     4. `from` 모듈 `import` 데이터 `as` 별명
        - 내가 지정하는 이름을 붙여 가져올 수 있다.


## 정리
#### 모듈
```py
import module
from module import var, function, Class
from module import *
```

#### 패키지
```py
from package import module
from package.module import var, function, Class
```