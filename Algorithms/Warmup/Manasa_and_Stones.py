# -*- coding: utf-8 -*-
#Question:
#
#---------------------
#Answer:
#
#----------------------
from itertools import *

series =[]
#n:x,y兩數最大的合
#i:遞迴序數
#x:a的權值
#y:b的權值
#s:序列
def possible_series(n,i,x,y,series,elements=list()):
	print i
	elements.append([x,y])
	if ( x + y ) == ( n - 1 ):
		if ()
		series.append(elements[0:len(elements)])
		print elements
		print
		print series
	else:
		possible_series(n,i+1,x+1,y,series,elements)
		series.pop()
		possible_series(n,i+1,x,y+1,series,elements)
	return series

#主程式
for testcases in range(input()):
	#初始輸入
	n,a,b = input(),input(),input()

	series = possible_series(n,0,0,0,series)
	print series
	print len(series[0])


	"""
	#製作[0,1,2,3,...,n]的陣列
	elements = []	
	for i in range(n+1):
		elements.append(i)

	#提取係數的組合可能性(x,y), 0<= (x+y) <= n
	comb =[]
	for i in list(combinations(elements, 2)) :
		if (i[0] + i[1]) <= n :
			comb.append(i)
	
	#提取係數與a、b的關係:i[0]*a+i[1]*b運算結果
	stones_with_number = []
	for i in comb :
		stones_with_number.append(i[0]*a+i[1]*b)
	"""

	
