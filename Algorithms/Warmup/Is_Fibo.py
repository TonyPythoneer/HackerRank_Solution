# -*- coding: utf-8 -*-
#Question:
#總之有碰過數學的人都知道這個奇怪數列
#ex:0,1,1,2,3,5,8,13...
#現在輸入某數，確認他是否屬於該數列的其中一個元素就對了
#---------------------
#Answer:
#解法是懂遞迴的話，自然好解
#----------------------
def is_fibo(i,num1,num2):
	if  i > num2 :
		num1 , num2 = num2 , num1 + num2
		return is_fibo(i,num1,num2)
	elif i == num2 :
		return True
	elif i < num2 :
		return False


for testcases in range(input()):
	if is_fibo( input() , 0 , 1 ) :
		print "IsFibo"
	else :
		print "IsNotFibo"
