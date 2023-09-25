from tkinter import *
from PIL import Image,ImageTk
import sqlite3
import tkinter.messagebox as messagebox
s_root = Tk()
s_root.geometry('600x600')

Label(s_root, text="Bus Booking Reservation System", font=('Times New Roman', 20)).pack()
Label(s_root, text="Developed as a part of courses: \n Advanced Programming Lab and \n DBMS Lab", font=('Times New Roman', 20)).pack()
Label(s_root, text="Developed By: Vaibhav Rajpoot \n", font=('Times New Roman', 20)).pack()
Label(s_root, text="Project Supervisors: \n Dr. Mahesh Kumar and Mr. Nileshkumar R. Patel", font=('Times New Roman', 15)).pack()
s_root.bind(("<Key>"), lambda event: s_root.destroy())
s_root.mainloop()
conn=sqlite3.connect('Form.db')
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS routedetails(rid INTEGER PRIMARY KEY,stationname TEXT,stationid INTEGER);")
cur.execute("CREATE TABLE IF NOT EXISTS busdetails(bid INTEGER PRIMARY KEY,type TEXT,capacity INTEGER,fare INTEGER,o_id INTEGER,r_id INTEGER,FOREIGN KEY(o_id) REFERENCES operatordetails(odid),FOREIGN KEY(r_id) REFERENCES routedetails(rid));")
cur.execute("CREATE TABLE IF NOT EXISTS runningtime(runningdate TEXT,seatavailable INTEGER,b_id INTEGER,FOREIGN KEY(b_id) REFERENCES busdetails(bid));")
cur.execute("CREATE TABLE IF NOT EXISTS operatordetail(odid INTEGER PRIMARY KEY,nameop TEXT,addressop TEXT,phoneop INTEGER,email TEXT);")

