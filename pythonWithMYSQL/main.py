from dbHelper import DBHelper


def main():
    db = DBHelper()
    while True:
        print("************WELCOME****************")
        print("Press 1 to insert user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()
        try:
            choice = int(input())
            if(choice==1):
                #insert
               uid = int(input("Enter User ID:"))
               username=input("Enter UserName:")
               userPhone=input("Enter phone Number:")
               db.insert_user(uid,username,userPhone)
            elif choice==2:
                #display
                db.fetch_userData()
            elif choice==3:
                #delete
                uid = int(input("Enter User ID to delete:"))
                db.delete_data(uid)
            elif choice==4:
                #update
                uid = int(input("Enter User ID you want to update:"))
                username=input("Enter new  UserName:")
                userPhone=input("Enter new phone Number:")
                db.update_data(uid,username,userPhone)
            elif choice==5:
                #exit
                break
            else:
                 print("Invalid Input Try Again")
        except Exception as e:
            print(e)
            print("Invalid User Try Again Dear!")


if __name__ =="__main__":
    main()


# Main Coding
# helper = DBHelper()
# # helper.insert_user(5,"Aarti","7678676767")
# # helper.insert_user(2,"Shivay","87878877")
# # helper.insert_user(3,"Simran","87788787")
# # helper.insert_user(4,"Aashish","989898")
# helper.fetch_userData()
# helper.fetch_userDataBYID()
# helper.delete_data(4)
# helper.fetch_userData()
# helper.update_data(3,"Shivam","Shurya")
# helper.fetch_userData()




















