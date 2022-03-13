import random
import time
from getpass import getpass

# Author: Soowhan Park
# Purpose: Custom Tasks for Bear Robotics Online Assesment 

# Class to store Savings account information
class SavingsAcoount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

# Class to store Checking account information
class ChecikingAcoount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

# Class to create a card, card PIN number, and bank account
class Bank:
    def __init__(self, card_num, PIN, accounts, hasCard):
        self.balance=0
        self.user_name = ""
        self.card_num = card_num
        self.PIN = PIN
        self.hasCard = hasCard
        self.account_cnt = 0
        self.accounts = accounts
        self.curr_account_balance = 0
        print("\nWelcome to Bank of BearRobotics")
        print("How can I assist you today?")
        self.backtoMain()

    def backtoMain(self):
        print("\n1. Create a new card")
        print("2. Change the PIN number")
        print("3. Create a new account")
        print("4. Delete the account")
        print("5. Delete the card")
        print("6. Exit\n")
        self.init_choice = int(input("Type your choice: "))
        if self.init_choice == 1:
            if self.hasCard:
                print("\nYou already have a card. Going back to main")
                time.sleep(1.5)
                self.backtoMain()
            else:
                self.createCard()
        elif self.init_choice == 2:
            self.createPIN()
        elif self.init_choice == 3:
            self.createAccount()
        elif self.init_choice == 4:
            self.deleteAccount()
        elif self.init_choice == 5:
            self.deleteCard()
        elif self.init_choice == 6:
            print("\nThank you for choosing Bank of BearRobotics. Going back to controller")
            time.sleep(2)
        else:
            print("Wrong choice! please type single integer of your choice.")


    def createPIN(self):
        if self.hasCard == False:
            print("\nYou must create card first. Going back to main")
            time.sleep(1.5)
            self.backtoMain()
        else:
            pin_num = getpass("Please set your 4 digit PIN number: ")
            if pin_num == self.PIN:
                print("You have entered the same PIN number. Please choose different digits")
                self.createPIN()
            else:
                for i in range(5):
                    if len(pin_num) != 4 or pin_num.isdigit() == False:
                        pin_num = getpass("You must type 4 digits. Try again: ")
                    else:           
                        break
                    if i == 4:
                        print("You have exceeded maximum try. Exit.")
                for i in range(5):
                    check = getpass("Re-type your PIN number: ")
                    if check == pin_num:
                        print("You have succesfully set the PIN number")
                        self.PIN = pin_num
                        break
                    if i == 4:
                        print("Your password does not match. For security purpose you have to restart the process")
                time.sleep(1.5)
                self.backtoMain()

    def createCard(self):
        self.user_name = str(input("Your name: "))
        print("Hello " + self.user_name.upper() + ", give me few seconds until we get a new card for you")
        time.sleep(2)
        num = str(int(random.random() * (10 ** 16)))
        new_card = num[:4] + '-' + num[4:8] + '-' + num[8:12] + '-' + num[12:16]
        self.card_num = new_card
        print("Your new card number is:", new_card)
        self.hasCard = True
        self.createPIN()
    
    def createAccount(self):
        if self.hasCard == False:
            print("\nYou must create card first. Going back to main")
            time.sleep(1.5)
            self.backtoMain()
        elif self.account_cnt == 2 :
            print("\nSorry, you can't make more than 2 accounts!\n")
            time.sleep(1.5)
            self.backtoMain()
        else:
            print("You currently have " + str(self.account_cnt) + " account")
            account = str(input("Would you like to make savings account or checking account? (Type savings or checking): "))
            if account =="savings":
                if "Savings" in self.accounts:
                    print("\nYou already have a Savings account\n")
                    time.sleep(1.5)
                    self.backtoMain()
                else:
                    new_account = SavingsAcoount(self.user_name)
                    self.accounts["Savings"] = new_account
                    self.account_cnt += 1 
                    print("\nYour Savings Account has been created.")
                    time.sleep(1.5)
                    self.backtoMain()
            elif account == "checking":
                if "Checking" in self.accounts:
                    print("\nYou already have a Savings account\n")
                    time.sleep(1.5)
                    self.backtoMain()
                else:
                    new_account = ChecikingAcoount(self.user_name)
                    self.accounts["Checking"] = new_account
                    self.account_cnt += 1 
                    print("\nYour Checking Account has been created.")
                    time.sleep(1.5)
                    self.backtoMain()
            else:
                print("\nPlease type valid account name\n")
                time.sleep(1.5)
                self.createAccount()

    def deleteAccount(self):
        if self.account_cnt == 0:
            print("\nYou currently have 0 account. Can't delete.")
            time.sleep(1.5)
            self.backtoMain()
        else:
            print("You currently have following accounts:")
            for key, val in self.accounts.items():
                print(key)
            rm = input("Which account do you want to remove?: ")
            if rm.lower() == "savings":
                del self.accounts["Savings"]
            else:
                del self.accounts["Checking"]
            self.account_cnt -= 1
            print("You have succesfully removed " + rm + " account")
        
    def changePIN(self):
        check = str(input("Would you like to change the PIN? type y or n: "))
        for i in range(5):
            if check != "y" or check != "n":
                check = str(input("Please type y or n: "))
            else:
                break
            if i == 4:
                print("You have entered wrong respons. Exit.")
                exit()
        if check == "y":
            self.createPIN()
        else:
            print("Password is not updated. Exit")
            exit()
    
    def deleteCard(self):
        check = str(input("Are you sure you want to delete your card?: "))
        if "y" in check.lower():
            self.hasCard = False
            self.PIN = ""
            self.card_num = ""
            print("\nYour card has been deleted\n")
            time.sleep(2)
        elif "n" in check.lower():
            self.backtoMain()
        else:
            print("\nPlease type either yes or no\n")
            time.sleep(1.5)
            self.deleteCard()

    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Class to perform basic ATM operations like deposit and withdraw
