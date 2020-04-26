in_file = open('./vocabulary.txt','r', encoding='utf-8')

for line in in_file:
    data = line.strip().split(': ')
    # english_word = line[]
    answer = input(f'{data[0]}: ')
    if data[1] == answer:
        print('맞았습니다!')
    else:
        print(f'아쉽습니다. 정답은{data[1]}입니다.')
        
in_file.close()