from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.title('Age Calculator - Sahil')
root.geometry("400x500")
root.maxsize(400,500)


def age():
    if my_entry.get():
        # Get the current year
        current_year = datetime.now().year
        # calculate age
        your_age = current_year - int(my_entry.get())
        # show age in message box
        if int(my_entry.get()) == current_year :
            messagebox.showinfo("smile","Happiest Born Year !!!")
        else:
            messagebox.showinfo("Your Age",f"your age is : {your_age}")
    else:
        messagebox.showerror("Error","You Forgot to enter your age")


my_label = Label(root, text="Enter Year Born : ",font=("Helvetica",24))
my_label.pack(pady=20)

my_entry = Entry(root,font=("Helvetica",18))
my_entry.pack(pady=20)

my_button = Button(root,text="Calculate Age!!",font=("Helvetica",18),command=age)
my_button.pack(pady=20)






root.mainloop()