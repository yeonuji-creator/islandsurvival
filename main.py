'''
이것저것 수정함 :3 막 제작이라던가.. 사냥이라던가~ 인벤토리 이런거도 만들어보쟈! 엔딩도!
'''



import pygame
import time
import random

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

    if motion == '3':
        print("아무것도 안하고 쉽니다.")

        time.sleep(1)

        #아래의 식사 코드는 선택지와 관계없이 공통으로 실행되어서, 비워놓아도 괜찮음!
    elif motion == '1':
        pass
    elif motion == 's':
        pass










        
        
    #여기서부터 선생님 코드임! 2번 탐험~

    
    elif motion == "2":

        BAG_CAPACITY = 30

        def remaining_space(bag):
            return BAG_CAPACITY - sum(bag.values())

        print("=======================================")
        print("탐험 전 챙길 물건들을 고르시오.")
        bag = {
            '물': 0,
            '고기': 0,
            '목재': 0,
            '돌': 0,
            '풀': 0,
            '가죽': 0,
            '석영': 0,
            '아름다운결정': 0,
            '레전드신기한꽃': 0
        }
        gogame = ""
        while gogame != "a":
            print("=======================================")
            print(f"\n남은 공간: {remaining_space(bag)}\n")
            print(f"1: 물 (남은 갯수 {inventory['물']}개)")
            print(f"2: 고기 (남은 갯수 {inventory['고기']}개)")
            print(f"3: 목재 (남은 갯수 {inventory['목재']}개)")
            gogame = input("\n선택한 물건의 번호와 갯수를 입력하시오(예 1,2)\n시작하려면 a를 입력하세요.\n: ")
            if gogame == "a":
                print("=======================================")
                onebyone("탐험을 시작합니다.")
                break
            if "," not in gogame:
                print("=======================================")
                print("잘못된 입력입니다. 다시 입력하세요.")
                continue
            num_item, num_quantity = gogame.split(",", 1)
            if not num_item in ['1', '2', '3'] or not num_quantity.isdigit():
                print("=======================================")
                print("잘못된 입력입니다. 다시 입력하세요.")
                continue
            num_item = int(num_item)
            num_quantity = int(num_quantity)
            if num_quantity <= 0:
                print("=======================================")
                print("수량은 1 이상이어야 합니다.")
                continue

            item_map = {1: '물', 2: '고기', 3: '목재'}
            
            item_name = item_map[num_item]
            if inventory[item_name] < num_quantity:
                print("=======================================")
                print(f"{item_name}이(가) 부족합니다.")
                continue

            if num_quantity > remaining_space(bag):
                print("=======================================")
                print("넣을 공간이 없습니다.")
                continue

            inventory[item_name] -= num_quantity
            bag[item_name] += num_quantity
            print("=======================================")
            print(f"{item_name} {num_quantity}개를 챙겼습니다.")

        location = {
            '숲': {
                '자원': ['물', '목재', '풀'],
                '동물': ['토끼', '조금큰토끼', '왕토끼', '사슴', '늑대']
            },
            '강': {
                '자원': ['물', '목재', '풀'],
                '동물': ['물고기', '개구리', '황소개구리', '수달', '피라니아']
            },
            '호수': {
                '자원': ['물', '목재', '풀', '석영'],
                '동물': ['개구리', '물고기', '잉어', '비단잉어', '여기있으면절대안되는아주아주무서운괴물']
            },
            '해변': {
                '자원': ['물', '목재', '돌'],
                '동물': ['게', '물고기', '왕물고기', '거북이', '상어']
            },
            '산': {
                '자원': ['물', '목재', '돌'],
                '동물': ['산양', '큰산양', '독수리', '바위너구리', '호랑이']
            },
            '동굴': {
                '자원': ['물', '목재', '돌', '석영'],
                '동물': ['박쥐', '큰박쥐', '뱀', '도롱뇽', '곰']
            },
            '뭔가놀랍고신기하고무지개색있는곳': {
                '자원': ['물', '목재','아름다운결정', '레전드신기한꽃'],
                '동물': ['무지개색토끼', '신비로운사슴', '그냥곰']
            }
        }
        lc, lclist = random.choice(list(location.items()))
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
                    if random.random() < 0.7:
                        onebyone(f"당신은 {animal}에게서 도망쳤습니다.")
                        break
                    else:
                        onebyone(f"당신은 {animal}이 눈치채지 못하게 조용히 지나갔습니다.")
                        onebyone("탐험은 계속됩니다.")
                else:
                    onebyone("사냥 중...")
                    time.sleep(0.8)
                    if random.random() < 0.8 - difficulty * 0.1:
                        onebyone(f"당신은 {animal}을 사냥했습니다!")
                        meat = random.randint(1 + difficulty, 5 + difficulty)
                        onebyone(f"고기를 {meat}개 얻었습니다.")
                        take_meat = remaining_space(bag) - meat

                        if remaining_space(bag) <= 0:
                            onebyone("가방이 가득 찼습니다. 고기는 버렸습니다.")
                        elif take_meat < 0:
                            onebyone(f"가방이 가득 찼습니다. {abs(take_meat)}개의 고기만 챙겼습니다.")
                            bag['고기'] += abs(take_meat)
                        else:
                            bag['고기'] += meat

                        leather = random.randint(0 + difficulty, 2 + difficulty)
                        onebyone(f"가죽을 {leather}개 얻었습니다.")
                        take_leather = remaining_space(bag) - leather

                        if remaining_space(bag) <= 0:
                            onebyone("가방이 가득 찼습니다. 가죽은 버렸습니다.")
                        elif take_leather < 0:
                            onebyone(f"가방이 가득 찼습니다. {abs(take_leather)}개의 가죽만 챙겼습니다.")
                            bag['가죽'] += abs(take_leather)
                        else:
                            bag['가죽'] += leather
                        print(f"남은 가방 공간: {remaining_space(bag)}")
                    else:
                        onebyone(f"당신은 {animal}를 놓쳤습니다.")
            else:
                resource_amount = random.randint(1, 5)
                resource = random.choice(lclist['자원'])
                onebyone(f"당신은 {resource}을 {resource_amount}개 발견했습니다!")
                take_resource = remaining_space(bag) - resource_amount

                if remaining_space(bag) <= 0:
                    onebyone("가방이 가득 찼습니다. 자원을 버렸습니다.")
                elif take_resource < 0:
                    onebyone(f"가방이 가득 찼습니다. {abs(take_resource)}개의 {resource}만 챙겼습니다.")
                    bag[resource] += abs(take_resource)
                else:
                    bag[resource] += resource_amount
                print(f"남은 가방 공간: {remaining_space(bag)}")

            if remaining_space(bag) <= 0:
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
                    print(f"남은 가방 공간: {remaining_space(bag)}")
                else:
                    onebyone("너무 추워서 나아갈 수 없습니다.")
                    break
            elif encounter == 2:
                onebyone("당신은 목이 마릅니다...")
                onebyone(f"남은 물: {bag['물']}개")
                if bag['물'] > 0:
                    onebyone("물통을 사용하여 목을 축입니다.")
                    bag['물'] -= 1
                    print(f"남은 가방 공간: {remaining_space(bag)}")
                else:
                    onebyone("목이 말라서 나아갈 수 없습니다.")
                    break
            else:
                onebyone("당신은 배가 고픕니다...")
                onebyone(f"남은 고기: {bag['고기']}개")
                if bag['고기'] > 0:
                    onebyone("고기를 먹어 배를 채웁니다.")
                    bag['고기'] -= 1
                    print(f"남은 가방 공간: {remaining_space(bag)}")
                else:
                    onebyone("배가 고파서 나아갈 수 없습니다.")
                    break
            print("=======================================")

        print("=======================================")
        onebyone("집 가는 중...")
        onebyone("탐험을 마치고 돌아왔습니다.")
        onebyone("다음의 물건을 가지고 왔습니다.")
        print(bag)
        for item_name, item_count in bag.items():
            inventory[item_name] += item_count
        onebyone("인벤토리에 저장 완료.")
    else:
        print("다시 입력하세요.")
        continue

    #아래의 식사 코드는 선택지와 관계없이 공통으로 실행되어서, 비워놓아도 괜찮음!
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
        pygame.mixer.music.load("주금/type.mp3")

        pygame.mixer.music.play()
        time.sleep(0.3)
        
        break
    state['day'] += 1
    state['thirst'] -= 90
