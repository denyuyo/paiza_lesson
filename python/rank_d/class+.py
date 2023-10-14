class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

class JewelryBox(Box):
    def look(self):
        print("宝箱はキラキラと輝いている。")

box = Box("鋼鉄の剣")
box.open()

jewelrybox = JewelryBox("魔法の指輪")
jewelrybox.look()
jewelrybox.open()

# メソッドのオーバーライド
class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

class MagicBox(Box):
    def look(self):
        print("宝箱は、妖しく輝いている。")
    
    def open(self):
        print("宝箱を開いた。" + self.item + "が襲ってきた!")

box = Box("大根")
box.open()

magicBox = MagicBox("料理人")
magicBox.look()
magicBox.open()

# RPGのプレイヤーを継承で記述１
class Player:
    def __init__(self, name):
        self.name = name
    
    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")
    
print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")

party = [hero, warrior]
for member in party:
    member.attack("スライム")

# RPGのプレイヤーを継承で記述２
class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def attack(self, enemy):
        print("ズバーン！")
        print(self.name + "は、" + enemy + "に炎を放った！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")
wizard = Wizard("魔法使い")

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

# クラスからメソッドを呼び出してみよう
class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")
    
    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")
    
    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
# hero.attack("スライム")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

wizard._Wizard__spell()

# クラス変数とクラスメソッド

class Player:
    __charactor_count = 0
    
    @classmethod
    def summary(cls):
        print(str(Player.__charactor_count) + "人で、スライムを攻撃した。")

    def __init__(self, name):
        self.name = name
        Player.__charactor_count += 1
        print(str(Player.__charactor_count) + "番目のプレーヤー、" + self.name + "が登場した。")

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
        self.__spell()
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

Player.summary()

# 標準ライブラリを読み込んでみよう

from datetime import datetime, timedelta, timezone

jst = timezone(timedelta(hours=9))
today = datetime.now(jst)
print(today)
print(today.year)
print(today.month)
print(today.day)

day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
print(day)

