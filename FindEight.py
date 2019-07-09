def findEight(array1):
    for x in range(0,4):
            if array1[0]+array1[x]==8 and x !=0:
                print("Indices 0 and", x, "create 8.")
            elif array1[1]+array1[x]==8 and x !=1:
                print("Indices 1 and ",x, "create 8.")
            elif array1[2]+array1[x]==8 and x !=2:
                print("Indices 2 and",x, "create 8.")
            elif array1[3]+array1[x]==8 and x !=3:
                print("Indices 3 and", x, "create 8.")
            else:
               print("No valid matches.")

        
topArray=[1,2,3,9]
bottomArray=[1,2,4,4]


findEight(topArray)
findEight(bottomArray)
