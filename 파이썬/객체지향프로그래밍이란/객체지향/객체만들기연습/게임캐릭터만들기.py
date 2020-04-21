class GameCharacter:
    # 게임 캐릭터 클래스
    def __init__(self, name, hp, power):
    # 게임 캐릭터는 속성으로 이름, hp, 공격력을 갖는다
      self.name = name
      self.hp = hp
      self.power = power

    def is_alive(self):
      # 게임 캐릭터가 살아있는지(체력이 0이 넘는지) 확인하는 메소드
      return self.hp > 0

    def get_attacked(self, damage):
      """
      게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
      조건:    
          1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
          2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
      """
      if self.is_alive():
        self.hp = self.hp - damage if self.hp >= damage else 0

      else:
        print("{}님은 이미 죽었습니다.".format(self.name))

    def attack(self, other_character):
      # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
      if self.is_alive():
        other_character.get_attacked(self.power)

    def __str__(self):
      # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다.
      return self.name + "님의 hp는 " + str(self.hp) + "만큼 남았습니다."

# 게임 캐릭터 인스턴스 생성                        
younghoon = GameCharacter("Ww영훈전사wW", 200, 30)
jiwoong = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
younghoon.attack(jiwoong)
# jiwoong.get_attacked(younghoon.power) > jiwoong.hp(70) = jiwoong.hp(100) - younghoon.power(30)

jiwoong.attack(younghoon)
# younghoon.get_attacked(jiwoong.power) > younghoon.hp(150) = younghoon.hp(200) - jiwoong.power(50)

jiwoong.attack(younghoon)
# younghoon.get_attacked(jiwoong.power) > younghoon.hp(100) = younghoon.hp(150) - jiwoong.power(50)

jiwoong.attack(younghoon)
# younghoon.get_attacked(jiwoong.power) > younghoon.hp(50) = younghoon.hp(100) - jiwoong.power(50)

jiwoong.attack(younghoon)
# younghoon.get_attacked(jiwoong.power) > younghoon.hp(0) = younghoon.hp(50) - jiwoong.power(50)

jiwoong.attack(younghoon)
# younghoon.get_attacked(jiwoong.power) > Ww영훈전사wW님은 이미 죽었습니다.


# 게임 캐릭터 인스턴스 출력
print(younghoon)
# Ww영훈전사wW님의 hp는 0만큼 남았습니다.
print(jiwoong)
# Xx지웅최고xX님의 hp는 70만큼 남았습니다.