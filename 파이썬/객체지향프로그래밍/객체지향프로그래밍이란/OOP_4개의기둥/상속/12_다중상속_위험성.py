# -*- encoding: utf8 -*-
'''


'''

class Employee: 
    '''직원 클래스'''
    company_name = '코드잇 버거'
    raise_percentage = 1.03 

    def __init__(self, name, wage):
        ''' 생성자 메소드'''
        self.name = name
        self.wage = wage
    
    def raise_pay(self):
        '''직원 시급을 인상하는 메소드'''
        self.wage *= self.raise_percentage
    
    def __str__(self):
        '''직원의 정보를 문자열로 리턴하는 메소드'''
        return Employee.company_name + ' 직원: ' + self.name


class Cashier(Employee):
    '''계산대 직원 클래스'''
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name,wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        '''주문과 돈을 받고 거스름돈을 리턴한다. '''
        if Cashier.burger_price > money_received: 
            print('돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!')
            return money_received
        else: 
            self.number_sold += 1 
            change = money_received - Cashier.burger_price
            return change
    
    def __str__(self):
        return Cashier.company_name + ' 계산대 직원: ' + self.name
    
class DeliveryMan(Employee):
    def __init__(self, name, wage, on_standby):
        ''' 배달원 클래스 생성자 메소드, super 메소드를 이용해서 일부 인스턴스 변수의 초기값을 설정한다'''
        super().__init__(name,wage)
        self.on_standby = on_standby
        
    def deliver_to(self, address):
        '''배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 설명 메시지를 출력함.'''
        if self.on_standby:
            print(address + '로 배달 나갑니다!')
            self.on_standby = False
        else: 
            print('이미 배달하러 나갔습니다.')
    
    def back(self):
        '''배달원을 복귀 처리한다'''
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + ' 배달원: ' + self.name

'''
                        ____________
          상속          | Emloyee   |           상속
         _______________|___________|____________________
    _____|____                                    ______|_______
   | Cashier |                                   |  DeliveryMan |
   |_________|                                   |______________|
         |                                               |
         |_______________________________________________|
       상속            | CashierDeliveryMan |      상속
                       |____________________|

'''




class CashierDeliveryMan(DeliveryMan, Cashier):
    def __init__(self, name, wage, on_standby, number_sold=0):
        Employee.__init__(self, name, wage)
        self.on_standby = on_standby
        self.number_sold = number_sold

cashierDeliveryMan = CashierDeliveryMan('강영훈',7000,True,10)

cashierDeliveryMan.take_order(3000)

cashierDeliveryMan.deliver_to('코드잇 건물 101호')
cashierDeliveryMan.deliver_to('코드잇 건물 102호')

cashierDeliveryMan.back()

print(cashierDeliveryMan)
print(CashierDeliveryMan.mro()) # 클래스명.mro()를 통해서 상속 우선순위 클래스를 알수 있다.

"""
DeliveryMan 클래스와 Cashier 클래스의 __str__ 실행 우선순위는 결국 CashierDeliveryMan클래스의 파라미터 순서를 어떻게 두냐에 따라 달라집니다. 
하지만 이건 또 문제가 되겠조. 번거롭기 때문입니다. 
결국 이러한 다중상속의 문제점을 해결 하기 위해서, 자식 클래스 해당 문제의 메소드를 오버라이딩 해버리면 되겠지오?

다시 한번 다중상속의 문제점 해결 방법: 
1. 부모 클래스끼리 같은 이름의 메소드를 갖지 않도록 하기 
2. 같은 이름의 메소드는 자식 클래스에서 오버라이딩 하기 
"""