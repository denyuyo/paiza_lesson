# 2次元リスト

player = "忍者"
team_a = [player, "戦士", "魔法使い"]
print(team_a)
print(team_a[1])

team_b = [team_a[0], team_a[1], team_a[2]]
print(team_b)
print(team_b[0])

team_c = ["勇者", "戦士", "魔法使い"]
team_d = ["盗賊", "忍者", "商人"]
team_e = ["スライム", "ドラゴン", "魔王"]

teams = [team_c, team_d, team_e]
print(teams)
print(teams[1])
print(teams[2][0])
print(teams[2][1])
print(teams[2][2])

# 2次元リスト 基本操作1

teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
print(teams)
print(teams[0])
print(teams[0][0])
print(teams[0][1])

teams[0][1] = "魔導士"
print(teams)
print(len(teams))
print(len(teams[0]))

# 2次元リスト 基本操作

teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
print(teams)

teams.append(["メタルモンスター", "シルバーモンスター", "ブラックモンスター"])
print(teams)
print(len(teams))

teams[0].append("レッドドラゴン")
print(teams)
print(len(teams))
print(len(teams[0]))

del teams[1]
print(teams)
print(len(teams))

del teams[0][1]
print(teams)
print(len(teams))
print(len(teams[0]))

# ループ リスト処理
team = ["勇者", "戦士", "魔法使い"]
print(team)
print(team[0])

for (i, person) in enumerate(team):
    print(str(i + 1) + "番目の" + person + "が、スライムと戦った")

numbers = [3, 1, 4, 1, 5]
results = []
for item in numbers:
    results.append(item * 10)
    
print(results)