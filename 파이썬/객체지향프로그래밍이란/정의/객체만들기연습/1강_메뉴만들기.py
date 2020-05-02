class MenuItem:

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name} 가격: {self.price}"

hamburger = MenuItem('햄버거','4000')
coke = MenuItem('콜라','1500')
french_fri = MenuItem('후렌치 후라이','1500')

print(hamburger)
print(coke)
print(french_fri)