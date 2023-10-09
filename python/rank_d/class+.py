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