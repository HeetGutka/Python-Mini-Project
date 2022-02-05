#import modules

from tkinter import *
from tkinter import messagebox
import os

# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("500x500")

    global fullname
    global email
    global username
    global password
    global fullname_entry
    global email_entry
    global username_entry
    global password_entry
    fullname = StringVar()
    email = StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    fullname_lable = Label(register_screen, text="Full Name * ")
    fullname_lable.pack()
    fullname_entry = Entry(register_screen, textvariable=fullname)
    fullname_entry.pack()
    email_lable = Label(register_screen, text="Email * ")
    email_lable.pack()
    email_entry = Entry(register_screen, textvariable=email)
    email_entry.pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("500x500")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global email_verify
    global password_verify

    email_verify = StringVar()
    password_verify = StringVar()

    global email_login_entry
    global password_login_entry

    Label(login_screen, text="Email * ").pack()
    email_login_entry = Entry(login_screen, textvariable=email_verify)
    email_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()

# Implementing event on register button

def register_user():

    fullname_info = fullname.get()
    email_info = email.get()
    username_info = username.get()
    password_info = password.get()

    file = open(email_info, "w")
    file.write(fullname_info + "\n")
    file.write(email_info + "\n")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

# Implementing event on login button 

def login_verify():
    email1 = email_verify.get()
    password1 = password_verify.get()
    email_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if email1 in list_of_files:
        file1 = open(email1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=yoga_details).pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()



#Screening the Yoga Activities Page
def yoga_details():
    global yoga_screen
    yoga_screen = Toplevel(main_screen)
    yoga_screen.title("Yoga Details")
    yoga_screen.geometry("500x500")
    yoga_screen.configure(bg="orange")

    global photo
    global btn
    global photo2
    global btn2

    photo = PhotoImage(file="images/yoga.png")
    photo2 = PhotoImage(file="images/meditate.png")

    btn = Button(yoga_screen, image=photo, command=asanas, border=0).grid(row=0, column=1, padx=200, pady=100)
    Label(yoga_screen, text="1. Types of Asanas", font=("times new roman", 40, "bold")).grid(row=1, column=1)

    btn2 = Button(yoga_screen, image=photo2, command=adv_yoga, border=0).grid(row=0, column=2, padx=100, pady=100)
    Label(yoga_screen, text="2. Advantages of Yoga", font=("times new roman", 40, "bold")).grid(row=1, column=2)


