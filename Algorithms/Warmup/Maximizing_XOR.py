# -*- coding: utf-8 -*-
#Question:
#輸入L和R，找X⊕X最大值
#
#Constraints:
#1.X範圍為L<=X<=R
#2.⊕=xor
#---------------------
#Answer:
#1.(如正文)用雙迴圈列出所有組合可能性做XOR
#2.如果知道使用itertools的combinations的話，程式碼會更短
#----------------------
def  maxXor( l,  r):
    max = 0
    for i in range(l,r+1):
        for j in range(l,r+1):
            result = int(bin(i),2) ^ int(bin(j),2)
            if max < result:
                max = result
    return max

_l = int(raw_input())
_r = int(raw_input())
res = maxXor(_l, _r)
print res