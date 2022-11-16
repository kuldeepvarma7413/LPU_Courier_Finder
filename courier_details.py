from tkinter import *
from tkinter import Tk
from PIL import ImageTk, Image
import main_page


class courier_details:
    def __init__(self, window,data):
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
        # ============Order details label =============================================
        # ========================================================================
        self.order_details = Label(self.lgn_frame, text="Product Found", bg="#FFFFFF", fg="#fa8507",
                                    font=("yu gothic ui", 17, "bold"))
        self.order_details.place(x=390, y=150)


        text1='Name : '+data[0][0]+'\nContact no. : '+data[0][3]+'\nAddress : '+data[0][1]

        self.print_details = Label(self.lgn_frame, text=text1, bg="#FFFFFF", fg="#fa8507",
                                    font=("yu gothic ui", 17, "bold"))
        self.print_details.place(x=350, y=150)

        
        self.find_btn = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.find_btn)

        self.login = Button(self.window, text='Print', font=("yu gothic ui", 13, "bold"), bd=0, bg='#fa8507', cursor='hand2', activebackground='#fa8507', fg='white', command=self.open_file)
        self.login.pack()
        self.login.place(x=500, y=500, width=100)

        self.back = Button(self.window, text='Home', font=("yu gothic ui", 13, "bold"), bd=0, bg='#fa8507', cursor='hand2', activebackground='#fa8507', fg='white', command=self.backing)
        self.back.pack()
        self.back.place(x=700, y=500, width=100)

    def open_file(self):
        pass
    def backing(self):
        main_page.details(self.window)
