import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    n = lines[0]
    A = list(lines[1].split())
    # print(n)
    # print(A)

    dict = {}

    for a in A :
        if a in dict :
            dict[a] += 1
        else: 
            dict.update({a:1})
    for v in dict.values() :
        if v >= 4 :
            print('YES')
            return
    
    print('NO')
    return
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
