f = open('vocabulary.txt', 'w',encoding='utf-8')
# stop = lambda x: break if 'q' == eng else pass

    
while f: 
    eng = input('영어 단어를 입력하세요: ')
    if 'p' == eng:
        break
    kor = input('한국어 뜻을 입력하세요: ')
    # lambda : eng : break if 'q' == eng
    if 'p' == kor:
        break
    f.write(f'{eng}: {kor}\n')
f.close()



# boolean = lambda x: 'True' if x == 2 else 'False'
# print(boolean(2))
while 1: 
    print('dkss')
    break