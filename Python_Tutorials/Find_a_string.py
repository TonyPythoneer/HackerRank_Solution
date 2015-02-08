# Enter your code here. Read input from STDIN. Print output to STDOUT
first_string = raw_input()
second_string = raw_input()

times_of_occurrence = 0

find_string = 0

while True :
    find_string= first_string.find(second_string,find_string)
    if find_string >= 0 :        
        find_string = find_string + 1
        times_of_occurrence = times_of_occurrence + 1
    else :
        break

print (times_of_occurrence)