# -*- coding: utf-8 -*-
#Question:
#有N個餅乾罐，各自編號
#經過M次的餅乾分配
#從編號a~b(1<=a<=b<=N，包括a、b本身)的罐子內
#放置K個餅乾
#最後計算每罐餅乾平均數
#---------------------
#方法一、按部就班(結果不能全對!?)
import math

jars , operations = [ int(i) for i in raw_input().split(" ") ]
jar = [ 0 for i in range(jars) ]

for operation in range(operations) :
    a,b,k = [ int(i) for i in raw_input().split(" ")]
    for i in range(a-1,b) :
        jar[i]+=k

print int(math.floor(float(sum(jar))/jars))
#方法二、已知會投入的罐頭數乘以餅乾數(這個反而是全對的!?)
"""
jars , operations = [ int(i) for i in raw_input().split(" ") ]
candies = 0

for operation in range(operations) :
    a,b,k = [ int(i) for i in raw_input().split(" ")]
    candies += (b - a + 1) * k

print candies/jars
"""

