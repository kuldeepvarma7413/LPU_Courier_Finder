from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from PIL import ImageTk, Image
import main_page as home
import signin
import service_provider
import mysql.connector

class Login_Page:  
    def loginDb(self):
        self.db=mysql.connector.connect(host="localhost",user='root',password='Kuldeep@7413',db='college')   
    def __init__(self, window):
        self.window = window
        self.window.geometry('1300x760')
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.title('Login - LPU Courier Finder')

        # ========================================================================
        # ============================fevicon=====================================
        # ========================================================================
        self.photoicon = PhotoImage(file = "images\\delivery-man.png")
        self.window.iconphoto(False, self.photoicon)
        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Welcome To LPU Courier Finder"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), fg='#fa8507', bd=5, relief=FLAT)
        self.heading.place(x=165, y=30, width=600, height=30)

        # ========================================================================
        # ============ Left Side Image ================================================
        # ========================================================================
        self.side_image = Image.open('images\\vector1.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo)
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo)
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=100)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", fg="black",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=250)


        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=590, y=335, width=258)

        self.username_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=590, y=359)
        # ===== Username icon =========
        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo)
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=590, y=416, width=233)

        self.password_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=590, y=440)
        # ======== Password icon ================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo)
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=830, y=420)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo)
        self.lgn_button_label.Image = photo
        self.lgn_button_label.place(x=560, y=455)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#fa8507', cursor='hand2', activebackground='#fa8507', fg='white', command=self.open_file)
        self.login.pack()
        self.login.place(x=20, y=10)
        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="#fa8507", relief=FLAT, borderwidth=0, cursor="hand2")
        self.forgot_button.place(x=630, y=510)
        
        # =========== Sign Up ==================================================
        self.sign_label = Label(self.lgn_frame, text='Account not created?', font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, fg='#4f4e4d')
        self.sign_label.place(x=570, y=560)


        self.sign_button = Button(self.lgn_frame,font=("yu gothic ui", 13, "bold underline"), text="Sign In",fg="#fa8507", cursor="hand2", borderwidth=0,  command=self.signup )
        self.sign_button.place(x=730, y=555)

        
        self.loginDb()

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=830, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=830, y=420)
        self.password_entry.config(show='*')

    def open_file(self):
        if self.username_entry.get() and self.password_entry.get():
            username=self.username_entry.get()
            password=self.password_entry.get()
            #data current window
            if(self.checking(self.window,username,password)):
                if(self.tpl[0][5]=='C'):
                    home.details(self.window)
                elif(self.tpl[0][5]=='S'):
                    for widgets in self.lgn_frame.winfo_children():
                        widgets.destroy()
                    service_provider.service(self.window)
                else:
                    messagebox.showerror('Login Error', 'Username or Password is wrong!')
        else:
            messagebox.showerror('Login Error', 'Enter username and password')
    def signup(self):
        signin.SignUp(self.window)

    def loginUser(self,userName,password):
        try:
            queryy='''select * from curiour_details 
            where userName='{0}' and password='{1}';'''.format(userName,password)
            cursr=self.db.cursor()
            cursr.execute(queryy)
            self.tpl=cursr.fetchall()
            return True
        except:
            messagebox.ERROR('Database error','Failed to login the database.')
            return False
            
    def checking(self,window,username,password):
        try:
            if self.loginUser(username,password):
                return True
            else:
                return False
        except :
            messagebox.ERROR('Database error','Failed to login the database.')
            raise
        
