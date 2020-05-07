class GameCharacter:

    def __init__(self,name,hp,power):
        self.name = name
        self.hp = hp
        self.power = power


    def is_alive(self): 
            return self.hp > 0


    def get_attacked(self,damage):
        # 게임케릭터가 살아있으면 파라미터로받은 다른 케릭의 체력을 자신의 공격력만큼 깍음
            if self.is_alive():
            #     if self.hp >= damage:
            #         self.hp = self.hp - damage
            #     else:
            #         self.hp = 0
            # 위 4줄 한줄로 써보기
                self.hp = self.hp - damage  if self.hp >= damage else 0

            # 아래는 이미 죽었는데 공격을 당한 경우를 보는것.
            else: 
                print(f'{self.name}은 이미 죽었습니다.')


    def attack(self,other_character):
        # 게임케릭터가 살아있으면 파라미터로 받은 다른 케릭터의 체력을 깍는다. 
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        return f'{self.name}님의 hp는 {str(self.hp)}만큼 남았습니다.'

# 게임 캐릭터 인스턴스 생성
character_1 = GameCharacter('Ww영훈전사wW',200,30)
character_2 = GameCharacter('Xx지웅최고xX',100,50)

character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

print(character_1)
print(character_2) 