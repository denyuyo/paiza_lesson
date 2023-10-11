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