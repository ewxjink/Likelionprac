# 본인의 정보를 적어주세요. "address" 키는 00시만 적어주세요. ex) 서울시
Dic = {
    "name" : "주영빈",
    "age" : 22,
    "phonenumber" : "01034205470",
    "address" : "고양시"
}

# Key 값으로 리스트만들기 -- keys()
print("Key 값으로 만든 리스트 : ", Dic.keys())

# Value 값으로 리스트만들기 -- values()
print("Value 값으로 만든 리스트 : ", Dic.values())

# Key 값 리스트로 변환하기 -- list
print("Key 값 리스트로 변환하기 : ", list(Dic.keys()))

# Value 값 리스트로 변환하기 -- list
print("Value 값 리스트로 변환하기 : ", list(Dic.values()))

# Key 와 Value 쌍 얻기 -- items()
print("Key 와 Value 쌍 : ", Dic.items())

# Key 로 Value 얻기 -- get()

print("이름 value 얻기 : ", Dic.get("name") )
print("나이 value 얻기 : ", Dic.get("age"))
print("전화번호 value 얻기 : ", Dic.get("phonenumber"))
print("주소 value 얻기 : ", Dic.get("address"))

# 존재하지 않는 "grade" Key 가져오기 -- get()


# default 값 "A" 설정하기 -- get()


# Key 가 딕셔너리에 존재하는지 확인하기 -- in





# Key 와 Value의 쌍을 모두 지우기 -- clear
