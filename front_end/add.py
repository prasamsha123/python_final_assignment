from tkinter import*
from tkinter import ttk
from model.add import *
from back_end.Connection import *
from tkinter import messagebox

class add_details:
    def __init__(self,root):
        self.root =root
        self.root.title("Library Management System")
        self.root.geometry("650x500")


        #==============================Connection=====================
        self.dbconnect =DbConnection()


        #========================Frame===================================
        F1=Frame(root,bg='green')
        F1.place(x=0, y=0,width=650,height=500)

        frame1 = Frame(root, bg='black')
        frame1.place(x=70, y=140, width=510, height=335)

        frame2 = Frame(frame1, bg='orange')
        frame2.place(x=15, y=10, width=480, height=315)

        headingFrame1 = Frame(root, bg="black", bd=5)
        headingFrame1.place(relx=0.30, rely=0.1, relwidth=0.4, relheight=0.12)

        headingFrame2 = Frame(headingFrame1, bg="orange")
        headingFrame2.place(relx=0.01, rely=0.04, relwidth=0.98, relheight=0.9)

        headingLabel = Label(headingFrame2, text="Add Books",
                             font=('arial', '17', 'bold'),bg="orange", fg='black')
        headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)

        #===================Manage Frame===============

        self.lblBookID = Label(frame2, font=('arial', 18, 'bold'), text='BookID:',bd=6,  bg="orange",padx=2, pady=2)
        self.lblBookID.grid(row=0,column=0,sticky=W)
        self.txtBookID = Entry(frame2, font=('arial', 14, 'bold'), width=20)
        self.txtBookID.grid(row=0,column=1)

        self.lblBookName = Label(frame2, font=('arial', 18, 'bold'), text='Book Name:', bd=4, bg="orange", padx=2, pady=2)
        self.lblBookName.grid(row=1, column=0, sticky=W)

        self.cboBookName = ttk.Combobox(frame2,font=('arial', 14, 'bold'),
                                      state='readonly', width=18)
        self.cboBookName['value'] = ('Computing', 'Maths', 'Networking', 'Computer', 'Usability')
        self.cboBookName.grid(row=1, column=1)

        self.lblAuthor = Label(frame2, font=('arial', 18, 'bold'), text='Author:', bd=4, bg="orange", padx=2, pady=2)
        self.lblAuthor.grid(row=2, column=0, sticky=W)
        self.txtAuthor = Entry(frame2, font=('arial', 14, 'bold'), width=20)
        self.txtAuthor.grid(row=2, column=1)

        self.lblBookEdition = Label(frame2, font=('arial', 18, 'bold'), text='Book Edition:', bd=4, bg="orange", padx=2, pady=2)
        self.lblBookEdition.grid(row=3, column=0, sticky=W)
        self.txtBookEdition = Entry(frame2,font=('arial', 14, 'bold'), width=20)
        self.txtBookEdition.grid(row=3, column=1)



        self.lblDateBorrowed = Label(frame2, font=('arial', 18, 'bold'), text='Date Borrowed:', bd=4, bg="orange", padx=2, pady=2)
        self.lblDateBorrowed.grid(row=4, column=0, sticky=W)
        self.txtDateBorrowed = Entry(frame2, font=('arial', 14, 'bold'), width=20)
        self.txtDateBorrowed.grid(row=4, column=1)

        self.lblDateIssued = Label(frame2, font=('arial', 18, 'bold'), text='Date Issued:', bd=4, bg="orange", padx=2,
                                     pady=2)
        self.lblDateIssued.grid(row=5, column=0, sticky=W)
        self.txtDateIssued = Entry(frame2,  font=('arial', 14, 'bold'), width=20)
        self.txtDateIssued.grid(row=5, column=1)


     #=================================Button Frame======================================

        self.btn_add = Button(frame2, text='Add', font=('arial', 15, 'bold'),
                              width=5, bd=4,command=self.add)
        self.btn_add.place(x=3,y=260)

        self.btn_update = Button(frame2, text='Update', font=('arial', 15, 'bold'),
                                 width=5, bd=4,command=self.update)
        self.btn_update.place(x=82, y=260)

        self.btn_clear = Button(frame2, text='Clear', font=('arial', 15, 'bold'),
                                width=5, bd=4,command=self.clear)
        self.btn_clear.place(x=162,y=260)

        self.btn_del = Button(frame2, text='Delete', font=('arial', 15, 'bold'),
                              width=5, bd=4,command=self.delete)
        self.btn_del.place(x=242, y=260)

        self.btn_exit = Button(frame2, text='Exit', font=('arial', 15, 'bold'),
                               width=5, bd=4, command=root.destroy)
        self.btn_exit.place(x=320, y=260)

        self.btn_view = Button(frame2, text='View',command=self.view,
                               font=('arial', 15, 'bold'), width=5, bd=4)
        self.btn_view.place(x=400, y=260)

    def add(self):
     add_obj=Book(self.txtBookID.get(), self.cboBookName.get(), self.txtAuthor.get(),
                     self.txtBookEdition.get(), self.txtDateBorrowed.get(), self.txtDateIssued.get())
     query = 'insert into detail values (%s,%s,%s,%s,%s,%s);'
     values= (add_obj.get_BookID(),add_obj.get_BookName(), add_obj.get_Author(),
              add_obj.get_BookEdition(),add_obj.get_DateBorrowed(),add_obj.get_DateIssued())

     self.dbconnect.insert(query, values)
     messagebox.showinfo('Success','Data inserted successfully')

     self.fetch_data()
     self.clear()

    def update(self):
        cus_obj = Book(self.txtBookID.get(), self.cboBookName.get(), self.txtAuthor.get(),
                          self.txtBookEdition.get(),
                          self.txtDateBorrowed.get(), self.txtDateIssued.get())
        query = "update detail set BookName=%s,Author=%s,BookEdition=%s,DateBorrowed=%s,DateIssued=%s where BookID=%s;"
        values = (
        cus_obj.get_BookName(), cus_obj.get_Author(), cus_obj.get_BookEdition(), cus_obj.get_DateBorrowed(),
        cus_obj.get_DateIssued(),cus_obj.get_BookID())
        self.dbconnect.update(query, values)
        messagebox.showinfo('Success', 'Data updated successfully')

        self.fetch_data()
        self.clear()

    def clear(self):
        self.txtBookID.delete('0', END)
        self.cboBookName.set('')
        self.txtAuthor.delete('0', END)
        self.txtBookEdition.delete('0', END)
        self.txtDateBorrowed.delete('0', END)
        self.txtDateIssued.delete('0', END)

        self.fetch_data()
        self.clear()

    def delete(self):

        cus_obj = Book(self.txtBookID.get(), self.cboBookName.get(), self.txtAuthor.get(),
                          self.txtBookEdition.get(),
                          self.txtDateBorrowed.get(), self.txtDateIssued.get())
        query = ('delete from detail where BookID=%s')
        values = (cus_obj.get_BookID(),)
        self.dbconnect.delete(query, values)
        messagebox.showinfo('Success', 'Data deleted successfully')

        self.fetch_data()
        self.clear()


    def fetch_data(self):
        cus_obj = Book(self.txtBookID.get(), self.cboBookName.get(), self.txtAuthor.get(),
                       self.txtBookEdition.get(),
                       self.txtDateBorrowed.get(), self.txtDateIssued.get())

        query = 'select * from detail'
        rows = self.dbconnect.select(query)

        if len(rows) != 0:
            self.Tree_Table.delete(
                *self.Tree_Table.get_children())

            for row in rows:
                self.Tree_Table.insert('', END, values=row)

    def show_data(self, ev):
        data_row = self.Tree_Table.focus()
        content = self.Tree_Table.item(data_row)
        row = content['values']

        cus_obj = Book(self.txtBookID.get(), self.cboBookName.get(), self.txtAuthor.get(),
                       self.txtBookEdition.get(),
                       self.txtDateBorrowed.get(), self.txtDateIssued.get())
        self.txtBookID.insert(END, row[0])
        self.cboBookName.set(row[1])
        self.txtAuthor.insert(END, row[2])
        self.txtBookEdition.insert(END, row[3])
        self.txtDateBorrowed.insert(END, row[4])
        self.txtDateIssued.insert(END, row[5])


