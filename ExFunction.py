def workday(x):
    if(x == "멋사하는날"):
        print("우와 멋사다 !")
        return "멋사 화이팅 !"
    elif(x == "주말"):
        print("주말이다 !")
        return "쉬는 날이다 !"
    elif(x == "평일"):
        print("평일이다 ..")
        return "강의 화이팅 !"
    else:
        print("무슨 날이지??")
        return "아무래도 잘못 입력한듯 !"

day = input("오늘은 무슨 요일? (월, 화, 수, 목, 금, 토, 일 중에서 입력하세요.)")
date = "무슨날이지?"

if(day == "화") or (day == "금"):
    date = "멋사하는날"
    answer = workday(date)
elif (day == "토") or (day == "일"):
    date = "주말"
    answer = workday(date)
elif (day == "월") or (day == "수") and (day == "금"):
    date = "평일"
    answer = workday(date)
else:
    answer = workday(Date)
print(answer)