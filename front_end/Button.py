from tkinter import *
from front_end.member import *
from front_end.Student import *
from front_end.add import *

class Button_details:
    def __init__(self, root):
        self.root = root
        self.root.title('LIBRARY MANAGEMENT SYSTEM')
        self.root.geometry("600x500")

       #=============================Manage Frame=======================

        F1 = Frame(root, bg='maroon')
        F1.place(x=0, y=0, width=650, height=500)

        frame1 = Frame(root, bg='black')
        frame1.place(x=140, y=140, width=330, height=285)

        frame2 = Frame(frame1, bg='light blue')
        frame2.place(x=15, y=10, width=300, height=265)

        headingFrame1 = Frame(root, bg="#333945", bd=5)
        headingFrame1.place(relx=0.21, rely=0.1, relwidth=0.6, relheight=0.14)

        headingFrame2 = Frame(headingFrame1, bg="#EAF0F1")
        headingFrame2.place(relx=0.01, rely=0.04, relwidth=0.98, relheight=0.9)

        headingLabel = Label(headingFrame2, text="Library Management",
                             font=('arial', '17', 'bold'), fg='black')
        headingLabel.place(relx=0.15, rely=0.15, relwidth=0.8, relheight=0.5)

        #===========================Button Frame==============================
        btn_log = Button(frame1, text="Member Info", command=self.member, width=18,
                         font=("times new roman", 20, "bold"),
                         bg="grey", fg="black").place(x=16,y=20)

        btn_log = Button(frame1, text="Student Details", command=self.Student, width=18,
                         font=("times new roman", 20, "bold"),
                         bg="grey", fg="black").place(x=16, y=80)

        btn_log = Button(frame1, text="Add Book Details", command=self.add, width=18,
                         font=("times new roman", 20, "bold"),
                         bg="grey", fg="black").place(x=16, y=140)

        btn_log = Button(frame1, text="Exit", command=root.destroy, width=18,
                         font=("times new roman", 20, "bold"),
                         bg="grey", fg="black").place(x=16, y=200)

    def member(self):
        next_window = Tk()
        Main_Interface(next_window)

    def Student(self):
        next_window = Tk()
        student_details(next_window)

    def add(self):
        next_window = Tk()
        add_details(next_window)


# root=Tk()
# obj=Button_details(root)
# root.mainloop()