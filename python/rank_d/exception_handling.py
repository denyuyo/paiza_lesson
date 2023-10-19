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

# いろいろな形式で例外に対応しよう

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    # print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)

# 発生させる例外を変えてみよう

print(1)
try:
    number = 1
    answer = 100 / number
    print(answer2)
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
finally:
    print(2)

# 複数の例外を捕捉してみよう

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer2)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
finally:
    print(2)