import uuid

class Project:
    file_name = "project.db"
    def __init__(self, user_id, title, details, total_target, start_time, end_time ):
        self.p_id = str(uuid.uuid1())
        self.u_id = user_id
        self.title = title
        self.details = details
        self.total_target = total_target
        self.start_time = start_time
        self.end_time = end_time

    def set_project_id(self, pid):
        self.p_id = pid

    def __iter__(self):
        return self

    def __next__(self):
        args = list(self.__dict__.values())
        return args

    def __str__(self):
        output = str(":".join(map(str,self.__dict__.values())))
        return output