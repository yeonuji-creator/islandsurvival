import pygame
import time

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
""", end = "")