def asanas():
    global asanas_screen
    asanas_screen = Toplevel(main_screen)
    asanas_screen.title("Types of Asanas")
    asanas_screen.geometry("500x500")
    asanas_screen.configure(bg="orange")

    global bridge_pose
    global bridge_pose_lbl
    global downward_dog_pose
    global downward_dog_pose_lbl
    global easy_yoga_pose
    global easy_yoga_pose_lbl
    global king_dancer
    global king_dancer_lbl
    global the_tree_pose
    global the_tree_pose_lbl
    global boat_pose
    global boat_pose_lbl
    global warrior_1_pose
    global warrior_1_pose_lbl
    global warrior_2_pose
    global warrior_2_pose_lbl
    global triangle_pose
    global triangle_pose_lbl
    global the_crow_pose
    global the_crow_pose_lbl

    Label(asanas_screen, text="", bg="orange").grid(row=0, column=0, padx=40, pady=50)
    Label(asanas_screen, text="", bg="orange").grid(row=1, column=0, padx=40, pady=50)

    bridge_pose = PhotoImage(file="images/Bridge-Pose.png")
    bridge_pose_lbl = Label(asanas_screen, image = bridge_pose, bd=0).grid(row=1, column=1, padx=50, pady=20)
    Label(asanas_screen, text="1. Bridge Pose").grid(row=2, column=1)

    downward_dog_pose = PhotoImage(file="images/Downward-Dog-pose.png")
    downward_dog_pose_lbl = Label(asanas_screen, image = downward_dog_pose, bd=0).grid(row=1, column=2, padx=50, pady=20)
    Label(asanas_screen, text="2. Downward Dog Pose").grid(row=2, column=2)

    easy_yoga_pose = PhotoImage(file="images/Easy-yoga-pose.png")
    easy_yoga_pose_lbl = Label(asanas_screen, image = easy_yoga_pose, bd=0).grid(row=1, column=3, padx=50, pady=20)
    Label(asanas_screen, text="3. Meditation").grid(row=2, column=3)

    king_dancer = PhotoImage(file="images/King-Dancer.png")
    king_dancer_lbl = Label(asanas_screen, image = king_dancer, bd=0).grid(row=1, column=4, padx=50, pady=20)
    Label(asanas_screen, text="4. King Dancer").grid(row=2, column=4)

    the_tree_pose = PhotoImage(file="images/The-tree-pose.png")
    the_tree_pose_lbl = Label(asanas_screen, image = the_tree_pose, bd=0).grid(row=1, column=5, padx=50, pady=20)
    Label(asanas_screen, text="5. The Tree Pose").grid(row=2, column=5)

    Label(asanas_screen, text="", bg="orange").grid(row=3, column=0, padx=40, pady=50)
    Label(asanas_screen, text="", bg="orange").grid(row=1, column=0, padx=40, pady=50)

    boat_pose = PhotoImage(file="images/Boat-pose.png")
    boat_pose_lbl = Label(asanas_screen, image = boat_pose, bd=0).grid(row=4, column=1, padx=50, pady=20)
    Label(asanas_screen, text="6. Boat Pose").grid(row=5, column=1)

    warrior_1_pose = PhotoImage(file="images/Warrior-1-pose.png")
    warrior_1_pose_lbl = Label(asanas_screen, image = warrior_1_pose, bd=0).grid(row=4, column=2, padx=50, pady=20)
    Label(asanas_screen, text="7. Warrior 1 Pose").grid(row=5, column=2)

    warrior_2_pose = PhotoImage(file="images/Warrior-2-pose.png")
    warrior_2_pose_lbl = Label(asanas_screen, image = warrior_2_pose, bd=0).grid(row=4, column=3, padx=50, pady=20)
    Label(asanas_screen, text="8. Warrior 2 Pose").grid(row=5, column=3)

    triangle_pose = PhotoImage(file="images/Triangle-pose.png")
    triangle_pose_lbl = Label(asanas_screen, image = triangle_pose, bd=0).grid(row=4, column=4, padx=50, pady=20)
    Label(asanas_screen, text="9. Triangle Pose").grid(row=5, column=4)

    the_crow_pose = PhotoImage(file="images/The-crow-pose.png")
    the_crow_pose_lbl = Label(asanas_screen, image = the_crow_pose, bd=0).grid(row=4, column=5, padx=50, pady=20)
    Label(asanas_screen, text="10. The Crow Pose").grid(row=5, column=5)




def adv_yoga():
    global adv_yoga_screen
    adv_yoga_screen = Toplevel(main_screen)
    adv_yoga_screen.title("Advantages of Yoga")
    adv_yoga_screen.geometry("500x500")
    adv_yoga_screen.configure(bg="orange")

    Advantages_Frame = Frame(adv_yoga_screen)
    Advantages_Frame.place(x=500, y=100)

    adv1 = Label(Advantages_Frame, text="1. Increased Flexibility", font=("times new roman", 40, "bold")).grid(row=1, column=0, padx=20, pady=10)
    adv2 = Label(Advantages_Frame, text="2. Increased Muscle Strength and Tone", font=("times new roman", 40, "bold")).grid(row=2, column=0, padx=20, pady=10)
    adv3 = Label(Advantages_Frame, text="3. Improved Respiration, Energy and Vitality", font=("times new roman", 40, "bold")).grid(row=3, column=0, padx=20, pady=10)
    adv4 = Label(Advantages_Frame, text="4. Maintaining a Balanced Metabolism", font=("times new roman", 40, "bold")).grid(row=4, column=0, padx=20, pady=10)
    adv5 = Label(Advantages_Frame, text="5. Weight Reduction", font=("times new roman", 40, "bold")).grid(row=5, column=0, padx=20, pady=10)
    adv6 = Label(Advantages_Frame, text="6. Cardio and Circulatory Health", font=("times new roman", 40, "bold")).grid(row=6, column=0, padx=20, pady=10)
    adv7 = Label(Advantages_Frame, text="7. Improved Athletic Performance", font=("times new roman", 40, "bold")).grid(row=7, column=0, padx=20, pady=10)
    adv8 = Label(Advantages_Frame, text="8. Protection from Injury", font=("times new roman", 40, "bold")).grid(row=8, column=0, padx=20, pady=10)
    adv9 = Label(Advantages_Frame, text="9. Regulates your Adrenal Glands", font=("times new roman", 40, "bold")).grid(row=9, column=0, padx=20, pady=10)
    adv10 = Label(Advantages_Frame, text="10. Founds a Healthy Lifestyle", font=("times new roman", 40, "bold")).grid(row=10, column=0, padx=20, pady=10)

 

# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()