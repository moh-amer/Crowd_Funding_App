from dbhelpers import project_dbhelper as phelper

def add_project(project):
    return phelper.insert_project(project)

def delete_project(project, user):
    return phelper.delete_project(project, user)

def edit_project(project, user):
    return phelper.update_project(project, user)

def get_all_projects():
    return phelper.getProjects()


