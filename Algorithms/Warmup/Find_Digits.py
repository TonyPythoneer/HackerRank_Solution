# -*- coding: utf-8 -*-
#Question:
#例如一個數字24，將每個位數的數字拆開:即2和4
#然而2和4可以整除24，所以答案是2
#以可整除的數字計入count
#---------------------
#Answer:
#拆解而已，沒什麼
#----------------------
for testcases in range(input()):
	num = input()
	count = 0
	for digtal in str(num) :
		digtal = int(digtal)
		try:
			if ( num % digtal ) == 0 :
				count += 1
		except ZeroDivisionError:
			continue
	print count
