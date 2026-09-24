from game_text import onebyone

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

onebyone("당신은 60일차까지 살아남았습니다.")
if inventory['목재'] >= 10:
    onebyone("당신은 남은 목재로 배를 만들고 떠났습니다.")
    onebyone("---끝---")
else:
    onebyone("당신은 목재가 부족합니다.(필요한 목재: 10개)")
    onebyone("목재를 더 모아서 배를 만드시오.")

