'''
   1 
  2 2 
 3 3 3 
4 4 4 4
'''
num = int(input("Enter number of rows : "))
for i in range(num): # 0,1,2,3
    print((' '*(num-i-1))+(str(i+1)+' ')*(i+1))
