from tkinter import *
from PIL import Image, ImageTk 
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox
import mysql.connector 



class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+235+220") 
        
        # ====================== VARIABLES ======================

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_room_type = StringVar()
        self.var_available_room = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days = StringVar()
        self.var_paid_tax = StringVar()
        self.var_sub_total = StringVar()
        self.var_total_cost = StringVar()
        
        self.search_var = StringVar() 
        self.txt_search = StringVar() 
        
        # Title Label
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS",
                          font=("times new roman", 18, "bold"),
                          bg="#7F5628", fg="#FFFFFF", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        
        # ================= LOGO LEFT ====================
        try:
            img2 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\logo2.png")
            img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lbl_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE, bg="#2F1F10")
            lbl_logo.place(x=5, y=2, width=100, height=45)
        except FileNotFoundError:
             print("Error: logo2.png not found. Skipping logo.")

        # Label Frame for Customer Details
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", 
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)
        
        # ================== label ==================
        
        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky="w")

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=("arial", 13, "bold"), width=20)
        enty_contact.grid(row=0, column=1, padx=2, pady=2,sticky=W)
        
        
        btnFetchData = Button(labelframeleft, command=self.fetch_contact, text="Fetch data", font=("arial", 8 , "bold"), bg="#7F5628", fg="#FFFFFF", width=8)
        btnFetchData.place(x=347,y=4)

        # Check-in Date
        lbl_CheckInDate = Label(labelframeleft, font=("arial", 12, "bold"), text="Check_in Date:", padx=2, pady=6)
        lbl_CheckInDate.grid(row=1, column=0, sticky="w")
        txt_check_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("arial", 13, "bold"), width=29)
        txt_check_in_date.grid(row=1, column=1, padx=2, pady=2)

        # Check-out Date
        lbl_CheckOutDate = Label(labelframeleft, font=("arial", 12, "bold"), text="Check_Out Date:", padx=2, pady=6) 
        lbl_CheckOutDate.grid(row=2, column=0, sticky="w")
        txt_check_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
        txt_check_out_date.grid(row=2, column=1, padx=2, pady=2)

        # Room Type
        lbl_RoomType = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky="w")
        
        self.var_room_type.set("Single") 
        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_room_type, font=("arial", 12, "bold"), 
                                        width=27, state="readonly", values=["Single", "Double", "Luxury"])
        combo_RoomType.grid(row=3, column=1, padx=2, pady=2)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, font=("arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky="w")
        #txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_available_room, font=("arial", 13, "bold"), width=29)
        #txtRoomAvailable.grid(row=4, column=1, padx=2, pady=2)

        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        lbl_RoomNo = Label(labelframeleft, font=("arial", 12, "bold"), text="Room Type:", padx=2, pady=6)
        lbl_RoomNo.grid(row=3, column=0, sticky="w")
        
        self.var_room_type.set("Single") 
        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_available_room, font=("arial", 12, "bold"), 
                                        width=27, state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.grid(row=4, column=1, padx=2, pady=2)

        # Meal
        lblMealLabel = Label(labelframeleft, font=("arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMealLabel.grid(row=5, column=0, sticky="w")
        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1, padx=2, pady=2)

        # No Of Days
        lblNoOfDaysLabel = Label(labelframeleft, font=("arial", 12, "bold"), text="No Of Days:", padx=2, pady=6)
        lblNoOfDaysLabel.grid(row=6, column=0, sticky="w")
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_no_of_days, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1, padx=2, pady=2)

        # Paid Tax
        lblPaidTaxLabel = Label(labelframeleft, font=("arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblPaidTaxLabel.grid(row=7, column=0, sticky="w")
        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paid_tax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1, padx=2, pady=2)

        # Sub Total
        lblSubTotalLabel = Label(labelframeleft, font=("arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotalLabel.grid(row=8, column=0, sticky="w")
        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_sub_total, font=("arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1, padx=2, pady=2)

        # Total Cost
        lblTotalCostLabel = Label(labelframeleft, font=("arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCostLabel.grid(row=9, column=0, sticky="w")
        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total_cost, font=("arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1, padx=2, pady=2)

        #=================bill Button===================

        btnBill = Button(labelframeleft, text="Bill", command=self.total,font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        
        # ================== BUTTONS FRAME (Added for completeness) ==================
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data,font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.delete, font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset ,font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=10)
        btnReset.grid(row=0, column=3, padx=1)

      #=========================rightside image======================
        try:
            img3 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\room1.jpg")
            img3 = img3.resize((520, 300), Image.Resampling.LANCZOS) 
            self.photoImg3 = ImageTk.PhotoImage(img3)
            lblImg = Label(self.root, image=self.photoImg3, bd=0, relief=RIDGE)
            lblImg.place(x=760, y=55, width=520, height=300)
        except FileNotFoundError:
             print("Error: room1.jpg not found. Skipping room image.")

#====================table frame and serch style==========================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System", font=("arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        
        lblSearchByLabel = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="#0F0E0E", fg="white")
        lblSearchByLabel.grid(row=0, column=0, sticky=W, padx=2)

        
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search['values'] = ("contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        # Creating an entry box for entering the search text
        txtSearchText = Entry(Table_Frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txtSearchText.grid(row=0, column=2, padx=2)

        
        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        
        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"), bg="#7F5628", fg="#FFFFFF", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)
#=============================data table================================================
    
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        
        
        self.room_table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfDays"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        
        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfDays", text="NoOfDays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfDays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()



    #add_data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "Customer Name and Mobile are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values ( %s, %s, %s, %s, %s, %s, %s)", (
                            self.var_contact.get(),
                            self.var_checkin.get(),
                            self.var_checkout.get(),
                            self.var_room_type.get(),
                            self.var_available_room.get(),
                            self.var_meal.get(),
                            self.var_no_of_days.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)       

    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_room_type.set(row[3]),
        self.var_available_room.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_no_of_days.set(row[6])


#update function
    def update(self):
        if self.var_contact.get() == "":
           messagebox.showerror("Error", "Please enter contact number", parent=self.root)
           return

        try:
            conn = mysql.connector.connect(
               host="localhost",
               username="root",
               password="Test@123",
               database="management"
            )
            my_cursor = conn.cursor()

            my_cursor.execute("""
               UPDATE room
               SET Check_in=%s,
                  Check_out=%s,
                  roomtype=%s,
                  Room=%s,
                  meal=%s,
                  noOfdays=%s
                WHERE Contact=%s
            """, (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_room_type.get(),
                self.var_available_room.get(),
                self.var_meal.get(),
                self.var_no_of_days.get(),
                self.var_contact.get()
            ))

            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Room details updated successfully", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Update failed: {str(es)}", parent=self.root)



    def delete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if mDelete:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
                my_cursor = conn.cursor()

                if self.var_contact.get() == "":
                    messagebox.showerror("Error", "Select a record to delete or enter a Contact Number", parent=self.root)
                    return

                query = "DELETE FROM room WHERE Contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                self.fetch_data()  
                conn.close()
                messagebox.showinfo("Success", "Customer has been deleted", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
        else:
            return
        

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_room_type.set(""),
        self.var_available_room.set(""),
        self.var_meal.set(""),
        self.var_no_of_days.set("")
        self.var_paid_tax.set("")
        self.var_sub_total.set("")
        self.var_total_cost.set("")

# ===================== Customer Data Fetch (Moved INSIDE the class) =====================

    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
            return

        conn = None # Initialize conn
        try:
            
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Test@123",
                database="management"
            )
            my_cursor = conn.cursor()

           
            query = ("SELECT Name FROM customer WHERE Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row_name = my_cursor.fetchone()

            if row_name is None:
                messagebox.showerror("Error", "This number Not Found", parent=self.root)
                conn.close()
                return
            
           
            showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showDataframe.place(x=450, y=55, width=300, height=180)

            # Display Name
            lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
            lblName.place(x=0, y=0)
            lbl1 = Label(showDataframe, text=row_name[0], font=("arial", 12, "bold"))
            lbl1.place(x=90, y=0)
            
            # --- Fetch Gender ---
            query=("SELECT Gender FROM customer WHERE Mobile=%s")
            value=(self.var_contact.get(),) 
            my_cursor.execute(query,value)
            row_gender=my_cursor.fetchone()

            lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
            lbl2=Label(showDataframe,text=row_gender[0],font=("arial",12,"bold"))
            lbl2.place(x=90,y=30)

            # --- Fetch Email ---
            query=("SELECT Email FROM customer WHERE Mobile=%s")
            value=(self.var_contact.get(),) 
            my_cursor.execute(query,value)
            row_email=my_cursor.fetchone()

            lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
            lblemail.place(x=0,y=60)
            lbl3=Label(showDataframe,text=row_email[0],font=("arial",12,"bold"))
            lbl3.place(x=90,y=60)

            # --- Fetch Nationality ---
            query=("SELECT Nationality FROM customer WHERE Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row_nationality=my_cursor.fetchone()

            lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
            lblNationality.place(x=0,y=90)
            lbl4=Label(showDataframe,text=row_nationality[0],font=("arial",12,"bold"))
            lbl4.place(x=90,y=90)

            # --- Fetch Address ---
            query=("SELECT Address FROM customer WHERE Mobile=%s")
            value=(self.var_contact.get(),) 
            my_cursor.execute(query,value)
            row_address=my_cursor.fetchone()

            lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
            lbladdress.place(x=0,y=120)
            
            lbl5=Label(showDataframe,text=row_address[0],font=("arial",12,"bold")) 
            lbl5.place(x=90,y=120)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error connecting to MySQL: {err}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Application Error", f"An unexpected error occurred: {e}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                conn.close()

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE " + "'%" + str(self.txt_search.get()) + "%'")

        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()

        conn.close()


    def total(self):
        try:
            
            inDate = self.var_checkin.get()
            outDate = self.var_checkout.get()
            
            
            if not inDate or not outDate:
                messagebox.showerror("Error", "Please enter Check-in and Check-out dates in DD/MM/YYYY format.", parent=self.root)
                return

            try:
                inDate_dt = datetime.strptime(inDate, "%d/%m/%Y")
                outDate_dt = datetime.strptime(outDate, "%d/%m/%Y")
            except ValueError:
                messagebox.showerror("Error", "Date format must be DD/MM/YYYY.", parent=self.root)
                return

            if outDate_dt <= inDate_dt:
                messagebox.showerror("Error", "Check-out date must be after Check-in date.", parent=self.root)
                return
                
            number_of_days = abs(outDate_dt - inDate_dt).days
            self.var_no_of_days.set(number_of_days)
            
            if number_of_days == 0:
                
                number_of_days = 1
                self.var_no_of_days.set(number_of_days)


           
            room_rates = {
                "Single": 2000.00,
                "Double": 3800.00,
                "Luxury": 6000.00
            }

            # Meal Rates per day
            meal_rates = {
                "Breakfast": 800.00,
                "Half Board": 2000.00,
                "Full Board": 4000.00,
                "None": 0.00
            }
            
            TAX_RATE = 0.09 

            
            room_type = self.var_room_type.get()
            meal_plan = self.var_meal.get() 
            
            # Get base daily cost
            base_room_cost_per_day = room_rates.get(room_type, 0.00) 
            base_meal_cost_per_day = meal_rates.get(meal_plan, 0.00) 

            if base_room_cost_per_day == 0.00:
                messagebox.showwarning("Warning", "Room Type is not selected or rate is zero.", parent=self.root)
                return

            
            daily_cost = base_room_cost_per_day + base_meal_cost_per_day
            
          
            sub_total = daily_cost * number_of_days
            self.var_sub_total.set(f"Rs: {sub_total:.2f}")

            
            paid_tax = sub_total * TAX_RATE
            self.var_paid_tax.set(f"Rs: {paid_tax:.2f}")

            
            total_cost = sub_total + paid_tax
            self.var_total_cost.set(f"Rs: {total_cost:.2f}")
            
        except Exception as es:
             messagebox.showwarning("Warning", f"Calculation Error: {str(es)}", parent=self.root)








if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()