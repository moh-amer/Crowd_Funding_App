from models.project import Project
"""
Starting with database operations
"""
def getProjects():
    projects_list = []
    try:
        file = open(Project.file_name, "r")
    except IOError as e:
        print(e)
    else:
        for line in file.readlines():
            params = line.rstrip("\n").split(":")
            project = Project(*params[1:])
            project.set_project_id(params[0])
            projects_list.append(project)
    finally:
        file.close()
        return projects_list



def insert_project(project, mode="a"):
    try:
        file = open(project.file_name, mode)
    except IOError as e:
        print(e)
        return False
    else:
        file.writelines(f"{str(project)}\n")
        return True

def delete_project(project, user):
    if not project.u_id == user.id:
        raise Exception("This User isn't authorized to delete this project")

    flag = False
    projects = getProjects()

    for pro in projects:
        if pro.p_id == project.p_id:
            projects.remove(pro)
            flag=True

    open(project.file_name , "w").close() # this line used to clear file contents
    for project in projects:
        insert_project(project)
    return flag

def update_project(updated_project, user):
    if not updated_project.u_id == user.id:
        raise Exception("This User isn't authorized to delete this project")

    flag = False
    projects = getProjects()
    for i, pro in enumerate(projects):
        if pro.p_id == updated_project.p_id:
            projects[i] = updated_project
            flag = True

    open(updated_project.file_name,"w").close() # this line used to clear file contents
    for project in projects:
        insert_project(project)
        flag = True
    return flag
""" 
 End database operations
"""
