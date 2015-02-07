# -*- coding: utf-8 -*-
#Question:
#一個超級大蛋糕，你切幾刀而會得最多幾塊?
#---------------------
#Hint:
#1.切5次(橫的2刀，直的3刀)，得6塊
#2.切6次(橫的3刀，直的3刀)，得9塊
#3.以此類推
#---------------------
#Answer:
#找到規則自然好辦事
#----------------------
def cut(k):
    if k>=2 :
        h = k/2
        v = (k+1)/2
        return h*v

loop = input()
while loop >0:
    cut_num = input()
    print cut(cut_num)
    loop = loop -1