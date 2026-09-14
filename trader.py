import random, time
import game_text as g
import pygame

pygame.init()

# 나중에 지우기
inventory = {
        '물': 3,
        '고기' : 3,
        '목재' : 3,
        '돌' : 0,
        '풀' : 0,
        '가죽' : 0,
        '석영' : 0, 
        '아름다운결정' : 0,
        '레전드신기한꽃' : 0,
        '돈' : 0
    }

def sell(inventory):

    trader = random.choice(["빡빡이주민", "친절한말랑말랑괴물", "살아있는쵸코칩쿠키", "항상웃고있는핸드폰"])

    g.onebyone(f"당신은 {trader}을(를) 만났습니다!")

    print(f"당신의 인벤토리: {inventory}")


    

    if trader == "빡빡이주민":
        g.onebyone('빡빡이주민: 안녕하세요!!! 저한테 물건을 팔면 돈을 드리겠습니다.')
        g.onebyone("팔 물건을 고르세요: ", "")
        sell_some = input()
        try:
        
            if inventory[sell_some] > 0:
                g.onebyone("팔 개수를 고르세요.", "")
                sell_num = int(input())

                if sell_num <= inventory[sell_some]:
                    g.onebyone(f"당신은 {sell_some}을(를) 팔았습니다.")
                    inventory[sell_some] -= sell_num

                    inventory["돈"] += sell_num

                else:
                    g.onebyone("아 뭐야!!! 없잖아!!!")

            else:

                g.onebyone("아니!!! 이 사람이 그냥 아무것도 안 팔고 그냥 돈만 가지려고 하네!!!")


        except KeyError:
            g.onebyone("아니 그런 물건이 어딨어!!!")

    elif trader == "친절한말랑말랑괴물":
        g.onebyone("안녕하세요!!! 저는 아무 물건을 팔아주시면 돈을 드리겠습니다.")
        g.onebyone("팔 물건을 고르세요: ")
        sell_some = input()

        try:
            if inventory[sell_some] > 0:
                g.onebyone("팔 개수를 고르세요: ", "")
                sell_num = int(input())


                if sell_num <= inventory[sell_some]:
                    pygame.mixer.music.load("audio/trader.mp3")
                    g.onebyone("감사합니다.")

                    inventory[sell_some] -= sell_num

                    inventory["돈"] += sell_num

                    


                else:
                    g.onebyone("물건이 팔려는 개수만큼 없어요.")


            else:
                g.onebyone("0개는 못 팔아요.")



        except KeyError:
            g.onebyone(f"{sell_some}(이)라는 물건이 없습니다.")


    elif trader == "살아있는쵸코칩쿠키":
        g.onebyone("안녕하세요!!! 저는 아무 물건을 팔아주시면 돈을 드리겠습니다.")
        g.onebyone("팔 물건을 고르세요: ")
        sell_some = input()

        try:
            if inventory[sell_some] > 0:
                g.onebyone("팔 개수를 고르세요: ", "")
                sell_num = int(input())


                if sell_num <= inventory[sell_some]:
                    pygame.mixer.music.load("audio/trader.mp3")
                    g.onebyone("감사합니다.")

                    inventory[sell_some] -= sell_num

                    inventory["돈"] += sell_num

                    


                else:
                    g.onebyone("물건이 팔려는 개수만큼 없잖아.")


            else:
                g.onebyone("0개는 못 팔아.")



        except KeyError:
            g.onebyone(f"{sell_some}(이)라는 물건이 없어.")



    elif trader == "항상웃고있는핸드폰":
        g.onebyone("안녕하세요!!! 저는 아무 물건을 팔아주시면 돈을 드리겠습니다.")
        g.onebyone("팔 물건을 고르세요: ")
        sell_some = input()

        try:
            if inventory[sell_some] > 0:
                g.onebyone("팔 개수를 고르세요: ", "")
                sell_num = int(input())


                if sell_num <= inventory[sell_some]:
                    pygame.mixer.music.load("audio/trader.mp3")
                    g.onebyone("감사합니다.")

                    inventory[sell_some] -= sell_num

                    inventory["돈"] += sell_num

                    


                else:
                    g.onebyone("물건이 팔려는 개수만큼 없잖아.")


            else:
                g.onebyone("0개는 못 팔잖아.")



        except KeyError:
            g.onebyone(f"{sell_some}(이)라는 물건 없잖아.")



    elif trader == "항상웃고있는핸드폰":
        g.onebyone("안녕하세요!!! 저는 아무 물건을 팔아주시면 돈을 드리겠습니다.")
        g.onebyone("팔 물건을 고르세요: ")
        sell_some = input()

        try:
            if inventory[sell_some] > 0:
                g.onebyone("팔 개수를 고르세요: ", "")
                sell_num = int(input())


                if sell_num <= inventory[sell_some]:
                    pygame.mixer.music.load("audio/trader.mp3")
                    g.onebyone("감사합니다.")

                    inventory[sell_some] -= sell_num

                    inventory["돈"] += sell_num

                    


                else:
                    g.onebyone("하하하하.물건이 팔려는 개수만큼 없잖아.")


            else:
                g.onebyone("하하하하.0개는 못 팔잖아.")



        except KeyError:
            g.onebyone(f"하하하하.{sell_some}(이)라는 물건 없잖아.")


    
                

        


sell(inventory)
