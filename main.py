'''
약간 어렵네요
'''



import pygame
import time
import random

pygame.init()



state = {"day":1, "thirst":100}

inventory = {
        '식수': 3,
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
        #pygame.mixer.music.load("audio/type.mp3")

        #pygame.mixer.music.play()
        time.sleep(0.3)
        

    print(s_end, end = '')




onebyone("당신의 닉네임을 입력하십시오: ",'')
name = input()

state["name"] = name

print("당신은 아주 큰 쓰나미에 휩쓸려서 무인도에 왔습니다. 생존하세요.")


print("""플레이 방법:
상태 보기: s

""")

while True:
    motion = input(f"""{state['day']}일차: 할 행동을 고르시오.
    1: 사냥
    2: 탐험
    3: 아무것도 안 하고 쉬기
    """)

    if motion == '1':
        pass
    elif motion == '3':
        pass











        
        
    #여기서부터 선생님 코드임! 2번 탐험~
    elif motion == "2":
        print("=======================================")
        print("탐험 전 챙길 물건들을 고르시오.")
        bagsize = 30
        bag = {
        '식수': 0,
        '고기' : 0,
        '목재' : 0,
        '돌' : 0,
        '풀' : 0,
        '가죽' : 0,
        '석영' : 0, 
        '아름다운결정' : 0,
        '레전드신기한꽃' : 0
    }
        gogame = ""
        while gogame != "a":
            
            print(f"\n남은 공간: {bagsize}\n")
            print(f"1: 식수 (남은 갯수 {inventory['식수']}개)")
            print(f"2: 고기 (남은 갯수 {inventory['고기']}개)")
            print(f"3: 목재 (남은 갯수 {inventory['목재']}개)")
            gogame = input("\n선택한 물건의 번호와 갯수를 입력하시오(예 1,2)\n시작하려면 a를 입력하세요.\n: ")
            if gogame[0] == "1":
                if inventory['식수'] >= int(gogame[2]):
                    inventory['식수'] -= int(gogame[2])
                    bag['식수'] += int(gogame[2])
                    bagsize -= int(gogame[2])
                else:
                    print("식수가 없습니다.")
            elif gogame[0] == "2":
                if inventory['고기'] >= int(gogame[2]):
                    inventory['고기'] -= int(gogame[2])
                    bag['고기'] += int(gogame[2])
                    bagsize -= int(gogame[2])
                else:
                    print("고기가 없습니다.")
            elif gogame[0] == "3":
                if inventory['목재'] >= int(gogame[2]):
                    inventory['목재'] -= int(gogame[2])
                    bag['목재'] += int(gogame[2])
                    bagsize -= int(gogame[2])
                else:
                    print("목재가 없습니다.")
        print("=======================================")
        onebyone("탐험을 시작합니다.")

        location = {
            '숲' :{
                '자원': ['목재', '풀', '식수'], 
                '동물': ['토끼', '조금큰토끼', '왕토끼', '사슴', '늑대']
                },
            '해변':{
                '자원': ['목재', '돌', '식수'], 
                '동물': ['게', '물고기', '왕물고기', '거북이', '상어']
                }, 
            '동굴':{"자원": ['돌', '석영', '식수', '목재'], 
                '동물': ['박쥐', '큰박쥐', '뱀', '도롱뇽','곰']
                }, 
            '산':{
                '자원': ['돌', '목재', '식수'],
                '동물': ['산양', '큰산양', '독수리', '바위너구리', '호랑이']
                }, 
            '강':{'자원': ['식수', '풀', '목재'], 
                '동물': ['물고기', '개구리', '황소개구리', '수달','피라니아']
                }, 
            '호수':{'자원': ['식수', '목재', '풀', '석영'], 
                '동물': ['개구리', '물고기', '잉어', '비단잉어','여기있으면절대안되는아주아주무서운괴물']
                }, 
            '뭔가놀랍고신기하고무지개색있는곳':{
                '자원': ['아름다운결정','레전드신기한꽃'], 
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
                        onebyone(f"고기를 {meat}개 얻었습니다.")
                        bagsize -= meat
                        if bagsize < 0:
                            onebyone(f"가방이 가득 찼습니다. 남은 {bagsize * -1}개의 고기는 버렸습니다.")
                            meat += bagsize
                            bagsize = 0
                            bag['고기'] += meat
                        else:
                            bag['고기'] += meat
                        leather = random.randint(0+difficulty, 3 + difficulty)
                        onebyone(f"가죽을 {leather}개 얻었습니다.")
                        bagsize -= leather

                        if bagsize < 0:
                            onebyone(f"가방이 가득 찼습니다. 남은 {bagsize * -1}개의 가죽은 버렸습니다.")
                            leather += bagsize
                            bagsize = 0
                            bag['가죽'] += leather
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
                    bag[sourse] += numlc
                    bagsize = 0
                else:
                    bag[sourse] += numlc
                    bagsize -= numlc


            if bagsize <= 0:
                onebyone("가방이 가득 찼습니다. 탐험을 종료합니다.")
                break
            choice = ""
            while True:
                print("계속 나아가시겠습니까 (y/n)?")
                choice = input().lower()
                if choice == 'n':
                    break
                elif choice == 'y':
                    break
                else:
                    print("잘못된 입력입니다. 다시 입력하세요.")
            if choice == 'n':
                break

            encounter = random.choice([1, 2, 3])
            if encounter == 1:
                onebyone("당신은 춥습니다...")
                onebyone(f"남은 목재: {bag['목재']}개")
                if bag['목재'] > 0:
                    onebyone("목재를 태워 몸을 녹입니다.")
                    bag['목재'] -= 1
                    bagsize -= 1
                else:
                    onebyone("너무 추워서 나아갈 수 없습니다.")
                    break
            elif encounter == 2:
                onebyone("당신은 목이 마릅니다...")
                onebyone(f"남은 식수: {bag['식수']}개")
                if bag['식수'] > 0:
                    onebyone("물통을 사용하여 목을 축입니다.")
                    bag['식수'] -= 1
                    bagsize -= 1
                else:
                    onebyone("목이 말라서 나아갈 수 없습니다.")
                    break
            else:
                onebyone("당신은 배가 고픕니다...")
                onebyone(f"남은 고기: {bag['고기']}개")
                if bag['고기'] > 0:
                    onebyone("고기를 먹어 배를 채웁니다.")
                    bag['고기'] -= 1
                    bagsize -= 1
                else:
                    onebyone("배가 고파서 나아갈 수 없습니다.")
                    break
            print("=======================================")

        print("=======================================")
        onebyone("집 가는 중...")
        onebyone("탐험을 마치고 돌아왔습니다.")
        onebyone("다음의 물건을 가지고 왔습니다.")
        print(bag)
        for name, item in bag.items():
            inventory[name] += item
        onebyone("인벤토리에 저장 완료.")
        print("=======================================")

        onebyone("식사를 하고 하루를 마칩니다. (식수, 목재, 고기 하나씩 필요.)")
        print(f"\n가지고 있는 양 : [ 식수 :{inventory['식수']}, 목재 : {inventory['목재']}, 고기 : {inventory['고기']}]\n")

        if inventory['고기'] > 0 and inventory['식수'] > 0 and inventory['목재']:
            onebyone("당신은 고기를 구워먹고 물도 마셨습니다.")
            
            inventory['식수'] -= 1
            inventory['목재'] -= 1
            inventory['고기'] -= 1
        else:
            onebyone("저런... 당신은 죽었습니다. 안녕.")
            break
        state['day'] += 1
        state['thirst'] -= 90
        print("=======================================\n\n")
    else:
        print("다시 입력하세요.")
