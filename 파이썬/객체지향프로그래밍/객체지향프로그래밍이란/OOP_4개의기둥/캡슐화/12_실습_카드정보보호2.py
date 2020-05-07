# -*- encoding: utf-8 -*-
"""
이전 과제에서 CreditCard 클래스를 캡슐화했습니다. 이번에는 다른 방법으로 캡슐화를 해봅시다.


CreditCard 클래스의 비밀번호, 카드 한도 인스턴스 변수 이름 앞에 밑줄 한 개를 써서 다른 개발자들에게 해당 변수를 직접 사용하는 것을 자제하라는 표시를 남깁시다. (_password, _payment_limit)

@property를 이용해서 앞에 밑줄 하나를 쓴 변수들을 캡슐화하세요.
    변수 _password
        getter 메소드: 문자열 "비밀 번호는 볼 수 없습니다"를 리턴한다.
        setter 메소드: 파라미터로 받은 값을 변수에 설정한다.
    변수 _payment_limit
        getter 메소드: _payment_limit 변수를 리턴한다.
        setter 메소드: 파라미터로 받은 값을 변수에 설정한다.
            단, setter 메소드에서 파라미터로 받은 값이 0과 MAX_PAYMENT_LIMIT 사이에 있는 값이 아니면 "카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!" 라는 메시지를 출력한다.
"""


class CreditCard:

    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        # 코드를 쓰세요
        self.name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def password(self):
        return '비밀 번호는 볼 수 없습니다.'

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= MAX_PAYMENT_LIMIT:
            self._payment_limit = new_payment_limit
        else: 
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")


card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)