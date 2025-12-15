from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import hashlib 
from hotel import HotelManagementSystem 


def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

class Register:
    """Handles User Registration (Sign Up)"""
    def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="white")

        # ============= Variables =============
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # ================= Background Image ===================
      
        try:
            bg_img = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\hotel8.jpg")
            bg_img = bg_img.resize((1550, 800), Image.Resampling.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(bg_img)
            bg_lbl = Label(self.root, image=self.photoimg_bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
    
            bg_lbl = Label(self.root, text="Registration Screen", font=("times new roman", 30, "bold"), bg="white")
            bg_lbl.pack(fill=BOTH, expand=1)

        # ================= Registration Frame ===================
        frame = Frame(self.root, bg="black")
        frame.place(x=400, y=100, width=800, height=550)

        register_lbl = Label(frame, text="CREATE NEW ACCOUNT", font=("times new roman", 20, "bold"), fg="#FFFFFF", bg="white")
        register_lbl.place(x=20, y=20)

        # ================= Form Fields ===================
        
        # ================= Registration Frame ===================
       
        frame = Frame(self.root, bg="black")
        frame.place(x=400, y=100, width=800, height=550)

        # Main Title: White text on Black background
        register_lbl = Label(frame, text="CREATE NEW ACCOUNT", font=("times new roman", 20, "bold"), fg="white", bg="black")
        register_lbl.place(x=20, y=20)

# ================= Form Fields ===================


        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=50, y=100)
        
        Entry(frame, textvariable=self.var_fname, font=("times new roman", 15), bg="white", fg="black").place(x=50, y=130, width=250)

        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=400, y=100)
        Entry(frame, textvariable=self.var_lname, font=("times new roman", 15), bg="white", fg="black").place(x=400, y=130, width=250)


        Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=50, y=170)
        Entry(frame, textvariable=self.var_contact, font=("times new roman", 15), bg="white", fg="black").place(x=50, y=200, width=250)

        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=400, y=170)
        Entry(frame, textvariable=self.var_email, font=("times new roman", 15), bg="white", fg="black").place(x=400, y=200, width=250)

        
        Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=50, y=240)
        security_Q_combo = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        security_Q_combo["values"] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        security_Q_combo.current(0)
        security_Q_combo.place(x=50, y=270, width=250)

        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=400, y=240)
        Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15), bg="white", fg="black").place(x=400, y=270, width=250)


        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=50, y=310)
        Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*", bg="white", fg="black").place(x=50, y=340, width=250)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=400, y=310)
        Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*", bg="white", fg="black").place(x=400, y=340, width=250)

