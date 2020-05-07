# 기능
# 1. 현재 시간을 설정할 수 있다. 
# 2. 현재 시간을 변경할 수 있다. 
# 3. 현재 시간에 1초씩 더 할 수 있다. 

# 위 코드처럼 작동하는 Clock 클래스를 작성한다고 할 때, 어떤 속성과 기능(행동)을, 어떻게 넣어야 할까요?
# 다음 레슨의 설명을 듣기 전에 꼭 스스로 이 부분에 대해 고민해보세요!

class Clock:

    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second

    
    def set(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def tick(self):


clock = Clock(1, 30, 48)

print(clock)