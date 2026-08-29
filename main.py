'''
이것저것 추가해봣음! 가져간 물건에 따라 발생하는 이벤트도 넣을 예정
'''



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
    ready = {'물통': 5, '육포': 7, '횃불': 3}
    bagsize = 20
    bag = {'물통': 0, '육포': 0, '횃불': 0}
    gogame = ""
    while gogame != "a":
        
        print(f"\n남은 공간: {bagsize}\n")
        print(f"1: 물통 (남은 갯수 {ready['물통']}개)")
        print(f"2: 육포 (남은 갯수 {ready['육포']}개)")
        print(f"3: 횃불 (남은 갯수 {ready['횃불']}개)")
        gogame = input("\n선택한 물건의 번호와 갯수를 입력하시오(예 1,2)\n시작하려면 a를 입력하세요.\n: ")
        if gogame[0] == "1":
            if ready['물통'] > int(gogame[2]):
                ready['물통'] -= int(gogame[2])
                bag['물통'] += int(gogame[2])
                bagsize -= int(gogame[2])
            else:
                print("물통이 없습니다.")
        elif gogame[0] == "2":
            if ready['육포'] > int(gogame[2]):
                ready['육포'] -= int(gogame[2])
                bag['육포'] += int(gogame[2])
                bagsize -= int(gogame[2])
            else:
                print("육포가 없습니다.")
        elif gogame[0] == "3":
            if ready['횃불'] > int(gogame[2]):
                ready['횃불'] -= int(gogame[2])
                bag['횃불'] += int(gogame[2])
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
            '동물': ['박쥐', '뱀', '도롱뇽','곰']
            }, 
        '산':{
            '자원': ['돌', '나무', '석영', '부싯돌','열매'],
            '동물': ['산양', '독수리', '바위너구리', '호랑이']
            }, 
        '강':{'자원': ['물', '부들', '연꽃'], 
            '동물': ['물고기', '개구리', '수달','피라니아']
            }, 
        '호수':{'자원': ['물', '풀','열매'], 
            '동물': ['개구리', '물고기', '물고기', '물고기','여기있으면절대안되는아주아주무서운괴물']
            }, 
        '뭔가놀랍고신기하고무지개색있는곳':{
            '자원': ['신비롭고뭔지모를돌', '신비로운풀', '신기한꽃'], 
            '동물': ['무지개색토끼', '신비로운사슴', '그냥곰']
            }
        }
    lc, lclist = random.choice(list(location.items()))
    numlc = random.randint(1, 5)
    onebyone(f"당신은 {lc}에 도착했습니다.")
    
    while True:
        onebyone("주변을 탐험합니다...")
        time.sleep(0.5)
        onebyone("탐험 중...")
        time.sleep(0.5)
        if random.random() < 0.4:
            animal = random.choice(lclist['동물'])
            onebyone(f"당신은 {animal}을 발견했습니다!")
            difficulty = lclist['동물'].index(animal)
            if lclist['동물'][-1] == animal:
                onebyone(f"당신은 {animal}에게서 도망쳤습니다.")
                break
            else:
                onebyone("사냥 중...")
                time.sleep(0.8)
                if random.random() < 0.8 - difficulty * 0.1:
                    onebyone(f"당신은 {animal}을 사냥했습니다!")
                    meat = random.randint(1+difficulty, 5 + difficulty)
                    onebyone(f"고기를{meat}개 얻었습니다.")
                    bagsize -= meat
                    if bagsize < 0:
                        onebyone(f"가방이 가득 찼습니다. 남은 {bagsize * -1}개의 고기는 버렸습니다.")
                        meat += bagsize
                        bagsize = 0
                        bag['고기'] = meat
                    else:
                        bag['고기'] += meat
                    leather = random.randint(0+difficulty, 3 + difficulty)
                    onebyone(f"가죽을{leather}개 얻었습니다.")
                    bagsize -= leather

                    if bagsize < 0:
                        onebyone(f"가방이 가득 찼습니다. 남은 {bagsize * -1}개의 가죽은 버렸습니다.")
                        leather += bagsize
                        bagsize = 0
                        bag['가죽'] = leather
                    else:
                        bag['가죽'] += leather
                        bagsize -= leather
                else:
                    onebyone(f"당신은 {animal}를 놓쳤습니다.")
        else:
            numlc = random.randint(1, 5)
            sourse = random.choice(lclist['자원'])
            onebyone(f"당신은 {sourse}을 {numlc}개 발견했습니다!")
            bagsize -= numlc
            if bagsize < 0:
                onebyone(f"가방이 가득 찼습니다. 남은 {bagsize * -1}개의 {sourse}은 버렸습니다.")
                numlc += bagsize
                bag[sourse] = numlc
                bagsize = 0
            else:
                bag[sourse] += numlc
                bagsize -= numlc


        if bagsize <= 0:
            onebyone("가방이 가득 찼습니다. 탐험을 종료합니다.")
            break
        choice = ""
        while True:
            onebyone("계속 나아가시겠습니까 (y/n)?")
            choice = input().lower()
            if choice == 'n':
                break
            elif choice == 'y':
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")
        if choice == 'n':
            break
print("=======================================")
onebyone("집 가는 중...")
onebyone("탐험을 마치고 돌아왔습니다.")
