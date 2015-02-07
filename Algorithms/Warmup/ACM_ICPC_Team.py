# -*- coding: utf-8 -*-
#Question:
#假設有一個隊伍，W、X、Y、Z參加隱藏空間猜猜樂
#已經一個空間有5個人，分別為A、B、C、D、E
#但參賽者四人都不知道5人的身分
#假設X說他看到A、C、E
#而Y說他看到B、D
#只要有兩人的意見和在一起，確實找出5人是何許人
#則將此計入count
#---------------------
#Answer:
#拆解而已，沒什麼
#----------------------
import itertools

people,topics = raw_input().split(" ")
people,topics = int(people),int(topics)
count = {}

people_array = []
for i in range(people):
	people_array.append( "0b" + raw_input() )

for i,j in itertools.combinations(people_array, 2):
	match = 0
	for index in range(people):
		if (int(i[index]) | int(j[index])) == 1 :
			match += 1
	if match == topics :
		
