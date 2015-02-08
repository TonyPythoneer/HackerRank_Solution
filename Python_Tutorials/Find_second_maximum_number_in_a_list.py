# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = input()
numbers = raw_input()
numbers = numbers.split()
for index in range(cases):
    numbers[index] = int(numbers[index])

numbers_set = set(numbers)
numbers_list = list(numbers_set)
numbers_list.sort()
print (numbers_list[-2])