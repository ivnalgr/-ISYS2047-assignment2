# procurement_main_gui.py
# France Cheong
# 22/11/2018

# ########
# Packages
# ########
import tkinter as tk
from student_gui import StudentGUI
from teacher_gui import TeacherGUI
from PIL import ImageTk, Image 
# #################################################
# Import any of your classes defined in other files
# #################################################

# Import all the GUI classes implementing each menu option
# From file xxx.py import class Xxxx
#from employee_gui import EmployeeGUI
#from purchase_order_gui import PurchaseOrderGUI
#from product_gui import ProductGUI
#from supplier_gui import SupplierGUI
# Reports GUI
#from product_report_gui import ProductReportGUI
#from category_report_gui import CategoryReportGUI

# ####################
# ProcurementGUI Class
# ####################



class MainmenuGUI():


    def __init__(self):   
        
        print("Main Menu GUI")


        self.current_gui = MainmenuGUI

        self.root = tk.Tk()
        self.root.title("Main menu")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        width = 900
        height = 600
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        print("Main window coordinated (width, height, x, y) :", width, height, x, y)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.root.resizable(0, 0)

        menubar = tk.Menu(self.root)

        filemenu = tk.Menu(menubar, tearoff=0)

        filemenu.add_command(label="Open", command="")
        filemenu.add_command(label="Save", command="")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

        menubar.add_cascade(label="File", menu=filemenu)

        student_menu = tk.Menu(menubar, tearoff=0)

        student_menu.add_command(label="Student", command=self.create_student_gui)
        menubar.add_cascade(label="Student", menu=student_menu)

        teacher_menu = tk.Menu(menubar, tearoff=0)
        teacher_menu.add_command(label="Teacher", command=self.create_teacher_gui)

        menubar.add_cascade(label="Teacher", menu=teacher_menu)

       
        self.root.config(menu=menubar)
        pass
       
    # Functions to create child frames 
    # when menu options are selected

    def create_student_gui(self):
        student_gui = StudentGUI()
        self.current_gui = student_gui.create_gui(self.root)
        

        
       
        pass

    def create_teacher_gui(self):
        if self.current_gui:
            self.current_gui.destroy()
        
        teacher_gui = TeacherGUI()
        self.current_gui = teacher_gui.create_gui(self.root)
        pass
        
        

        

  

# ###########
# Main method
# ###########

if __name__ == '__main__':
    
    # Instantiate the main application gui
    # it will create all the necessary GUIs
    gui = MainmenuGUI()
    

    # Run the mainloop 
    # the endless window loop to process user inputs
    gui.root.mainloop()
    pass        