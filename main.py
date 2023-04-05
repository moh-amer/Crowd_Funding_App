from utils import show_table

from views.login_view import show_login_view
# show_table(["username", "password", "gmail"], [["1", "2", "3"]])




show_login_view()
# user = User("Mohamed", "Amer", "medo0@mail.com", "123", "01020")
# # project = Project(user.id, "new project", "this is details", 30_000, "20-4-2007", "1-1-2029")
# # print(user)
#
# listofusers = user_dbhelper.getusers()
# # user_controller.insertUser(user)
# print(listofusers[0].id)
# project = Project(listofusers[0].id, "third project", "some details", 20000, "20-10-2020", "20-2-2025")
# # project_controller.insert_project(project)
# pro = project_dbhelper.getProjects()[0]
# # print(pro)
# # print(project_controller.getProjects())
# #
# pro.title = "hello world"
# pro.details = "another details"
# #project_controller.delete_project(pro, listofusers[0])
# project_dbhelper.update_project(pro, listofusers[0])
# #
# # print(project_controller.getProjects())
# #
# # print(project_controller.getProjects().pop())