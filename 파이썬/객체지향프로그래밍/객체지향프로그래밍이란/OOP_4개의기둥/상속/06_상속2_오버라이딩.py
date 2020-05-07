# -*- encoding: utf8 -*-
"""
이전 챕터에서 
              _____Employee 클래스__________
            |                               |
            |      ___공통부분____           |
            |      |변수 &메소드  |          |
            |      |_____________|          |
            |                               |
            |                               |
        Cashier클래스                DeliveryMan클래스
         (공통부분)                     (공통부분)


            물려 받은 내용의 공통부분(메서드,변수)를 자신에 맞게 수정이 필요함. 그렇지 않으면 
            두 클래스를 제대로 사용할 수 없다. 

            결국 해결 방법은 오버라이딩!!!
            : 자식 클래스에서 물려받은 메소드 -> 같은 이름의 메소드의 내용을 바꿔서 정의

            하지만 겹치는 부분이 존재하조 여전히?!
        self.name = name # 이름
        self.wage = wage # 시급

        이 부분이 겹치니깐. 이를 다시 축약해야함.


        다음은 __str__() 메소드를 오버라이딩 해봅시다. 

        지금까지 1. __init__(), __str__() 두 가지를 오버라이딩 해봤습니다. 
                2. 이제는 변수를 오버라이딩 해봅시다. 
                변수를 오버라이딩 할 때는 자식 클래스의 변수에 똑같은 변수명을 두고 다른 값을 할당하면 됨
"""

class Employee: 
    """ 직원 클래스 """

    company_name = "코드잇 버거" # 가게이름
    raise_percentage = 1.03 # 시급 인상률

    def __init__(self,name,wage):
        """인스턴스 변수 설정"""
        self.name = name # 이름
        self.wage = wage # 시급
    
    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """ 직원 정보를 문자열로 리턴하는 메소드 """
        return Employee.company_name + ' 직원: ' + self.name


class Cashier(Employee):
    raise_percentage = 1.05

    def __init__(self, name, wage,number_sold):
        # self.name = name # 부모 클래스의 내용과 동일  [방법1 ]
        # self.wage = wage # 부모 클래스의 내용과 동일

        # Employee.__init__(self,name,wage)              [방법2] 
        super().__init__(name,wage)              #[방법3] super() 쓸떼는 SELF 파라미터 빼야함.
        self.number_sold = number_sold # 자식 클래스에서 인스턴스 변수부분을 새롭게 추가한 부분임.
    
    def __str__(self):
        return Cashier.company_name + " 계산대 직원: "+self.name

class DeliveryMan(Employee):
    pass

John = Cashier('John', 8900,12)
John.raise_pay()

# print(Cashier.raise_percentage)
# print(Cashier.company_name)
print(John)

# print(John.name)
# print(John.wage)
# print(John.number_sold)
print(John.raise_percentage)