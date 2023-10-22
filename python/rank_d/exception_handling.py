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

# raiseで意図的に例外を投げよう

print(1)
try:
    print(2)
    raise Exception("意図的な例外")
    print(3)
except Exception as e:
    print("予期せぬエラーが発生しました")
    print(e)
finally:
    print(4)

# 例外は伝わる

def test_exceptin(number):
    print(2)
    try:
        print(3)
        answer = 100 / number
        return answer
        print(4)
    except ZeroDivisionError as e:
        print(5)
        raise e
    print(6)

print(1)
try:
    answer = test_exceptin(0)
    print(7)
except ZeroDivisionError as e:
    print(8)
    print(e)

# finallyをもっと理解しよう

import sys

def test_exception(number):
    try:
        return 100 / number

    except ZeroDivisionError as e:
        raise e
    finally:
        print("処理が終了しました")


try:
    test_exception(0)

except ZeroDivisionError as e:
    sys.stderr.write('0で割り算できません')