class ATM:
    def __init__(self, card_info, pin_num, balance, accounts):
        self.balance = balance
        self.accounts = accounts
        self.isInserted = False
        self.init_choice = None
        self.curr_account = ""

        print("\nWelcome to ATM machine\n")
        inserted_card = str(input("Please insert your card: "))
        for i in range(5):
            if inserted_card == card_info:
                pin = getpass("Please type 4 digit PIN number: ")
                for i in range(5):
                    if pin == pin_num:
                        self.isInserted = True
                        print("\nCard succesfully inserted\n")
                        time.sleep(1)
                        break
                    else:
                        pin = getpass("\nWrong PIN number. Please type again: ")
                    if i == 4:
                        print("\nYou have exceeded maximum try")
                break
            else:
                inserted_card = str(input("\nSystem Error: Please re-insert your card: "))
        if self.isInserted:
            self.chooseAccount()

    def chooseAccount(self):
        if len(self.accounts) == 0:
            print("You have to create at least one bank account")
            time.sleep(2)
        else:
            print("\nSelect the account")
            i = 1
            d = {}
            for key, val in self.accounts.items():
                print(str(i) + ".", key)
                d[i] = key
                i += 1
            account_select = int(input("\nChoose the account :"))
            if account_select == 1 or account_select == 2:
                bal = self.accounts[d[account_select]]
                self.curr_account = d[account_select]
                #account_balance = bal.balance 
                print("\n",d[account_select] + " account has been selected\n")
                time.sleep(1)
            else:
                print("\nPlease type in a digit\n")
                self.chooseAccount()
            self.toMain()
            
    def toMain(self):
        print("\n Choose the operation")
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Current Balance")
        print("4. Exit\n")
        self.init_choice = int(input("Type your choice: "))
        if self.init_choice == 1:
            self.deposit(self.curr_account)
        elif self.init_choice == 2:
            self.withdraw(self.curr_account)
        elif self.init_choice == 3:
            self.display(self.curr_account)
        elif self.init_choice == 4:
            print("\nThank you for choosing ATM of BearRobotics. Going back to controller")
            time.sleep(2)
        else:
            print("Wrong choice! please type single integer of your choice.")

 
    def deposit(self, curr_account):
        amount=int(input("\nEnter amount to be Deposited: "))
        a  = self.accounts[curr_account]
        a.balance += amount
        print("\n SUCESS! Amount Deposited:",amount)
        time.sleep(2)
        self.toMain()
 
    def withdraw(self, curr_account):
        amount = int(input("\nEnter amount to be Withdrawn: "))
        if self.accounts[curr_account].balance >= amount:
            self.accounts[curr_account].balance -= amount
            print("\n SUCCESS! You Withdrew:", amount)
        else:
            print("\n FALIED! Insufficient balance  ")
        time.sleep(2)
        self.toMain()
 
    def display(self, curr_account):
        print("\n Available Balance=",self.accounts[curr_account].balance)
        time.sleep(2)
        self.toMain()
 
# Driver code
has_card = False 
usr_bank = None
balance = 0
accounts = {}
card_info = ""
pin_num = ""

print("\nWelcome to virtual Bank/ATM Controller")
while True:
    print("WARNING: If you don't have a card, you must go to bank and create a card first.")
    print("\n1. Go to bank")
    print("2. Go to ATM")
    print("3. Exit the module")
    usr_choice = int(input("\nType your choice: "))
    if usr_choice == 1:
        usr_bank = Bank(card_info, pin_num, accounts, has_card)
        card_info = usr_bank.card_num
        pin_num = usr_bank.PIN
        accounts = usr_bank.accounts
        has_card = True
    elif usr_choice == 2:
        y_n = str(input("\nDo you have a card?: "))
        if "y" in y_n.lower():
            if has_card == False:
                print("Sorry, we couldnt verify your card.")
            else:
                print("Directing you to ATM...")
                time.sleep(1.5)
                usr_atm = ATM(card_info, pin_num, balance, accounts)
        elif "n" in y_n.lower():
            print("Directing you to bank...")
            time.sleep(1.5)
            usr_bank = Bank(card_info, pin_num, accounts, has_card)
            card_info = usr_bank.card_num
            pin_num = usr_bank.PIN
            accounts = usr_bank.accounts
            has_card = True
        else:
            print("\nPlease type either yes or no\n")
            time.sleep(1.5)
    elif usr_choice == 3:
        print("Thank you for testing Bank/ATM Controller")
        time.sleep(2)
        exit()