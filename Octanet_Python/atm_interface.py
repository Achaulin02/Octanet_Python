import time as t
user_pin=2005
user_balance=20000
user_name="ABC"
transaction_history=[]
print("welcome to your bank account",user_name,end="\n")

choice=9
while(True):
    print("\t\t0.Logout and Exit")
    print("\t\t1.View Account Balance")
    print("\t\t2.Withdraw Cash")
    print("\t\t3.Deposit Cash")
    print("\t\t4.Transfer")
    print("\t\t5.Transaction history")
    choice=int(input("Enter a number to proceed:"))
    print("\n\n")

    if choice==0:
        print("Exiting...")
        t.sleep(2)
        print("You have been logged out.Thank you!\n\n")
        break
    elif choice in (1,2,3,4,5):
        num_of_tries=3
        while(num_of_tries!=0):
            input_pin=int(input("Please enter your 4-digit PIN>"))

            if input_pin==user_pin:
                print("Account authorized!\n\n")

                if choice==1:
                    print("Loading Account Balance...")
                    t.sleep(1.5)
                    print("Your Current balance is RS.",user_balance,end="\n\n\n")
                    break
                elif choice==2:
                    print("opening Cash Withdrawal")
                    t.sleep(1.5)

                    while(True):
                        withdraw_amt=float(input("Enter the amount you wish to withdraw>"))

                        if withdraw_amt>user_balance:
                            print("Can't withdraw Rs.",withdraw_amt)
                            print("Please enter alowere amount!")
                            continue

                        else:
                            print("Withdrawing RS.",withdraw_amt)
                            confirm=input("Confirm?Y/N>")
                            if confirm in('Y','y'):
                                user_balance-=withdraw_amt
                                print("Amount withdraw-Rs.",withdraw_amt)
                                print("Remaining balance-Rs.",user_balance,end="\n\n\n")
                                break

                            else:
                                print("Cancelling Transcation...")
                                t.sleep(1)
                                print("Tranasaction Cancelled!\n\n")
                                break

                    break

                elif choice==3:
                    print("loading cash Deposit...")
                    t.sleep(1.5)

                    deposit_amt=float(input("Enter the amount you wish to deposit>"))
                    print("Depositing Rs.",deposit_amt)
                    confirm=input("Confirm? Y/N>")
                    if confirm in('Y','y'):
                        user_balance+=deposit_amt
                        print("Amount deposited-Rs.",deposit_amt)
                        print("Updated balance-Rs.",user_balance,end="\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1)
                        print("Tranascation Cancelled!\n\n")

                    break

                elif choice==4:
                    print("Loading transfer details")
                    t.sleep(1.5)

                    recipient_name=input("Enter recipient's name:")
                    transferring_amt=float(input("Enter transfer amount:"))
                    print("Transferring amount")
                    Confirm=input("Confirm? Y/N>")
                    if confirm in('Y','y'):
                        print("Transferred successfully!\n\n")
                    else:
                        print("Cancelling Process!\n\n")
                        t.sleep(1)
                        print("process cancelled!\n\n")
                        transaction_history.append(transferring_amt)

                    break

                elif choice==5:
                    print("Loadint tranasaction history...")
                    t.sleep(1.5)

                    print("\n======Transaction History======\n")
                                
                    print("Transferred amount:","[",transferring_amt,"]\n\n")

                    break
                else:
                    print("Loading Card Return...")
                    t.sleep(1.5)

                    print("Retutning your ATM card")
                    confirm=input("Confirm? Y/N>")
                    if confirm in('Y','y'):
                        print("Card returned successfully!\n\n")
                    else:
                        print("Cancelling Process...")
                        t.sleep(1)
                        print("Process Cancelled!\n\n")

                    break

            else:
                num_of_tries-=1
                print("PIN incorrect!Number of tries left-",num_of_tries,end="\n\n")

        else:
            print("Existing...")
            t.sleep(2)
            print("You have been logged out.Thank You!\n\n")
            break

    else:
        print("invalid input!")
        print("\t\t0.Enter 0 to Logout and Exit!")
        continue
