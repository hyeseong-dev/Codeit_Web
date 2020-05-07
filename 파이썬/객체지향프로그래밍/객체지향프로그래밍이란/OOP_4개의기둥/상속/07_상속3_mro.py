# -*- encoding: utf8 -*-

"""

오버라이딩은 mro() 메서드와 관련이 깊습니다.  mro(Method Resolution Order), 메서드 검색순서
파이썬에서는 물려 받은 메서드를 다시 정의해서 오버라이딩합니다. 

그럼 ______자식 Class_________ 
    |  1. 물려받은 메소드      |
    |   2. 오버라이딩 메소드   | ==> 2. 오버라이딩 한 메소드가 호출 되는 것일까?
    |_________________________|         정답은: mro()에 나와있는 리스트의 순서대로 나오는거임.

    mro()메서드로 만들어진 리스트의 0번쨰 순서부터 호출되어서 그럼.
    mro() 사용방법 : 클래스명.mro()

    예를 들어, Cashier.mro()를 호출하면 아래와 같이 리스트가 나타난다. 
    [<class '__main__.Cashier'>, <class '__main__.Employee'>, <class 'object'>]
    즉, 바로위의 리스트 순서가 자식 클래스에서 같은 이름의 메소드가 있을때(상속,오버라이딩) 실행되는 순서이다
    짧게 표현하면 메서드 검색 방향은: 자식클래스 -> 부모클래스
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

print(Cashier.mro())

young = Cashier('강영훈', 2833,4)
young.raise_pay()           # 현재 Cashier클래스에 raise_pay() 메서드가 없으니 부모클래스에서 가져옴