from controllers import add_project, edit_project, get_all_projects, delete_project
from models import Project
from utils import show_table
def show_main_menu(user):
    print("----------MAIN-----------")
    print("----CHOOSE-ONE-OPTION-----")
    print("--------------------------")
    print("1--ADD-NEW-PROJECT--------")
    print("2--EDIT-PROJECT-----------")
    print("3--VIEW-ALL-PROJECTS------")
    print("4--DELETE-PROJECT---------")
    print("5--EXIT-------------------")
    print("--------------------------")

    while True:
        option = input("Your Option: ")
        if option.isdigit() and int(option) == 1:
            title = input("Title: ")
            details = input("Details: ")
            total_target = input("Total Target: ")
            start_time = input("Start Time: ")
            end_time = input("End Time: ")
            project = Project(user.id, title, details, total_target, start_time, end_time)
            if add_project(project):
                print("Inserted Successfully")
            continue

        elif option.isdigit() and int(option) == 2:

            projects = get_all_projects()

            var = "|{:>15}|" * 6
            print("-" * 17 * 6)
            print(var.format("#", "Title", "Details", "Total Target", "Start time", "End Time"))
            print("-" * 17 * 6)
            var = "|{:>15}|" * 6
            for i, pro in enumerate(projects):
                print(var.format(i+1,pro.title, pro.details, pro.total_target, pro.start_time, pro.end_time))
            print("-" * 17 * 6)

            while True:
                edit_option = input("Enter the number of project you want to Edit: ")
                if edit_option.isdigit() and len(projects) >= int(edit_option):
                    deleted_pro= projects[int(edit_option)-1]

                    for key in deleted_pro.__dict__:
                        if key in ["u_id", "p_id"]:
                            continue
                        # just update if value entered else do nothing
                        myinput = input(f"{key} [{deleted_pro.__dict__[key]}] : ")
                        if myinput.strip(" "):
                            deleted_pro.__setattr__(key, myinput)

                    if edit_project(deleted_pro, user):
                        print("Edited Successfully")
                        break

        elif option.isdigit() and int(option) == 3:
           projects = get_all_projects()

           var = "|{:>15}|" * 5
           print("-"*17*5)
           print(var.format("Title", "Details", "Total Target", "Start time", "End Time"))
           print("-"*17*5)
           var = "|{:>15}|" * 5
           for pro in projects:
               print(var.format(pro.title, pro.details, pro.total_target, pro.start_time, pro.end_time))

           print("-"*17*5)
           continue

        elif option.isdigit() and int(option) == 4:

            projects = get_all_projects()

            var = "|{:>15}|" * 6
            print("-" * 17 * 6)
            print(var.format("#", "Title", "Details", "Total Target", "Start time", "End Time"))
            print("-" * 17 * 6)
            var = "|{:>15}|" * 6
            for i, pro in enumerate(projects):
                print(var.format(i+1,pro.title, pro.details, pro.total_target, pro.start_time, pro.end_time))
            print("-" * 17 * 6)

            while True:
                delete_option = input("Enter the number of project you want to delete: ")
                if delete_option.isdigit() and len(projects) >= int(delete_option):
                    deleted_pro= projects[int(delete_option)-1]
                    if delete_project(deleted_pro,user):
                        print("Deleted Successfully")
                        break

            continue

        elif option.isdigit() and int(option) == 5:
            exit(1)
