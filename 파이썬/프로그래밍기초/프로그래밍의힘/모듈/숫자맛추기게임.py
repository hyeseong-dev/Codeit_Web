from random import randint

answer = randint(1,20)

chance = 4
tries = 1

while tries<= 4:
    guess = int(input(f'기회가 {tries}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: '))
    if answer > guess:
        print('Up')
    
    elif answer < guess:
        print('Down')
    

    elif answer == guess:
        print(f'축하합니다. {tries}번만에 숫자를 맞추셨습니다.')
        break

    elif chance == 0:
        print(f'아쉽습니다. 정답은 {answer}였습니다.')
        break
    tries += 1
    chance -=1