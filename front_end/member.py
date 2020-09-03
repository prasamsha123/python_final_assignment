from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from model.Library import *
from back_end.Connection import *


class Main_Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1280x530')

        # =========================Connection Object====================
        self.dbconnect = DbConnection()

        # ===============Frame in Window==================
        main_frame = Frame(self.root)
        main_frame.pack()

        # =========================manage frame=================================
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="orange")
        Manage_Frame.place(x=10, y=50, width=550, height=460)

        # title for manage student frame
        m_title = Label(Manage_Frame, text="Library Membership Info:", bg="black", fg="white",
                        font=("arial", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=10)

        self.lblTitle = Label(width=40, font=('arial', 25, 'bold'), bd=1, bg='yellow',
                              text='Library Management System',
                              padx=12)
        self.lblTitle.pack(side=TOP, fill=X)

        # ============Button Frame===============================================================================
        btn_frame = Button(Manage_Frame, bd=4, relief=RIDGE, bg="orange", )
        btn_frame.place(x=10, y=400, width=480)

        # =========================Detail frame===================================================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=570, y=50, width=695, height=460)

        # lable for search by shown at the top of detail frame
        lbl_search = Label(Detail_Frame, text="Search By", font=("arial", 13, "bold"))
        lbl_search.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # combobox for showing search by status
        self.combo_search = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_search['values'] = ("BookID", "Author", "FirstName")
        self.combo_search.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        # entry for searching keyword
        self.txt_search = Entry(Detail_Frame, width=12, font=("arial", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=2, padx=20, pady=10, sticky="w")

        #=============search and show button shown at top=================
        searchbtn = Button(Detail_Frame, text="Search", width=8, pady=5,
                           command=self.search_item).grid(row=0, column=3, padx=10, pady=10)
        showbtn = Button(Detail_Frame, text="Show All", width=8, pady=5,
                         command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # lable for search by shown at the top of detail frame
        lbl_sort = Label(Detail_Frame, text="Sort By:", font=("arial", 13, "bold"))
        lbl_sort.grid(row=1, column=0, padx=20, pady=5, sticky="w")

        # combobox for showing sort by status
        self.combo_sort = ttk.Combobox(Detail_Frame, width=12, font=("arial", 12, "bold"), state="readonly")
        self.combo_sort['values'] = ("Ascending", "Descending")
        self.combo_sort.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # =============search and show button shown at top=================
        sortbtn = Button(Detail_Frame, text="Sort", width=8, pady=1,
                           command=self.sorting).grid(row=1, column=2, padx=1, pady=10)

        # ==========================Table Frame=========================================
        Table_Frame = Button(Detail_Frame, bd=4, relief=RIDGE, bg="crimson", )
        Table_Frame.place(x=10, y=100, width=760, height=100)

        # for scroll bar horizontal and vertical
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

       # ===================Manage Frame===========

        self.lblBookID = Label(Manage_Frame, font=('arial', 18, 'bold'),
                               text='Book ID:',bd=4,bg='orange', padx=2, pady=2)
        self.lblBookID.grid(row=1, column=0, sticky=W)
        self.txtBookID = Entry(Manage_Frame, font=('arial', 14, 'bold'), width=20)
        self.txtBookID.grid(row=1, column=1)

        self.lblBookTitle = Label(Manage_Frame, font=('arial', 18, 'bold'),
                                  text='Book Title:',bg='orange',bd=4, padx=2, pady=2)
        self.lblBookTitle.grid(row=2, column=0, sticky=W)

        self.cboBookTitle = ttk.Combobox(Manage_Frame, font=('arial', 14, 'bold'),
                                         state='readonly', width=20)
        self.cboBookTitle['value'] = ('','2012', 'CRUX', 'Fantasy', 'Horrible')
        self.cboBookTitle.grid(row=2, column=1)

        self.lblAuthor = Label(Manage_Frame, font=('arial', 18, 'bold'),
                               text='Author:',bg='orange',bd=4, padx=2, pady=2)
        self.lblAuthor.grid(row=3, column=0, sticky=W)
        self.txtAuthor = Entry(Manage_Frame, font=('arial', 14, 'bold'), width=20)
        self.txtAuthor.grid(row=3, column=1)

        self.lblMemberType = Label(Manage_Frame, font=('arial', 18, 'bold'),
                                   text='Member Type:',bg='orange',bd=4, padx=2, pady=2)
        self.lblMemberType.grid(row=4, column=0, sticky=W)


        self.cboMemberType = ttk.Combobox(Manage_Frame,  font=('arial', 14, 'bold'),
                                          state='readonly', width=20)
        self.cboMemberType['value'] = ('','Student', 'Lecturer', 'Admin Staff')
        self.cboMemberType.grid(row=4, column=1)

        self.lblFirstName = Label(Manage_Frame, font=('arial', 18, 'bold'),
                                  text='First Name:',bg='orange',bd=4, padx=2, pady=2)
        self.lblFirstName.grid(row=5, column=0, sticky=W)
        self.txtFirstName = Entry(Manage_Frame, font=('arial', 14, 'bold'), width=20)
        self.txtFirstName.grid(row=5, column=1)

        self.lblSurname = Label(Manage_Frame, font=('arial', 18, 'bold'),
                                text='Surname:',bg='orange',bd=4, padx=2, pady=2)
        self.lblSurname.grid(row=6, column=0, sticky=W)
        self.txtSurname = Entry(Manage_Frame, font=('arial', 14, 'bold'), width=20)
        self.txtSurname.grid(row=6, column=1)

        self.lblDateBorrowed = Label(Manage_Frame, font=('arial', 18, 'bold'),
                                     text='Date Borrowed:',bg='orange',bd=4, padx=2, pady=2)
        self.lblDateBorrowed.grid(row=7, column=0, sticky=W)
        self.txtDateBorrowed = Entry(Manage_Frame, font=('arial', 14, 'bold'),
                                     width=20)
        self.txtDateBorrowed.grid(row=7, column=1)

        self.lblAddress = Label(Manage_Frame, font=('arial', 18, 'bold'),
                                text='Address:',bd=4,bg='orange', padx=2, pady=2)
        self.lblAddress.grid(row=8, column=0, sticky=W)
        self.txtAddress = Entry(Manage_Frame, font=('arial', 14, 'bold'), width=20)
        self.txtAddress.grid(row=8, column=1)


        # ========================Table Frame========================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='green')
        Table_Frame.place(x=10, y=100, width=675, height=345)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.Library_table = ttk.Treeview(Table_Frame, columns=('BookID', 'BookTitle', 'Author', 'MemberType',
                                                                'FirstName', 'Surname', 'DateBorrowed', 'Address'))


        self.Library_table.heading('BookID', text='BookID')
        self.Library_table.heading('BookTitle', text='BookTitle')
        self.Library_table.heading('Author', text='Author')
        self.Library_table.heading('MemberType', text='MemberType')
        self.Library_table.heading('FirstName', text='FirstName')
        self.Library_table.heading('Surname', text='Surname')
        self.Library_table.heading('DateBorrowed', text='DateBorrowed')
        self.Library_table.heading('Address', text='Address')
        self.Library_table['show'] = 'headings'

        self.Library_table.column('BookID', width=50)
        self.Library_table.column('BookTitle', width=70)
        self.Library_table.column('Author', width=70)
        self.Library_table.column('MemberType', width=80)
        self.Library_table.column('FirstName', width=70)
        self.Library_table.column('Surname', width=70)
        self.Library_table.column('DateBorrowed', width=80)
        self.Library_table.column('Address', width=120)

        self.Library_table.pack(fill=BOTH, expand=1)
        self.Library_table.bind('<ButtonRelease-1>', self.show_data)
        self.fetch_data()

       # =============================Buttons=================================

        self.btn_add = Button(btn_frame, text='Add', font=('arial', 10, 'bold'), width=10, bd=4, command=self.add)
        self.btn_add.grid(row=0, column=0)

        self.btn_update = Button(btn_frame, text='Update', font=('arial', 10, 'bold'), width=10, bd=4,
                                 command=self.update)
        self.btn_update.grid(row=0, column=1)

        self.btn_clear = Button(btn_frame, text='Clear', font=('arial', 10, 'bold'), width=10, bd=4, command=self.clear)
        self.btn_clear.grid(row=0, column=2)

        self.btn_del = Button(btn_frame, text='Delete', font=('arial', 10, 'bold'), width=10, bd=4, command=self.delete)
        self.btn_del.grid(row=0, column=3)

        self.btn_exit = Button(btn_frame, text='Exit', font=('arial', 10, 'bold'), width=10, bd=4, command=root.destroy)
        self.btn_exit.grid(row=0, column=4)

    def add(self):
        lbr_obj = Library(self.txtBookID.get(), self.cboBookTitle.get(), self.txtAuthor.get(),
                          self.cboMemberType.get(), self.txtFirstName.get(), self.txtSurname.get(),
                          self.txtDateBorrowed.get(), self.txtAddress.get())

        query = 'insert into management values(%s,%s,%s,%s,%s,%s,%s,%s);'
        values = (lbr_obj.get_BookID(), lbr_obj.get_BookTitle(), lbr_obj.get_Author(),
                  lbr_obj.get_MemberType(), lbr_obj.get_FirstName(), lbr_obj.get_Surname(),
                  lbr_obj.get_DateBorrowed(), lbr_obj.get_Address())

        self.dbconnect.insert(query, values)
        messagebox.showinfo('Success', 'Data inserted successfully')

        self.fetch_data()
        self.clear()

    def update(self):
        lbr_obj= Library(self.txtBookID.get(),self.cboBookTitle.get(),self.txtAuthor.get(),
                         self.cboMemberType.get(),self.txtFirstName.get(),self.txtSurname.get(),
                         self.txtDateBorrowed.get(),self.txtAddress.get())
        query='update management set BookTitle=%s,Author=%s,MemberType=%s,' \
              'FirstName=%s, Surname=%s, DateBorrowed=%s, Address=%s where BookID=%s;'

        values=(lbr_obj.get_BookTitle(), lbr_obj.get_Author(), lbr_obj.get_MemberType(),
                lbr_obj.get_FirstName(), lbr_obj.get_Surname(),lbr_obj.get_DateBorrowed(),
                lbr_obj.get_Address(),lbr_obj.get_BookID())

        self.dbconnect.update(query, values)
        messagebox.showinfo('Success','Data updated successfully')

        self.fetch_data()
        self.clear()


    def clear(self):
        self.txtBookID.delete('0',END)
        self.cboBookTitle.set('')
        self.txtAuthor.delete('0',END)
        self.cboMemberType.set('')
        self.txtFirstName.delete('0',END)
        self.txtSurname.delete('0',END)
        self.txtDateBorrowed.delete('0',END)
        self.txtAddress.delete('0',END)

        self.fetch_data()
        self.clear()

    def delete(self):
        lbr_obj = Library(self.txtBookID.get(), self.cboBookTitle.get(), self.txtAuthor.get(),
                          self.cboMemberType.get(), self.txtFirstName.get(), self.txtSurname.get(),
                          self.txtDateBorrowed.get(), self.txtAddress.get())
        query = ('delete from management where BookID=%s')
        values = (lbr_obj.get_BookID(),)
        self.dbconnect.delete(query, values)
        messagebox.showinfo('Success', 'Data deleted successfully')
        self.fetch_data()
        self.clear()

    def fetch_data(self):
        lbr_obj = Library(self.txtBookID.get(), self.cboBookTitle.get(), self.txtAuthor.get(),
                          self.cboMemberType.get(), self.txtFirstName.get(), self.txtSurname.get(),
                          self.txtDateBorrowed.get(), self.txtAddress.get())
        query = 'select * from management'
        rows=self.dbconnect.select(query)

        if len(rows) != 0:
            self.Library_table.delete(
                *self.Library_table.get_children())
            for row in rows:
                self.Library_table.insert('', END, values=row)

    def show_data(self, ev):
        data_row = self.Library_table.focus()
        content = self.Library_table.item(data_row)
        row = content['values']

        lbr_obj = Library(self.txtBookID.delete('0',END), self.cboBookTitle.get(), self.txtAuthor.delete('0',END),
                self.cboMemberType.get(), self.txtFirstName.delete('0',END), self.txtSurname.delete('0',END),
                self.txtDateBorrowed.delete('0',END), self.txtAddress.delete('0',END))
        self.txtBookID.insert(END, row[0])
        self.cboBookTitle.set(row[1])
        self.txtAuthor.insert(END, row[2])
        self.cboMemberType.set(row[3])
        self.txtFirstName.insert(END, row[4])
        self.txtSurname.insert(END, row[5])
        self.txtDateBorrowed.insert(END, row[6])
        self.txtAddress.insert(END, row[7])


#===================Linear Search===============================
    @classmethod
    def search(cls,record, values,index):
        rows=[]
        for item in record:
            if type(item[index])!=str:
                if item[index]==values:
                    rows.append(item)
            else:
                if item[index].upper()==values.upper():
                    rows.append(item)
        return rows


    def search_item(self):
        searchbtn=self.combo_search.get()
        search_item=self.txt_search.get()
        try:
            search_item=int(search_item)

        except ValueError:
            pass

        if searchbtn=='' or search_item =='':
            messagebox.showinfo('Error','Select all required item')

        elif searchbtn == 'BookID' and type(search_item) !=int:
            messagebox.showerror('Error','Please input integer value')

        else:
            query= 'select * from management'
            record=self.dbconnect.select(query)
            if searchbtn == 'BookID':
                rows= Main_Interface.search(record,search_item,0)

            elif searchbtn == 'Author':
                rows= Main_Interface.search(record,search_item,2)

            elif searchbtn == 'FirstName':
                rows= Main_Interface.search(record,search_item,4)

            else:
                rows= []

            if len(rows) !=0:
                self.Library_table.delete(
                    *self.Library_table.get_children())
                for row in rows:
                    self.Library_table.insert('',END,values=row)


    #===================merge sort==============================

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

    def sorting(self):
        sortby= self.combo_sort.get()
        query='select * from management'
        value_fetch=self.dbconnect.select(query)
        if sortby == 'Ascending':
            row= self.mergesort(value_fetch,True)

        elif sortby == 'Descending':
            row=self.mergesort(value_fetch,False)

        else:
            row=[]

        if len(row)!= 0:
            self.Library_table.delete(
                *self.Library_table.get_children())
            for rows in row:
                 self.Library_table.insert('',END,values=rows)



# root = Tk()
# Main_Interface(root)
# root.mainloop()
