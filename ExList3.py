List = ["짱구", "훈이", "철수", "맹구", "유리"]

# List 전체 출력하기
for x in List:
    print("리스트 전체 출력하기 : ", x)

# range()로 범위 지정하기
for x in range(0,3):
    print("리스트 범위 지정하기 : ", List[x])

# 반복문과 조건문 혼합하기
for x in List:
    if (x == "철수"):
        print("철수다 !")
    else:
        print(x)
