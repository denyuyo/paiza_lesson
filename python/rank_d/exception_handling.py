# 簡単な例外処理してみよう

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print(e)
finally:
    print(2)