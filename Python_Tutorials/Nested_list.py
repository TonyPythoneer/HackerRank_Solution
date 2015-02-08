# Enter your code here. Read input from STDIN. Print output to STDOUT
#step1:input datas of students
cases = input()
element = []
while cases > 0 :
    person = raw_input()
    score = input()
    element.append([person,score]) 
    cases = cases - 1
    
#step2:score sort
for i in range(len(element)-1):
    for j in range(i,len(element)):
        if (element[i][1] > element[j][1]):
            element[i] , element[j] = element[j] , element[i]

#step3:find lowest_second_score
lowest_score = element[0][1]
lowest_second_score = None
for i in range(1,len(element)):
    if lowest_score <  element[i][1]:
        lowest_second_score = element[i][1]
        break

#step4:find students who get lowest_second_score
mark_name=[]
for i in range(len(element)):
    if lowest_second_score == element[i][1]:
        mark_name.append(element[i][0])

#step5:sort name
mark_name.sort()
for i in mark_name:
    print (i)