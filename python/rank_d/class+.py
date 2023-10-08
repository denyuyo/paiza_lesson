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