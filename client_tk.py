from tkinter import *
from tkinter import messagebox
# TEAM 5 
# JOSHUA WYATT, BENJAMIN RHEE, NATHAN BIAGIONI, ALLEN CARTER, AND JAKE FARLEY
#
# Application Class: The client for the user.
class Application(Frame):

    # login(self) Method: Takes two entries from user (username and password),
    # and upon submission the credentials are checked with the backend to
    # see if login is valid.
    def login(self):
        self.LoginFrame = Frame(root, padx=5, pady=5)
        self.LoginFrame.place(relx=0.435, rely=0.255, relwidth=0.36, relheight=0.18)
        self.LoginFrame.configure(relief=GROOVE)
        self.LoginFrame.configure(borderwidth="2")
        self.LoginFrame.configure(relief=GROOVE)
        self.LoginFrame.configure(background="#ffffff")
        self.LoginFrame.configure(highlightbackground="#ffffff")
        self.LoginFrame.configure(highlightcolor="white")
        label1 = Label(self.LoginFrame, text='Username:', padx=5, pady=5)
        label1.grid(row=0, column=2)
        e1 = Entry(self.LoginFrame)
        e1.grid(row=0, column=3)
        label2 = Label(self.LoginFrame, text='Password:', padx=5, pady=5)
        label2.grid(row=1, column=2)
        e2 = Entry(self.LoginFrame)
        e2.grid(row=1, column=3)
        self.submitlogin = Button(self.LoginFrame,
                                  text="Submit",
                                  command=lambda: (self.checkLoginCred(e1, e2)))
        self.submitlogin.grid(row=3, column=3)

    # add_account(user, password) method takes the username and password
    # of the user and adds the account to the USER_DATA.txt file.
    def add_account(self, user, password):
        with open(USER_DATA, "a") as data:
            data.write(user + " " + password +"\n")

    # get_existing_users() method is used for checking a new user against
    # the other existing users for duplicates etc.
    def get_existing_users(self):
        with open(USER_DATA, "r") as data:
            for line in data.readlines():
                # This expects each line of a file to be (name pass) seperated by whitespace
                username, password = line.split()
                yield username, password

    # is_registered(username, password) method takes the username and password
    # of a user to return a boolean showing if the account exists or not.
    def is_registered(self, username, password):
        with open(USER_DATA, "r") as data:
            for line in data.readlines():
                userData, passData = line.split()
                if (userData == username):
                    if (passData == password):
                        self.setUsername(username)
                        return True
            return False

    # setUsername(user) method sets the username.
    def setUsername(self, user):
        self.username = user

    # getUsername() method gets the username.
    def getUsername(self):
        return self.username

    # checkLoginCred(e1, e2) takes the username and password of user and makes sure it's credible,
    # then assigns the logged in user to a group if they're in one.
    def checkLoginCred(self, e1, e2):
        if (e1 != ""):
            if (e2 != ""):
                if (self.is_registered(e1.get(), e2.get())):
                    self.setUsername(e1.get())
                    if (self.findGroupIn(e1.get()) != None):
                        # Need to check if user is already in a group upon login, then assign them to said group upon login submission.
                        grouparr = self.findGroupIn(e1.get())
                        self.setGroupArray(grouparr[0][0], grouparr[0][1], grouparr[0][2], grouparr[0][3], grouparr[0][4], grouparr[0][5])
                        self.setGroupName(grouparr[0][0])
                        self.postLoginScreen()
                    self.postLoginScreen()
                else:
                    messagebox.showerror("showerror", "Invalid username and/or password.")
            else:
                messagebox.showerror("showerror", "Please enter a password.")
        else:
            messagebox.showerror("showerror", "Please enter a username and password.")

    # View model for the screen that is shown after a user successfully logs in.
    def postLoginScreen(self):
        try:
            self.RegisterFrame.place_forget()
        except AttributeError as e:
            self.LoginFrame.place_forget()
            self.MainMenuFrame.place_forget()
        self.LoginFrame.place_forget()
        self.MainMenuFrame.place_forget()
        self.PostLoginFrame = Frame(root, padx=5, pady=5)
        self.PostLoginFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)
        self.PostLoginFrame.configure(relief=GROOVE)
        self.PostLoginFrame.configure(borderwidth="2")
        self.PostLoginFrame.configure(relief=GROOVE)
        self.PostLoginFrame.configure(background="#ffffff")
        self.PostLoginFrame.configure(highlightbackground="#ffffff")
        self.PostLoginFrame.configure(highlightcolor="black")
        self.createGroupButton = Button(self.PostLoginFrame,
                                        text='Create Group',
                                        padx=20, pady=20,
                                        command=lambda: self.beforeCreateGroup(self.getUsername()))
        self.createGroupButton.pack(side=TOP, expand=True, fill=BOTH)
        self.manageGroupButton = Button(self.PostLoginFrame,
                                        text='Manage Group',
                                        padx=20, pady=20,
                                        command=lambda: self.manageGroup())
        self.manageGroupButton.pack(side=TOP, expand=True, fill=BOTH)
        self.logoutButton = Button(self.PostLoginFrame,
                                        text='LOGOUT',
                                        fg='red',
                                        padx=20, pady=20,
                                        command=lambda: self.logout())
        self.logoutButton.pack(side=TOP, expand=True, fill=BOTH)

    # Event handler for the LOGOUT button. Logs the user out.
    def logout(self):
        self.PostLoginFrame.place_forget()
        self.createWidgets()

    # Checks if user is already in a group before they create the group.
    def beforeCreateGroup(self, user):
        if self.findGroupIn(user) == None:
            self.createGroup()
        else:
            messagebox.showerror("showerror", "You are already in a group. Please leave your group to create another.")

    # Returns the groups that are in the array. Useful for checking against existing groups via for loops.
    def get_existing_groups(self):
        group_array = []
        with open(GROUP_DATA, "r") as data:
            for line in data.readlines():
                # This expects each line of a file to be (name pass) seperated by whitespace
                group_array.append(line.split())
                yield group_array

    # Finds if a user is in a group. If they are, returns that group.
    def findGroupIn(self, user):
        group_array = []
        with open(GROUP_DATA, "r") as data:
            for line in data.readlines():
                if user in line:
                    group_array.append(line.split())
                    return group_array
            return None

    # Checks if a group exists with the given groupname. Called upon new group creation.
    def groupExists(self, groupname):
        groups = []
        with open(GROUP_DATA, "r") as data:
            for line in data.readlines():
                groups.append(line.split())
                if (groups[0] == groupname):
                    return True
            return False

    # Has the user leave the group via deleteGroup(...), throws an error if they are not in a group.
    def leaveGroup(self):
        try:
            self.deleteGroup(self.getGroupName(), self.getUsername())
        except AttributeError as e:
            messagebox.showerror("showerror", "You are not currently in a group.")

    # Adds group to the group database. Also checks if the user is already in a group.
    def addGroup(self, group):
        groupCheck = []
        with open(GROUP_DATA, "r") as gdata2:
            for line in gdata2.readlines():
                groupCheck = line.split()
                if (self.getUsername() in groupCheck):
                    messagebox.showerror("showerror", "You are already in a group.\nTo make another one, you must leave your current one.")
                    return
        with open(GROUP_DATA, "a") as gdata:
            gdata.write(group[0] + " " + group[1] + " " + group[2] + " " + group[3] + " " + group[4] + " " + group[5] +"\n")
            messagebox.showinfo("showinfo", "Your group, " + group[0] + ", has been created!")

    # Removes the specified group from the group database.
    def deleteGroup(self, groupname, user):
        with open("GROUP_DATA.txt", "r") as gdata:
            lines = gdata.readlines()

        with open("GROUP_DATA.txt", "w") as gdata:
            for line in lines:
                if str(user) not in line:
                    gdata.write(line)
        messagebox.showinfo("showinfo", "You have successfully left the group.")

    # Checks if the given group is currently registered in the database.
    def checkGroupExists(self, groupname, group):
        if (self.groupExists(groupname)):
            messagebox.showerror("showerror", "Group name is taken. Please try another.")
        else:
            self.addGroup(self.getGroupArray())
            self.returnFromNewGroup()

    # Setter method for the groupname of logged in user.
    def setGroupName(self, groupname):
        self.groupNameOvr = groupname

    # Getter method for the group name of the logged in user.
    def getGroupName(self):
        return self.groupNameOvr

    # Setter method for the group array of the logged in user.
    def setGroupArray(self, groupname, m1, m2, m3, m4, m5):
        self.groupArray = [groupname, m1, m2, m3, m4, m5]

    # Setter method for the group array and group name of newly created group.
    def createGroupArraySet(self, groupname, m1, m2, m3, m4, m5):
        group = [groupname.get(), m1.get(), m2.get(),
                 m3.get(), m4.get(), m5.get()]
        self.groupArray = group
        self.setGroupName(groupname)
    
    # Getter method for the group array, plays into other methods.
    def getGroupArray(self):
        return self.groupArray

    # View model for creating a new group.
    def createGroup(self):
        self.PostLoginFrame.place_forget()
        self.CreateGroupFrame = Frame(root, padx=5, pady=5)
        self.CreateGroupFrame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.5)
        self.CreateGroupFrame.configure(relief=GROOVE)
        self.CreateGroupFrame.configure(borderwidth="2")
        self.CreateGroupFrame.configure(relief=GROOVE)
        self.CreateGroupFrame.configure(background="#ffffff")
        self.CreateGroupFrame.configure(highlightbackground="#ffffff")
        self.CreateGroupFrame.configure(highlightcolor="black")

        member1Label = Label(self.CreateGroupFrame, text='Group Owner:', padx=5, pady=2)
        member1Label.grid(row=0, column=0)
        member1Entry = Entry(self.CreateGroupFrame)
        member1Entry.grid(row=0, column=1)
        member1Entry.insert(0, self.getUsername())
        member2Label = Label(self.CreateGroupFrame, text='Member 2:', padx=5, pady=2)
        member2Label.grid(row=1, column=0)
        member2Entry = Entry(self.CreateGroupFrame)
        member2Entry.grid(row=1, column=1)
        member3Label = Label(self.CreateGroupFrame, text='Member 3:', padx=5, pady=2)
        member3Label.grid(row=2, column=0)
        member3Entry = Entry(self.CreateGroupFrame)
        member3Entry.grid(row=2, column=1)
        member4Label = Label(self.CreateGroupFrame, text='Member 4:', padx=5, pady=2)
        member4Label.grid(row=3, column=0)
        member4Entry = Entry(self.CreateGroupFrame)
        member4Entry.grid(row=3, column=1)
        member5Label = Label(self.CreateGroupFrame, text='Member 5:', padx=5, pady=2)
        member5Label.grid(row=4, column=0)
        member5Entry = Entry(self.CreateGroupFrame)
        member5Entry.grid(row=4, column=1)

        groupNameLabel = Label(self.CreateGroupFrame, text='Group Name:', padx=5, pady=10)
        groupNameLabel.grid(row=5, column=0)
        groupNameEntry = Entry(self.CreateGroupFrame)
        groupNameEntry.grid(row=5, column=1)
        self.submitNewGroupButton = Button(self.CreateGroupFrame,
                                           text="Submit",
                                           command=lambda: (self.createGroupArraySet(groupNameEntry, member1Entry, 
                                                            member2Entry, member3Entry, member4Entry, member5Entry), 
                                                            self.checkGroupExists(groupNameEntry.get(), self.getGroupArray())))
        self.submitNewGroupButton.place(relx=0.27, rely=0.7, relwidth=0.2, relheight=0.1)
        self.clearGroupEntriesButton = Button(self.CreateGroupFrame,
                                              text="Clear",
                                              command=lambda: self.clearNewGroupEntries(member2Entry,
                                              member3Entry, member4Entry, member5Entry, groupNameEntry))
        self.clearGroupEntriesButton.place(relx=0.52, rely=0.7, relwidth=0.2, relheight=0.1)
        self.returnFromNewGroupButton = Button(self.CreateGroupFrame,
                                               text="GO BACK",
                                               fg='red',
                                               command=lambda: self.returnFromNewGroup())
        self.returnFromNewGroupButton.place(relx=0.4, rely=0.83, relwidth=0.2, relheight=0.1)

    # Event handler for the "clear" button when creating a new group. Clears all entries besides owner.
    def clearNewGroupEntries(self, member2, member3, member4, member5, groupName):
        member2.delete(0, 'end')
        member3.delete(0, 'end')
        member4.delete(0, 'end')
        member5.delete(0, 'end')
        groupName.delete(0, 'end')

    # View model for the manage group screen.
    def manageGroup(self):
        self.PostLoginFrame.place_forget()
        self.ManageGroupFrame = Frame(root, padx=5, pady=5)
        self.ManageGroupFrame.place(relx=0.12, rely=0.1, relwidth=0.75, relheight=0.5)
        self.ManageGroupFrame.configure(relief=GROOVE)
        self.ManageGroupFrame.configure(borderwidth="2")
        self.ManageGroupFrame.configure(relief=GROOVE)
        self.ManageGroupFrame.configure(background="#ffffff")
        self.ManageGroupFrame.configure(highlightbackground="#ffffff")
        self.ManageGroupFrame.configure(highlightcolor="black")
        self.leaveGroupButton = Button(self.ManageGroupFrame,
                                  text="Leave Group",
                                  command=lambda: self.leaveGroup())
        self.leaveGroupButton.place(relx=0.12, rely=0.41, relwidth=0.2, relheight=0.1)
        self.returnFromGroupButton = Button(self.ManageGroupFrame,
                                            text="GO BACK",
                                            fg='red',
                                            command=lambda: self.returnFromGroup())
        self.returnFromGroupButton.place(relx=0.12, rely=0.52, relwidth=0.2, relheight=0.1)

    # View modifier for returning from the group creation screen.
    def returnFromNewGroup(self):
        self.CreateGroupFrame.place_forget()
        self.postLoginScreen()

    # View modifier for returning from the manage group screen.
    def returnFromGroup(self):
        try:
            self.viewGroupFrame.place_forget()
        except AttributeError as e:
            self.ManageGroupFrame.place_forget()
            self.postLoginScreen()
        self.ManageGroupFrame.place_forget()
        self.postLoginScreen()

    # register_acc(self) Method: Takes (3) entries from user (username,
    # password, and password confirmation), ensures that the passwords
    # match, and submits the info to the backend so user can login.
    def register_acc(self):
        self.RegisterFrame = Frame(root, padx=5, pady=5)
        self.RegisterFrame.place(relx=0.435, rely=0.255, relwidth=0.36, relheight=0.18)
        self.RegisterFrame.configure(relief=GROOVE)
        self.RegisterFrame.configure(borderwidth="2")
        self.RegisterFrame.configure(relief=GROOVE)
        self.RegisterFrame.configure(background="#ffffff")
        self.RegisterFrame.configure(highlightbackground="#ffffff")
        self.RegisterFrame.configure(highlightcolor="black")
        label1 = Label(self.RegisterFrame, text='Username:', padx=5, pady=5)
        label1.grid(row=0, column=1)
        user1 = Entry(self.RegisterFrame)
        user1.grid(row=0, column=2)
        label2 = Label(self.RegisterFrame, text='Password:', padx=5, pady=5)
        label2.grid(row=1, column=1)
        pass1 = Entry(self.RegisterFrame)
        pass1.grid(row=1, column=2)
        label3 = Label(self.RegisterFrame, text='Confirm Password:', padx=5, pady=5)
        label3.grid(row=2, column=1)
        pass2 = Entry(self.RegisterFrame)
        pass2.grid(row=2, column=2)
        self.submitreg = Button(self.RegisterFrame,
                                text="Submit",
                                command=lambda: (self.verifyPasswordRegister(user1, pass1, pass2)))
        self.submitreg.grid(row=3, column=2)

    # verifyPasswordRegister(...) Method: Checks if passwords match.
    def verifyPasswordRegister(self, user1, pass1, pass2):
        if (pass1.get() == pass2.get()):
            messagebox.showinfo("showinfo", "Congratulations! You are registered.")
            self.add_account(user1.get(), pass1.get())
            user1.delete(0, 'end')
            pass1.delete(0, 'end')
            pass2.delete(0, 'end')
            self.RegisterFrame.place_forget()
            self.login()
        else:
            messagebox.showerror("showerror", "Passwords do not match. Try again.")
            pass1.delete(0, 'end')
            pass2.delete(0, 'end')

    # createWidgets(self) Method: Creates the main widgets for the client.
    def createWidgets(self):
        self.MainMenuFrame = Frame(root, padx=5, pady=5)
        self.MainMenuFrame.place(relx=0.12, rely=0.1, relwidth=0.75, relheight=0.5)
        self.MainMenuFrame.configure(relief=GROOVE)
        self.MainMenuFrame.configure(borderwidth="2")
        self.MainMenuFrame.configure(relief=GROOVE)
        self.MainMenuFrame.configure(background="#ffffff")
        self.MainMenuFrame.configure(highlightbackground="#ffffff")
        self.MainMenuFrame.configure(highlightcolor="black")
        self.loginButton = Button(self.MainMenuFrame,
                                  text="Login",
                                  command=self.login)
        self.loginButton.place(relx=0.12, rely=0.3, relwidth=0.2, relheight=0.1)

        self.register = Button(self.MainMenuFrame,
                               text="Register",
                               command=self.register_acc)
        self.register.place(relx=0.12, rely=0.41, relwidth=0.2, relheight=0.1)

        self.QUIT = Button(self.MainMenuFrame,
                           text="EXIT",
                           fg="red",
                           command=self.quit)
        self.QUIT.place(relx=0.12, rely=0.52, relwidth=0.2, relheight=0.1)

    # Initializer for the client.
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

GROUP_DATA = "Group_Data.txt"
USER_DATA = "User_Data.txt"
root = Tk()
root.geometry("720x720")
app = Application(master=root)
app.mainloop()
root.destroy()