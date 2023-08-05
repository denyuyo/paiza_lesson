# 1 ~ N の整数を 1 から順に改行区切りで出力

n = int(input())

for i in range(1, n+1):
    print(i)
    
# FizzBuzz

for i in range(1, 101):
 if i % 3 == 0 and i % 5 == 0:
     print("FizzBuzz")
 elif i % 3 == 0:
     print("Fizz")
 elif i % 5 == 0:
     print("Buzz")
 else:
     print(i)