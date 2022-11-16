from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image
import main_page


class courier_details:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1300x760')
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.title('LPU Courier Finder')

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
        self.txt = "Courier Details"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#FFFFFF", fg='#fa8507', bd=5, relief=FLAT)
        self.heading.place(x=165, y=80, width=600, height=30)

        # ========================================================================
        # ============sad ========================================================
        # ========================================================================

        self.find_btn = Image.open('images\\sad.png')
        photo = ImageTk.PhotoImage(self.find_btn)
        self.find_button = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.find_button.Image = photo
        self.find_button.place(x=370, y=160,width=200)

        # ========================================================================
        # ============Order details label =============================================
        # ========================================================================
        self.order_details = Label(self.lgn_frame, text="Product Not Found", bg="#FFFFFF", fg="red",
                                    font=("yu gothic ui", 17, "bold"))
        self.order_details.place(x=360, y=330)


        self.order_details = Label(self.lgn_frame, text="Wait for some days. May be your order is on the way to our branch.\nThank you for using LPU Courier Finder.\nStay safe and Healthy", bg="#FFFFFF", fg="#fa8507",
                                    font=("yu gothic ui", 13, "bold"))
        self.order_details.place(x=200, y=390)

        
        self.find_btn = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.find_btn)
        self.find_button = Label(self.lgn_frame, image=photo, bg='#FFFFFF')
        self.find_button.Image = photo
        self.find_button.place(x=370, y=475,width=200)
        self.login = Button(self.find_button, text='Home', font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#fa8507', cursor='hand2', activebackground='#fa8507', fg='white', command=self.open_file)
        self.login.pack()
        self.login.place(x=-28, y=10)

    def open_file(self):
        main_page.details(self.window)
