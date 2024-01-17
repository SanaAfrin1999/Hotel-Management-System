from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random, os
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import tempfile


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # =====================variable============================
        self.var_cust_name = StringVar()
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdayst = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # =================title===================================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =================logo===================================
        img2 = Image.open(r"hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=100, height=40)

        # =================lableFrame===================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details",
                                    font=("times new roman", 18, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # =================lables and entry===================================
        #  custContact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft, width=20, textvariable=self.var_contact, font=("arial", 13, "bold"))

        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch data Button
        btnFetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", font=("arial", 9, "bold"),
                              bg="black", fg="gold", width=8)
        btnFetchData.place(x=350, y=4)

        # checkinDate
        check_in_date = Label(labelframeleft, text="Check in Date:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkin,
                                     font=("arial", 13, "bold"))

        txtcheck_in_date.grid(row=1, column=1)

        # checkoutDate
        check_out = Label(labelframeleft, text="Check Out:", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out.grid(row=2, column=0, sticky=W)
        txtcheck_out = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkout, font=("arial", 13, "bold"))

        txtcheck_out.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="Password@21", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, width=27, textvariable=self.var_roomtype,font=("arial", 12, "bold"),
                                      state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        # txtRoomAvailable = ttk.Entry(labelframeleft, width=29, textvariable=self.var_roomavailable,
        #                              font=("arial", 13, "bold"))
        # txtRoomAvailable.grid(row=4, column=1)
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@21", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select Roomno from details")
        rows = my_cursor.fetchall()
        combo_RoomNo = ttk.Combobox(labelframeleft, width=27, textvariable=self.var_roomavailable,font=("arial", 12, "bold"),
                                      state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal = ttk.Entry(labelframeleft, width=29, textvariable=self.var_meal, font=("arial", 13, "bold"))
        txtMeal.grid(row=5, column=1)

        # NoOfDays
        lblNoOfDays = Label(labelframeleft, text="No Of Days:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, width=29, textvariable=self.var_noOfdayst, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(labelframeleft, width=29, textvariable=self.var_paidtax, font=("arial", 13, "bold"))
        txtPaidTax.grid(row=7, column=1)

        # Sub total
        lblSubTotal = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(labelframeleft, width=29, textvariable=self.var_actualtotal, font=("arial", 13, "bold"))
        txtSubTotal.grid(row=8, column=1)

        # totalcost
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(labelframeleft, width=29, textvariable=self.var_total, font=("arial", 13, "bold"))
        txtTotalCost.grid(row=9, column=1)

        # ====================Bill Button=================
        btnBill = Button(labelframeleft, text="Bill", command=self.total,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)
        btnBillPrint = Button(labelframeleft, text=" Print Bill", command=self.Receipt,font=("arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBillPrint.grid(row=10, column=1, padx=1, sticky=W)

        # ====================btns=========================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update,font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.mdelete, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset,font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # ================right Side img==============================================

        img3 = Image.open(r"hotel images\bed.jpg")
        img3 = img3.resize((530, 220), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=530, height=220)

        # =================tableFrame Search system===================================
        Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                 font=("times new roman", 12, "bold"), padx=2)
        Table_frame.place(x=435, y=280, width=860, height=260)

        lblSearchby = Label(Table_frame, text="Search By", font=("arial", 12, "bold"), bg="red", fg="white")
        lblSearchby.grid(row=0, column=0, sticky=W, padx=1)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_frame, width=27, textvariable=self.search_var, font=("arial", 12, "bold"),
                                    state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=1)

        self.text_search = StringVar()
        txtSearch = ttk.Entry(Table_frame, width=24, textvariable=self.text_search, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=1)

        btnSearch = Button(Table_frame, text="Search", command=self.search,font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_frame, text="Show All", command=self.fetch_data,font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ==============================Show data Table==============================
        details_table = Frame(Table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scorll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scorll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_Table = ttk.Treeview(details_table,
                                       columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal",
                                                "noOfdays",),
                                       xscrollcommand=scorll_x.set, yscrollcommand=scorll_y.set)
        scorll_x.pack(side=BOTTOM, fill=X)
        scorll_y.pack(side=RIGHT, fill=Y)

        scorll_x.config(command=self.room_Table.xview)
        scorll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkin", text="Check-in")
        self.room_Table.heading("checkout", text="Check-out")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("roomavailable", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noOfdays", text="NoOfDays")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkin", width=100)
        self.room_Table.column("checkout", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.column("roomavailable", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noOfdays", width=100)
        self.room_Table.pack(fill=BOTH, expand=1)

        self.room_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # add data

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                               database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noOfdayst.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Some thing went wrong:{str(es)}", parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@21", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()

        conn.close()

    # get cursor
    def get_cursor(self, event=""):
        cursor_row = self.room_Table.focus()
        content = self.room_Table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdayst.set(row[6])

    # update
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                           database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, "
                              "noOfdays=%s where Contact=%s", (
                                  self.var_checkin.get(),
                                  self.var_checkout.get(),
                                  self.var_roomtype.get(),
                                  self.var_roomavailable.get(),
                                  self.var_meal.get(),
                                  self.var_noOfdayst.get(),
                                  self.var_contact.get()
                              ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room Details has been update successfully", parent=self.root)

    # delete
    def mdelete(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:

            mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer",
                                          parent=self.root)
            if mdelete > 0:

                conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                               database="management")
                my_cursor = conn.cursor()
                query = "delete from room where Contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
            else:
                if not mdelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()

    # reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdayst.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    # ===========================all data fetch=========================

    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            # ==============================Name=================================
            conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                           database="management")
            my_cursor = conn.cursor()
            query = "select Name from customer where Mobile=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Number not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=450, y=55, width=300, height=180)

                lblName = Label(showDataFrame, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lblName = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lblName.place(x=90, y=0)

                # ========================gender=======================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                               database="management")
                my_cursor = conn.cursor()
                query = "select Gender from customer where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName = Label(showDataFrame, text="Gender:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=30)

                lblName = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lblName.place(x=90, y=30)

                # ========================email=======================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                               database="management")
                my_cursor = conn.cursor()
                query = "select Email from customer where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName = Label(showDataFrame, text="email:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=60)

                lblName = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lblName.place(x=90, y=60)

                # ========================nationality=======================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                               database="management")
                my_cursor = conn.cursor()
                query = "select Nationality from customer where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName = Label(showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=90)

                lblName = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lblName.place(x=90, y=90)

                # ========================Address=======================================
                conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                               database="management")
                my_cursor = conn.cursor()
                query = "select Address from customer where Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblName = Label(showDataFrame, text="Address:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=120)

                lblName = Label(showDataFrame, text=row, font=("arial", 12, "bold"))
                lblName.place(x=90, y=120)

    # ========================search system=================

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Password@21",
                                       database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(
            self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()

        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noOfdayst.set(abs(outDate-inDate).days)

        if self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury":
            q1=float(300)
            q2=float(1500)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single":
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double":
            q1=float(300)
            q2=float(1000)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury":
            q1=float(500)
            q2=float(1500)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single":
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double":
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury":
            q1=float(500)
            q2=float(1500)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single":
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
        elif self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double":
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noOfdayst.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.09))
            ST = "Rs."+str("%.2f"%((q5)))
            TT = "Rs."+str("%.2f"%(q5+(q5)*0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)



    def Receipt(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            roott = Tk()
            roott.title("Receipt")
            roott.geometry("550x500+230+220")
            Receipt_Ref = StringVar()


            # =======================Frame===================

            f1 = Frame(roott, width = 1600, height = 700, bd = 12, relief =RIDGE)
            f1.pack()

            lblReceipt = Label(f1, font=('arial', 12, 'bold'), text="Welcome to Hotel Grand", bd=2, anchor='w')
            lblReceipt.grid(row=0, column=0, sticky=W)

            txtReceipt = Text(f1, width=64, height=35, bg="white", bd=8, font=('arial', 11, 'bold'))
            txtReceipt.grid(row=3, column=0)
            txtReceipt.delete("1.0", END)
            x = random.randint(1000, 500890)
            randomRef = str(x)
            Receipt_Ref.set("BILL" + randomRef)

            txtReceipt.insert(END, '========================================================'+"\n")
            txtReceipt.insert(END, '\t\t\tRECEIPT\t\t\t'+'\n')
            txtReceipt.insert(END, '========================================================'+"\n")
            txtReceipt.insert(END, 'Receipt Ref:\t\t\t\t\t'+ Receipt_Ref.get() +"\n",)
            txtReceipt.insert(END, '------------------------------------------------------------------------------------------------------'+"\n")
            txtReceipt.insert(END, 'Contact Details:\t\t\t\t\t' + self.var_contact.get() + "\n")
            txtReceipt.insert(END, 'Checkin Date:\t\t\t\t\t' + self.var_checkin.get() + "\n")
            txtReceipt.insert(END, 'Checkout Date:\t\t\t\t\t' + self.var_checkout.get() + "\n")
            txtReceipt.insert(END, 'Meal:\t\t\t\t\t' + self.var_meal.get() + "\n")
            txtReceipt.insert(END, 'No Of days :\t\t\t\t\t' + self.var_noOfdayst.get() + "\n")
            txtReceipt.insert(END, "----------------------------------------------------------------------------------------------------" + "\n")
            txtReceipt.insert(END, 'Amount :\t\t\t\t\t'+"\n")
            txtReceipt.insert(END, "----------------------------------------------------------------------------------------------------" + "\n")
            txtReceipt.insert(END, 'Sub Total :\t\t\t\t\t' + self.var_actualtotal.get() + "\n")
            txtReceipt.insert(END, 'Paid Tax :\t\t\t\t\t' + self.var_paidtax.get() + "\n")
            txtReceipt.insert(END, 'Total :\t\t\t\t\t' + self.var_total.get() + "\n")
            txtReceipt.insert(END, '========================================================'+"\n\n",)
            txtReceipt.insert(END, "----------------------------------THANK YOU,VISIT AGAIN-------------------------------" + "\n\n")
            txtReceipt.insert(END, '========================================================'+"\n\n",)



            roott.mainloop()




if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
