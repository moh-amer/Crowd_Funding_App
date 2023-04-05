from models.user import User
""" 
Starting with database operations
"""
def getusers():
    userlist = []
    file = None
    try:
        file = open(User.file_name, "r")
    except Exception as e:
        print(e)
    else:
        for line in file.readlines():
            params = line.rstrip("\n").split(":")
            user = User(*params[1:])
            user.setID(params[0])
            userlist.append(user)
    finally:
        file.close()
        return userlist

def getuser_by_id(id):
    for user in getusers():
        if user.id == id:
            return user
    else:
        return None

def getuser(email, password):
    for user in getusers():
        if user.email == email and user.password == password :
            return user
    else:
        return None
def is_registered_before(input_user):
    for user in getusers():
        if user.email == input_user.email and user.password == input_user.password:
            return True

    return False


def insert_user(user):
    if is_registered_before(user):
       raise Exception("Duplicated User Entry , Can not insert it")

    try:
       file = open(user.file_name, "a")
    except Exception as e:
        print(e)
    else:
        file.writelines(f"{str(user)}\n")
        file.close()
        return True
    # finally:
    #     file.close()
    #     return False


""" 
 End database operations
"""
