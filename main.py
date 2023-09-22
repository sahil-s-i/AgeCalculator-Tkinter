from tkinter import *
from datetime import datetime
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Age Calculator - Sahil')
root.geometry("400x500")
# root.maxsize(400,500)
root.resizable(False, False)

# Load the image using Pillow (PIL)
img = Image.open("bg.png")
img = img.resize((350, 220))
photo = ImageTk.PhotoImage(img)

# Create a label to display the image
image_label = Label(root, image=photo)
image_label.place(x=35, y=50)

messagedata = ["Smile! You are amazing.","You are the narrator of \n your next great adventure.","You are glitter and rainbows \n Never lose your sparkle.","When everything seems to be \n going against you,remember… \n the airplane takes off against the wind, \n not with it.","The beautiful journey of today can \n only begin when we learn to let \n go of yesterday.","The best is yet to come.","Magic is believing in yourself.","Take a deep breath and step on through \n This is your new chapter.","Age is just a number.","Don't let anyone tell you old age \n means you have to slow down \n Wrinkles will only go where the \n smiles have been.","Don't let age fool you; \n it's just a number Old age can be the best time \n of your life since restrictions that \n come with youth have fallen away \n We are always the same age inside.","One day you will look back and see \n that all along you were blooming.","About the only thing that \n comes to us without effort is old age."]

def age():
    if my_entry.get():
        # Get the current year
        current_year = datetime.now().year
        # calculate age
        try:
            your_age = current_year - int(my_entry.get())
        except ValueError:
            #print("Enter A numberic value")
            messagebox.showinfo("sorry!", f"Please Enter \n Numeric Value")
        else:
            # show age in message box
            if int(my_entry.get()) == current_year:
                messagebox.showinfo("smile", f"Happiest Born Year !!! \n\n {messagedata[0]}")
            else:
                # different quote for the different age groups
                if your_age < 0:
                    messagebox.showinfo("Sorry !!", f"You are not born Yet !!!")
                elif your_age > 0 and your_age <= 5:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[0]}")
                elif your_age > 5 and your_age <= 10:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[1]}")
                elif your_age > 10 and your_age <= 15:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[2]}")
                elif your_age > 15 and your_age <= 20:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[3]}")
                elif your_age > 20 and your_age <= 25:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[4]}")
                elif your_age > 25 and your_age <= 30:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[5]}")
                elif your_age > 30 and your_age <= 40:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[6]}")
                elif your_age > 40 and your_age <= 50:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[7]}")
                elif your_age > 50 and your_age <=60:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[8]}")
                elif your_age > 60 and your_age <= 70:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[9]}")
                elif your_age > 70 and your_age <= 80:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[10]}")
                elif your_age > 80 and your_age <= 90:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[11]}")
                elif your_age > 90 and your_age <= 100:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n {messagedata[12]}")
                else:
                    messagebox.showinfo("Your Age", f"your age is : {your_age}\n\n You are Just more then Amazing !!")
    else:
        messagebox.showerror("Error", "You Forgot to enter your age")

# Add a label for the title
title_label = Label(root, text="- Age Calculator -", font=("Helvetica", 26),fg="#003366")
title_label.place(x=72, y=10)

# a quote to display
head = Label(root, text=" \"Life is three hours journey; "
                        "childhood,adulthood & "
                        "old-hood;\n filled with "
                        "inspiration, perspiration "
                        "and desperation\" ",font=("Helvetica", 10),fg="#003366")
head.place(x=25, y=252)

# a label for the heading
my_label = Label(root, text="Enter Year Born : ", font=("Helvetica", 24),fg="#333333" )
my_label.place(x=50, y=300)

# a label for the entry
my_entry = Entry(root, font=("Helvetica", 18))
my_entry.place(x=50, y=350)

# a label for the button
my_button = Button(root, text="Calculate Age!!",font=("Helvetica", 18), command=age ,bg="#333333",fg="white")
my_button.place(x=100, y=420)

root.mainloop()

