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

# 2次元リストをforで作成する

numbers = [i * 2 for i in range(10)]
print(numbers)
print(len(numbers))

numbers2 = [[1 for i in range(3)] for j in range(4)]
numbers2[0][1] = 2
print(numbers2)

# ドット絵を表示する

enemy_img = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]

for line in enemy_img:
    for dot in line:
        if dot == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

# 3次元リストでドット絵を表示する

enemy_img = [[[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
              [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
              [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
              [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]],
             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
              [1,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1],
              [1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0]],
             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
              [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],
              [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
              [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]],
             [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
              [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
              [1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1],
              [1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,1],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0],
              [1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0]]]

for img in enemy_img:
    for line in img:
        for dot in line:
            if dot == 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()

# 2次元リストで地図を表示する

landmap = [["森" for i in range(20)] for j in range(10)]
landmap[0][0] = "城"
landmap[0][19] = "町"
landmap[9][19] = "町"
for i,line in enumerate(landmap):
    print(str(i) + ":", end="")
    for area in line:
        print(area, end="")
    print()

# 2次元リストで地図を表示する[2]

landmap = [["森" for i in range(20)] for j in range(10)]
landmap[0][0] = "城"
landmap[0][19] = "町"
landmap[9][19] = "町"
for i,line in enumerate(landmap):
    print(str(i) + ":", end="")
    for j,area in enumerate(line):
        if (i % 2 == 0 or j % 3 == 0) and area == "森":
            print("＋", end="")
        else:
            print(area, end="")
    print()