print(".............................................................WELCOME..................................................................................")
accounts = {
            111:["user 1","17-08-2004",10000,1369],
            222:["user 2","12-08-1983",20000,9631],
            333:["user 3","12-02-1973",30000,9966],
            444:["user 4","12-04-1980",4000,None]
            }
dobm = {1:"January",2:"Feb",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
while True:    
    print("choose your option")
    print("1. WITHDRAWAL")
    print("2. DEPOSIT")
    print("3. REMAINING BALENCE")
    print("4. PIN GENERATION")
    print("5. MINI STATEMENT")
    print("6. EXIT")
    option = int(input("ENTER YOUR OPTION: "))
    print()
    if option==1:
        accno = int(input("ENTER YOUR ACCOUNT NUMBER:"))
        if accno not in accounts:
            print(".......................................XXX || ACCOUNT DOES NOT EXIST || XXX..........................................")

        else:
            pin = int(input("ENTER YOUR PIN: "))
            if accounts [accno][-1] == None:
                print("GENERATE PIN")
            else:
                if accounts[accno][-1] != pin:
                    print("................................XXX|| INVALID PIN ||XXX......................................................")
                else:
                    amount = int(input("ENTER AMOUNT TO WITHDRAW: "))
                    if amount> accounts[accno][-2]:
                        print("............................XXX||| INSUFICENT FUNDS |||XXX...............................................")
                    else:
                        print("WITHDRAW SUCCESSFULL")
                        accounts[accno][-2] -= amount
        print("REMAINING BALANCE",accounts[accno][-2])
    elif option==2:
        accno = int(input("ENTER YOUR ACCOUNT NUMBER: "))
        if accno not in accounts:
            print("........................................XXX|||ACCOUNT DOESN'T EXISTS|||XXX............................................")
        else:
            amount= int(input("ENTER YOUR DEPOSITE AMMOUNT: "))
            accounts[accno][-2]+= amount
        print("AVAILABLE AMOUNT",accounts[accno][-2])
    elif option==3:
        accno=int(input("ENTER YOUR ACCOUNT NUMBER: "))
        if accno not in accounts:
            print(".........................................XXX|||INVALID ACCOUNT NUMBER|||XXX...........................................")
        else:
            print("YOUR CURRENT BALANCE IS:",accounts[accno][-2])
    elif option==4:
        accno= int(input("ENTER YOUR ACCOUNT NUMBER:"))
        if accno not in accounts:
            print(".........................................XXX|||ACCOUNT DOES NOT EXISTS|||XXX..........................................")
        else:
            if accounts[accno][-1] == None:
                pin = int(input("ENTER PIN:"))
                cpin = int(input("CONFIRM YOUR PIN:"))
                if pin != cpin:
                    print("................................XXX|||PIN DOESN'T MATCH|||XXX.................................................")
                else:
                    accounts[accno][-1]= pin
                    print("PIN GENERATED SUCCESSFULLY")
            else:
                print("PIN ALREADY EXISTS")
    elif option==5:
        accno= int(input("ENTER YOUR ACCOUNT NUMBER:"))
        if accno not in accounts:
            print("........................................XXX|||ACCOUNT DOES NOT EXIST|||XXX............................................")
        else:
             print(f"Name: {accounts[accno][0]}")
             print(f"Account Number: {accno}")
             dob = accounts[accno][1].split("-")
             date = dob[0]
             month = dobm[int(dob[1])]
             year = dob[2]
             dob = date + "-" + month + "-" + year
             print(f"Date of Birth: {dob}")
             print(f"Account Balance: {accounts[accno][-2]}")

            
        
    elif option==6:
        break