
"""
03_추상화잘하기.py 에서 추상화 잘하는 법에 대해서 봤습니다. 
                        클래스, 변수, 메소드 이름 잘 짓기.

하지만 이름 짓기에도 한계가 있으니 이럴때 유용한 방법이 바로 문서화이다. 

A클래스는 ~~~를 위해 만들어 졌습니다. 이렇게 저렇게 사용하세요. 

B변수는 인스턴스 변수로 실수형입니다. 

C메소드는 잔액 인스턴스 변수 balance를 파라미터로 amount만큼 늘려주는 메소드 입니다. 

즉 지금 이렇게 노랗게 글자가 표현 된걸 Doc string(문서화)라고도 한다. 
"""

"""
추상화를 잘하려면 어떻게 해야 할까요?

일단 먼저 이름을 잘 지어야 합니다. 그래야 해당 변수가 어떤 역할을 하는지 쉽게 파악 할 수 있습니다. 

아래 클래스는 이름을 제대로 짓지 못한 예시입니다. 
과연 어디에 쓰이는 것일 까요?
"""

# class SomeClass: 
#     class _variable = 0.02

#     def __init__(self, variable_1, variable_2):
#         self.variable_1 = variable_1
#         self.variable_2 = variable_2

#     def method_1(self, some_vale):
#         self.variable_2 += some_value
    
#     def method_2(self, some_vale):
#         if self.variable_2 < some_value:
#             print("Insufficient balance!")
#         else: 
#             self.variable_2 -= some_value
    
#     def method_3(self, some_vale):
#         self.variable_2 *= 1 + SomeClass.class_value

   
class BankAccout: 
    """ 은행 계좌 클래스 """
    interest = 0.02

    def __init__(self, owner_name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """ 잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balance += amount
    
    def withdrow(self, amount):
        """ 잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄이는 메소드"""
        if self.balance < amount:
            print("Insufficient balance!")
        else: 
            self.balance -= amount
    
    def add_interest(self):
        """ 잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance *= 1 + BankAccout.interest

ex_account = BankAccout('홍길동', 1000)

ex_account.add_interest()
print(ex_account.balance)

ex_account.deposit(500)
print(ex_account.balance)

ex_account.withdrow(2000)
ex_account.withdrow(1000)
print(ex_account.balance)

""" 유용한 꿀팀! help()를 통해서 해당 모듈의 이름을 넣으면 docstring을 볼수 있습니다."""

