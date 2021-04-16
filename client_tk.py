from tkinter import *

class Application(Frame):
    def register_acc(self):
        print("getting there...")

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