from test1 import BankAccout

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

# ex_account = BankAccout('홍길동', 1000)

# ex_account.add_interest()
# print(ex_account.balance)

# ex_account.deposit(500)
# print(ex_account.balance)

# ex_account.withdrow(2000)
# ex_account.withdrow(1000)
# print(ex_account.balance)

""" 유용한 꿀팀! help()를 통해서 해당 class의 이름을 넣으면 docstring을 볼수 있습니다."""

# help(BankAccout)
help(BankAccout)

''' 다른 파일의 docstring을 보고 싶은 경우에는 해당 파일을 import하면 불러올수 있습니다.'''