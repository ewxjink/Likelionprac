List = [1, 2, 3, 1, 2, 3]

# 리스트 길이 구하기
List_len = len(List)
print(List_len)

# 리스트 요소 1개 추가 -- append()
List.append(1)
List.append("A")
List.append(["B", "C"])

print("리스트 요소 추가하기 : ", List)


# 리스트 확장하기 -- extend()
List.extend(["가", "나", "다"])
print("리스트 확장하기 :",List)

#extend => 그냥 추가 됨 append => [,, ]이렇게 추가됨

# 리스트 요소 제거하기 -- remove()
List.remove(1)
print("첫번째 1 삭제하기 : ", List)

List.remove(1)
print("두번째 1 삭제하기 : ", List)

List.remove(1)
print("세번째 1 삭제하기 ", List)

# 리스트 요소 개수세기 -- count()
print("2의 개수세기 : ", List.count(2))
print("3의 개수세기 : ", List.count(3))

# 리스트 요소 끄집어내기 -- pop()
print(List.pop())
print("마지막 요소 끄집어내기 : ", List)

print(List.pop(7))
print("요소 끄집어내기 : ",List)

print(List.pop(6))
print("요소 끄집어내기 : ", List)