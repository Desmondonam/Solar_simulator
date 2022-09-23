#in this program, we displayed how to calculate electricity bill
unit=int(input("Enter the unit consumed: "))
#//Reads input from user and store in variable num
def Bill_Calc(unit):#function definition
    
    if(unit<=50):
          #below 50 units
        print(unit*1.50);
    
    elif(unit<=150):
           #below 150 units
        print((50*1.5)+(unit-50)*2.00);
    
    elif((unit<=250)):#below 250 units
        print((50*1.5)+((150-50)*2.00)+(unit-150)*3.00);
    
    else:   #above 250 units
        print((50*1.5)+((150-50)*2.00)+((250-150)*3.00)+(unit-250)*4);
Bill_Calc(unit)#function call