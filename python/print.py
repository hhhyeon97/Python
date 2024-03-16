# = 기본 주석 
# 실행 ctrl + f5  
print('Hello python!')

"""
Escape 시퀀스 : 문자열 내에서 특수 문자를 나타내기 위해 사용

\n : 개행
\t : tab
\\ : \ 문자
\' : ' 문자
\" : " 문자
\000 : null 문자

"""

# 기본 출력
# 괄호 안에 인수(파라미터)를 넣지 않으면 줄바꿈과 같음 
print('python!')
print("python!")
print()
print()
print('''python!''')
print("""python!""")

# separator 옵션 = 원하는 포맷 형식으로 출력을 할 때 사용
print('p','y','t','h','o','n' , sep='   ')
print('010','1111','2222', sep='-')
print('python','google.com',sep='@')

print()

# end 옵션 = 줄바꿈을 하지 않고 하나의 라인으로 연결 가능

print('welcome to', end=' ')
print('IT News',end=' ')
print('Web Site')
print()

# import 키워드 
# 모듈이나 패키지를 불러와서 그 안에 정의된 함수, 클래스 등을 사용할 수 있다.
import sys

# 또는 모듈의 특정 요소만 가져오고 싶을 때는 from 키워드를 사용
# ex) from math import sqrt


# file 옵션
print('Learn Python', file=sys.stdout)
# file 매개변수를 사용하여 출력 대상을 설정할 수 있다.
# sys.stdout은 파이썬의 표준 출력 스트림을 나타내는 것 /
# 즉 이 코드는 'Learn Python'을 표준 출력으로 출력하라는 의미
print()

# format 사용 (d : 3, s : 'python', f : 0.1234)

# 같은 결과 
print('%s %s' % ('one','two'))
print('{} {}' .format('one','two'))
print('{0} {1}' .format('one','two'))

print()

# %s : 문자열 포맷팅에 사용되는 포맷 코드 
print('%10s' % ('nice'))
print('{:>10}' .format('nice'))

print('%-10s' % ('nice'))
print('{:10}' .format('nice'))

print('{:_>10}' .format('nice'))
print('{:^10}' .format('nice')) # 중앙 정렬

print('%.5s' % ('nice')) # .을 붙이면 왼쪽부터 출력
print('%.5s' % ('python study')) # pytho  / 공간이 5개라 5글자까지만 나옴
print('%5s' % ('python study')) # python study / 공간이 5개지만 글자 모두가 나옴
print('{:10.5}' .format('python study')) # pytho  / 공간이 10개지만 5개만 나옴

# ex) 
name = "John"
age = 30
print("My name is %s and I am %s years old." % (name, age))

# %d : 정수를 포맷하는 데 사용되는 문자열 포맷 코드

print('%d %d' % (1,2))
print('{} {}' .format (1,2))

print('%4d' % (42))
print('{:4d}' .format(42))

# ex)

age = 30
print("I am %d years old." % age)

# %f : 부동 소수점 숫자(실수)를 포맷하는 데 사용되는 문자열 포맷 코드

print('%f' % (3.14132123123123)) # 3.141321  / 기본적으로 소수점 이하 여섯 자리까지 표시
print('%1.13f' % (3.14132123123123)) # 정수부는 1자리, 소수부는 13자리까지 출력한다는 의미
print('{:f}' .format(3.14132123123123))
print('%06.2f' % (3.11112321312245)) # 003.11
print('{:06.2f}' .format(3.11112321312245))


# ex ) 
pi = 3.14159
print("The value of pi is approximately %f." % pi)