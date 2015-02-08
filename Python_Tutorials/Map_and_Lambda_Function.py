# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = input()
cubes = []
a = 0
b = 1

for i in range(cases):    
    cubes.append(a ** 3)
    a, b = b, a+b
    
print (cubes)