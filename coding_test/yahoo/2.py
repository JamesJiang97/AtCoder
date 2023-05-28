import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))
    n = int(lines[0])
    S = lines[1:]

    dict_l = {}
    dict_r = {}

    for s in S :
        if len(s) < 2 : continue
        if s[:2] in dict_l:
            dict_l[s[:2]] = max(dict_l[s[:2]], len(s))
        else :
            dict_l.update({s[:2]:len(s)})
        
        if s[-2:] in dict_r:
            dict_r[s[-2:]] = max(dict_r[s[-2:]], len(s))
        else :
            dict_r.update({s[-2:]:len(s)})
    
    # print(dict_l)
    # print(dict_r)

    maxa = -1

    for l in dict_l :
        if l in dict_r :
            t = dict_l[l] + dict_r[l] - 2
            maxa = max(maxa, t)

    print(maxa)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
