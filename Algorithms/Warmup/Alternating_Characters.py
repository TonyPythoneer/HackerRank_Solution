# -*- coding: utf-8 -*-
#Question:
#給你一個字串，請問要變成字元交替的字串
#一個字串要刪除幾個字元
#---------------------
#Answer:
#抓住第一個字元，存入"比對暫存器"
#下一個字元與第一個不同，則覆寫"比對暫存器"
#否則刪除該字元，並累計"刪除數"
#----------------------
def delete(s):
    length  = len(s)
    start   = s[0]
    del_num = 0
    for letter in s[1:]:
        if start != letter:
            start = letter
        else:
            del_num = del_num +1 
    return del_num
    

loop_num = input()
while loop_num >0:
    string = raw_input()
    print delete(string)
    loop_num = loop_num -1