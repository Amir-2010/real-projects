
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import messagebox
import time
import mysql.connector as sql

def gender_func():
    """
    in this function I write command of gender in the main page menu
    this function is search in the database and find gender of persons and show it to user if user want and you can see most of peoples in the database are male or female
    """
    cursor.execute("select gender from users where gender='male'")
    result_male = cursor.fetchall()

    cursor.execute("select gender from users where gender='female'")
    result_female = cursor.fetchall()

    male = len(result_male)
    female = len(result_female)

    messagebox.showinfo("Info",f"males = {male} person\persons\nfemales = {female} person\persons")

def get_average():
    """
    this function is for getting average of user ages who submit in the program
    """
    cursor.execute("select user_age from users")
    result = list(cursor.fetchall())
    number = 0
    devition = 0
    for i in result:
        number = number+i[0]
        devition = devition+1
    
    if number != 0 and devition != 0:
        average_result = number//devition
        messagebox.showinfo("Info",f"Average of ages = {average_result}")
    else:
        pass

def sub_button():
    """
    this function is submit command and It just check the entry and list box and if they aren't empty it will add you into database with your info
    """
    global entry_1
    global list_box_1
    global scale_1
    messagebox_1 = messagebox.askyesno("Question","Are you sure")
    if messagebox_1 == True:
        user_name = str(entry_1.get())
        gender = list_box_1.curselection()
        age = int(scale_1.get())

        try:
            list_box_1.get(gender[0])
            if list_box_1.get(gender[0]) != "" and user_name != "":
                cursor.execute(f"insert into users (user_name,gender,user_age) values('{user_name}','{list_box_1.get(gender[0])}','{age}')")
                connection.commit()
            else:
                messagebox.showerror("Error","fill in the entry")
            scale_1.set(value=10)
        except:
            messagebox.showerror("Error","fill in the list box")

def porg_func():
    """
    this function is a bit different becuse this function is not for main page
    this function is for loding page and It's progress bar command in the program
    """
    for i in range(0,101,10):
        if i < 100:
            prog_1["value"]=i
            window.update()
            time.sleep(1)
        elif i==100:
            prog_1["value"]=i
            label_loding.config(foreground="#06A942",text="welcome",font=("Arial",14))
            window.update()
            time.sleep(1)
        else:
            break
    
    label_loding.destroy()
    prog_1.destroy()
    main_page()

def main_page():
    """
    this is main page of the program
    after loding, window change and progress bar and the loding label are destroy and the back ground is change but the window still window
    """
    global entry_1
    global list_box_1
    global scale_1
    window.config(background="#B6E3E9",cursor="plus")
    
    main_menu = Menu(window)
    window.config(menu=main_menu)

    options_menu = Menu(main_menu,tearoff=False)
    main_menu.add_cascade(menu=options_menu,label="options")
    options_menu.add_command(label="Average",command=get_average)

    options_menu.add_command(label="gender",command=gender_func)

    options_menu.add_separator()

    options_menu.add_command(label="Exit",foreground="#AC0000",command=window.destroy)

    scale_1 = Scale(window,
                    from_=10,
                    to=100,
                    label="Enter your age:",
                    font=("Arial",13),
                    orient="horizontal",
                    length=250,
                    width=20,
                    background="#2563EB",
                    foreground="#EEF2FF",
                    highlightbackground="#93C5FD",
                    border=3,
                    relief="ridge")
    scale_1.place(relx=0.5,y=70,anchor="center")

    labelfr_1 = LabelFrame(window,
                           text="Answer the questions:",
                           font=("Arial",14),
                           background="#EA580C",
                           foreground="#F9FAFB",
                           height=310,
                           width=400)
    labelfr_1.place(relx=0.5,y=285,anchor="center")

    label_1 = Label(labelfr_1,
                    text="Enter your name:",
                    font=("Arial",14),
                    background="#F97316",
                    foreground="#F9FAFB",)
    label_1.place(x=95,y=30,anchor="center")

    entry_1 = Entry(labelfr_1,
                    font=("Arial",14,"bold"),
                    width=15,
                    background="#F9FAFB",
                    foreground="#F97316",
                    justify="center")
    entry_1.place(x=290,y=30,anchor="center")

    label_2 = Label(labelfr_1,
                    text="Select your genter:",
                    font=("Arial",14),
                    background="#F97316",
                    foreground="#F9FAFB")
    label_2.place(x=100,y=100,anchor="center")

    list_box_1 = Listbox(labelfr_1,
                         font=("Arial",14),
                         foreground="#F97316",
                         width=10,
                         height="2")
    list_box_1.insert(END,"male")
    list_box_1.insert(END,"female")
    list_box_1.place(x=290,y=90,anchor="center")

    submit_button = Button(labelfr_1,
                           text="Submit!",
                           font=("Arial",14),
                           background="#2563EB",
                           foreground="#F9FAFB",
                           activebackground="#1E40AF",
                           activeforeground="#F9FAFB",
                           bd=3,
                           relief="raised",
                           height=2,
                           command=sub_button)
    submit_button.place(relx=0.5,y=190,anchor="center")

try:
    connection = sql.connect(user="root",
                            password="",
                            host="localhost",
                            database="age")
    cursor = connection.cursor()
except:
    connection = sql.connect(user="root",
                            password="",
                            host="localhost")
    cursor = connection.cursor()
    cursor.execute("Create database age")

    connection = connection = sql.connect(user="root",
                            password="",
                            host="localhost",
                            database="age")
    cursor = connection.cursor()

    cursor.execute("""Create table users(
                        id integer primary key auto_increment,
                        user_name varchar(250),
                        gender varchar(250),
                        user_age int
                    );""")
    connection.commit()

# in here I create loding window
window = Tk()
window.geometry("500x500")
window.resizable(False,False)
window.title("age")

# this label is the loding window label and that text is wait a minnet until progress bar value = 100
label_loding = Label(window,
                     text="Wait a minnet...",
                     font=("Arial",14,"bold"))
label_loding.place(relx=0.5,y=50,anchor="center")

# this is the loding page progress bar
prog_1 = Progressbar(window,
                     length=400,
                     mode="determinate",)
prog_1.place(relx=0.5,y=100,anchor="center")

# in here I call prog_func becuse I want to start fill the progress bar with out any buttons
porg_func()

window.mainloop()
