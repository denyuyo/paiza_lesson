# クラスを作成する

class Player:
    def walk(self):
        print("勇者は荒野を歩いていた")
        
    def attack(self, enemy):
        print("勇者は" + enemy + "を、攻撃した")

player1 = Player()
player1.walk()
player1.attack("スライム")

# 変数をクラスで管理する

class Player:
    def __init__(self, job):
        self.job = job
    
    def walk(self):
        print(self.job + "は荒野を歩いていた。")

player1 = Player("戦士")
player1.walk()

player2 = Player("魔法使い")
player2.walk()

player1.walk()

# RPGの敵クラスを作る

class Enemy:
    def __init__(self, name):
        self.name = name
        
    def attack(self):
        print(self.name + "は、勇者を攻撃した")

enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy  in enemies:
    enemy.attack()

