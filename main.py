#Name: PasswordManager
#Author: Mark Ejakpomewhe
#Date: Mon Jan 30th
#Description: A program to help store my passwords
#Note: Passwords wont be encrypted because the purpose of this program is to view the passwords
#Version: version 1.0
#Completed: false

#Error: cant read multiple dictionaries
#possible solution: Read json file and store before appending
#                   if file empty, create an array of accounts
import json
import os

class PasswordManager:
    #def __init__
    #id=0

    def add_account(self,name,password,password_strength):
       # self.id+=1
        self.name=name
        self.password=password
        self.password_strength=password_strength

    def save_account(self):

        accnt={ 'name':self.name, 'password':self.password,'password_strength':self.password_strength}
        with open("accounts.json", "r+") as f:
            file_data=json.load(f)
            file_data["accounts"].append(accnt)
            f.seek(0)
            json.dump(file_data,f,indent=4)
            #f.write(json.dumps(accnt,indent=4))

    def view_account(self):
        with open("accounts.json", 'r') as f:
            data = json.loads(f.read())

            #print(f"{data['accounts']}")
            accnt_data = data['accounts']
            #print(accnt_data)
            for ad in accnt_data:
                print(f"{ad}")

        # self.name=data['name']
        # self.password=data['password']
        # self.password_strength= data['password_strength']
        #
        # print(f"Name: {self.name}")
        # print(f"Password: {self.password}")
        # print(f"Password_Strength: {self.password_strength}")

        #new_json= json.dumps(data)
        #print(new_json)

def password_strength_(password_):
    pass

def is_file_empty():
    return os.path.exists("accounts.json") and os.stat("accounts.json").st_size==0
def add_accnt():

    is_empty= is_file_empty()
    if is_empty:
        accnt = {"accounts": []}
        with open("accounts.json", "a") as f:
            f.write(json.dumps(accnt, indent=4))
        print("file is empty")
    else:
        print("file not empty")
    print("**** Enter Details ****")
    input_name=input("Name: ")
    input_password=input("Password: ")
    input_pass_strength="mid"

    p1 = PasswordManager()
    p1.add_account(input_name, input_password, input_pass_strength)
    p1.save_account()

def view_accnt():
    p1 = PasswordManager()
    print(p1.view_account())
#p1.show_account()

print("************** Welcome back, Mark **************")

print("Choose from the following options:\n")
print("1.View Accounts\n2.Add Account\n3.End Program")




option = None
while option is None:
    input_value = input("Enter Value: ")
    try:
        # try and convert the string input to a number
        option = int(input_value)
    except ValueError:
        # tell the user off
        print("{input} is not a number, please enter a number only".format(input=input_value))

    if option == 1:
        view_accnt()
    elif option == 2:
        add_accnt()
    elif option == 3:
        break
    else:
        option=None




