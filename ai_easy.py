import random

def ai(a):
    
    arr = [] # arr은 한줄씩 저장함 'O' 와 'X' 그리고 ' '를 저장하는 변수
             # 탐색 루프가 한번 돌면 빈 리스트로 초기화됨


    # 가로줄 탐색
    for i in range(0,9,3):
        for j in range(0,3,1):
            arr.append(a[i+j])
            if (arr.count('X')==2 and arr.count(' ')==1)or(arr.count('O')==2 and arr.count(' ')==1): 
                return i+j-2+arr.index(' ')
        arr = [] # 빈리스트로 초기화


    # 세로줄 탐색
    for i in range(0,3,1):
        for j in range(0,9,3):
            arr.append(a[i+j])
            if (arr.count('X')==2 and arr.count(' ')==1)or(arr.count('O')==2 and arr.count(' ')==1):
                return i+j+(-3)*(2-arr.index(' '))
        arr = [] # 빈리스트로 초기화
    
    # 대각선 탐색
    for i in range(0,9,4):
        arr.append(a[i])
        if (arr.count('X')==2 and arr.count(' ')==1)or(arr.count('O')==2 and arr.count(' ')==1):
            return arr.index(' ')*4
    arr = []  # 빈리스트로 초기화


    # 대각선 탐색
    for i in range(2,7,2):
        arr.append(a[i])
        if (arr.count('X')==2 and arr.count(' ')==1)or(arr.count('O')==2 and arr.count(' ')==1):
            return arr.index(' ')*2+2     
    arr = []  # 빈리스트로 초기화


    # 1번째 수에따른 2번째수의 위치 결정
    # 선택지가 많을경우 Ramdom으로 배정

    if a.count('O')==2: # 배열 a의 기존 "O"한개 + 첫수를 뒀을때의 'O'한개
        if a.index('O') == 0 or a.index('O') == 2 or a.index('O') == 6 or a.index('O') == 8 :
            return 4
        elif a.index('O')==4:
            return random.randrange(0,2)*6+random.randrange(0,2)*2
        else :
            return 4
    else: # 두번째 수 부터는 랜덤으로 배정 (위쪽 코드에서 한줄씩 탐색을 거치고 난후)
        while True:
            random_num = random.randrange(0,9)
            if a[random_num]==' ':
                return random_num


# easy 버전
def easy(a):
    while True:
        random_num = random.randrange(0,9)
        if a[random_num]==' ':
            return random_num