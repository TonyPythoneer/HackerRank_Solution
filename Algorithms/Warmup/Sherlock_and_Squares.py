# -*- coding: utf-8 -*-
#Question:
#我們會得到他到一個平方數，例如:1、4、9、16
#是由1、2、3、4等數字平方而來
#接著福爾摩斯要從這些輸入和輸出的規則性，推導背後架構
#---------------------
#Answer:
#兩數各開根號相減
#----------------------
from math import *

testcases = input()
for testcase in range(testcases) :
    a,b = [ int(i) for i in raw_input().split(" ") ]
    print int(floor(sqrt(b)) - ceil(sqrt(a)) + 1 )
