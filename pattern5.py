rows = int(input("Enter the number of rows: "))  

#Outer for loop executing in reverse order
for i in range(rows + 1, 0, -1):  
        for j in range(0, i - 1):  
            print("* ", end=" ")       
        print()