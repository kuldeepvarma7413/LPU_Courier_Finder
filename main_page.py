from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image
import mysql.connector
import courier_details as found
import order_not_found as not_found


class details:
    def __init__(self, window):
        self.window = window
        #self.window.state('zoomed')
        # self.window.title('LPU Courier Finder')

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
        self.lgn_frame = Frame(self.window, bg='#FFFFFF', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "Enter Your Details Here"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#FFFFFF", fg='#fa8507', bd=5, relief=FLAT)
        self.heading.place(x=165, y=80, width=600, height=30)

        # ========================================================================
        # ============Order details label =============================================
        # ========================================================================
        self.order_details = Label(self.lgn_frame, text="Order Details", bg="#FFFFFF", fg="#fa8507",
                                    font=("yu gothic ui", 17, "bold"))
        self.order_details.place(x=400, y=150)

        # ========================================================================
        # ============================Order Id====================================
        # ========================================================================
        self.order_id = Label(self.lgn_frame, text="Order Id", bg="#FFFFFF", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.order_id.place(x=300, y=280)

        self.order_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.order_entry.place(x=375, y=280, width=258)

        self.order_entry.focus_set()

        self.order_line = Canvas(self.lgn_frame, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.order_line.place(x=375, y=302)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        
        self.find_btn = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.find_btn)
        self.find_button = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.find_button.Image = photo
        self.find_button.place(x=330, y=415)
        self.login = Button(self.find_button, text='Find', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#fa8507', cursor='hand2', activebackground='#fa8507', fg='white', command=self.open_file)
        self.login.pack()
        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.mo_label = Label(self.lgn_frame, text="Mobile No.", bg="#FFFFFF", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.mo_label.place(x=300, y=330)

        self.mo_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"))
        self.mo_entry.place(x=390, y=330, width=233)

        self.mo_line = Canvas(self.lgn_frame, width=245, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.mo_line.place(x=390, y=352)

    def loginDb(self):
        self.db=mysql.connector.connect(host="localhost",user='root',password='Kuldeep@7413',db='college')   

    def open_file(self):
        self.loginDb()
        #take values
        order_id=self.order_entry.get()
        mo_no=self.mo_entry.get()

        try:
            query='''select * from courier_data where order_id={0} and phone_no={1};'''.format(order_id,mo_no)
            cursr=self.db.cursor()
            cursr.execute(query)
            tpl=cursr.fetchall()
            found.courier_details(self.window,tpl)
        except:
            #messagebox.showinfo('Order not found','Order not found!\nTry again after sometime.')
            not_found.courier_details(self.window)


        
