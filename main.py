import pygame
import time
import random

pygame.init()


state = {"day":1, "thirst":100}

def onebyone(sentence, s_end = '\n'):
    for i in sentence:
        print(i, end="", flush = True)
        pygame.mixer.music.load("audio/type.mp3")

        pygame.mixer.music.play()
        time.sleep(0.3)
        

    print(s_end, end = '')




onebyone("당신의 닉네임을 입력하십시오: ",'')
name = input()

state["name"] = name

print("당신은 아주 큰 쓰나미에 휩쓸려서 무인도에 왔습니다. 생존하세요.")


print("""플레이 방법:
상태 보기: s

""")

motion = input(f"""{state['day']}일차: 할 행동을 고르시오.
1: 사냥
2: 탐험
3: 아무것도 안 하고 쉬기
""")

#선생님 코드임!
if motion == "2":
    print("=======================================")
    print("탐험 전 챙길 물건들을 고르시오.")
    bag = {'water': 5, 'jerky': 7, 'torch': 3}
    bagsize = 20
    gogame = ""
    while gogame != "a":
        
        print(f"\n남은 공간: {bagsize}\n")
        print(f"1: 물통 (남은 갯수 {bag['water']}개)")
        print(f"2: 육포 (남은 갯수 {bag['jerky']}개)")
        print(f"3: 횃불 (남은 갯수 {bag['torch']}개)")
        gogame = input("\n선택한 물건의 번호와 갯수를 입력하시오(예 1,2)\n시작하려면 a를 입력하세요.\n: ")
        if gogame[0] == "1":
            if bag['water'] > int(gogame[2]):
                bag['water'] -= int(gogame[2])
                bagsize -= int(gogame[2])
            else:
                print("물통이 없습니다.")
        elif gogame[0] == "2":
            if bag['jerky'] > int(gogame[2]):
                bag['jerky'] -= int(gogame[2])
                bagsize -= int(gogame[2])
            else:
                print("육포가 없습니다.")
        elif gogame[0] == "3":
            if bag['torch'] > int(gogame[2]):
                bag['torch'] -= int(gogame[2])
                bagsize -= int(gogame[2])
            else:
                print("횃불이 없습니다.")
    print("=======================================")
    print("탐험을 시작합니다.")

    location = {
        '숲' :{
            '자원': ['나무', '풀', '꽃', '버섯', '열매'], 
            '동물': ['토끼', '사슴', '늑대']
            },
        '해변':{
            '자원': ['해초', '조개'], 
            '동물': ['게', '물고기', '거북이', '상어']
            }, 
        '동굴':{"자원": ['돌', '석영', '부싯돌','신비롭고뭔지모를돌'], 
            '동물': ['박쥐', '뱀', '곰']
            }, 
        '산':{
            '자원': ['돌', '나무', '석영', '부싯돌','열매'],
            '동물': ['산양', '호랑이', '독수리']
            }, 
        '강':{'자원': ['물', '부들', '연꽃'], 
            '동물': ['물고기', '개구리', '수달']
            }, 
        '호수':{'자원': ['물', '풀','열매'], 
            '동물': ['개구리']
            }, 
        '뭔가놀랍고신기하고무지개색있는곳':{
            '자원': ['무지개색돌', '신비로운풀', '신기한꽃'], 
            '동물': ['무지개색토끼', '신비로운사슴', '신기한곰']
            }
        }
    lc, lclist = random.choice(list(location.items()))
    numlc = random.randint(1, 5)
    onebyone(f"당신은 {lc}에 도착했습니다.")
    onebyone("주변을 탐험합니다...")
    time.sleep(0.5)
    onebyone("탐험 중...")
    time.sleep(0.5)
    if random.random() < 0.3:
        animal = random.choice(lclist['동물'])
        onebyone(f"당신은 {animal}을 발견했습니다!")
        if lclist['동물'][-1] == animal:
            onebyone(f"당신은 {animal}에게서 도망쳤습니다.")
        else:
            onebyone("사냥 중...")
            time.sleep(0.8)
            if random.random() < 0.5:
                onebyone(f"당신은 {animal}을 사냥했습니다!")
            else:
                onebyone(f"당신은 {animal}를 놓쳤습니다.")
    else:
        numlc = random.randint(1, 5)
        onebyone(f"당신은 {random.choice(lclist['자원'])}을 {numlc}개 발견했습니다!")
