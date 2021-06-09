from Dbconn import DbConn


class Student_model(DbConn):

    def __init__(self):

        super(Student_model, self).__init__()

    def add_student_info(self,_name,_marks,_age,_attandance):

        query = "insert into student_info(name,marks,age,ATENDANCE) values('{}','{}','{}','{}')".format(_name,_marks,_age,_attandance)

        self.myCursor.execute(query)

        self.myConnection.commit()


class person(DbConn):

    def __init__(self):

        super(person, self).__init__()

    def personal_info(self,_name,_mobile_no,_age,_graduation):

        query = "insert into person_info(name,mobile_no,age,graduation) values('{}','{}','{}','{}')".format(_name,_mobile_no,_age,_graduation)

        self.myCursor.execute(query)

        self.myConnection.commit()
