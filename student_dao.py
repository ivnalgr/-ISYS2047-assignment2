from schema import Student
from random import randint

class StudentDAO():
    def create(self, session, data):

        print("creating")
        print(data)

        student = Student(student_id = f's{randint(1000000,9999999)}',
                    first_name = data['first_name'],
                    last_name = data['last_name'], 
                    date_of_birth = data['date_of_birth'], 
                    email = data['email'],
                    phone_num = data['phone_num']
                    )

        session.add(student)
        session.commit()
        result = {}  
        result['message'] = 'Employee added successfully!'
        # inserted_student_id = student.student_id
        # result['student_id'] = inserted_student_id

        return result

    def find_by_id(self, session, student_id):

        print("\nFinding an student ...")
        print(student_id)

        cus = session.query(Student).get(student_id)
        result = {}

        if not cus:
            result['message'] = "Student NOT found"
        else:
            d = {} # Create an empty dict and add items to it
            d['student_id'] = cus.student_id # include the employee_id
            d['first_name'] = cus.first_name
            d['last_name'] = cus.last_name
            d['date_of_birth'] = cus.date_of_birth
            d['email'] = cus.email
            d['phone_num'] = cus.phone_num

            result['student'] = d

        return result

    def find_by_lastname(self, session, last_name):

        print("\nFinding student(s) by lastname ...")
        print(last_name)
        result = {}

        rows = session.query(Student) \
                .filter(Student.last_name.like(last_name)) \
                .order_by(Student.student_id).all()
        
        if not rows:
            result['message'] = "No student found"
        else:
            list_cus = []
            for x in rows:
                d = {}
                d['student_id'] = x.student_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['date_of_birth'] = x.date_of_birth
                d['email'] = x.email
                d['phone_num'] = x.phone_num
                list_cus.append(d)
                pass
            
            result['student'] = list_cus

        return result

    def find_all(self, session):
        print("\nFinding all students ...")

        result = {}
        rows = session.query(Student).all()

        if not rows:
            result['message'] = "No students found"
        else:
            list_emp = []
            for x in rows:
                d = {}
                d['student_id'] = x.student_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['date_of_birth'] = x.date_of_birth
                d['email'] = x.email
                d['phone_num'] = x.phone_num
                list_emp.append(d)
                pass

            result['student'] = list_emp
        return result

    def find_ids(self, session):
        print("\nFinding all student ids ...")
        result = {}
        rows = session.query(Student).all()

        if not rows:
            result['message'] = "No students found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.student_id)
                pass

            result['student_ids'] = list_ids

        return result

    def update(self, session, student_id, data):
        print("\nUpdating student ...")
        print(student_id)
        print(data)

        result = {}
        cus = session.query(Student).get(student_id)

        cus.first_name = data['first_name']
        cus.last_name = data['last_name']
        cus.date_of_birth = data['date_of_birth']
        cus.email = data['email']
        cus.phone_num = data['phone_num']

        session.commit()
        result['message'] = "Student updated"

        return result

    def delete(self, session, student_id):

        print("\nDeleting student ...")
        print(student_id)
        result = {}

        cus = session.query(Student).get(student_id)
        session.delete(cus)          
        session.commit()

        result['message'] = "Student deleted"

        return result


