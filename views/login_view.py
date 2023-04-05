from controllers import login, register
from views.main_menu_view import show_main_menu


def show_login_view():
    print("----------LOGIN-----------")
    print("----CHOOSE-ONE-OPTION-----")
    print("--------------------------")
    print("1---------LOGIN-----------")
    print("2---------REGISTER--------")
    print("3---------EXIT------------")
    print("--------------------------")
    while True:
        option = input("Your Option: ")
        if option.isdigit() and int(option) == 1:
            email = input("Email     : ")
            password = input("Password  : ")

            user = login(email, password)
            if user:
                print("Logged In successfully")
                show_main_menu(user)
            else:
                print("Invalid Credentials")
            break

        elif option.isdigit() and int(option) == 2:
            fname = input("First Name     : ")
            lname = input("Last Name      : ")
            email = input("Email          : ")
            passowrd = input("Password       : ")
            confirm = input("Confirm Pass   : ")
            phone = input("Phone Number   : ")

            if register(fname, lname, email, passowrd, confirm, phone):
                print("Registered Successfully")
            else:
                print("Failed To Register")
            break

        elif option.isdigit() and int(option) == 3:
            exit(1)