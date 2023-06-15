# schema.py
# France Cheong
# 21/01/2019

# Import packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric, Float, Date, ForeignKey
# Used by classes PurchaseOrder and PurchaseOrderItem
from sqlalchemy.orm import relationship 

# Get a base class from which all mapped classes should inherit
Base = declarative_base()

# Employee class should inherit from Base class
# Note that "Employee" is spelt with an UPPERCASE "E"
class Student(Base): 

    # Define the name of the table i.e. employee (all lower case, singular)
    # Note that "employee" is spelt with a LOWERCASE "e"
    # Also note that there are TWO UNDERSCORES before and after "tablename"
    __tablename__ = 'student'

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    student_id = Column(String(255), primary_key=True) # primary key
    first_name = Column(String(255), nullable=False) # non null
    last_name = Column(String(255), nullable=False) # non null
    date_of_birth = Column(String(255), nullable=False) # non null, unique
    email = Column(String(255), nullable=False, unique=True) # non null, unique
    phone_num = Column(String(20), nullable=False, unique=True) # non null, unique
    pass

class CourseOffered(Base):

    __tablename__ = 'course_offered'

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    class_no = Column(String(20), nullable=False, unique=True)
    mode = Column(String(255), nullable=False)
    units_of_credit = Column(Integer, nullable=False)
    census_date = Column(Date, nullable=False)
    
class Teacher(Base): 

    # Define the name of the table i.e. employee (all lower case, singular)
    # Note that "employee" is spelt with a LOWERCASE "e"
    # Also note that there are TWO UNDERSCORES before and after "tablename"
    __tablename__ = 'teacher'

    # Define the column names, types, primary key, foreign keys, 
    # null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    teacher_id = Column(String(255), primary_key=True) # primary key
    first_name = Column(String(255), nullable=False) # non null
    last_name = Column(String(255), nullable=False) # non null
    department = Column(String(255), nullable=False)
    date_of_birth = Column(String(255), nullable=False) # non null, unique
    email = Column(String(255), nullable=False, unique=True) # non null, unique

class CourseEnrolment(Base):

    # Define the name of the table
    __tablename__ = 'course_enrolment' # i.e. purchase_order (all lower case, singular)

    # Define the column names, types, primary key, foreign keys, null values allowed, unique, etc
    # Column names should be all lower case, use an underscore to concatenate
    enrolment_no = Column(Integer, primary_key=True) # primary key
    enrolment_date = Column(Date, nullable=False)
    program_name = Column(String(255), nullable=False)
    semester = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False)
    student_id = Column(Integer, ForeignKey("student.student_id")) # foreign key
    course_id = Column(Integer, ForeignKey("course_offered.course_id")) # foreign key
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))

    # Define the 1:m relationship between purchase_order and purchase_order_items
    # format: field_name = relationship("ClassName", back_populates="field_name")
    # "back_populates" means populate the other side of the mapping
    # "cascade="all, delete-orphan" needed for 
    # cascading the deletion of a purchase_order to its purchase_order_items
    # "all" means the child object should follow along with its parent in all cases, 
    # and be deleted once it is no longer associated with that parent
