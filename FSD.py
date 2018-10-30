import datetime
now = datetime.datetime.now()
delta = datetime.timedelta(days=140)
n_days = now + delta

number_of_student1 = 1
number_of_student2 = 1
A = 1
while(A == 1):
    print("=============================================")
    print("==Welcome to University Apartments Rental System==")
    print("=============================================")
    print()
    B = 1
    while(B == 1):
        print("Please choose the function you want : ")
        print("\t 1. Log in")
        print("\t 2. Registered")
        print()
        function = input("Your choose : ")
        while(function != "1" and function != "2"):
            print("Invalid password, please enter again")
            print("======================================")
            function = input("Your choose : ")          
        if(function == "1"):
            print()
            name = input("Please enter your name : ")
            name2 = name.upper()
            TP = input("Please enter your TP number : ")
            password = input("Please enter your password : ")
            while(password != TP):               
                print("Invalid password, please enter again")
                print("======================================")
                name = input("Please enter your name : ")
                TP = input("Please enter your TP number : ")
                password = input("Please enter your password : ")
            print()
            print("——————[You have successfully logged in]——————")
            print()
            break
        elif(function == "2"):
            print()
            name = input("Please enter your name : ")
            name2 = name.upper()
            TP = input("Please enter your TP number : ")
            password = input("Please enter your password : ")
            password2 = input("Please enter your password again : ")
            while(password != password2):
                print("Invalid password, please enter again")
                print("======================================")
                password = input("Please enter your password : ")
                password2 = input("Please enter your password again : ")
            print()
            print("——————[You have successfully registered]——————")
            print()
            print("——————————[Please login again]—————————")
            print()
            name = input("Please enter your name : ")
            name2 = name.upper()
            TP = input("Please enter your TP number : ")
            password = input("Please enter your password : ")
            while(password != password2):               
                print("Invalid password, please enter again")
                print("======================================")
                name = input("Please enter your name : ")
                name2 = name.upper()
                TP = input("Please enter your TP number : ")
                password = input("Please enter your password : ")
            print()
            print("——————[You have successfully logged in]——————")
            print()
            break
    print()
    print()
    print("Please choose the type of functions you want : ")
    print("1.Move into the apartment          2.Move out of the apartment ")
    print()
    number1 = (input("Please enter 1 or 2 : "))
    while(number1 != "1" and number1 != "2"):
            print()
            print("Invalid code, please enter again")
            print()
            number1 = input("Please enter 1 or 2 : ")
    if(number1 == "1"):
        print()
        print("======================================")
        print("=========[Apartment Information]=========")
        print("======================================")
        print()
        print("————Apartment Type A————")
        print()
        print("2 bedrooms and equiped with kitchen and")
        print("laundry facilities. The monthly rental for the")
        print("rooms in this apartment type is RM300.")
        print()
        print(" ————Apartment Type B————")
        print("3 bedrooms includes one master bedroom with attached")
        print("bathroom but does not have kitchen and laundry facilities.")
        print("The monthly rental for the rooms in this apartment type is")
        print("RM200 and students staying in the master bedroom will be")
        print("paying an additional 40%.")
        print()
        print("-----Register and assigns an apartment to you-----")
        print("-----for 140 days from the date of registration-----")
        print()
        letter = input("Please enter A or B to choose your apartment : ")
        letter2 = letter.upper()
        while(letter2 != "A" and letter2 != "B"):
            print()
            print("Invalid code, please enter again")
            print()
            letter = input("Please enter A or B to choose your apartment : ")
            letter2 = letter.upper()
        if(letter2 == "A"):
                rental_deposit_for_one_month= 300
                the_rental_for_the_current_month = 300
                type_of_bedroom = "Apartment Type A "
                result = "You have moved into the apartment type A"
                xyz = 1
        else:
            print()
            print("======================================")
            print("Please choose the sizes of the apartment : ")
            print("1.Master bedroom              2.Guest bedroom")
            print()
            number = input("Please enter 1 or 2 : ")
            while(number != "1" and number != "2"):
                print()
                print("Invalid code, please enter again")
                print()
                number = input("Please enter 1 or 2 : ")                
            if(number == "1"):
                rental_deposit_for_one_month= 280
                the_rental_for_the_current_month = 280
                type_of_bedroom = "Apartment Type type B (Master bedroom)"
                result = "You have moved into the apartment type B (Master bedroom)"
                xyz = 1
            else:
                rental_deposit_for_one_month= 200
                the_rental_for_the_current_month = 200
                type_of_bedroom = "Apartment Type type B(Guest bedroom)"
                result = "You have moved into the apartment type B (Guest bedroom)"
                xyz = 1
    else:
        print()
        print("Please choose where are you live before : ")
        print("A : Apartment Type A")
        print("B : Apartment Type B (Master bedroom)")
        print("C : Apartment Type B (Guest bedroom)")
        print()
        letter3 = input("Please enter A or B or C : ")
        letter4 = letter3.upper()
        while(letter4 != "A" and letter4 != "B" and letter4 != "C"):
            print()
            print("Invalid code, please enter again")
            print()          
            letter3 = input("Please enter A or B or C : ")
            letter4 = letter3.upper()
        if(letter4 == "A"):
            result = "You have moved out of the apartment type A"
            xyz = 0
        elif(letter4 == "B"):
            result = "You have moved out of the apartment type B (Master bedroom)"
            xyz = 0
        else:
            result = "You have moved out of the apartment type B (Guest bedroom)"
            xyz = 0




    print("==========[ Your Information]==========")
    print("Name : ",name2)
    print("TP number : ",TP)
    str1 = "["
    str2 = "]"
    if(xyz == 1):
        utility_charges = 100
        print("Rental deposit for one month is : RM",rental_deposit_for_one_month)
        print("The rental for the current month is : RM",the_rental_for_the_current_month)
        print("Utility charges is : RM",utility_charges)
        total_fees = rental_deposit_for_one_month + the_rental_for_the_current_month + utility_charges
        print("Your total fees is : RM",total_fees)
        print()
        print(result)
        print("Check date : ",now.strftime("%d/%m/%Y"))
        print("Check out date : ",n_days.strftime("%d/%m/%Y"))


        myfile1 = open("Move in.txt","a")
        myfile1.write(str1+str(number_of_student1)+str2+"\n")
        myfile1.write("name :"+name2 +"\n")
        myfile1.write("TP number : "+TP +"\n")
        myfile1.write("Password : "+ password+"\n")
        myfile1.write("Type of bedroom : "+type_of_bedroom+"\n")
        myfile1.write("Check date : "+now.strftime("%d/%m/%Y")+"\n")
        myfile1.write(n_days.strftime("Check out date : "+"%d/%m/%Y")+"\n")
        myfile1.close()
        number_of_student1 =  number_of_student1 + 1
    else:
        print(result)
        print("Check out date : ", now.strftime("%d/%m/%Y"))

        myfile2 = open("Move out.txt","a")
        myfile2.write(str1+str(number_of_student2)+str2+"\n")
        myfile2.write("name :"+name2+"\n")
        myfile2.write("TP number : "+TP+"\n")
        myfile2.write("Password : "+ password+"\n")
        myfile2.write("Type of bedroom : "+type_of_bedroom+"\n")
        myfile2.write("Check date : "+now.strftime("%d/%m/%Y")+"\n")
        myfile2.close()
        number_of_student2 = number_of_student2 + 1

    print()
    print("==============================================")
    print("Thank you for using University Apartments Rental System")
    print("==============================================")
    kill = input("Press Enter key to Exit")
    if(kill == ""):
        print("============================================")
        print("=============You have logged out=============")
        print("============================================")
        print()                
        print()
        print()
        print("================Welcome =================")
    else:
        continue

    
    
    
    
        




    

        
            

        







       
    

    

                
    
            
        


        
            
    
            
            
            
    

    
    
