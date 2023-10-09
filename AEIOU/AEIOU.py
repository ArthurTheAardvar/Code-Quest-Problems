import sys #needed for readline function


cases = (int(sys.stdin.readline().rstrip())) #get the first number of cases

for i in range(cases): #go through the other lines
 
    line = sys.stdin.readline().rstrip()#strips off extra spaces at the end of the line
    num = 0
  

    idk = len(line)

    for i in range(idk):

        if line[i] == 'a' or line[i]== 'e' or line[i]== 'i' or line[i] == 'o' or line[i] == 'u':
            num+=1

    print(num)


        
              
              
