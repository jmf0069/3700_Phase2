from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def login(self):
        self.Frame2 = Frame(root, padx=5, pady=5)
        self.Frame2.grid(row=0, column=1)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#ffffff")
        self.Frame2.configure(highlightbackground="#ffffff")
        self.Frame2.configure(highlightcolor="black")
        label1 = Label(self.Frame2, text='Username:', padx=5, pady=5)
        label1.grid(row=0, column=1)
        e1 = Entry(self.Frame2)
        e1.grid(row=0, column=2)
        label2 = Label(self.Frame2, text='Password:', padx=5, pady=5)
        label2.grid(row=1, column=1)
        e2 = Entry(self.Frame2)
        e2.grid(row=1, column=2)

    def register_acc(self):
        self.Frame3 = Frame(root, padx=5, pady=5)
        self.Frame3.grid(row=0, column=1)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(background="#ffffff")
        self.Frame3.configure(highlightbackground="#ffffff")
        self.Frame3.configure(highlightcolor="black")
        label1 = Label(self.Frame3, text='Username:', padx=5, pady=5)
        label1.grid(row=0, column=1)
        user = Entry(self.Frame3)
        user.grid(row=0, column=2)
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
                    command=partial(verifyPasswordRegister, user, pass1, pass2)) #fix this ahhhhhhhhhhhhhh
        self.submitreg.grid(row=3, column=2)


    def registerAccount(self):
        username = self.register_acc.e1
        password = self.register_acc.e2
    
    def verifyPasswordRegister(user, pass1, pass2):
        if (self.pass1 != self.pass2):
            messagebox.showerror("showerror", "Passwords do not match. Try again.")
        else:
            messagebox.showinfo("showinfo", "Congratulations, " + user + "! You are registered.")
        

    def createWidgets(self):
        self.Frame1 = Frame(root, padx=5, pady=5)
        self.Frame1.grid(row=0, column=0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="black")
        # self.Frame1.configure(width=720)

        # self.Frame1.rowconfigure(0, weight=1, minsize=20)
        # self.Frame1.columnconfigure(0, weight=1, minsize=4)

        self.login = Button(self.Frame1,
                        text="Login",
                        command=self.login)
        self.login.grid(row=0, column=0)

        self.register = Button(self.Frame1,
                        text="Register",
                        command=self.register_acc)
        self.register.grid(row=1, column=0)

        self.QUIT = Button(self.Frame1,
                    text="EXIT",
                    fg="red",
                    command=self.quit)
        self.QUIT.grid(row=2, column=0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.pack()
        self.createWidgets()

root = Tk()
root.geometry("720x720")
app = Application(master=root)
app.mainloop()
root.destroy()