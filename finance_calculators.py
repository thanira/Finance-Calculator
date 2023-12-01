import math

print("investment -\t to calculate the amount of interest you'll earn on your investment")
print("bond -\t\t to calculate the amount you'll have to pay on a home loan")
print("Type either 'investment' or 'bond' from the menu above to proceed:")

#input for investment or bond
user_option = input(str("Please choose investment or bond\n")).lower()

#investment option and input values:
if user_option == "investment":
    P = float(input("Please enter the amounf of money you are depositing today, e.g. 2000:\n"))
    r = float(input("Please enter interest rate, e.g. 3\n"))
    r = r/100
    t = int(input("Please enter the number of years you plan to invest, e.g. 5\n"))
    interest_type = input("Please enter the interest type: compound or simple\n") 
    #lower or upper function 
    interest_type = interest_type.lower()

    #Calculate how much interest the user will earn and output the answer:
    if interest_type == "simple":
        A = P * math.pow((1+r),t) #simple formula
        print(f"The total amount plus the interest earned over {t} years is £{A:.2f}".format())
    elif interest_type == "compound":
        A = P * math.pow((1 + r), t) #compound formula
        print(f"The total amount plus the interest earned over {t} years is £{A:.2f}".format())
    else:
        print("Please try again with a valid option.")

#bond option and input values:
elif user_option == "bond":
    P = float(input("Please enter the present value of the house, e.g. 100000:\n"))
    i = float(input("Please enter interest rate, e.g. 7:\n"))
    #interest rate entered by the user devided by 100 e.g. (8 / 100) before dividing by 12:
    i = (i/100) / 12
    n = float(input("Please enter the number of months you plan to take to repay the bond, e.g. 120:\n"))

    ##Calculate how much money the user will have to repay each month and output the answer: 
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f"Your monthly repayment will be £{repayment:.2f}".format()) 

#invalid option
else:
    print("Please try again with a valid option.")
    
#how to loop if user enters invalid options in all sections??
