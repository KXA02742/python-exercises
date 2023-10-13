# FizzBuzz問題
# １から４０までの数字それぞれに対して、以下のような出力を行うプログラムを作成してください
# 3の倍数の時に'Fizz'と出力
# 5の倍数の時に'Buzz'と出力
# 15の倍数の時に'FizzBuzz'と出力
# 上記以外の時は、そのまま数字を出力
# なお、数字を引数で渡すと、出力する文字列を返却するfizzbuzz関数を作成して、それを用いてプログラムを作成してください

def fizzbuzz(n):
    # 以下を実装してプログラムを完成させてください
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

n = 40
for i in range(1, n+1):
    print(i,fizzbuzz(i),sep=": ")