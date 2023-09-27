# 関数を作る

def say_hello():
    print("hello python")

say_hello()

# 引数と戻り値を追加する

def sum(x, y):
    return x + y
    
num1 = sum(555, 777)
print(num1)
num2 = sum(5555, 7777)
print(num2)

# 九九の表を生成

def multiply(x, y):
    return x * y

for x in range(1, 10):
    for y in range(1, 10):
        result = multiply(x, y)
        print(result, end="")
        if y < 9:
            print(", ", end="")
        else:
            print()

# スコープを理解する

message = "paiza"
a = 10
b = 20

def sum(x, y):
    a = 3
    global message
    message += "paiza"
    print(message + " " + str(a))
    return x + y

num = sum(a, b)
print(num)
print(message + " " + str(a))