from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("REGISTER")
        self.root.geometry("1600x900+0+0")

        ############ VARIABLES ###############
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # =============================bg image=================================
        self.bg = ImageTk.PhotoImage(
            file=r"C:\Users\MI\Desktop\Hotel Management\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relheight=1, relwidth=1)

        # ==================LEFT IMAGE ==================
        self.bg1 = ImageTk.PhotoImage(
            file=r"C:\Users\MI\Desktop\Hotel Management\hotel images\register_left_background.jpg")

        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, height=550, width=470)

        # ========================= MAIN FRAME  =======================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGESTER HERE", font=("arial", 15, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # =============LABELS AND ENTRIES==================

        # ------------------ ROW 1
        fname = Label(frame, text="FIRST NAME :", font=("arial", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname,font=("arial", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="LAST NAME :", font=("arial", 15, "bold"), bg="white", fg='black')
        lname.place(x=370, y=100)

        self.lname_entry = ttk.Entry(frame, textvariable= self.var_lname,font=("arial", 15, "bold"))
        self.lname_entry.place(x=370, y=130, width=250)

        # --------------------ROW 2

        contact = Label(frame, text="CONTACT NO.:", font=("arial", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,  textvariable=self.var_contact,font=("arial", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="EMAIL:", font=("arial", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("arial", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)

        # =====================ROW 3 ==========

        security_q = Label(frame, text="SELECT SECURITY QUESTION:", font=("arial", 15, "bold"), bg="white", fg="black")
        security_q.place(x=50, y=240)

        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_security_q,font=("arial", 15, "bold"),
                                             state="readonly")
        self.combo_security_q["values"] = ("SELECT", "YOUR BIRTH PLACE", "YOUR COLLEGE NAME", "YOUR PET NAME")
        self.combo_security_q.place(x=50, y=270, width=250)
        self.combo_security_q.current(0)

        security_a = Label(frame, text="SECURITY ANSWER", font=("arial", 15, "bold"), bg="white", fg="black")
        security_a.place(x=370, y=240)

        self.txt_security_a = ttk.Entry(frame, textvariable=self.var_security_a,font=("arial", 15, "bold"))
        self.txt_security_a.place(x=370, y=270, width=250)

        ########### ROW 4 ################
        pswd = Label(frame, text="PASSWORD", font=("arial", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,  textvariable= self.var_pass,font=("arial", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="CONFIRM PASSWORD", font=("arial", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,  textvariable=self.var_confpass,font=("arial", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        ############ CHECK BUTTON ############

        self.var_check_btn = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check_btn, text="I AGREE THE TERMS AND CONDITIONS.",
                               font=("arial", 11, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=400)

        ########### BUTTONS #############
        img = Image.open(r"C:\Users\MI\Desktop\Hotel Management\hotel images\register-now-button1.jpg")
        img = img.resize((200, 50), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage,  command=self.register_data,borderwidth=0, cursor="hand2", fg="white",
                    activeforeground="white", activebackground="white", bg="white", font=("arial", 15, "bold"))
        b1.place(x=10, y=440, width=200)

        img1 = Image.open(r"C:\Users\MI\Desktop\Hotel Management\hotel images\loginpng.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame,  image=self.photoimage1, borderwidth=0, cursor="hand2", fg="white",
                    activeforeground="white", activebackground="white", bg="white", font=("arial", 15, "bold"))
        b2.place(x=330, y=440, width=200)

    # ============ FUNCTION =================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_security_q.get() == "SELECT":
            messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("ERROR", "PASSWORD AND CONFIRM PASSWORD MUST BE SAME!!!")
        elif self.var_check_btn.get() == 0:
            messagebox.showerror("ERROR", "PLEASE AGREE THE TERMS AND CONDITION!!!")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                           database="management")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("ERROR", "USER ALREADY EXIST, PLEASE TRY ANOTHER EMAIL!!!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_q.get(),
                    self.var_security_a.get(),
                    self.var_pass.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("SUCCESS", "REGISTER SUCCESSFULLY!!!")


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)

    root.mainloop()
