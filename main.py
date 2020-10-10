import random
print("タイトル名を入力してください")
Title = input()
print("何番勝負ですか？")
N = input()
print("タイトルホルダーの名前を入力してください")
Player1 = input()
print("挑戦者の名前を入力してください")
Player2 = input()
print("棋戦名:" + Title + str(N) + "番勝負")
print("対局者:" + Player1 + "対" + Player2 + "の対局となりました")
NeedWins = int(N) // 2 + 1
print(str(NeedWins) + "勝が必要になります")
Game = 1
senteFLG = 0
Player1Wins = 0
Player2Wins = 0
Winner = "hoge"
while Player1Wins != NeedWins and Player2Wins != NeedWins:
    print("第" + str(Game) + "局を開始します")
    if Game == 1 or Game == int(N):
        print("振り駒です")
        Hurigoma = random.randint(0,1)
        if Hurigoma == 0:
            print(Player1 + "の先手番でお願いします")
        else:
            print(Player2 + "の先手番でお願いします")
    print("それではよろしくお願いします。")
    print(Player1 + "と" + Player2 + "のうち、勝者を入力してください。")
    Winner = input()
    if Winner == Player1:
        Player1Wins += 1
        Game += 1
    elif Winner == Player2:
        Player2Wins += 1
        Game += 1
    else:
        print("入力エラーです。もう一度入力をお願いします。")
    Winner = "hoge"
    print("ただいま、" + Player1 + str(Player1Wins) + "-" + str(Player2Wins) + Player2 + "となっております")
if Player1Wins == NeedWins:
    print(str(Player1Wins) + "-" + str(Player2Wins) + "で、" + Player1 + "が防衛を決めました。")
else:
    print(str(Player1Wins) + "-" + str(Player2Wins) + "で、" + Player2 + "が奪取を決めました。")
    #羽生さんがんばれ
