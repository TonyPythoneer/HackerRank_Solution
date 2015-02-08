# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
y=input()
z=input()
n=input()

sets = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i+j+k) != n :
                sets.append([i,j,k])
                
print (sets)