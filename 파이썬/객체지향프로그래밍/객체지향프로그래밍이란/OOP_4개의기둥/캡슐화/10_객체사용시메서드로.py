""" 캡슐화 전의 Citizen 클래스""" 

class Citizen: 
    """주민 클래스"""
    drinking_age = 19 # 음주가능 나이 

    def __init__(self, name,age,resident_id):
        """ 이름, 나이, 주민번호 """
        self.name = name 
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        """ 본인이 맞는지 확인하는 메서드"""
        return self.resident_id == id_field
    
    def can_drink(self):
        """음주 가능 나이인지 확인해주는 메서드"""
        return self.age>= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메서드"""
        return f'{self.name} 씨는 {self.age} 살입니다!'


young = Citizen('강영훈', 25, '123456')

# 음주 가능 나이인지 확인 
# if young.age >= Citizen.drinking_age:
#     print(f'{young.name}님은 음주 가능 나이입니다.')
# if young.age >= Citizen.drinking_age:
#     print('들어오세요.')
# if young.age >= Citizen.drinking_age:
#     print('무슨 술을 드시겠습니까?')

"""young.age >= Citizen.drinking_age: 
    young.can_drink()를 썻다면 어떻게 적용해야 할까요?

    return 부분에 +1 하나만 넣어주면 가능하다.
    def can_drink(self):
        return self.age +1 >= Citizen.drinking_age
"""

# 음주 가능 나이인지 확인 
""" 코드는 더 짧아지고 더 효율적으로 바뀜."""
if young.can_drink():
    print(f'{young.name}님은 음주 가능 나이입니다.')
if young.can_drink():
    print('들어오세요.')
if young.can_drink():
    print('무슨 술을 드시겠습니까?')


"""
결론은, 

변수 직접 사용을 최소화 ==> 유지 보수에 최적화된 코드를 의미함.
"""