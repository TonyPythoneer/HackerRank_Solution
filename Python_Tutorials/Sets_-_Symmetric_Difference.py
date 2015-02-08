#step1:input case1
case1 = input()
element1 = raw_input()
list1 = element1.split()
set1 = set(list1)

#step2:input case2
case2 = input()
element2 = raw_input()
list2 = element2.split()
set2= set(list2)

#step3:set1 XOR set2 - It find different elements.
ans_set = set1 ^ set2
ans_list = list(ans_set)

#elements convert integer form string.
for index in range(len(ans_list)):
    ans_list[index] = int(ans_list[index])
    
ans_list.sort()

for ans in ans_list :
    print (ans)