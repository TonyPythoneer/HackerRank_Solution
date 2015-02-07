# -*- coding: utf-8 -*-
#Question:
#給一個字串，如果他任一排列組合，是否有回文的可能性
#---------------------
#Answer:
#該種類的字母數量是偶數，則不影響回文
#如果奇數的字母超過兩種，就不能構成回文了
#----------------------
tring = raw_input()
string = list(string)
collect = {}
found = True

for i in range(len(string)):
    if string[i] in collect.keys():
        collect[string[i]] +=1
    else:
        collect[string[i]] = 1        

odd = 0
for i in collect.keys():
    if collect[i] % 2 != 0:
        odd += 1

if odd > 1:
    found = False
   

# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False

if not found:
    print("NO")
else:
    print("YES")