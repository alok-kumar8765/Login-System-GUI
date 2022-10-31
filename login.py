from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class Login_system():
    def __init__(self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
    
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon = ImageTk.PhotoImage(file="images/user2.jpg")
        self.pass_icon = ImageTk.PhotoImage(file="images/pass.jpg")
        self.logo_icon = ImageTk.PhotoImage(file="images/user.jpg")
        
        self.uname = StringVar()
        self.passw = StringVar()
        bg_lb1 = Label(self.root,image=self.bg_icon).pack()
        title = Label(self.root,text='Login System',
        font=('times new roman',40,'bold'),bg='yellow',fg='red',
        relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame = Frame(self.root,bg='white')
        Login_Frame.place(x=400,y=150)
        
        logolb1 = Label(Login_Frame,image=self.logo_icon,bd=0)
        logolb1.grid(row=0,columnspan=2,pady=20)

        lbusr = Label(Login_Frame,image=self.user_icon,
        text='Username',compound=LEFT,bg='white',font=('times new roman',20,'bold'))
        lbusr.grid(row=1,column=0,padx=20,pady=10)
        txtusr = Entry(Login_Frame,bd=5,relief=GROOVE,
        font=('arial',15),textvariable=self.uname)
        txtusr.grid(row=1,column=1,padx=20)

        lbpass = Label(Login_Frame,image=self.pass_icon,
        text='Password',compound=LEFT,bg='white',font=('times new roman',20,'bold'))
        lbpass.grid(row=2,column=0,padx=20,pady=10)
        txtpass = Entry(Login_Frame,bd=5,relief=GROOVE,
        font=('arial',15),textvariable=self.passw)
        txtpass.grid(row=2,column=1,padx=20)

        btn_log = Button(Login_Frame,text='Login',width=15,
        font=('arial',14,'bold'),fg='red',bg='yellow',command=self.loginbtn)
        btn_log.grid(row=3,column=1,pady=10)

    def loginbtn(self):
        if self.uname.get() == "" or self.passw.get() == "":
            messagebox.showerror("Error","All Fields Are Required")
        elif self.uname.get()=="alok" or self.passw.get() == "1234":
            messagebox.showinfo("Successfull",f"Welcome  {self.uname.get()}")
        else:
            messagebox.showerror("Error","Invalid User")

    
root=Tk()
obj=Login_system(root)
root.mainloop()
