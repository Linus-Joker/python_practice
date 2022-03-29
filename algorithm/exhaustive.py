string_t = "ababcabc"

string_p = "abc"

for i in range(len(string_t)):

    find = True
    for j in range(len(string_p)):
        if(string_t[i+j] != string_p[j]):
            find = False
            # print(i+j, "and ", j, "postion not match.")
            break
    if find:
        print("從第", i, "個位置開始吻合")
