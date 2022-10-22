s = input()

if s[0] == '1' : print('No')
else:
    tag = []

    if s[6] == '1' : tag.append(1)
    else : tag.append(0)

    if s[3] == '1' : tag.append(1)
    else : tag.append(0)

    if s[1] == '1' or s[7] == '1' : tag.append(1)
    else : tag.append(0)

    if s[4] == '1' : tag.append(1)
    else : tag.append(0)

    if s[2] == '1' or s[8] == '1' : tag.append(1)
    else : tag.append(0)

    if s[5] == '1' : tag.append(1)
    else : tag.append(0)

    if s[9] == '1' : tag.append(1)
    else : tag.append(0)

    #print(tag)

    flag1 = 0

    flag2 = 0

    flag3 = 1

    for x in tag :
        if x == 1 : flag1 = 1
        if x == 0 and flag1 == 1 : flag2 = 1
        if x == 1 and flag1 and flag2 : 
            print('Yes') 
            flag3 = 0
            break
        #print(str(x) + " " + str(flag1) + str(flag2))

    if flag3 : print('No')



