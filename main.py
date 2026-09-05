'''
이것저것 수정함 :3 막 제작이라던가.. 사냥이라던가~ 인벤토리 이런거도 만들어보쟈! 엔딩도!
'''



import pygame
import time
import random
import motion2
from game_text import onebyone

pygame.init()



state = {"day":1, "thirst":100}

inventory = {
        '물': 3,
        '고기' : 3,
        '목재' : 3,
        '돌' : 0,
        '풀' : 0,
        '가죽' : 0,
        '석영' : 0, 
        '아름다운결정' : 0,
        '레전드신기한꽃' : 0
    }

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

onebyone("당신은 아주 큰 쓰나미에 휩쓸려서 무인도에 왔습니다. 생존하세요.\n")


print("""플레이 방법:
상태 보기: s

""")

while True:
    print("=======================================\n\n")
    motion = input(f"""{state['day']}일차: 할 행동을 고르시오.
    1: 사냥
    2: 탐험
    3: 아무것도 안 하고 쉬기
""")

    if motion == '1':
        pass
    elif motion == 's':
        pass
            
    elif motion == '3':
        print("아무것도 안하고 쉽니다.")
        time.sleep(1)
 
    #개발 완료
    elif motion == "2":
        motion2.start_motion2(inventory)

    else:
        print("다시 입력하세요.")
        continue

    print("=======================================")
    onebyone("식사를 하고 하루를 마칩니다.)")
    print("(물, 목재, 고기 하나씩 필요.)")
    print(f"\n가지고 있는 양 : [ 물 :{inventory['물']}, 목재 : {inventory['목재']}, 고기 : {inventory['고기']}]\n")

    if inventory['고기'] > 0 and inventory['물'] > 0 and inventory['목재']>0:
        onebyone("당신은 고기를 구워먹고 물도 마셨습니다.")
        
        inventory['물'] -= 1
        inventory['목재'] -= 1
        inventory['고기'] -= 1
    else:
        onebyone("저런... 당신은 죽었습니다. 안녕.")
        break
    state['day'] += 1
    state['thirst'] -= 90
        
pygame.mixer.music.load("audio/주금.mp3")        
pygame.mixer.music.play()