# ================= Check box and Buttons ===================

        Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=("times new roman", 12), onvalue=1, offvalue=0, bg="black", fg="white", activebackground="black", activeforeground="white", selectcolor="black").place(x=50, y=380)

        Button(frame, text="Register", command=self.register_data, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#7F5628", activebackground="#7F5628", activeforeground="white").place(x=50, y=420, width=150, height=35)

        Button(frame, text="Already have an account? Login", command=self.return_login, font=("times new roman", 12, "bold"), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="lightblue", cursor="hand2").place(x=400, y=430, width=250)


    def register_data(self):
        """Validates input and inserts new user into the database."""
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select" or self.var_pass.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and Confirm Password must match.", parent=self.root)
            return
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the terms and conditions.", parent=self.root)
            return
        
        try:
            
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
            my_cursor = conn.cursor()

            query = "SELECT * FROM user WHERE email=%s"
            my_cursor.execute(query, (self.var_email.get(),))
            if my_cursor.fetchone() is not None:
                messagebox.showerror("Error", "User already exists with this email.", parent=self.root)
                conn.close()
                return
            
            hashed_password = hash_password(self.var_pass.get())

            
            insert_query = """
            INSERT INTO user (fname, lname, contact, email, securityQ, securityA, password) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            insert_values = (
                self.var_fname.get(), self.var_lname.get(), self.var_contact.get(),
                self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get(),
                hashed_password 
            )
            my_cursor.execute(insert_query, insert_values)

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration Successful! Please login.", parent=self.root)
            self.root.destroy()
            

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Database error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)


    def return_login(self):
        """Destroys current window and goes back to Login (handled by the main function)."""
        self.root.destroy()


class Login:
    """Handles User Login and launching the main application"""
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

       
        try:
            bg_img = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\hotel8.jpg")
            bg_img = bg_img.resize((1550, 800), Image.Resampling.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(bg_img)
            bg_lbl = Label(self.root, image=self.photoimg_bg)
            bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
             bg_lbl = Label(self.root, text="Login Screen", font=("times new roman", 30, "bold"), bg="white")
             bg_lbl.pack(fill=BOTH, expand=1)

        # ============= Login Frame =============
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # ============= Logo and Title =============
    
        try:
            img1 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\logo2.png")
            img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
            self.photoimg1 = ImageTk.PhotoImage(img1)
            Label(frame, image=self.photoimg1, bg="black").place(x=120, y=5)
        except Exception:
            Label(frame, text="LOGO", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=120, y=5)

        Label(frame, text="Get Started", font=("times new roman", 20, "bold"), bg="black", fg="white").place(x=95, y=100)

        # ============= Labels and Entries =============
        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=70, y=155)
        self.txt_user = ttk.Entry(frame, font=("times new roman", 15))
        self.txt_user.place(x=70, y=180, width=200)

        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="black", fg="white").place(x=70, y=225)
        self.txt_pass = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.txt_pass.place(x=70, y=250, width=200)

        # ============= Buttons =============
        Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="#7F5628", activebackground="#7F5628", activeforeground="white").place(x=110, y=300, width=120, height=35)

        Button(frame, text="New User Register", command=self.register_window, font=("times new roman", 10), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white").place(x=10, y=360, width=160)

        Button(frame, text="Forgot Password", command=self.forgot_password_window, font=("times new roman", 10), borderwidth=0, fg="white", bg="black", activebackground="black", activeforeground="white").place(x=170, y=360, width=160)


    def login(self):
        """Validates credentials and launches the main app."""
        user_email = self.txt_user.get()
        user_pass = self.txt_pass.get()

        if user_email == "" or user_pass == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return

        try:
           
            conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
            my_cursor = conn.cursor()

            
            hashed_input_pass = hash_password(user_pass)

            query = "SELECT * FROM user WHERE email=%s AND password=%s"
            value = (user_email, hashed_input_pass)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome, {row[1]}!", parent=self.root)
                
                self.root.destroy()
                
                
                main_root = Tk()
                app = HotelManagementSystem(main_root)
                main_root.mainloop()

            conn.close()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Database error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)


    def register_window(self):
        """Opens the Register window."""

        self.new_window = Toplevel(self.root)
        Register(self.new_window)

    
    def forgot_password_window(self):
      
        messagebox.showinfo("Forgot Password", "Implement password reset logic here (e.g., security question check).", parent=self.root)


# ================= Main Application Execution =================
if __name__ == "__main__":
    
    
    try:
        conn = mysql.connector.connect(host="localhost", username="root", password="Test@123", database="management")
        my_cursor = conn.cursor()
        
        # SQL to create the user table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fname VARCHAR(45) NOT NULL,
            lname VARCHAR(45) NOT NULL,
            contact VARCHAR(15) NOT NULL,
            email VARCHAR(45) UNIQUE NOT NULL,
            securityQ VARCHAR(100) NOT NULL,
            securityA VARCHAR(100) NOT NULL,
            password VARCHAR(256) NOT NULL 
        )
        """
        my_cursor.execute(create_table_query)
        conn.commit()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Database setup error: {err}")
        messagebox.showerror("Database Error", f"Could not connect or setup database table 'user'. Ensure MySQL is running and credentials are correct.\nError: {err}")

    root = Tk()
    obj = Login(root)
    root.mainloop()