#==============================view===================================
    def view(self):
        self.root2=Toplevel()
        self.root2.title('view')
        self.root2.geometry('900x460')

        # self.lblTitle = Label(F1,width=40, font=('arial', 25, 'bold'), bd=1,fg='white', bg='black',
        #                       text='View Page',
        #                       padx=12)
        # self.lblTitle.pack(side=TOP, fill=X)

        #===============================Frame==========================

        F1 = Frame(self.root2, bg='light green')
        F1.place(x=0, y=0, width=900, height=500)

        self.lblTitle = Label(F1, width=40, font=('arial', 25, 'bold'), bd=1, fg='yellow',bg='black',
                              text='View Page',
                              padx=12)
        self.lblTitle.pack(side=TOP, fill=X)

        Detail_Frame = Frame(self.root2, bd=4, relief=RIDGE, bg="maroon")
        Detail_Frame.place(x=5, y=50, width=800, height=400)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson", )
        Table_Frame.place(x=10, y=70, width=760, height=300)

        Tree_Table = Frame(Table_Frame, bd=4, relief=RIDGE, bg='crimson')
        Tree_Table.place(x=10, y=70, width=760, height=350)

        #================================Tree View===================================

        self.Tree_Table = ttk.Treeview(Table_Frame, columns=('BookID', 'BookName', 'Author', 'BookEdition',
                                                                'DateBorrowed', 'DateIssued'))

        self.Tree_Table.heading('BookID', text='BookID')
        self.Tree_Table.heading('BookName', text='BookName')
        self.Tree_Table.heading('Author', text='Author')
        self.Tree_Table.heading('BookEdition', text='BookEdition')
        self.Tree_Table.heading('DateBorrowed', text='DateBorrowed')
        self.Tree_Table.heading('DateIssued', text='DateIssued')
        self.Tree_Table['show'] = 'headings'

        self.Tree_Table.column('BookID', width=100)
        self.Tree_Table.column('BookName', width=100)
        self.Tree_Table.column('Author', width=100)
        self.Tree_Table.column('BookEdition', width=100)
        self.Tree_Table.column('DateBorrowed', width=100)
        self.Tree_Table.column('DateIssued', width=100)


        self.Tree_Table.pack(fill=BOTH, expand=1)
        self.Tree_Table.bind('<ButtonRelease-1>', self.show_data)
        self.fetch_data()

        # ===============================Exit Button==================================

        self.btn_exit = Button(self.root2, text='Exit', font=('arial', 15, 'bold'),
                               fg='orange', bg='black', width=5, bd=4, command=self.root2.destroy)
        self.btn_exit.place(x=810, y=380)

        # entry for searching keyword

        self.lbl_search = Label(Detail_Frame, text="Search By:", font=("arial", 13, "bold"))
        self.lbl_search.place(x=10, y=5)

        # combobox for showing search by status
        self.combo_search = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_search['values'] = ("BookID", "Author", "BookName")
        self.combo_search.place(x=120, y=5)

        # entry for searching keyword
        self.txt_search = Entry(Detail_Frame, width=12, font=("arial", 15, "bold"), bd=3, relief=GROOVE)
        self.txt_search.place(x=270, y=4)

        # # =============search and show button shown at top=================
        searchbtn = Button(Detail_Frame, text="Search", width=8, pady=5, command=self.search_add)
        searchbtn.place(x=430, y=5)
        showbtn = Button(Detail_Frame, text="Show All", width=8, pady=5,
                         command=self.fetch_data).place(x=500, y=5)

        # lable for search by shown at the top of detail frame
        lbl_sort = Label(Detail_Frame, text="Sort By:", font=("arial", 13, "bold"), )
        lbl_sort.place(x=10, y=40)

        # combobox for showing sort by status
        self.combo_sort = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.place(x=120, y=40)

        # =============search and show button shown at top=================
        sortbtn = Button(Detail_Frame, text="Sort", width=8, pady=1,
                         command=self.sort).place(x=270, y=40)

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

    def search_add(self):
        searchbtn=self.combo_search.get()
        search_add = self.txt_search.get()
        try:
            search_add=int(search_add)

        except ValueError:
            pass

        if searchbtn == '':
            messagebox.showinfo('Error', 'Select all required item')

        elif searchbtn == 'BookID' and type(search_add) != int:
            messagebox.showerror('Error', 'Please input integer value')

        else:
            query = 'select * from detail'
            record = self.dbconnect.select(query)
            if searchbtn == 'BookID':
                rows = add_details.search(record, search_add, 0)

            elif searchbtn == 'Author':
                rows = add_details.search(record, search_add, 2)

            elif searchbtn == 'BookName':
                rows = add_details.search(record, search_add, 1)

            else:
                rows = []

            if len(rows) != 0:
                self.Tree_Table.delete(
                    *self.Tree_Table.get_children())
                for row in rows:
                    self.Tree_Table.insert('', END, values=row)



        # ===================merge sort==============================
    @classmethod
    def mergesort(self,order,ascending=True):
        list=[]
        if len(order)==1:
            return order

        mit=len(order)//2

        first_section=self.mergesort(order[:mit])
        second_section=self.mergesort(order[mit:])

        x=0
        y=0
        while x < len(first_section) and y< len(second_section):
            if first_section[x] > second_section[y]:
                list.append (second_section[y])
                y=y+1

            else:
                list.append(first_section[x])
                x=x+1

        conclusion=list+ first_section[x:]
        conclusion=conclusion+second_section[y:]

        if ascending==True:
            return conclusion

        else:
            conclusion.reverse()
            return conclusion

    def sort(self):
        sortby= self.combo_sort.get()
        query='select * from detail'
        value_fetch=self.dbconnect.select(query)
        if sortby == 'Ascending':
            row= self.mergesort(value_fetch,True)

        elif sortby == 'Descending':
            row=self.mergesort(value_fetch,False)

        else:
            row=[]

        if len(row)!= 0:
            self.Tree_Table.delete(
                *self.Tree_Table.get_children())
            for rows in row:
                 self.Tree_Table.insert('',END,values=rows)

#
# root=Tk()
# obj=add_details(root)
# root.mainloop()

