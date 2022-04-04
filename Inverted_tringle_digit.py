'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
num = int(input("Enter a rows : "))
for i in range(num):
    for j in range(num-i):
        print(j+1,end=' ')
    print()