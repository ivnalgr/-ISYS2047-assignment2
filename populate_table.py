from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ###########################################
# Import your classes defined in other files
# ###########################################
# From file xxx.py import class Xxxx
from schema import Student
from schema import CourseEnrolment
from schema import CourseOffered
from schema import Teacher

DATABASE_URI = 'sqlite:///app.db'

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def populate():

    # Get a session
    session = get_db_session()

    session.add_all([
        Student(student_id = 's3849118',
                 first_name = 'Ivan', 
                 last_name = 'Alegria', 
                 date_of_birth = '23/08/2002', 
                 email = 's3849118@student.rmit.edu.au', 
                 phone_num = '02 1999 9999'),

        Student(student_id = 's1234567',
                 first_name = 'John', 
                 last_name = 'Martin', 
                 date_of_birth = '01/01/1990', 
                 email = 's1234567@student.rmit.edu.au', 
                 phone_num = '02 2999 9999'),

        Student(student_id = 's7654321',
                 first_name = 'Bob', 
                 last_name = 'Ross', 
                 date_of_birth = '29/10/1942', 
                 email = 's7654321@student.rmit.edu.au', 
                 phone_num = '02 3999 9999') 
        ])

    session.add_all([
        Teacher(teacher_id = 't9085477',
                 first_name = 'Ivan', 
                 last_name = 'Alegria', 
                 department = 'Information Technology',
                 date_of_birth = '29/10/1942', 
                 email = 't9085477@teacher.rmit.edu.au'), 


        Teacher(teacher_id = 't5437894',
                 first_name = 'Ken', 
                 last_name = 'Rob', 
                 department = 'Business',
                 date_of_birth = '03/12/2000', 
                 email = 't5437894@teacher.rmit.edu.au'), 

        Teacher(teacher_id = 't6348763',
                 first_name = 'Rock', 
                 last_name = 'Baker', 
                 department = 'Information Systems',
                 date_of_birth = '04/09/1999', 
                 email = 't6348763@teacher.rmit.edu.au')
    ])

    session.commit()


    session.close()


if __name__ == "__main__":
        populate()
