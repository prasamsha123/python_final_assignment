from tkinter import *
from PIL import ImageTk
from front_end.Button import *

class Welcome:
    def __init__(self, root):
        self.root = root
        self.root.title('LIBRARY MANAGEMENT SYSTEM')
        self.root.geometry("1495x750+10+20")

        self.bg_icon = ImageTk.PhotoImage(file="Image/books.jpg")

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

       #=============================Manage Frame=======================
        self.frame1 = Frame(self.root, bg='black')
        self.frame1.place(x=570, y=250, width=378, height=240)

        self.frame2 = Frame(self.frame1, bg='light blue')
        self.frame2.place(x=15, y=10, width=348, height=220)

        self.headingFrame1 = Frame(self.root, bg="#333945", bd=5)
        self.headingFrame1.place(relx=0.40, rely=0.2, relwidth=0.4, relheight=0.16)

        self.headingFrame2 = Frame(self.headingFrame1, bg="#EAF0F1")
        self.headingFrame2.place(relx=0.01, rely=0.04, relwidth=0.98, relheight=0.9)

        self.headingLabel = Label(self.headingFrame2, text="WELCOME TO LIBRARY", font=('arial', '16', 'bold'), fg='black')
        self.headingLabel.place(relx=0.25, rely=0.15, relwidth=0.5, relheight=0.5)


        btn_log = Button(self.frame1, text="Login", command=self.Login, width=21,
                         font=("times new roman", 20, "bold"),
                         bg="grey", fg="black").place(x=16,y=40)

        btn_exit = Button(self.frame1, text="Exit", command=self.root.destroy, width=21,
                         font=("times new roman", 20, "bold"),
                         bg="grey", fg="black").place(x=16, y=120)

    def Login(self):
        self.root.title("Login")
        self.root.geometry()
        self.frame1.place_forget()
        self.headingFrame1.place_forget()


        self.bg_icon = ImageTk.PhotoImage(file="Image/background.jpg")
        self.user_icon = ImageTk.PhotoImage(file="Image/user.png")
        self.pass_icon = ImageTk.PhotoImage(file="Image/pass.png")
        self.logo_icon = ImageTk.PhotoImage(file="Image/logo.png")

        self.uname = StringVar()
        self.pass_ = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).place(x=0,y=0,width=1800,height=800)
        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="yellow", fg="black")
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="grey")
        Login_Frame.place(x=400, y=150)
        logo_lbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)
        lblusername = Label(Login_Frame, text='Username:', image=self.user_icon, compound=LEFT,
                            font=("Arial", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10),
        self.txtusername = Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE,
                                 font=("", 15)).grid(row=1, column=1, padx=20)
        lblpassword = Label(Login_Frame, text='Password:', image=self.pass_icon, compound=LEFT,
                            font=("Arial", 20, "bold"), bg="white").grid(row=2, column=0, padx=20, pady=10),
        self.txtpassword = Entry(Login_Frame, bd=5, textvariable=self.pass_, relief=GROOVE, show="*",
                                 font=("", 15)).grid(row=2, column=1, padx=20)
        self.btn_log = Button(Login_Frame, text="Login", width=15, command=self.login,
                              font=("Arial", 14, "bold"), bg="yellow", fg="red").grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.uname.get() == "a" and self.pass_.get() == "a":
            messagebox.showinfo("successful", "welcome")
            next_window = Tk()
            Button_details(next_window)
        else:
            messagebox.showerror("Error", "Invalid Username or Password")


root=Tk()
obj=Welcome(root)
root.mainloop()