def fun():
    root=Tk()
    root.geometry('600x600')
    root.configure(background='#F3F3F3')
    root.title('Bus Booking Reservation system ')
    global img1
    head_frame=Frame(root, width=400, height=180)
    head_frame.pack()
    head_frame.place(anchor='center',relx=0.5, rely=0.17)
    img = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
    panel = Label(head_frame, image = img)
    panel.place(x=130,y=20)
    labeltx1= Label(root,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
    # "New window for booking seats"

    def seatbooking():
        root.destroy()
        rroot6=Tk()
        rroot6.geometry('600x900')
        rroot6.configure(background='#F3F3F3')
        rroot6.title('Bus booking Reservation system ')
        
        img1 = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
        panel = Label(rroot6, image = img1)
        panel.place(x=130,y=20)
        labeltx2= Label(rroot6,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
        labeltx2= Label(rroot6,text="Enter Journey Details",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
        labelname= Label(rroot6,text="To",fg='black').place(x=50,y=300)
        labeladd= Label(rroot6,text="From",fg='black').place(x=290,y=300)
        labelph= Label(rroot6,text="Date",fg='black').place(x=50,y=340)
        from1=StringVar()
        date8=StringVar()
        entryto=Entry(rroot6).place(x=90,y=300)
        entryfrom=Entry(rroot6,textvar=from1).place(x=360,y=300)
        entrydate=Entry(rroot6,textvar=date8).place(x=120,y=340)
        def seatbookingback():
            rroot6.destroy()
            fun()
        backbutton=Button(rroot6,text="Home",command=seatbookingback).place(x=320,y=340)
        def checkavailable():
                
            cur.execute("SELECT rid FROM routedetails WHERE stationname=?",(from1.get(),))
            rrid=cur.fetchall()
            print (rrid)
            

            cur.execute("SELECT b_id FROM runningtime WHERE runningdate=(?)",(date8.get(),))
            bbid=cur.fetchall()
            
            print(bbid)
            
            tuple_of_tuples=()
            for x in bbid:
                tuple_of_tuples+=tuple(x)
            print(tuple_of_tuples)
            alist=list(tuple_of_tuples)
            print(alist)


            cur.execute("SELECT * FROM busdetails WHERE bid IN (?)",alist)
            busdate=cur.fetchall()
            print(busdate)
            showbus= Label(rroot6,text="Available Buses",fg='#000000',bg="#FFF",font=("Verdana","20")).place(x=120,y=400)
            ii=450
            
            for data in busdate:
                
                for da in range(len(data)):
                    aa=Label(rroot6,text=data[da],fg='#000000',bg="#FFF",width=7,font=("Verdana","10"),anchor='s').grid(row=ii,column=da+350)
                
                
                    
                ii=ii+1
            
                

            
            

        addbutton=Button(rroot6,text = "Show Bus",command=checkavailable).place( x=420,y=340)
    btnadbus = Button(root, text = 'Seat Booking',command = seatbooking).place(x=80,y=300)


    # "New window for checking booked seats"
    def checkbookesseats():

        root.destroy()
        rroot5=Tk()
        rroot5.geometry('600x600')       
        global img1
        rroot5.configure(background='#F3F3F3')
        rroot5.title('Bus booking Reservation system ')
        head_frame1=Frame(rroot5, width=400, height=180)
        head_frame1.pack()
        head_frame1.place(anchor='center',relx=0.5, rely=0.17)
        img1= ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
        panel = Label(head_frame1, image = img1)
        panel.place(x=130,y=20)
        labeltx2= Label(rroot5,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
        labeltx2= Label(rroot5,text="Check Booked Seats",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
        labelname= Label(rroot5,text="Enter your number",fg='black').place(x=150,y=340)
        mobilenum=Entry(rroot5).place(x=300,y=340)


    btnbseat = Button(root, text = 'Check Booked Seat',command = checkbookesseats).place(x=240,y=300)
    
    # "New window for adding bus details"
    def sec():
        root.destroy()
        rroot=Tk()
        rroot.geometry('600x600')
        global img1
        rroot.configure(background='#F3F3F3')
        rroot.title('Bus booking Reservation system ')
        head_frame1=Frame(rroot, width=400, height=180)
        head_frame1.pack()
        head_frame1.place(anchor='center',relx=0.5, rely=0.17)
        img1 = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
        panel = Label(head_frame1, image = img1)
        panel.place(x=130,y=20)
        labeltx2= Label(rroot,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
        labeltx2= Label(rroot,text="Add new details to database",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
        
        # """"""window for the operator details inside bus details"""""""
        def operatordetailss():
            # defining variables 
            global img1

            rroot.destroy()
            rroot1=Tk()
            rroot1.geometry('600x600')
            rroot1.configure(background='#F3F3F3')
            rroot1.title('Bus booking Reservation system ')
            head_frame1=Frame(rroot1, width=400, height=180)
            head_frame1.pack()
            head_frame1.place(anchor='center',relx=0.5, rely=0.17)
            img1 = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
            panel = Label(head_frame1, image = img1)
            panel.place(x=130,y=20)
            labeltx2= Label(rroot1,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
            labeltx2= Label(rroot1,text="Add bus operator details",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
            labelid= Label(rroot1,text="Operator id",fg='black').place(x=150,y=300)
            labelname= Label(rroot1,text="Name",fg='black').place(x=150,y=340)
            labeladd= Label(rroot1,text="Address",fg='black').place(x=150,y=380)
            labelph= Label(rroot1,text="Phone",fg='black').place(x=150,y=420)
            labelem= Label(rroot1,text="Email",fg='black').place(x=150,y=460)
            oid0=IntVar()
            name0=StringVar()
            address0=StringVar()
            phone0=IntVar()
            email0=StringVar()
            entryid=Entry(rroot1,textvar=oid0).place(x=250,y=300)
            entryname=Entry(rroot1,textvar=name0).place(x=250,y=340)
            entryadd=Entry(rroot1,textvar=address0).place(x=250,y=380)
            entryph=Entry(rroot1,textvar=phone0).place(x=250,y=420)
            entryem=Entry(rroot1,textvar=email0).place(x=250,y=460)
            def operatordetailsdestroy():
                rroot1.destroy()
                fun()
            homebutton=Button(rroot1,text = "Home",command=operatordetailsdestroy).place( x=200,y =500)
            def addingodetails():
                
                cur.execute("INSERT INTO operatordetail VALUES(?,?,?,?,?)",(oid0.get(),name0.get(),address0.get(),phone0.get(),email0.get()))
                conn.commit()
                messagebox.showinfo("Info", "Record Added")
            addbutton=Button(rroot1,text = "Add",command=addingodetails).place( x=300,y =500)
        btnoperator = Button(rroot, text = 'New operator',command = operatordetailss).place(x=50,y=300)

        # """"""""window for the new bus inside bus details""""""""
        def newbus():
            rroot.destroy()
            rroot2=Tk()
            rroot2.geometry('600x600')
            rroot2.configure(background='#F3F3F3')
            # defining variables
            bid2=IntVar()
            btype2=StringVar()
            capacity2=IntVar()
            fare2=IntVar()
            o_id3=IntVar()
            r_id3=IntVar()
            global img1
            rroot2.title('Bus booking Reservation system ')
            head_frame1=Frame(rroot2, width=400, height=180)
            head_frame1.pack()
            head_frame1.place(anchor='center',relx=0.5, rely=0.17)
            img1 = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
            panel = Label(head_frame1, image = img1)
            panel.place(x=130,y=20)
            labeltx2= Label(rroot2,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
            labeltx2= Label(rroot2,text="Add bus operator details",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
            labelid2= Label(rroot2,text="Bus id",fg='black').place(x=150,y=300)
            labeltype2= Label(rroot2,text="Bus Type",fg='black').place(x=150,y=340)
            labelcapa= Label(rroot2,text="Capacity",fg='black').place(x=150,y=380)
            Fares= Label(rroot2,text="Fare Rs",fg='black').place(x=150,y=420)
            operatorid= Label(rroot2,text="Operator id",fg='black').place(x=150,y=460)
            routeid= Label(rroot2,text="Route id",fg='black').place(x=150,y=500)
            entryid2=Entry(rroot2,textvar=bid2).place(x=250,y=300)
            
            btype2.set("BUS TYPE")
            drop= OptionMenu(rroot2, btype2,"AC 2X2", "AC 3X2","NON AC 2X2","NON AC 3X2","AC SLEEPER 2X1","NON-AC SLEEPER 2X1").place(x=250,y=340)
            entrycapa=Entry(rroot2,textvar=capacity2).place(x=250,y=380)
            entryfare=Entry(rroot2,textvar=fare2).place(x=250,y=420)
            entryop=Entry(rroot2,textvar=o_id3).place(x=250,y=460)
            entryri=Entry(rroot2,textvar=r_id3).place(x=250,y=500)
            def newbusdestroy():
                rroot2.destroy()
                fun()
            homebutton=Button(rroot2,text = "Home",command=newbusdestroy).place( x=200,y =540)
            def addingnewdetails1():
                cur.execute("INSERT INTO operatordetail VALUES(?,?,?,?,?)",(bid2.get(),btype2.get(),btype2.get(),bid2.get(),btype2.get()))
               
                cur.execute("INSERT INTO busdetails VALUES(?,?,?,?,?,?)",(bid2.get(),btype2.get(),capacity2.get(),fare2.get(),o_id3.get(),r_id3.get()))
                conn.commit()
                messagebox.showinfo("Info", "Record Added")
            addbutton=Button(rroot2,text = "Add",command=addingnewdetails1).place( x=300,y =540)

        btnb = Button(rroot, text = 'New Bus',command = newbus).place(x=200,y=300)

        # """"""""window for the new root inside bus details""""""""

        def newroute():
            rroot.destroy()
            rroot3=Tk()
            rroot3.geometry('600x600')
            rroot3.configure(background='#F3F3F3')
            rroot3.title('Bus booking Reservation system ')
            head_frame1=Frame(rroot3, width=400, height=180)
            head_frame1.pack()
            head_frame1.place(anchor='center',relx=0.5, rely=0.17)
            global img1
            img1 = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
            panel = Label(head_frame1, image = img1)
            panel.place(x=130,y=20)
            labeltx2= Label(rroot3,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
            labeltx2= Label(rroot3,text="Add bus route details",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
            routeid= Label(rroot3,text="Route id",fg='black').place(x=150,y=300)
            stationname= Label(rroot3,text="Station Name",fg='black').place(x=150,y=340)
            stationid= Label(rroot3,text="Station id",fg='black').place(x=150,y=380)
            rid4=IntVar()
            name4=StringVar()
            sid4=IntVar()
            entryid3=Entry(rroot3,textvar=rid4).place(x=250,y=300)
            entryname3=Entry(rroot3,textvar=name4).place(x=250,y=340)
            entrysid3=Entry(rroot3,textvar=sid4).place(x=250,y=380)
            def newroutedestroy():
                rroot3.destroy()
                fun()
            homebutton=Button(rroot3,text = "Home",command=newroutedestroy).place( x=200,y =420)
            def addingnewdetails2():
                cur.execute("INSERT INTO routedetails VALUES(?,?,?)",(rid4.get(),name4.get(),sid4.get()))
                
                conn.commit()
                messagebox.showinfo("Info", "Record Added")
            addbutton=Button(rroot3,text = "Add",command=addingnewdetails2).place( x=300,y =420)


        btnroute = Button(rroot, text = 'New Route',command = newroute).place(x=330,y=300)

        # """"""""window for the new run inside bus details""""""""

        def newrun():
            rroot.destroy()
            rroot4=Tk()
            rroot4.geometry('600x600')
            rroot4.configure(background='#F3F3F3')
            rroot4.title('Bus booking Reservation system ')
            head_frame1=Frame(rroot4, width=400, height=180)
            head_frame1.pack()
            global img1
            head_frame1.place(anchor='center',relx=0.5, rely=0.17)
            img1 = ImageTk.PhotoImage(Image.open("/home/vaibhav/Desktop/new/bus_img.png"))
            panel = Label(head_frame1, image = img1)
            panel.place(x=130,y=20)
            labeltx2= Label(rroot4,text="Online Bus Booking System",fg='#fff',bg="#66ffcc",font=("Verdana","20")).place(x=120,y=200)
            labeltx2= Label(rroot4,text="Add bus route details",fg='#fff',bg="#66ffcc",font=("Verdana","15")).place(x=140,y=250)
            routeid= Label(rroot4,text="Bus",fg='black').place(x=150,y=300)
            stationname= Label(rroot4,text="Running Date",fg='black').place(x=150,y=340)
            stationid= Label(rroot4,text="Seat Avalibilty",fg='black').place(x=150,y=380)
            rid5=IntVar()
            date5=StringVar()
            seat5=IntVar()
            entryid4=Entry(rroot4,textvar=rid5).place(x=250,y=300)
            entrydate4=Entry(rroot4,textvar=date5).place(x=250,y=340)
            entrysa4=Entry(rroot4,textvar=seat5).place(x=250,y=380)
            def newrrundestroy():
                rroot4.destroy()
                fun()
            homebutton=Button(rroot4,text = "Home",command=newrrundestroy).place( x=170,y =420)
            def addingnewdetails3():
                cur.execute("INSERT INTO runningtime VALUES(?,?,?)",(date5.get(),seat5.get(),rid5.get()))
                conn.commit()
                messagebox.showinfo("Info", "Record Added")
            addbutton=Button(rroot4,text = "Add",command=addingnewdetails3).place( x=250,y =420)
        btnnrun = Button(rroot, text = 'New Run',command = newrun).place(x=480,y=300)

    btnbusd = Button(root, text = 'Add Bus Details',command=sec).place(x=440,y=300)
    root.mainloop()
fun()


     
 
