"""
Pettrus Konnoth
CS50
Master project main
Cmdr.Schenk Raymond
Menu file
"""
# importing the necessary modules
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter
from sqlfunctions import SqlFunctions
import time

from tkcalendar import *


# creating the menu class
class Menu():
    def __init__(self):
        # creating the variables
        # creating the current record variable

        self.currentRecord = 0


        # creating the sql object
        self.sql = SqlFunctions()
        # creating the root window
        self.root = tk.Tk()
        self.root.title("Workout App")
        # setting the window size
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file='man.png'))
        self.root.config(bg="black")

        # creating the login frame function so it is showed by default
        self.createLoginFrame()

    def load(self):
        # This function loads the current record
        workout_list = self.sql.GetWorkout()
        if self.currentRecord >= len(workout_list):
            print("Index out of range")
            return

        (self.id, self.user_id, self.exercise_1, self.exercise_1_sets, self.exercise_1_reps, self.exercise_2,
         self.exercise_2_sets, self.exercise_2_reps, self.exercise_3, self.exercise_3_sets, self.exercise_3_reps,
         self.exercise_4, self.exercise_4_sets, self.exercise_4_reps, self.exercise_5, self.exercise_5_sets,
         self.exercise_5_reps) = workout_list[self.currentRecord]
        self.clear()
        self.currentid = self.id
        self.exercise1.insert(0, self.exercise_1)
        self.exercise1Sets.insert(0, self.exercise_1_sets)
        self.exercise1Reps.insert(0, self.exercise_1_reps)
        self.exercise2.insert(0, self.exercise_2)
        self.exercise2Sets.insert(0, self.exercise_2_sets)
        self.exercise2Reps.insert(0, self.exercise_2_reps)
        self.exercise3.insert(0, self.exercise_3)
        self.exercise3Sets.insert(0, self.exercise_3_sets)
        self.exercise3Reps.insert(0, self.exercise_3_reps)
        self.exercise4.insert(0, self.exercise_4)
        self.exercise4Sets.insert(0, self.exercise_4_sets)
        self.exercise4Reps.insert(0, self.exercise_4_reps)
        self.exercise5.insert(0, self.exercise_5)
        self.exercise5Sets.insert(0, self.exercise_5_sets)
        self.exercise5Reps.insert(0, self.exercise_5_reps)

        # This function displays the current record
        self.txt = "Exercise ID: " + str(self.currentid)
        self.exerciseId = Label(self.workoutFrame, text=self.txt, font=("Arial", 20, "bold"), fg="black", bg="white")
        self.exerciseId.place(relx=0.18, rely=0.05, anchor="se")

    def createLoginFrame(self):
        # creating the login frame

        self.root.geometry("800x800")
        self.loginFrame = customtkinter.CTkFrame(self.root)
        self.loginFrame.configure(fg_color="#FFFFFF")

        # packing the login frame
        self.loginFrame.pack(fill=tk.BOTH, expand=True)

        # creating the username and password entry fields
        self.username = customtkinter.CTkEntry(self.loginFrame, width=200, height=40, placeholder_text="Username",
                                               corner_radius=15, font=("Arial", 20))
        self.username.pack(pady=10, padx=10)

        self.password = customtkinter.CTkEntry(self.loginFrame, width=200, height=40, placeholder_text="Password",
                                               show="*", corner_radius=15, font=("Arial", 20))
        self.password.pack(pady=20, padx=10)

        self.loginButton = customtkinter.CTkButton(self.loginFrame, text="Login", command=self.login, width=180,
                                                   height=40, corner_radius=10, font=("Arial", 20))
        self.loginButton.pack(pady=30, padx=10)

        self.orbutton = Label(self.loginFrame, text="OR", font=("Helvetica", 30, "bold"), fg="black", bg="#FFFFFF")
        self.orbutton.pack(pady=10, padx=10)

        # creating the create account button so it will open the create account frame
        self.createAccountButton = customtkinter.CTkButton(self.loginFrame, text="Create Account",
                                                           command=self.showCreateAccountFrame)
        self.createAccountButton.pack(pady=10, padx=10)

        self.connectionBtn = customtkinter.CTkButton(self.loginFrame, text='Connect', font=('Helvetica', 24, 'bold'),
                                                     fg_color='#53D769',
                                                     hover_color='#54bf66', text_color="#FFFFFF", height=76, width=245,
                                                     corner_radius=25, command=self.connect)
        self.connectionBtn.pack(pady=50, padx=10)

        self.msg = Label(self.loginFrame, text="", font=("Arial", 20))
        self.msg.pack(pady=10, padx=10)

        self.btn_state()

        self.root.mainloop()

    def connect(self):
        if not self.sql.connection_status:
            self.sql.connect()
            self.btn_state()
            self.currentRecord = 0
        else:
            self.sql.disconnect()
            self.btn_state()

    def btn_state(self):
        if self.sql.connection_status:

            self.connectionBtn.configure(text="Disconnect", fg_color="#E94D3D", hover_color="#db584b")
            self.msg.configure(text="Connected to database", font=("Arial", 40, "bold"), fg="green", bg="#FFFFFF")
            self.loginButton.configure(state="normal")
            self.createAccountButton.configure(state="normal")
            self.username.configure(state="normal")
            self.password.configure(state="normal")


        else:
            self.connectionBtn.configure(text="Connect", fg_color="#53D769", hover_color="#54BF66")
            self.msg.configure(text="No connection to database", font=("Arial", 40, "bold"), fg="red", bg="#FFFFFF")
            self.loginButton.configure(state="disabled")
            self.createAccountButton.configure(state="disabled")
            self.username.configure(state="disabled")
            self.password.configure(state="disabled")


    def showCreateAccountFrame(self):
        if self.sql.connection_status:
            # destroying the login frame
            self.loginFrame.destroy()
            # changing the window size
            self.root.geometry("900x800")
            # creating the create account frame
            self.createAccountFrame = customtkinter.CTkFrame(self.root)
            self.createAccountFrame.pack(fill=tk.BOTH, expand=True)
            self.createAccountFrame.configure(fg_color="#FFFFFF")
            # creatin the user sign up form
            self.username2 = customtkinter.CTkEntry(self.createAccountFrame, width=200, height=40,placeholder_text="enter username", corner_radius=15,font=("Arial", 20))
            self.username2.grid(row=0, column=5, pady=10, padx=10)
            self.password2 = customtkinter.CTkEntry(self.createAccountFrame, width=200, height=40,placeholder_text="create password", show="·", corner_radius=15,font=("Arial", 20))
            self.password2.grid(row=1, column=5, pady=10, padx=10)
            self.email = customtkinter.CTkEntry(self.createAccountFrame, width=200, height=40,placeholder_text="Enter email", corner_radius=15, font=("Arial", 20))
            self.email.grid(row=2, column=5, pady=10, padx=10)
            self.age = customtkinter.CTkEntry(self.createAccountFrame, width=200, height=40, placeholder_text="age",corner_radius=15, font=("Arial", 20))
            self.age.grid(row=3, column=5, pady=10, padx=10)
            self.genderlabel = Label(self.createAccountFrame, text="Gender:", font=("Arial", 20, "bold"), fg="black",bg="#FFFFFF", width=10, height=2)
            self.genderlabel.grid(row=4, column=4, pady=10, padx=10)
            self.gender = customtkinter.CTkComboBox(self.createAccountFrame, values=["", "M", "F"], state="readonly")
            self.gender.grid(row=4, column=5, pady=10, padx=10)
            self.createAccountButton2 = customtkinter.CTkButton(self.createAccountFrame, text="Create Account",command=self.create_account)
            self.createAccountButton2.grid(row=5, column=5, pady=10, padx=10)
            self.backButton = customtkinter.CTkButton(self.createAccountFrame, text="Back", command=self.back)
            self.backButton.grid(row=6, column=5, pady=10, padx=10)
            self.msg = customtkinter.CTkLabel(self.createAccountFrame, text="")
            self.msg.grid(row=7, column=0, pady=10, padx=10)
            self.root.mainloop()
        else:
            self.msg.configure(text="No connection to database", font=("Arial", 40, "bold"), fg_color="red")

    def ShowWorkoutFrame(self):
        # Destroy the login frame and create a new workout frame
        self.loginFrame.destroy()
        self.workoutFrame = customtkinter.CTkFrame(self.root)

        self.root.geometry("900x800")
        # Display the welcome label with the user ID
        welcome_text = "Welcome " + str(self.sql.name)
        self.welcome_label = Label(self.workoutFrame, text=welcome_text, font=("Arial", 40, "bold"),fg="black", bg="white")
        self.exerciseHeading = Label(self.workoutFrame, text="Exercise", font=("Arial", 20, "bold"), fg="black",bg="white")
        self.setsHeading = Label(self.workoutFrame, text="Sets", font=("Arial", 20, "bold"), fg="black", bg="white")
        self.repsHeading = Label(self.workoutFrame, text="Reps", font=("Arial", 20, "bold"), fg="black", bg="white")
        self.exercise1 = customtkinter.CTkEntry(self.workoutFrame, width=200, corner_radius=15, height=40,font=("Arial", 20))
        self.exercise1Sets = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise1Reps = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise2 = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise2Sets = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise2Reps = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise3 = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise3Sets = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise3Reps = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise4 = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise4Sets = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise4Reps = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise5 = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise5Sets = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.exercise5Reps = customtkinter.CTkEntry(self.workoutFrame, width=200, height=40, corner_radius=15,font=("Arial", 20))
        self.right = customtkinter.CTkButton(self.workoutFrame, text=">", command=lambda: self.jump(1),fg_color="#13d682",corner_radius=15,font=("helvetica", 42,"bold"),width=150,height=48, text_color="black",hover_color="#11995e")
        self.left = customtkinter.CTkButton(self.workoutFrame, text="<", command=lambda: self.jump(-1),fg_color="#13d682",corner_radius=15,font=("helvetica", 42,"bold"),width=150,height=48, text_color="black",hover_color="#11995e")
        # Add buttons to add, delete, and save workouts, and to log out
        self.addBtn = customtkinter.CTkButton(self.workoutFrame, text="Add Workout", command=self.addWorkout,fg_color="#13d682",corner_radius=15,font=("helvetica", 20,"bold"),width=180,height=50,text_color="black",hover_color="#11995e")
        self.deleteWorkout = customtkinter.CTkButton(self.workoutFrame, text="Delete Workout",command=self.deleteWorkout,fg_color="#bf572a",corner_radius=15,font=("helvetica", 20,"bold"),width=180,height=50,text_color="black",hover_color="#a44e27")
        self.updateWorkout = customtkinter.CTkButton(self.workoutFrame, text="Update Workout",command=self.updateWorkout,fg_color="#13d682",corner_radius=15,font=("helvetica", 20,"bold"),width=180,height=50,text_color="black",hover_color="#11995e")
        self.logoutbtn = customtkinter.CTkButton(self.workoutFrame, text="Logout", command=self.logout,fg_color="#ff0000",corner_radius=15,font=("helvetica", 22,"bold"),width=180,height=50,text_color="black",hover_color="#cc0000")
        self.msg2 = Label(self.workoutFrame, text="",font=("Arial", 40, "bold"), fg="white", bg="white")


        # Pack the widgets
        self.packFunction()
        self.load()
        # Start the main loop of the application
        self.root.mainloop()

    def packFunction(self):
        self.workoutFrame.pack(fill=tk.BOTH, expand=True)
        self.workoutFrame.configure(fg_color="#FFFFFF")

        # Set the position and dimensions of each widget using place
        self.welcome_label.place(relx=0.5, rely=0.05, anchor="center")
        self.exerciseHeading.place(relx=0.15, rely=0.15, anchor="center")
        self.setsHeading.place(relx=0.4, rely=0.15, anchor="center")
        self.repsHeading.place(relx=0.65, rely=0.15, anchor="center")

        self.exercise1.place(relx=0.15, rely=0.20, anchor="center")
        self.exercise1Sets.place(relx=0.40, rely=0.20, anchor="center")
        self.exercise1Reps.place(relx=0.65, rely=0.20, anchor="center")

        self.exercise2.place(relx=0.15, rely=0.30, anchor="center")
        self.exercise2Sets.place(relx=0.4, rely=0.30, anchor="center")
        self.exercise2Reps.place(relx=0.65, rely=0.30, anchor="center")

        self.exercise3.place(relx=0.15, rely=0.40, anchor="center")
        self.exercise3Sets.place(relx=0.4, rely=0.40, anchor="center")
        self.exercise3Reps.place(relx=0.65, rely=0.40, anchor="center")

        self.exercise4.place(relx=0.15, rely=0.50, anchor="center")
        self.exercise4Sets.place(relx=0.4, rely=0.50, anchor="center")
        self.exercise4Reps.place(relx=0.65, rely=0.50, anchor="center")

        self.exercise5.place(relx=0.15, rely=0.60, anchor="center")
        self.exercise5Sets.place(relx=0.4, rely=0.60, anchor="center")
        self.exercise5Reps.place(relx=0.65, rely=0.60, anchor="center")

        self.right.place(relx=0.65, rely=0.7, anchor="center")
        self.left.place(relx=0.15, rely=0.7, anchor="center")

        self.addBtn.place(relx=0.88, rely=0.20, anchor="center")
        self.deleteWorkout.place(relx=0.88, rely=0.4, anchor="center")
        self.updateWorkout.place(relx=0.88, rely=0.60, anchor="center")

        self.logoutbtn.place(relx=0.78, rely=.97, anchor="sw")
        self.msg2.place(relx=0.5, rely=0.85, anchor="center")



    def logout(self):
        # This function logs out the user
        self.workoutFrame.destroy()
        self.createLoginFrame()
        self.currentid = 0

    def back(self):
        # this function displays the login frame
        self.createAccountFrame.destroy()
        self.createLoginFrame()
        self.loginButton.focus_set()
        self.loginFrame.pack(fill=tk.BOTH, expand=True)

    from tkinter import messagebox

    def login(self):

        # This function validates the user username and password

        # Check if the user is connected to the database
        if not self.sql.connection_status:
            print("Not connected to the database")
            self.msg.configure(text="No connection to database", fg="red", bg="white")
            return

        # Get the username and password entered by the user
        username = self.username.get().strip()
        password = self.password.get().strip()

        # Check if the user entered a non-empty username and password
        if not username or not password:
            self.msg.configure(text="Please enter both username and password",fg="red", bg="white")
            self.msg.after(1000, lambda: self.msg.configure(text=""))
            self.loginButton.focus_set()
            return

        # Validate the user's credentials
        if self.sql.validateUser(username, password):
            # If the credentials are valid, show the workout frame
            print("Validated")
            self.username.configure(fg_color="#343638")
            self.password.configure(fg_color="#343638")
            print(f"this is the current user id:{self.sql.current_user}")

            self.ShowWorkoutFrame()

        else:
            # If the credentials are invalid, display an error message and clear the text boxes
            self.msg.configure(text="Invalid username or password", fg="red", bg="white")
            self.msg.after(1000, lambda: self.msg.configure(text=""))
            self.username.configure(fg_color="red")
            self.password.configure(fg_color="red")
            self.username.delete(0, tk.END)
            self.password.delete(0, tk.END)
            self.loginButton.focus_set()

            # Set the entry boxes to red for 1 second
            self.username.after(1000, lambda: self.username.configure(fg_color="#343638"))
            self.password.after(1000, lambda: self.password.configure(fg_color="#343638"))

    def create_account(self):
        # This function displays the create account frame
        # Get the values of the input fields
        username = self.username2.get().strip()
        password = self.password2.get().strip()
        email = self.email.get().strip()
        age = self.age.get().strip()
        gender = self.gender.get().strip()
        # Check if the user is connected to the database
        # Check if all required fields have values
        if not username or not password or not email or not age or not gender:
            # If not, mark the empty fields as red and show an error message
            if not username:
                self.username2.configure(fg_color="red")
            if not password:
                self.password2.configure(fg_color="red")
            if not email:
                self.email.configure(fg_color="red")
            if not age:
                self.age.configure(fg_color="red")
            if not gender:
                self.gender.configure(fg_color="red")
            messagebox.showerror("Error", "Please fill out all fields.")
        else:
            # All fields have values, create the account
            self.sql.createUser(username, password, email, age, gender)
            self.msg.configure(text="Account created", font=("Arial", 40, "bold"), fg="green", bg="white")

            self.createAccountFrame.destroy()
            self.createLoginFrame()
    # This function displays the create account frame
    def addWorkout(self):
        # This function displays the add workout frame
        self.clear()
        self.addBtn.configure(text="Save", command=self.save)

    import time

    def save(self):
        # This function saves the workout to the database
        exercise_names = [self.exercise1.get(), self.exercise2.get(), self.exercise3.get(), self.exercise4.get(),
                          self.exercise5.get()]
        for name in exercise_names:
            if not name:
                self.msg2.configure(text="Please enter an exercise name", fg="red", bg="white")
                self.msg2.after(1000, lambda: self.msg2.configure(text=""))
                return
        for entry in [self.exercise1Sets, self.exercise1Reps, self.exercise2Sets, self.exercise2Reps,
                      self.exercise3Sets, self.exercise3Reps, self.exercise4Sets, self.exercise4Reps,
                      self.exercise5Sets, self.exercise5Reps]:
            if not entry.get().isdigit():
                self.msg2.configure(text="Please enter a number for sets and reps", fg="red", bg="white")
                self.msg2.after(1000, lambda: self.msg2.configure(text=""))
                return
        self.sql.createRecord(
            self.exercise1.get(), self.exercise1Sets.get(), self.exercise1Reps.get(),
            self.exercise2.get(), self.exercise2Sets.get(), self.exercise2Reps.get(),
            self.exercise3.get(), self.exercise3Sets.get(), self.exercise3Reps.get(),
            self.exercise4.get(), self.exercise4Sets.get(), self.exercise4Reps.get(),
            self.exercise5.get(), self.exercise5Sets.get(), self.exercise5Reps.get()
        )
        print("Saved")
        self.addBtn.configure(text="Add Workout", command=self.addWorkout)
        self.msg2.configure(text="Workout saved", fg="green")
        # Schedule the removal of the message after 2 seconds
        self.msg2.after(1000, lambda: self.msg2.configure(text=""))

    def deleteWorkout(self):
        # This function deletes the current workout also clears the screen
        messagebox.showinfo("Delete", "Are you sure you want to delete this record?")
        self.sql.deleteRec(self.currentid)
        print("Record deleted")
        self.clear()
        self.load()

    def updateWorkout(self):
        # This function updates the current workout
        self.addBtn.configure(text="Commit", command=self.update)



    def update(self):
        # This function updates the current workout
        messagebox.showinfo("Update", "Are you sure you want to update this record?")
        self.sql.update(self.currentid,
                        self.exercise1.get(), self.exercise1Sets.get(), self.exercise1Reps.get(),
                        self.exercise2.get(), self.exercise2Sets.get(), self.exercise2Reps.get(),
                        self.exercise3.get(), self.exercise3Sets.get(), self.exercise3Reps.get(),
                        self.exercise4.get(), self.exercise4Sets.get(), self.exercise4Reps.get(),
                        self.exercise5.get(), self.exercise5Sets.get(), self.exercise5Reps.get()
                        )
        self.clear()
        self.load()
        self.addBtn.configure(text="Add Workout", command=self.addWorkout)
        print("Update")



    def clear(self):
        # This function clears the screen
        self.exercise1.delete(0, tk.END)
        self.exercise1Sets.delete(0, tk.END)
        self.exercise1Reps.delete(0, tk.END)
        self.exercise2.delete(0, tk.END)
        self.exercise2Sets.delete(0, tk.END)
        self.exercise2Reps.delete(0, tk.END)
        self.exercise3.delete(0, tk.END)
        self.exercise3Sets.delete(0, tk.END)
        self.exercise3Reps.delete(0, tk.END)
        self.exercise4.delete(0, tk.END)
        self.exercise4Sets.delete(0, tk.END)
        self.exercise4Reps.delete(0, tk.END)
        self.exercise5.delete(0, tk.END)
        self.exercise5Sets.delete(0, tk.END)
        self.exercise5Reps.delete(0, tk.END)

    def jump(self,number):
        # This function jumps to the next or previous record
        self.currentRecord += number
        if self.currentRecord >= len(self.sql.GetWorkout()):
            self.currentRecord = len(self.sql.GetWorkout()) - 1
        elif self.currentRecord < 0:
            self.currentRecord = 0
        self.load()
        self.left.focus_set()
        print(self.currentRecord)














