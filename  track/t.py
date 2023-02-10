import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    # print(lines)
    n = lines[0]
    lines = lines[1:]
    dict = {}

    for i in range(int(n)):
        key, value = map(int, lines[i].split(" "))        
        values = dict.get(key)
        if values == None :
            dict.update({key:[value]})
        else : 
            values.append(value)
            dict.update({key:values})

    res = 0

    dl = len(dict)

    # print(dict)

    while(dl>0):
        kv = dict.popitem()
        dl -= 1
        key = kv[1].pop()
        value = kv[0]

        if len(kv[1]) != 0:
            dict.update({kv[0]:kv[1]})
            dl += 1

        values = dict.get(key)
        
        if values != None :
            if value in values :
                res += 1
                values.remove(value)
                if len(values) == 0 :
                    del dict[key]
                    dl -= 1
                else : dict.update({key:values})
        
        # print(dict)
    
    print(res)
        
        


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)