from schema import Teacher
from random import randint


class TeacherDAO():
    def create(self, session, data):

        print("creating")
        print(data)

        teacher = Teacher(teacher_id = f't{randint(1000000,9999999)}',
                    first_name = data['first_name'],
                    last_name = data['last_name'], 
                    department = data['department'],
                    date_of_birth = data['date_of_birth'], 
                    email = data['email']
                    )

        session.add(teacher)
        session.commit()
        result = {}  
        result['message'] = 'Employee added successfully!'
        # inserted_teacher_id = teacher.teacher_id
        # result['teacher_id'] = inserted_teacher_id

        return result

    def find_by_id(self, session, teacher_id):

        print("\nFinding an teacher ...")
        print(teacher_id)

        tea = session.query(Teacher).get(teacher_id)
        result = {}

        if not tea:
            result['message'] = "Teacher NOT found"
        else:
            d = {} # Create an empty dict and add items to it
            d['teacher_id'] = tea.teacher_id # include the employee_id
            d['first_name'] = tea.first_name
            d['last_name'] = tea.last_name
            d['department'] = tea.department
            d['date_of_birth'] = tea.date_of_birth
            d['email'] = tea.email

            result['teacher'] = d

        return result

    def find_by_lastname(self, session, last_name):

        print("\nFinding teacher(s) by lastname ...")
        print(last_name)
        result = {}

        rows = session.query(Teacher) \
                .filter(Teacher.last_name.like(last_name)) \
                .order_by(Teacher.teacher_id).all()
        
        if not rows:
            result['message'] = "No teacher found"
        else:
            list_tea = []
            for x in rows:
                d = {}
                d['teacher_id'] = x.teacher_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['department'] = x.department
                d['date_of_birth'] = x.date_of_birth
                d['email'] = x.email
                list_tea.append(d)
                pass
            
            result['teacher'] = list_tea

        return result

    def find_all(self, session):
        print("\nFinding all teachers ...")

        result = {}
        rows = session.query(Teacher).all()

        if not rows:
            result['message'] = "No teachers found"
        else:
            list_tea = []
            for x in rows:
                d = {}
                d['teacher_id'] = x.teacher_id
                d['first_name'] = x.first_name
                d['last_name'] = x.last_name
                d['department'] = x.department
                d['date_of_birth'] = x.date_of_birth
                d['email'] = x.email
                list_tea.append(d)
                pass

            result['teacher'] = list_tea
        return result

    def find_ids(self, session):
        print("\nFinding all teacher ids ...")
        result = {}
        rows = session.query(Teacher).all()

        if not rows:
            result['message'] = "No teachers found!"
        else:
            list_ids = []
            for x in rows:
                list_ids.append(x.teacher_id)
                pass

            result['teacher_ids'] = list_ids

        return result

    def update(self, session, teacher_id, data):
        print("\nUpdating teacher ...")
        print(teacher_id)
        print(data)

        result = {}
        tea = session.query(Teacher).get(teacher_id)
        
        tea.teacher_id = data['teacher_id']
        tea.first_name = data['first_name']
        tea.last_name = data['last_name']
        tea.department = data['department']
        tea.date_of_birth = data['date_of_birth']
        tea.email = data['email']

        session.commit()
        result['message'] = "Teacher updated"

        return result

    def delete(self, session, teacher_id):

        print("\nDeleting student ...")
        print(teacher_id)
        result = {}

        tea = session.query(Teacher).get(teacher_id)
        session.delete(tea)          
        session.commit()

        result['message'] = "Teacher deleted"

        return result

