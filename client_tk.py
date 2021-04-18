from tkinter import *
from tkinter import messagebox

# Application Class: The client for the user. Relies on other classes.
class Application(Frame):

    # login(self) Funtion: Takes two entries from user (username and password), 
    # and upon submission the credentials are checked with the backend to 
    # see if login is valid.
    def login(self):
        self.Frame2 = Frame(root, padx=5, pady=5)
        self.Frame2.place(relx=0.435, rely=0.255, relwidth=0.36, relheight=0.18)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        label1 = Label(self.Frame2, text='Username:', padx=5, pady=5)
        label1.grid(row=0, column=2)
        e1 = Entry(self.Frame2)
        e1.grid(row=0, column=3)
        label2 = Label(self.Frame2, text='Password:', padx=5, pady=5)
        label2.grid(row=1, column=2)
        e2 = Entry(self.Frame2)
        e2.grid(row=1, column=3)
        self.submitlogin = Button(self.Frame2,
                                  text="Submit") #fix this ahhhhhhhhhhhhhh
        self.submitlogin.grid(row=3, column=3)

    # register_acc(self) Function: Takes (3) entries from user (username, 
    # password, and password confirmation), ensures that the passwords
    # match, and submits the info to the backend so user can login.
    def register_acc(self):
        self.Frame3 = Frame(root, padx=5, pady=5)
        self.Frame3.place(relx=0.435, rely=0.255, relwidth=0.36, relheight=0.18)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#ffffff")
        self.Frame3.configure(highlightbackground="#ffffff")
        self.Frame3.configure(highlightcolor="black")
        label1 = Label(self.Frame3, text='Username:', padx=5, pady=5)
        label1.grid(row=0, column=1)
        user1 = Entry(self.Frame3)
        user1.grid(row=0, column=2)
        label2 = Label(self.Frame3, text='Password:', padx=5, pady=5)
        label2.grid(row=1, column=1)
        pass1 = Entry(self.Frame3)
        pass1.grid(row=1, column=2)
        label3 = Label(self.Frame3, text='Confirm Password:', padx=5, pady=5)
        label3.grid(row=2, column=1)
        pass2 = Entry(self.Frame3)
        pass2.grid(row=2, column=2)
        self.submitreg = Button(self.Frame3,
                                text="Submit",
                                command=lambda: (self.verifyPasswordRegister(user1, pass1, pass2)))
        self.submitreg.grid(row=3, column=2)


    # def registerAccount(self):
    #     username = self.register_acc.user1
    #     password = self.register_acc.pass1
    
    # verifyPasswordRegister(...) Function: Checks if passwords match.
    def verifyPasswordRegister(self, user1, pass1, pass2):
        if (pass1.get() == pass2.get()):
            messagebox.showinfo("showinfo", "Congratulations! You are registered.")
            user1.delete(0, 'end')
            pass1.delete(0, 'end')
            pass2.delete(0, 'end')
            self.Frame3.place_forget()
            self.Frame3.destroy()
            self.login()
        else:
            messagebox.showerror("showerror", "Passwords do not match. Try again.")
            pass1.delete(0, 'end')
            pass2.delete(0, 'end')
    
    # createWidgets(self) Function: Creates the main widgets for the client.
    def createWidgets(self):
        self.Frame1 = Frame(root, padx=5, pady=5)
        self.Frame1.place(relx=0.12, rely=0.1, relwidth=0.75, relheight=0.5)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        self.loginButton = Button(self.Frame1,
                                  text="Login",
                                  command=self.login)
        self.loginButton.place(relx=0.12, rely=0.3, relwidth=0.2, relheight=0.1)

        self.register = Button(self.Frame1,
                               text="Register",
                               command=self.register_acc)
        self.register.place(relx=0.12, rely=0.41, relwidth=0.2, relheight=0.1)

        self.QUIT = Button(self.Frame1,
                           text="EXIT",
                           fg="red",
                           command=self.quit)
        self.QUIT.place(relx=0.12, rely=0.52, relwidth=0.2, relheight=0.1)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

root = Tk()
root.geometry("720x720")
app = Application(master=root)
app.mainloop()
root.destroy()