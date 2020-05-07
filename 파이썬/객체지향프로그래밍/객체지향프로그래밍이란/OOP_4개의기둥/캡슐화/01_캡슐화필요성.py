class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이 

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민번호"""
        self.name = name 
        self.age = age 
        self.resident_id = resident_id 
    
    def authenticate(self, id_field):
        ''' 본인이 맞는지 확인하는 메소드'''
        return self.resident_id == id_field
    
    def can_drink(self):
        '''음주 가능 나이인지 확인하는 메소드'''
        return self.age >= Citizen.drinking_age

    def __str__(self):
        '''주민 정보를 문자열로 리턴하는 메소드'''
        return self.name + "씨는 " + str(self.age) + '살입니다!'

kyusik = Citizen('최규식', 25, '12345678')
young = Citizen('young kang', 5, '8765346')

print(kyusik.resident_id)
kyusik.age = -12 
print(kyusik) # 출력값: 최규식씨는 -12살입니다.

young.age = 20 
print(young.can_drink())

''' 
위에 규식의 나이를 12살 미만으로 해버려서 어이없게 처리되는 경우가 있다. 
이를 해결하기 위해서 캡슐화를 하면 된다. 

그럼 캡슐화는? 
정의 
1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는것 

2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는것.
'''