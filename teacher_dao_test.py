from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the DAO
# From file xxx.py import class Xxxx
# Note: Filenames with hyphens cannot be imported, use underscores
from teacher_dao import TeacherDAO

# Database location
# Uniform Resource Identifier (URI) generic version of URL
# URI - a string of characters that unambiguously identifies a particular resource
DATABASE_URI = 'sqlite:///app.db'
# File app.db will be created in the folder where the python script is found

def get_db_session():
    engine = create_engine(DATABASE_URI, echo=False)
    # echo=False means do not show generated SQL statements
    # Can be set to echo=True to show SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

def test_create():

    session = get_db_session()
    tea = TeacherDAO()

    # Setup the data as a dictionary
    """
    data = {}
    data['first_name'] = "Ivan"
    data['last_name'] = "Alegria"
    data['department'] = "Information Technology"
    data['date_of_birth'] = "23/08/2002"
    data['email'] = "s3849118@student.rmit.edu.au"
    """

    # Alternatively, the data could be set up in JSON format
    data = {
        'first_name':"Ivan",
        'last_name': "Alegria",
        'department':"Information Technology",
        'date_of_birth': "23/08/2002",
        'email': "s3849118@teacher.rmit.edu.au",
    }

    result = tea.create(session, data)
    print(result)
    session.close()

def test_find_by_id():
    session = get_db_session()
    tea = TeacherDAO()
    teacher_id = 1
    result = tea.find_by_id(session, teacher_id)

    print(result)
    session.close()

def test_find_by_lastname():
    session = get_db_session()
    tea = TeacherDAO()
    last_name = "Alegria"
    
    result = tea.find_by_lastname(session, last_name)

    print(result)
    session.close()

def test_find_all():
    session = get_db_session()

    tea = TeacherDAO()
    result = tea.find_all(session)

    print(result)
    session.close()

def test_find_ids():
    session = get_db_session()
    

    tea = TeacherDAO()
    result = tea.find_ids(session)

    print(result)

    session.close()  

def test_update():
    session = get_db_session()
    tea = TeacherDAO()
    teacher_id = 1

    data = {}
    data['first_name'] = "Ivan"
    data['last_name'] = "Alegria"
    data['department'] = "Information Technology"
    data['date_of_birth'] = "23/08/2002"
    data['email'] = "s3849118@student.rmit.edu.au"
    

    result = tea.update(session, teacher_id, data)
    print(result)
    session.close()

def test_delete():
    session = get_db_session()
    tea = TeacherDAO()

    teacher_id = 1 
    result = tea.delete(session, teacher_id)

    print(result)
    session.close()

if __name__ == "__main__":

    print("\nTesting ...")

    # Test the create() method
    test_create()

    test_find_by_id()

    test_find_by_lastname()

    test_find_all()

    test_find_ids()

    test_update()

    test_delete()
