from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win  # Make sure 'customer.py' is in the same folder
from room import Roombooking
from details import DetailsRoom


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="white")

        # ================= HEADER IMAGE ====================
        img1 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\cover3.png")
        img1 = img1.resize((1550, 140), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ================= LOGO LEFT ====================
        img2 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\logo2.png")
        img2 = img2.resize((230, 140), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_logo = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE, bg="#7F5628")
        lbl_logo.place(x=0, y=0, width=230, height=140)

        # ================= TITLE ====================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM",
                          font=("times new roman", 40, "bold"),
                          bg="#7F5628", fg="#FFFFFF", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ================= LEFT MENU FRAME ====================
        menu_frame = Frame(self.root, bd=4, relief=RIDGE, bg="#FFFFFF")
        menu_frame.place(x=0, y=190, width=230, height=610)

        lbl_menu = Label(menu_frame, text="MENU", 
                         font=("times new roman", 20, "bold"),
                         bg="#7F5628", fg="#FFFFFF", bd=2, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230, height=50)

        # ================= BUTTON FRAME ====================
        btn_frame = Frame(menu_frame, bg="#FFFFFF")
        btn_frame.place(x=0, y=50, width=230, height=250)

        button_color = "#7F5628"  # Main background color
        fg_color = "#FFFFFF"  # Text color

        Button(btn_frame, text="CUSTOMER", command=self.cust_details, font=("times new roman", 14, "bold"),
               bg=button_color, fg=fg_color, bd=0).place(x=0, y=5, width=230, height=40)

        Button(btn_frame, text="BOOKING",command=self.Roombooking, font=("times new roman", 14, "bold"),
               bg=button_color, fg=fg_color, bd=0).place(x=0, y=50, width=230, height=40)

        Button(btn_frame, text="DETAILS",command=self.details_room ,font=("times new roman", 14, "bold"),
               bg=button_color, fg=fg_color, bd=0).place(x=0, y=95, width=230, height=40)

        Button(btn_frame, text="REPORT", font=("times new roman", 14, "bold"),
               bg=button_color, fg=fg_color, bd=0).place(x=0, y=140, width=230, height=40)

        Button(btn_frame, text="LOGOUT",command=self.logout, font=("times new roman", 14, "bold"),
               bg=button_color, fg=fg_color, bd=0).place(x=0, y=185, width=230, height=40)

        # ================= LEFT SIDE IMAGES ====================
        img4 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\images (1).jpg")
        img4 = img4.resize((225, 200), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE).place(x=0, y=460, width=230, height=210)

        img5 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\hotel8.jpg")
        img5 = img5.resize((230, 200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE).place(x=0, y=640, width=230, height=190)

        # ================= MAIN RIGHT SIDE LARGE IMAGE ====================
        img3 = Image.open(r"C:\Users\sajani nimeshika\Desktop\Hotel management system\images\AI Eraser_image.png")
        img3 = img3.resize((1320, 610), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE).place(x=230, y=190, width=1320, height=610)

    def cust_details(self):
        """ Opens the Customer Details Window """
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)  


    def Roombooking(self):
        """ Opens the Customer Details Window """
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window) 

    def details_room(self):
        """ Opens the Customer Details Window """
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window) 
      
    def logout(self):
        self.root.destroy()












if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()