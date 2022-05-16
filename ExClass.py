class Likelion:
    def __init__(self, name, phone_number, address, student_number):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.student_number = student_number

    def introduce_name(self):
        print("제 이름은 %s 입니다." % self.name)

    def introduce_phone_number(self):
        print("제 전화번호는 %s 입니다." % self.phone_number)
    
    def introduce_address(self):
        print("제 주소는 %s 입니다." % self.address)
    
    def introduce_student_number(self):
        print("제 학번은 %s 입니다." % self.student_number)

youngbeen = Likelion("주영빈", "01034205470", "일산", "202114041")
minjeong = Likelion("강민정", "??", "인천", "202114041")

youngbeen.introduce_name()
youngbeen.introduce_phone_number()
youngbeen.introduce_address()
youngbeen.introduce_student_number()

minjeong.introduce_name()
minjeong.introduce_phone_number()
minjeong.introduce_address()
minjeong.introduce_student_number()