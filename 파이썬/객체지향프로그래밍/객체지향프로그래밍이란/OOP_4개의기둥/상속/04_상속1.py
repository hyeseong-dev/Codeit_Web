# -*- encoding: utf-8 -*-
"""
01_중복되는코드.py의 class코드의 중복되는 부분을 따와서 Employee클래스를 아래에 만들어 봤습니다.

hlep(클래스이름) 
해당 클래스가 무엇으로 구성되어 있는지 한눈에 볼 수 있습니다. 

Method resolution order: 
Cashier Employee
builtins.object <--- 모든 클래스가 상속받는 공통 요소
                     즉, 파이썬의 모든 클래스는 builtins.object클래스의 자식 클래스입니다.

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


class DeliveryMan(Employee):
    pass

jiwoong = DeliveryMan('지웅',1000)
jiwoong.raise_pay()
print(jiwoong.wage)
print(jiwoong)

