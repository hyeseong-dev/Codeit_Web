""" typing hint 현재 재약 상황 발생 코드잇 햇는것 처럼 되지 않음.""" 


class BankAccout: 
    """ 은행 계좌 클래스 """
    interest: float = 0.02

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None: 
        self.balance += amount
    
    def withdrow(self, amount: float) -> None:
        if self.balance < amount:
            print("Insufficient balance!")
        else: 
            self.balance -= amount
    
    def add_interest(self) -> None:
        self.balance *= 1 + BankAccout.interest
