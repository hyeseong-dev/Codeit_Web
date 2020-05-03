class Cashier: 
    """계산대 직원 클래스"""
    company_name = "Codeit Burger"  # 가게 이름
    rasie_percentage = 1.03        # 시급 인상률
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        self.name = name                    # 이름 
        self.wage = wage                    # 시급
        self.number_sold = number_sold      # 하루 판매량
    
    def raise_pay(self):
        """시급을 인상한다. """
        self.wage *= self.rasie_percentage
      
    def take_order(self, money_received):
        """ 주문과 돈을 받고 거스름돈을 리턴함"""
        if Cashier.burger_price > money_received:
            print('돈이 충분하지 않습니다.')
            return money_received
        else: 
            self.number_sold += 1 
            change = money_received - Cashier.burger_price
            return change
    
    def __str__(self):
        return Cashier.company_name + " 계산대 직원: "+ self.name

jiwoong = Cashier('최지웅', 8900, 0)

jiwoong.raise_pay()
print(jiwoong.wage)

print(jiwoong.take_order(7000))
print(jiwoong.take_order(3000))

print(jiwoong.burger_price)
print(Cashier.burger_price)
print(jiwoong.number_sold)

print(jiwoong)



class DeliveryMan: 
    """ 배달원 클래스 """
    company_name = "코드잇 버거"    # 가게이름
    rasie_percentage = 1.03        # 시급 인상률

    def __init__(self, name, wage, on_standby=True):
        self.name = name                            # 이름 
        self.wage = wage                            # 시급
        self.on_standby = on_standby                # 대기 상태
    
    def raise_pay(self):
        """시급을 인상한다. """
        self.wage *= self.rasie_percentage

    def deliver(self, address):
        """ 배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 설명 메시지를 출력한다."""
        if self.on_standby:
            print(address+'로 배달 나갑니다!')
            self.on_standby = False
        else: 
            print('이미 배달하러 나갔습니다.')

    def back(self):
        """배달원을 복귀 처리한다. """
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: "+ self.name

taeho = DeliveryMan('성태호', 7000, True)

taeho.raise_pay()
print(taeho.wage)

taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

taeho.back()
taeho.deliver("서울시 코드잇로 51 최고 건물 402호")

print(taeho)

"""
위에서 두개의 클래스를 각각 만들었지만 중복되는 부분이 있습니다. 

중복되는 부분 : 클래스 변수 , 인스턴스 변수, 인스턴스 메소드 

이를 해결 할 수 있는 방법이 바로 ~~~~! 상속입니다. 


"""