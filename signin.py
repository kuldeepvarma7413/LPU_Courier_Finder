from sqlite3 import DatabaseError
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
from PIL import ImageTk, Image
import main_page as home
import LoginPage as logging
import mysql.connector

class SignUp:
    def __init__(self,win):
        self.loginDb()
        self.window = win
        self.window.geometry('1300x760')
        self.window.resizable(0, 0)
        self.window.title('Sign In - LPU Courier Finder')

        # ============================fevicon=====================================
        self.photoicon = PhotoImage(file = "images\\delivery-man.png")
        self.window.iconphoto(False, self.photoicon)
        # ============================background image============================
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ================================== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#FFFFFF', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ==============================LPU COURIER LABEL=========================
        txt = "Sign In To LPU Courier Finder"
        heading = Label(self.lgn_frame, text=txt, font=('yu gothic ui', 25, "bold"), bg="#FFFFFF", fg='#fa8507', bd=5, relief=FLAT)
        heading.place(x=165, y=50, width=600, height=50)

        # ============================Full Name===================================
        name_label = Label(self.lgn_frame, text="Full Name", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        name_label.place(x=150, y=140)

        self.name_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"))
        self.name_entry.place(x=190, y=175, width=258)

        name_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        name_line.place(x=190, y=199)
        # =============================== Username icon ===========================
        name_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(name_icon)
        name_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        name_icon_label.image = photo
        name_icon_label.place(x=150, y=172)

        # ============================Registration No.=============================

        reg_label = Label(self.lgn_frame, text="Registration No.", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        reg_label.place(x=500, y=140)

        self.reg_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"))
        self.reg_entry.place(x=540, y=175, width=258)

        reg_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        reg_line.place(x=540, y=199)
        # ======================Username icon =====================================
        reg_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(reg_icon)
        reg_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        reg_icon_label.image = photo
        reg_icon_label.place(x=500, y=172)

        # ============================Type of user===================================
        self.var1=IntVar()
        self.var2=IntVar()
        self.t1 = Checkbutton(win, text="Customer", variable=self.var1, onvalue=1, offvalue=0, command=self.discheck2)
        self.t1.pack()
        self.t1.place(x=700,y=400)
        self.t1.select()
        self.t2 = Checkbutton(win, text="Service Provider", variable=self.var2, onvalue=1, offvalue=0, command=self.discheck1)
        self.t2.pack()
        self.t2.place(x=800, y=400)

        # =================================Username==================================
        username_label = Label(self.lgn_frame, text="Username", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        username_label.place(x=150, y=220)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"))
        self.username_entry.place(x=190, y=255, width=258)

        username_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        username_line.place(x=190, y=279)
        # ====================== Username icon ======================================
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        username_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        username_icon_label.image = photo
        username_icon_label.place(x=150, y=252)

        # ============================Mobile no======================================
        mo_label = Label(self.lgn_frame, text="Phone Number", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold"))
        mo_label.place(x=500, y=210)

        self.mo_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"))
        self.mo_entry.place(x=540, y=258, width=258)

        mo_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        mo_line.place(x=540, y=278)
        # ================================= Username icon ===============================
        mo_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(mo_icon)
        mo_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        mo_icon_label.image = photo
        mo_icon_label.place(x=500, y=250)

        # ==================================== password =================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#FFFFFF", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=150, y=300)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=190, y=336, width=233)

        self.password_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=190, y=360)
        # ================================= Password icon ==================================
        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=150, y=334)
        # ================================= show/hide password =============================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=430, y=340)

        # ============================fevicon=====================================
        photoicon = PhotoImage(file = "images\\delivery-man.png")
        self.window.iconphoto(False, photoicon)


        # ================ show/hide password ====================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=430, y=340)

        # ============================sign up button================================

        sign_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(sign_button)
        sign_button_label = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        sign_button_label.Image = photo
        sign_button_label.place(x=330, y=405)
        signup = Button(sign_button_label, text='SIGN UP', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#fa8507', cursor='hand2', activebackground='#fa8507', fg='white', command=self.open_file)
        signup.pack()
        signup.place(x=20, y=10)

        # ========================= log in ==========================================
        sign_label = Label(self.lgn_frame, text='Already have an account?', font=("yu gothic ui", 11, "bold"),relief=FLAT, borderwidth=0, background="#FFFFFF", fg='#4f4e4d')
        sign_label.place(x=360, y=530)


        sign_button = Button(self.lgn_frame,font=("yu gothic ui", 13, "bold underline"), text="Log In", bg='#4f4e4d',fg="#fa8507", cursor="hand2", borderwidth=0, background="#FFFFFF", activebackground="#FFFFFF", command=self.openloginpage)
        sign_button.place(x=540, y=525)

    def show(self):
        hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT, activebackground="white" , borderwidth=0, background="white", cursor="hand2")
        hide_button.place(x=430, y=340)
        self.password_entry.config(show='')

    def hide(self):
        show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT, activebackground="white" , borderwidth=0, background="white", cursor="hand2")
        show_button.place(x=430, y=340)
        self.password_entry.config(show='*')
    
    def discheck1(self):
        self.t1.deselect()
    def discheck2(self):
        self.t2.deselect()
    def openloginpage(self):
        logging.Login_Page(self.window)

    def open_file(self):
        #data current window
        try:
            username=self.username_entry.get()
            password=self.password_entry.get()
            fullname=self.name_entry.get()
            Mobile_no=self.mo_entry.get()
            reg_no=int(self.reg_entry.get())
            if self.var2.get():
                typeofuser='S'
            else:
                typeofuser='C'
            self.insertRecord(fullname,username,password,reg_no,Mobile_no,typeofuser)
            home.details(self.window)
        except DatabaseError:
            messagebox.showerror('record error','User already exist / database error!')
        except:
            messagebox.showerror('record error','Incomplete details.')

    #database
    def loginDb(self):
        self.db=mysql.connector.connect(host="localhost",user='root',password='Kuldeep@7413',db='college')
        
    def insertRecord(self,fullName,userName,password,regNo,phoneNo,type):
        createTablee='''
        create table if not exists curiour_details(
        fullName varchar(50) not null,userName varchar(25) primary key,password varchar(25) not null,regNo int unique not null,phoneNo varchar(10) not null,type char(1) not null
        );
        '''
        self.db.cursor().execute(createTablee)
        queryInsert='''
        insert into curiour_details values('{0}','{1}','{2}',{3},'{4}','{5}')'''.format(fullName,userName,password,regNo,phoneNo,type)
        try:
            self.db.cursor().execute(queryInsert)
            self.db.commit()
        except:
            raise DatabaseError('User already exist or database error!')

