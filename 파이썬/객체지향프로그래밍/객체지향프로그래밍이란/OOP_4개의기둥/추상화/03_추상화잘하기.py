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
    """
    잘못된 예시를 수정한것이 아래 예제입니다.
    # 일단 이 클래스가 은행 계좌에 쓰인다는걸 파악 가능함 

    """
    interest = 0.02

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdrow(self, amount):
        if self.balance < amount:
            print("Insufficient balance!")
        else: 
            self.balance -= amount
    
    def add_interest(self):
        self.balance *= 1 + BankAccout.interest

ex_account = BankAccout('홍길동', 1000)

ex_account.add_interest()
print(ex_account.balance)

ex_account.deposit(500)
print(ex_account.balance)

ex_account.withdrow(2000)
ex_account.withdrow(1000)
print(ex_account.balance)

"""
추상화를 잘 하기위한 첫 걸음은 변수명,함수명,클래스명, 파라미터명등 
이름 짓기를 잘해야하는것이다. 
"""