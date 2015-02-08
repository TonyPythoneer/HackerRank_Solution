# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = input()
dic_date = {}
for case in range(cases):
    student_with_scores = raw_input()
    student_with_scores = student_with_scores.split()
    student = student_with_scores[0]
    average_score = 0
    for index in range(1,len(student_with_scores)):
        average_score = average_score + float(student_with_scores[index])
    average_score = average_score/3
    dic_date.update({student:average_score})

search_student = raw_input()
print("{0:.2f}".format(dic_date[search_student]))