from asyncio.windows_events import NULL
from distutils.cmd import Command
from sqlite3 import DatabaseError
from tkinter import *
from tkinter import messagebox
from turtle import color, left
from PIL import ImageTk, Image
import mysql.connector
import LoginPage

class service:
    def __init__(self,window):
        self.window = window
        self.window.geometry('1300x760')
        self.window.resizable(0, 0)
        #self.window.state('zoomed')
        self.window.title('Dashboard - LPU Courier Finder')

        #=========== Login Database ================
        self.db=mysql.connector.connect(host="localhost",user='root',password='Kuldeep@7413',db='college')

        # ========================================================================
        # ============================fevicon=====================================
        # ========================================================================
        self.photoicon = PhotoImage(file = "images\\delivery-man.png")
        self.window.iconphoto(False, self.photoicon)
        # ========================================================================
        # ============================ Header ====================================
        # ========================================================================

        self.header=Frame(self.window,bg='#1c355e')
        self.header.place(x=300, y=0, width=1000, height=60)

        self.logout_text=Button(self.header,text='Log out', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white', cursor='hand2', activebackground='#32cf8e', command=self.Logout)
        self.logout_text.place(x=780,y=15,width=150)

        # ========================================================================
        # ============================ Sidebar ===================================
        # ========================================================================
        self.sidebar=Frame(self.window,bg='#ffffff')
        self.sidebar.place(x=0,y=0,width=300,height=750)


        #===================== logo ==================
        self.logoImage=Image.open('images\\hyy.png')
        photo=ImageTk.PhotoImage(self.logoImage)
        self.logo=Label(self.sidebar, image=photo, bg='#ffffff')
        self.logo.image=photo;
        self.logo.place(x=70,y=80)

        #=============== User Details ==================
        self.heading=Label(self.sidebar,text='Kul Deep Varma', font=("",15,"bold"), fg='black', bg='#eff5f6')
        self.heading.place(x=70, y=250)

        self.heading2=Button(self.sidebar,text='Add Products', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white', cursor='hand2', activebackground='#1c355e', command=self.adding)
        self.heading2.place(x=0, y=400, width=300, height=45)

        self.heading2=Button(self.sidebar,text='Search Products', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white', cursor='hand2', activebackground='#1c355e', command=self.frame2)
        self.heading2.place(x=0, y=450, width=300, height=45)

        # ========================================================================
        # ============================ Body ===================================
        # ========================================================================

        
        #==================== Frame 2 ================
        self.bodyFrame2=Frame(self.window,bg='#ffffff')
        self.bodyFrame2.place(x=328,y=495, width=940, height=220)

        #========= details of stock ===================
        self.refresh_button = Button(self.bodyFrame2,text='Refresh', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white', cursor='hand2', activebackground='white', command=self.total_data_info)
        self.refresh_button.place(x=750,y=15, width=70)

        self.total_info=Label(self.bodyFrame2, text='Details About Stock', fg='black', bg='#ffffff',font=("yu gothic ui ", 15, "bold"))
        self.total_info.place(x=350, y=20)


        self.frame2()

    # Functions

    def frame2(self):
        #================ Dashboard =================
        self.heading=Label(self.window,text='Dashboard', font=("",13,"bold"), fg='black')
        self.heading.place(x=325, y=70)

        #==================== Frame 1 ================
        self.bodyFrame1=Frame(self.window,bg='#ffffff')
        self.bodyFrame1.place(x=328,y=110, width=940, height=350)

        #==================== Search ================
        self.search_label=Label(self.bodyFrame1, text='Search Here', fg='black', bg='#eff5f6',font=("yu gothic ui ", 13, "bold"))
        self.search_label.place(x=20, y=20)

        self.search_entry=Entry(self.bodyFrame1, highlightthickness=0,width=540 , relief=FLAT, bg="#FFFFFF", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.search_entry.place(x=170, y=20)
        self.search_entry.focus_set()

        self.search_canvas = Canvas(self.bodyFrame1, width=540, height=0.5, bg="#bdb9b1", highlightthickness=0)
        self.search_canvas.place(x=170, y=40)

        self.search_button = Button(self.bodyFrame1,text='Search', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white', cursor='hand2', activebackground='white', command=self.search)
        self.search_button.place(x=750,y=15, width=150)

    def total_data_info(self):
        queryy='''select count(*) from courier_data where status='In Stock' ;'''
        self.cursr=self.db.cursor()
        self.cursr.execute(queryy)
        tpl=self.cursr.fetchone()

        total_stock_data='''Total items left in stock : {0} '''.format(tpl[0])

        self.total_info=Label(self.bodyFrame2, text=total_stock_data, fg='black', bg='#ffffff',font=("yu gothic ui ", 13, "bold"))
        self.total_info.place(x=100, y=70)

        queryy='''select count(*) from courier_data;'''
        self.cursr.execute(queryy)
        tpl1=self.cursr.fetchone()
        total_data='''Total items arrived in Branch : {0}'''.format(tpl1[0])
        self.total_info=Label(self.bodyFrame2, text=total_data, fg='black', bg='#ffffff',font=("yu gothic ui ", 13, "bold"))
        self.total_info.place(x=100, y=100)
    
    def search(self):
        order_id=self.search_entry.get()

        if not (self.search_entry.get()):
            messagebox.showinfo('Invalid Input','Please Enter product id.')
        else:
            try:
                queryy='''select * from courier_data where order_id LIKE '%{0}'; '''.format(order_id)
                self.cursr=self.db.cursor()
                self.cursr.execute(queryy)
                tpl=self.cursr.fetchall()

                name=tpl[0][0]
                self.orderid=tpl[0][1]
                address=tpl[0][2]
                phone_no=tpl[0][3]
                payment=tpl[0][4]
                status=tpl[0][5]

                self.info='''Name : {0}\n\nOrder Id : {1}\n\nAddress : {2}\n\nMobile No. : {3}\n\nPayment : {4}'''.format(name,self.orderid,address,phone_no,payment)

                info2='''Status : {0}'''.format(status)


                self.showdata_label1=Label(self.bodyFrame1,text=self.info, fg='black', bg='#ffffff',font=("yu gothic ui ", 13, "bold"),justify=LEFT)
                self.showdata_label1.place(x=30, y=80)
                
                self.showdata_label2=Label(self.bodyFrame1,text=info2, fg='black', bg='#ffffff',font=("yu gothic ui ", 13, "bold"),justify=LEFT)
                self.showdata_label2.place(x=500, y=80)

                self.var1=IntVar()
                self.status_pending = Checkbutton(self.bodyFrame1, text="Delivered", variable=self.var1, onvalue=1, offvalue=0).place(x=330,y=290)

                self.submit = Button(self.bodyFrame1,text='Submit', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white', cursor='hand2', command=self.change).place(x=450,y=287,width=100)

                #self.Submit = Button(self.bodyFrame1,text='Submit', bg='#32cf8e', font=("",13,"bold"),bd=0,fg='white', cursor='hand2',command=self.change(orderid)).place(x=700, y=290)
                
            except:
                messagebox.showinfo('Item Not Found','No product is in record related to this id.')

    def change(self):
        #status of product change
        if(self.var1.get()):
            queryy='''update courier_data set status='Delivered' where order_id={0};'''.format(self.orderid)
            self.cursr=self.db.cursor()
            self.cursr.execute(queryy)
            self.db.commit()
            messagebox.showinfo('Delivery status','Order delivered sucessfully.')
        else:
            pass

    def Logout(self):
        LoginPage.Login_Page(self.window)

    def discheck1(self):
        self.status_pending.deselect()

    def discheck2(self):
        self.status_done.deselect()

    def discheck11(self):
        self.status_instock.deselect()

    def discheck22(self):
        self.status_delivered.deselect()

    def adding(self):
        for widget in self.bodyFrame1.winfo_children():
           widget.destroy()
        
        #taking details of new product

        self.name_label = Label(self.bodyFrame1, text="Name", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold")).place(x=50, y=50)
        self.orderid_label = Label(self.bodyFrame1, text="Order Id", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold")).place(x=350, y=50)
        self.address_label = Label(self.bodyFrame1, text="Address", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold")).place(x=650, y=50)
        self.mo_no_label = Label(self.bodyFrame1, text="Mo. No.", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold")).place(x=50, y=150)
        self.payment_label = Label(self.bodyFrame1, text="Payment Status", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold")).place(x=350, y=150)
        self.status_label = Label(self.bodyFrame1, text="Delivery Status", bg="#FFFFFF", fg="#4f4e4d",font=("yu gothic ui", 13, "bold")).place(x=600, y=150)

        #payment status
        self.var1=IntVar()
        self.var2=IntVar()
        self.status_pending = Checkbutton(self.bodyFrame1, text="Pending", variable=self.var1, onvalue=1, offvalue=0, command=self.discheck2)
        self.status_pending.pack()
        self.status_pending.place(x=350,y=200)
        self.status_pending.select()
        self.status_done = Checkbutton(self.bodyFrame1, text="Done", variable=self.var2, onvalue=1, offvalue=0, command=self.discheck1)
        self.status_done.pack()
        self.status_done.place(x=450, y=200)

        #delivery status
        self.var3=IntVar()
        self.var4=IntVar()
        self.status_instock = Checkbutton(self.bodyFrame1, text="In Stock", variable=self.var3, onvalue=1, offvalue=0, command=self.discheck22)
        self.status_instock.pack()
        self.status_instock.place(x=600,y=200)
        self.status_instock.select()
        self.status_delivered = Checkbutton(self.bodyFrame1, text="Delivered", variable=self.var4, onvalue=1, offvalue=0, command=self.discheck11)
        self.status_delivered.pack()
        self.status_delivered.place(x=700, y=200)

        #entries
        self.name_entry = Entry(self.bodyFrame1, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",font=("yu gothic ui", 12, "bold"))
        self.name_entry.pack()
        self.name_entry.place(x=55, y=85, width=258)
        self.orderid_entry = Entry(self.bodyFrame1, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",font=("yu gothic ui", 12, "bold"))
        self.orderid_entry.pack()
        self.orderid_entry.place(x=355, y=85, width=258)
        self.address_entry = Entry(self.bodyFrame1, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",font=("yu gothic ui", 12, "bold"))
        self.address_entry.pack()
        self.address_entry.place(x=655, y=85, width=258)
        self.mo_no_entry = Entry(self.bodyFrame1, highlightthickness=0, relief=FLAT, bg="#FFFFFF", fg="#6b6a69",font=("yu gothic ui", 12, "bold"))
        self.mo_no_entry.pack()
        self.mo_no_entry.place(x=55, y=185, width=258)

        #focus on name
        self.name_entry.focus_set()

        #canvas
        self.name_line = Canvas(self.bodyFrame1, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0).place(x=55, y=110)
        self.orderid_line = Canvas(self.bodyFrame1, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0).place(x=355, y=110)
        self.address_line = Canvas(self.bodyFrame1, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0).place(x=655, y=110)
        self.mo_no_line = Canvas(self.bodyFrame1, width=261, height=2.0, bg="#bdb9b1", highlightthickness=0).place(x=55, y=210)

        #add button
        self.add_button = Button(self.bodyFrame1,text='Add', bg='#fa9c05', font=("",13,"bold"),bd=0,fg='white' , command=self.addproduct, relief=FLAT,activebackground="#1c355e", borderwidth=0, cursor="hand2")
        self.add_button.place(x=320, y=270, width=250)

    def addproduct(self):
        try:
            name=self.name_entry.get()
            orderid=self.orderid_entry.get()
            address=self.address_entry.get()
            mo_no=self.mo_no_entry.get()
            if self.var1.get():
                payment='Pending'
            else:
                payment='Done'

            if self.var3.get():
                delivery='In Stock'
            else:
                delivery='Delivered'
            self.insertRecord(name,orderid,address,mo_no,payment,delivery)
            messagebox.showinfo('Product info','Product added sucessfully.')
        except DatabaseError:
            messagebox.showerror('record error','Product already exist / database error!')
        except:
            messagebox.showerror('record error','Incomplete details.')

    def insertRecord(self,name,orderid,address,mo_no,payment,delivery):
        createTablee='''
        create table if not exists courier_data(
        Name varchar(50) not null,order_id varchar(30) primary key,address varchar(100) not null,phone_no int unique not null,payment varchar(10) not null,status char(10) not null
        );
        '''
        self.db.cursor().execute(createTablee)
        queryInsert='''insert into courier_data values('{0}','{1}','{2}','{3}','{4}','{5}')'''.format(name,orderid,address,mo_no,payment,delivery)
        try:
            self.db.cursor().execute(queryInsert)
            self.db.commit()
        except:
            raise DatabaseError('User already exist or database error!')
