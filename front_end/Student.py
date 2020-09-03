from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from model.student import *
from back_end.Connection import *

class student_details:
    def __init__(self, root):

        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1215x420")
        title = Label(self.root, bd=10, relief=GROOVE, text="Student Details", font=('arial', 15, 'bold'), bg="grey",
                      fg="gold", pady=2).pack(fill=X)
        F1 = LabelFrame(self.root, bd=10, relief=GROOVE, font=("arial 15 bold"), bg="grey",
                        fg="gold", pady=2)
        F1.place(x=0, y=60, relwidth=1)

        # =========================Connection Object====================
        self.dbconnect = DbConnection()


        #=======================Frame in window==============================

        self.lblStudentID = Label(F1, font=('arial', 18, 'bold'), text='Student ID:',bd=4,bg="grey",padx=2, pady=2)
        self.lblStudentID.grid(row=0, column=0, sticky=W)
        self.txtStudentID = Entry(F1, font=('arial', 14, 'bold'), width=20)
        self.txtStudentID.grid(row=0, column=1)


        self.lblFirstName = Label(F1, font=('arial', 18, 'bold'), text='First Name:', bd=4,bg="grey",padx=2, pady=2)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.txtFirstName = Entry(F1, font=('arial', 14, 'bold'), width=20)
        self.txtFirstName.grid(row=1, column=1)

        self.lblLastName = Label(F1, font=('arial', 18, 'bold'), text='Last Name:',bd=4,bg="grey", padx=2, pady=2)
        self.lblLastName.grid(row=2, column=0, sticky=W)
        self.txtLastName = Entry(F1, font=('arial', 14, 'bold'), width=20)
        self.txtLastName.grid(row=2, column=1)

        self.lblAge= Label(F1, font=('arial', 18, 'bold'), text='Age:',bd=4,bg="grey", padx=2, pady=2)
        self.lblAge.grid(row=3, column=0, sticky=W)
        self.txtAge = Entry(F1, font=('arial', 14, 'bold'), width=20)
        self.txtAge.grid(row=3, column=1)

        self.lblGender = Label(F1, font=('arial', 18, 'bold'), text='Gender:',bd=4,bg="grey", padx=2, pady=2)
        self.lblGender.grid(row=4, column=0, sticky=W)

        self.cboGender = ttk.Combobox(F1, font=('arial', 14, 'bold'),
                                         state='readonly', width=20)
        self.cboGender['value'] = ('Male', 'Female')
        self.cboGender.grid(row=4, column=1)

        self.lblAddress = Label(F1, font=('arial', 18, 'bold'), text='Address:',bd=4,bg="grey", padx=2, pady=2)
        self.lblAddress.grid(row=5, column=0, sticky=W)
        self.txtAddress = Entry(F1, font=('arial', 14, 'bold'), width=20)
        self.txtAddress.grid(row=5,column=1)


        # =========================BUtton Frame============================

        btn_frame = Frame(self.root, bd=20, width=1000, height=100, padx=5, relief=RIDGE)
        btn_frame.place(x=0, y=330, height=80)

        self.btn_add = Button(btn_frame, text='Add', font=('arial', 15, 'bold'), width=7, bd=4,
                              command=self.add)
        self.btn_add.grid(row=0, column=0)

        self.btn_update = Button(btn_frame, text='Update', font=('arial', 15, 'bold'), width=7, bd=4,
                                 command=self.update)
        self.btn_update.grid(row=0, column=1)

        self.btn_clear = Button(btn_frame, text='Clear', font=('arial', 15, 'bold'), width=7, bd=4,
                                command=self.clear)
        self.btn_clear.grid(row=0, column=2)

        self.btn_del = Button(btn_frame, text='Delete', font=('arial', 15, 'bold'), width=7, bd=4,
                              command=self.delete)
        self.btn_del.grid(row=0, column=3)

        self.btn_exit = Button(btn_frame, text='Exit', font=('arial', 15, 'bold'), width=7, bd=4,
                               command=root.destroy)
        self.btn_exit.grid(row=0, column=4)

        self.btn_view = Button(btn_frame, text='View', font=('arial', 15, 'bold'),width=7,bd=4,
                               command=self.view)
        self.btn_view.grid(row=0, column=5)

    def add(self):
        cus_obj = Student(self.txtStudentID.get(), self.txtFirstName.get(), self.txtLastName.get(),
                          self.txtAge.get(),
                          self.cboGender.get(), self.txtAddress.get())
        query = 'insert into student values(%s,%s,%s,%s,%s,%s);'
        values = (cus_obj.get_StudentID(), cus_obj.get_FirstName(), cus_obj.get_LastName(), cus_obj.get_Age(),
                  cus_obj.get_Gender(), cus_obj.get_Address())
        self.dbconnect.insert(query, values)
        messagebox.showinfo('Success', 'Data inserted successfully')

        self.fetch_data()
        self.clear()

    def update(self):
        cus_obj = Student(self.txtStudentID.get(), self.txtFirstName.get(), self.txtLastName.get(),
                          self.txtAge.get(),
                          self.cboGender.get(), self.txtAddress.get())
        query = "update student set FirstName=%s,LastName=%s,Age=%s,Gender=%s,Address=%s where StudentID=%s;"
        values = (
        cus_obj.get_FirstName(), cus_obj.get_LastName(), cus_obj.get_Age(), cus_obj.get_Gender(), cus_obj.get_Address(),
        cus_obj.get_StudentID())
        self.dbconnect.update(query, values)
        messagebox.showinfo('Success', 'Data updated successfully')

        self.fetch_data()
        self.clear()

    def clear(self):
        self.txtStudentID.delete('0', END)
        self.txtFirstName.delete('0', END)
        self.txtLastName.delete('0', END)
        self.txtAge.delete('0', END)
        self.cboGender.set('')
        self.txtAddress.delete('0', END)

        self.fetch_data()
        self.clear()

    def delete(self):

        cus_obj = Student(self.txtStudentID.get(), self.txtFirstName.get(), self.txtLastName.get(),
                          self.txtAge.get(),
                          self.cboGender.get(), self.txtAddress.get())
        query = ('delete from student where StudentID=%s')
        values = (cus_obj.get_StudentID(),)
        self.dbconnect.delete(query, values)
        messagebox.showinfo('Success', 'Data deleted successfully')

        self.fetch_data()
        self.clear()

    def fetch_data(self):
        cus_obj = Student(self.txtStudentID.get(), self.txtFirstName.get(), self.txtLastName.get(),
                          self.txtAge.get(),
                          self.cboGender.get(), self.txtAddress.get())

        query = 'select * from student'
        rows = self.dbconnect.select(query)

        if len(rows) != 0:
            self.all_book_tree.delete(
                *self.all_book_tree.get_children())

            for row in rows:
                self.all_book_tree.insert('', END, values=row)

    def show_data(self, ev):
        data_row = self.all_book_tree.focus()
        content = self.all_book_tree.item(data_row)
        row = content['values']

        cus_obj = Student(self.txtStudentID.get(), self.txtFirstName.get(), self.txtLastName.get(),
                          self.txtAge.get(),
                          self.cboGender.get(), self.txtAddress.get())
        self.txtStudentID.insert(END, row[0])
        self.txtFirstName.insert(END, row[1])
        self.txtLastName.insert(END, row[2])
        self.txtAge.insert(END, row[3])
        self.cboGender.set(row[4])
        self.txtAddress.insert(END, row[5])

    # -====================================================view frame

    def view(self):
        self.root.geometry()

        self.srch = StringVar()

        self.frame1 = Frame(self.root, bg='black')
        self.frame1.place(x=400, y=60, width=810, height=250)

        self.frame2 = Frame(self.frame1, bg='black')
        self.frame2.place(x=10, y=40, width=760, height=200)

        self.all_book_tree = ttk.Treeview(self.frame2,
                                          columns=('StudentID', 'FirstName', 'LastName', 'Age', 'Gender', 'Address'))
        self.all_book_tree.place(x=20, y=500, width=750, height=1000)
        self.all_book_tree['show'] = 'headings'
        self.all_book_tree.column('StudentID', width=90)
        self.all_book_tree.column('FirstName', width=130)
        self.all_book_tree.column('LastName', width=130)
        self.all_book_tree.column('Age', width=130)
        self.all_book_tree.column('Gender', width=130)
        self.all_book_tree.column('Address', width=130)

        self.all_book_tree.heading('StudentID', text="StudentID")
        self.all_book_tree.heading('FirstName', text="FirstName")
        self.all_book_tree.heading('LastName', text="LastName")
        self.all_book_tree.heading('Gender', text="Gender")
        self.all_book_tree.heading('Age', text="Age")
        self.all_book_tree.heading('Address', text="Address")

        self.all_book_tree.pack(fill=BOTH, expand=1)
        self.all_book_tree.bind('<ButtonRelease-1>', self.show_data)
        self.fetch_data()


        # entry for searching keyword

        self.lbl_search = Label(self.frame1, text="Search By:", font=("arial", 13, "bold"))
        self.lbl_search.place(x=10, y=5)

        # combobox for showing search by status
        self.combo_search = ttk.Combobox(self.frame1, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_search['values'] = ("StudentID", "FirstName")
        self.combo_search.place(x=120, y=5)

        # entry for searching keyword
        self.txt_search = Entry(self.frame1, width=12, font=("arial", 15, "bold"), bd=3, relief=GROOVE)
        self.txt_search.place(x=270,y=5)


        # =============search and show button shown at top=================
        searchbtn = Button(self.frame1, text="Search", width=8, pady=5, command=self.search_student)
        searchbtn.place(x=430,y=5)

        showbtn = Button(self.frame1, text="Show All", width=8, pady=5,
                         command=self.fetch_data)
        showbtn.place(x=520,y=5)


        # ================================Exit Button============================
        self.btn_exit = Button(self.frame1, text='Exit', font=('arial', 10, 'bold'), fg='black', bg='orange', width=3,
                               bd=3, height=5, command=self.frame1.destroy)
        self.btn_exit.place(x=772, y=150)

        # ===================Linear Search===============================
    @classmethod
    def search(cls, record, values, index):
        rows = []
        for item in record:
            if type(item[index]) != str:
                if item[index] == values:
                    rows.append(item)
            else:
                if item[index].upper() == values.upper():
                    rows.append(item)
        return rows


    def search_student(self):
        searchbtn=self.combo_search.get()
        search_student = self.txt_search.get()
        try:
            search_student=int(search_student)

        except ValueError:
            pass

        if searchbtn == '':
            messagebox.showinfo('Error', 'Select all required item')

        elif searchbtn == 'StudentID' and type(search_student) != int:
            messagebox.showerror('Error', 'Please input integer value')

        else:
            query = 'select * from student'
            record = self.dbconnect.select(query)
            if searchbtn == 'StudentID':
                rows = student_details.search(record, search_student, 0)

            elif searchbtn == 'FirstName':
                rows = student_details.search(record, search_student, 1)

            else:
                rows = []

            if len(rows) != 0:
                self.all_book_tree.delete(
                    *self.all_book_tree.get_children())
                for row in rows:
                    self.all_book_tree.insert('', END, values=row)


# root = Tk()
# obj = student_details(root)
# root.mainloop()