
# 자료 없이 리턴 - > None 키워드 발생

def 함수리턴1():
    print("A위치 입니다.")
    return

print(함수리턴1())  # None 


# 자료와 함께 리턴

def 함수리턴1():
    print("A위치 입니다.")
    return 100

print(함수리턴1()) # 100


# 리턴 키워드 아래로는 다 주석처리 됨!(반환되고 나면 종료되는 특징)

def 함수리턴1():
    print("A위치 입니다.")
    return 100
    print("B위치 입니다.")
    print("B위치 입니다.")
    print("B위치 입니다.")

print(함수리턴1()) # 100

