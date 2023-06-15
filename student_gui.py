# product_gui.py
# France Cheong
# 11/12/2018

# ########
# Packages
# ########
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk # for combobox
from dateutil.parser import parse
from schema import Student
from datetime import datetime
import re

# #################################################
# Import any of your classes defined in other files
# #################################################

import database as db # Import database.py to get a session to a particular db
# From file xxx.py import class Xxxx
from student_dao import StudentDAO # To communicate with Product table
from validation import Validation # To validate the entries made on the form
from random import randint

class StudentGUI():

    def __init__(self):   
        """
        The initialiser is used to "instantiate" attributes of the class.
        The attributes are the "variables" that have been declared "outside" 
        of the methods of the class.
        Some attributes may have not been declared as they may be created 
        any where in the class methods (python allows this).

        Attributes are like global variables for the class, as they are 
        available to any method in the class.
        And, to use them, they must be prefixed with "self."
        
        This differentiates them from "local" variables which are 
        defined/created and used within a single method

        If you need to pass the value of a local variable from one method to 
        another, then you must pass "parameters" to the method 

        We cannot create the GUI here as we need to return a reference to the 
        frame created.
        Hence, we need to implement a 'normal' function to do this 
        e.g. create_gui()

        Parameters (apart from self): None

        Return: None

        """

        # Instantiate a data access object 
        # Contains methods to access the database
        self.stud_dao = StudentDAO()

        # Instantiate a validation object
        # Contains methods to validate input fields
        self.validator = Validation()

        # Form fields
        # Instantiate stringvars to hold the data entered on the form
        self.student_id = tk.StringVar()
        #self.product_name = tk.StringVar() # if using Entry field
        self.first_name = tk.StringVar() # if using larger Text field
        #self.product_description = tk.StringVar() # if using Entry field
        self.last_name = tk.StringVar() # if using larger Text field
        self.date_of_birth = tk.StringVar()
        self.email = tk.StringVar()
        self.phone_num = tk.StringVar()
        self.existing_ids = []
         # check button use IntVar

        # List of product ids - lb for listbox
        self.lb_ids = None

        # Messagebox title
        self.mb_title_bar = "Product CRUD"

        # Load the list of categories
        # session = db.get_db_session() # Get a session (database.py)
        # result = self.stud_dao.find_categories(session)
        # session.close()
        # # Check if key 'categories' is present in dict result
        # if 'categories' in result:
        #     result = result['categories']
        #     # Get the list of keys of the dict
        #     #self.list_cat = result.keys() 
        #         # TypeError: 'dict_keys' object does not support indexing
        #     self.list_cat = [x for x in result.keys()]
        # else:
        #     self.list_cat = []
        # pass

    def create_gui(self, root):
        """
        Create a high level frame which contains the entire GUI 
        (of this part of the application) and adds it to the root window.
        Notice that the "root" window is passed the second parameter in the 
        method header.
        Also notice that the first (and mandatory) parameter to all methods 
        is "self" i.e. a reference to the object instantiated from the class.

        Widgets like labels, entries, etc  (including inner frames) are 
        added to the high level frame 
        At the end, the function return a reference to the frame that was 
        created for the calling program to be able to access it.

        Parameters (apart from self):
            root: main window of application

        Return: 
            prod_frame: the frame containing all the widgets for the product CRUD
        """

        print("Creating product GUI ...")

        # Add a high level frame - will contain the entire product GUI
        prod_frame = tk.Frame(root)
        prod_frame.pack()

        # Add a frame to contain the form widgets
        form_frame = tk.Frame(prod_frame)
        form_frame.pack()

        # Add widgets to form frame
        # row 0:  title label
        tk.Label(form_frame, font=('arial', 10), 
            text = "Student").grid(row=0, column=0, columnspan=3)

        # row 1: product_id label, product_id entry and list_of_ids label
        tk.Label(form_frame, text= "Student Id", font=('arial', 10), 
                 width=20, anchor="e", bd=1, 
                 pady=10, padx=10).grid(row=1, column=0)
        tk.Entry(form_frame, textvariable=self.student_id, 
                 width=30, bd=1, state=tk.DISABLED).grid(row=1, column=1)
        tk.Label(form_frame, text= "Student IDs", 
                 font=('arial', 10)).grid(row=1, column=2)         

        tk.Label(form_frame, text= "First name", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=2, column=0)
        tk.Entry(form_frame, textvariable=self.first_name, 
                 width=30, bd=1).grid(row=2, column=1)
        self.lb_ids = tk.Listbox(form_frame)
        self.lb_ids.grid(row=2, column=2, rowspan=5) 
        self.lb_ids.bind('<<ListboxSelect>>', self.on_list_select)

        tk.Label(form_frame, text= "Last name", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=3, column=0)
        tk.Entry(form_frame, textvariable=self.last_name, 
                 width=30, bd=1).grid(row=3, column=1)

        tk.Label(form_frame, text= "Date of birth", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=4, column=0)
        tk.Entry(form_frame, textvariable=self.date_of_birth, 
                 width=10).grid(row=4, column=1, sticky="w")

        tk.Label(form_frame, text= "Email", font=('arial', 10), 
                 width=20, anchor="e", bd=1, pady=10, padx=10).grid(row=5, column=0)
        tk.Entry(form_frame, textvariable=self.email, width=30, bd=1).grid(row=5, column=1)

        tk.Label(form_frame, text= "Phone number", font=('arial', 10), width=20, 
                 anchor="e", bd=1, pady=10, padx=10).grid(row=6, column=0)
        tk.Entry(form_frame, textvariable=self.phone_num, 
                 width=30, bd=1).grid(row=6, column=1)

        # Buttons
        # There are 3 columns of widgets in the frame and 4 buttons
        # Better insert the button in another frame
        # Also easier to pack them from the left than using a grid 
        # with row and col locations
        # pady to leave a space from frame on top
        button_frame = tk.Frame(prod_frame, pady=10) 
        button_frame.pack()
        # For 'tkinter Button' options, 
        # refer to http://effbot.org/tkinterbook/button.htm
        # Use the anchor= option to position the button
        # External padding around buttons: padx= pady=  default is 0
        # Use the width= option to specify the number of characters, 
        # otherwise calculated based on text width
        tk.Button(button_frame, width=10, text="Clear", 
                  command=self.clear_fields).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Save", 
                  command=self.save).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Delete", 
                  command=self.delete).pack(side=tk.LEFT)
        tk.Button(button_frame, width=10, text="Load", 
                  command=self.load).pack(side=tk.LEFT)       

        # Return a reference to the product frame
        # Will need the reference to be able to destroy it in calling function
        return prod_frame

    def clear_fields(self):
        self.student_id.set("")
        self.first_name.set("")
        self.last_name.set("")
        self.date_of_birth.set("")
        self.email.set("")
        self.phone_num.set("")
        pass

    def save(self):
        print("Saving an student ...")

        # Get the data
        data = self.get_fields()   

        # Validate the data
        valid_data, message = self.validate_fields(data)
        if valid_data:
            if (len(data['student_id'])==0):
                # If nothing has been entered in employee_id 
                # i.e. its length is zero characters
                print("Calling create() as student_id is absent")
                self.create(data)
            else:
                print("Calling update() as student_id is present")
                self.update(data)
                pass
        else:
            message_text = "Invalid fields.\n" + message 
            messagebox.showwarning(self.mb_title_bar, message_text, icon="warning")
            pass

    def get_fields(self):
        
        stud = {}
        stud['student_id'] = self.student_id.get() 
        stud['first_name'] = self.first_name.get()
        stud['last_name'] = self.last_name.get()
        stud['date_of_birth'] = parse(self.date_of_birth.get())
        stud['email'] = self.email.get()
        stud['phone_num'] = self.phone_num.get()

        # if self.date_of_birth.get():
        #     stud['dob'] = parse(self.date_of_birth.get())
        # else:
        #     stud['dob'] = None
        
        return stud

    def validate_fields(self, data):
        valid_data = True 
        
        message_list = []

        if len(data['first_name'])==0:
            valid_data = False
            message_list.append("firstname is empty")
        if len(data['last_name'])==0:
            valid_data = False
            message_list.append("lastname is empty")
        if len(data['email'])==0:
            valid_data = False
            message_list.append("email is empty")
        if len(data['phone_num'])==0:
            valid_data = False
            message_list.append("work_phone is empty")


        message = ', '.join(message_list)

        return valid_data, message

    def create(self, data):
        print("Creating an students ...")
        print(data)

        session = db.get_db_session()
        result = self.stud_dao.create(session, data) 
        
        session.close() 

        messagebox.showinfo(self.mb_title_bar, result)
 
        pass

    def update(self, data):
        print("Updating an student ...")
        print(data)

        session = db.get_db_session() # Get a session (database.py)
        result = self.stud_dao.update(session, data['student_id'], data)
        session.close() # close the session

        # Display the returned message to the user - use a messagebox  
        # Display everything that is returned in the result      
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def delete(self):
        id = self.student_id.get() 
        print(id)
        
        session = db.get_db_session() 
        result = self.stud_dao.delete(session, id)
        session.close() 
  
        messagebox.showinfo(self.mb_title_bar, result)
        pass

    def load(self):
        session = db.get_db_session() # Get a session (database.py)
        result = self.stud_dao.find_ids(session) # {"employee_ids": [1, 2, 3]}
        session.close() # Close the session
        print("result", result)
        # Check if there is an entry in the result dictionary
        if "student_ids" in result: 
            list_ids = result['student_ids'] # will crash if there is no entry!
            # Set the returned list into the listbox
            # Before doing that, must clear any previous list in the box
            self.lb_ids.delete(0,tk.END)
            self.existing_ids.clear()
            print("Setting student_id in listbox ...")
            for x in list_ids:
                self.lb_ids.insert(tk.END, x)
                # print(x)
                self.existing_ids.append(x)
            pass


    def on_list_select(self, evt):
        w = evt.widget
        index = int(w.curselection()[0]) 
          # index = position of the item clicked in the list, first item is item 0 not 1
        value = w.get(index) 
          # value of the item clicked, in our case it's the employee_id
        print(index) 
        print(value)

        # Call find_by_id and populate the stringvars of the form
        session = db.get_db_session() # Get a session (database.py)
        result = self.stud_dao.find_by_id(session, value)   
        session.close() # close the session
        print("result", result) 
           # { "employee" : {"employee_id": "", "firstname": "", etc}}
        stu = result['student']
        self.populate_fields(stu)
        pass

    def populate_fields(self, stud):
        self.student_id.set(stud['student_id'])
        self.first_name.set(stud['first_name'])
        self.last_name.set(stud['last_name'])
        print(stud['date_of_birth'])
        if ":" in stud['date_of_birth']:
            self.date_of_birth.set('{}/{}/{}'.format(stud['date_of_birth'][8:10], stud['date_of_birth'][5:7],stud['date_of_birth'][0:4]))
        else:
            self.date_of_birth.set(stud['date_of_birth'])
        self.email.set(stud['email'])
        self.phone_num.set(stud['phone_num'])
        pass

    



# ###########
# Main method
# ###########

if __name__ == '__main__':
    """
    The main method is only executed when the file is 'run' 
    (not imported in another file)
    """
     
    # Setup a root window (in the middle of the screen)
    root = tk.Tk()
    root.title("Procurement System")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 900
    height = 500
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Instantiate the gui
    gui = StudentGUI()

    # Create the gui - pass the root window as parameter
    gui.create_gui(root)

    # Run the mainloop - the endless window loop to process user inputs
    root.mainloop()