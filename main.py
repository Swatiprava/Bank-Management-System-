# Key Concepts for project:
# 1. Bank account 
# 2.Deposit money
# 3.Withdraw money
# 4.Details of User
# 5.update the details of User
# 6,Delete the account


import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")        
    except Exception as err:
        print(f"an exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("$%^&*#",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def Createaccount(self):
        info= {
            "name": input("please Tell your name : "),
            "age": int ( input("Tell your age: ")),
            "email" : input("tell your email: "),
            "pin": int(input("Tell your pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
        }        
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you can't create your account")
        else:
            print("Account has be created succesfully.")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin aswell : "))     
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found.")
        else:
            amount = int(input("how much you want to deposit "))
            if amount > 10000 or amount < 0:
                print("sorry the amount is too much u can deposit below 10000 and above 0")
            else:
                print(userdata)
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")


    def withdrawmoney(self):
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin aswell : "))     
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry no data found.")
        else:
            amount = int(input("how much you want to withdraw: "))
            if userdata[0]['balance'] < amount :
                print("sorry you donot have that much money ")
            else:
                print(userdata)
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully")

    def showdetails(self):
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin aswell : "))  

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]   
        print("Your information are \n\n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")

    def update(self):
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin aswell : "))  

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]  

        if userdata == False:
            print("NO such user found")
        else:
            print("You cannot change age, account number , balance")

            print("Fill the details for change or leave it empty if no change")
            newdata = {
                "name": input("plese tell your new name or press enter : "),
                "email": input("please tell your new email or press enter for skip: "),
                "pin" : input("Enter new pin or press enter to skip : ")
            }

            if newdata["name"] == "" :
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "" :
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "" :
                newdata["pin"] = userdata[0]['pin'] 

            newdata["age"] = userdata[0]['age'] 
            newdata["accountNo."] = userdata[0]['accountNo.']
            newdata["balance"] = userdata[0]['balance'] 

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details updated successfully")

    def delete(self):
        accnumber = input("please tell your account number: ")
        pin = int(input("please tell your pin aswell : "))  

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]  
        if userdata == False:
            print("Sorry no such data exists.")
        else:
            check = ("press y if you want to actually delete the account or press n : ")
            if check == 'n' or check =='N':
                pass
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()



user = Bank()



print("Press 1 for creating an account")
print("Press 2 for Deposit the money in account")
print("Press 3 for withdrawing the money")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleteing your account")

check = int(input("tell your response: "))
if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()    

if check == 5:
    user.update()

if check == 6:
    user.delete()
