def addevent():
    def submitadd():
        id = idval.get()
        event_name = event_nameval.get()
        co_name = co_nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        event_address = event_addressval.get()
        event_date = event_dateval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into eventdata2 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,event_name,co_name,mobile,email,event_address,event_date,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,event_name),parent=addroot)
            if(res==True):
                idval.set('')
                event_nameval.set('')
                co_name.set('')
                mobileval.set('')
                emailval.set('')
                event_addressval.set('')
                event_dateval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...', parent=addroot)
        strr = 'select * from eventdata2'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        eventtable.delete(*eventtable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            eventtable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x490+220+250')
    addroot.title('Event Management System')
    addroot.config(bg='skyblue')
  
    addroot.resizable(False,False)
    #--------------------------------------------------- Add eventLabels

    idlabel = Label(addroot, text='Enter Event Id: ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                    borderwidth=3, width=22, anchor='w')
    idlabel.place(x=10, y=10)

    event_namelabel = Label(addroot, text='Enter Event Name: ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                      borderwidth=3, width=22, anchor='w')
    event_namelabel.place(x=10, y=70)

    co_namelabel = Label(addroot, text='Event Co-ordinator Name: ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                     borderwidth=3, width=22, anchor='w')
    co_namelabel.place(x=10, y=130)

    mobilelabel = Label(addroot, text='Event Co-ordinator Mobile: ', bg='skyblue', font=('times', 12, 'bold'),
                        relief=GROOVE, borderwidth=3, width=22, anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(addroot, text='Enter Co-ordinator Email: ', bg='skyblue', font=('times', 12, 'bold'),
                       relief=GROOVE, borderwidth=3, width=22, anchor='w')
    emaillabel.place(x=10, y=250)

    event_addresslabel = Label(addroot, text='Enter Address: ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                        borderwidth=3, width=22, anchor='w')
    event_addresslabel.place(x=10, y=310)

    event_datelabel = Label(addroot, text='Enter Event Date: ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                       borderwidth=3, width=22, anchor='w')
    event_datelabel.place(x=10, y=370)


    ##----------------------------------------------------------- Add event Entry
    idval = StringVar()
    event_nameval = StringVar()
    co_nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    event_addressval = StringVar()
    event_dateval = StringVar()

    identry = Entry(addroot, font=('roman', 12, 'bold'), bd=5, textvariable=idval)
    identry.place(x=260, y=10)

    event_nameentry = Entry(addroot, font=('roman', 12, 'bold'), bd=5, textvariable=event_nameval)
    event_nameentry.place(x=260, y=70)

    co_nameentry = Entry(addroot, font=('roman', 12, 'bold'), bd=5, textvariable=co_nameval)
    co_nameentry.place(x=260, y=130)

    mobileentry = Entry(addroot, font=('roman', 12, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=260, y=190)

    emailentry = Entry(addroot, font=('roman', 12, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=260, y=250)

    event_addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=event_addressval)
    event_addressentry.place(x=250, y=310)

    event_dateentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=event_dateval)
    event_dateentry.place(x=250, y=370)
    ############------------------------- add button

    submitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='skyblue',
                       activeforeground='white',
                       bg='skyblue3', command=submitadd)
    submitbtn.place(x=150, y=420)

    addroot.mainloop()

def deleteevent():
    cc = eventtable.focus()
    content = eventtable.item(cc)
    pp = content['values'][0]
    strr = 'delete from eventdata2 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select * from eventdata2'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    eventtable.delete(*eventtable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7],i[8]]
        eventtable.insert('', END, values=vv)


def updateevent():
    def update():
        id = idval.get()
        event_name = event_nameval.get()
        co_name = co_nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        event_address = event_addressval.get()
        event_date = event_dateval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update eventdata2 set event_name=%s,co_name =%s,mobile=%s,email=%s,event_address=%s,event_date,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(event_name,co_name,mobile,email,event_address,event_date,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id), parent=updateroot)
        strr = 'select *from eventdata2'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        eventtable.delete(*eventtable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            eventtable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='skyblue')
   
    updateroot.resizable(False,False)
    #--------------------------------------------------- Add event Labels
    idlabel = Label(updateroot, text='Enter Event Id : ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                    borderwidth=3, width=22, anchor='w')
    idlabel.place(x=10, y=10)

    event_namelabel = Label(updateroot, text='Enter Event Name : ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                      borderwidth=3, width=22, anchor='w')
    event_namelabel.place(x=10, y=70)

    co_namelabel = Label(updateroot, text='Enter Co-ordinator Name: ', bg='skyblue', font=('times', 12, 'bold'),
                     relief=GROOVE, borderwidth=3, width=22, anchor='w')
    co_namelabel.place(x=10, y=130)

    mobilelabel = Label(updateroot, text='Enter Co-ordinator Mobile : ', bg='skyblue', font=('times', 12, 'bold'),
                        relief=GROOVE, borderwidth=3, width=22, anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(updateroot, text='Enter Co-ordinator Email : ', bg='skyblue', font=('times', 12, 'bold'),
                       relief=GROOVE, borderwidth=3, width=22, anchor='w')
    emaillabel.place(x=10, y=250)

    event_addresslabel = Label(updateroot,text='Enter Address : ',bg='skyblue',font=('times',12,'bold'),relief=GROOVE,borderwidth=3,width=22,anchor='w')
    event_addresslabel.place(x=10,y=310)

    event_datelabel = Label(updateroot, text='Enter Date : ', bg='skyblue', font=('times', 12, 'bold'),
                               relief=GROOVE, borderwidth=3, width=22, anchor='w')
    event_datelabel.place(x=10, y=370)

    timelabel = Label(updateroot, text='Event Time : ', bg='skyblue', font=('times', 12, 'bold'), relief=GROOVE,
                      borderwidth=3, width=22, anchor='w')
    timelabel.place(x=10, y=430)

    ##----------------------------------------------------------- Add event Entry
    idval = StringVar()
    event_nameval = StringVar()
    co_nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    event_addressval = StringVar()
    event_dateval = StringVar()
    #dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 12, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    event_nameentry = Entry(updateroot, font=('roman', 12, 'bold'), bd=5, textvariable=event_nameval)
    event_nameentry.place(x=250, y=70)

    co_nameentry = Entry(updateroot, font=('roman', 12, 'bold'), bd=5, textvariable=co_nameval)
    co_nameentry.place(x=250, y=130)

    mobileentry = Entry(updateroot, font=('roman', 12, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=190)

    emailentry = Entry(updateroot, font=('roman', 12, 'bold'), bd=5, textvariable=idval)
    emailentry.place(x=250, y=250)

    event_addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=event_addressval)
    event_addressentry.place(x=250,y=310)

    event_dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=event_dateval)
    event_dateentry.place(x=250,y=370)

    timeentry = Entry(updateroot, font=('roman', 12, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=430)

    ############------------------------- add button
    submitbtn = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='skyblue', command=update)
    submitbtn.place(x=150,y=500)
    cc = eventtable.focus()
    content = eventtable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        event_nameval.set(pp[1])
        co_nameval.set(pp[2])
        mobileval.set(pp[3])
        emailval.set(pp[4])
        event_addressval.set(pp[5])
        event_dateval.set(pp[6])
        timeval.set(pp[7])

    updateroot.mainloop()
def showevent():
    strr = 'select *from eventdata2'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    eventtable.delete(*eventtable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]]
        eventtable.insert('', END, values=vv)

def exportevent():
    ff = filedialog.asksaveasfilename()
    gg = eventtable.get_children()
    id,event_name,co_name,mobile,email,event_address,event_date,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = eventtable.item(i)
        pp = content['values']
        id.append(pp[0]),event_name.append(pp[1]),co_name,append(pp[2]),mobile.append(pp[3]),email.append(pp[4]),event_address.append(pp[5]),event_date.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Event_Name','Co-Ordinator_Name','Mobile','Email','Event_Address','Event_Date','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,event_name,co_name,mobile,email,event_address,event_date,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))


def exitsevent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


###################################################################################Connecttion of Database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database eventmanagementsystem2'
            mycursor.execute(strr)
            strr = 'use eventmanagementsystem2'
            mycursor.execute(strr)
            strr = 'create table eventdata2(id int,event_name varchar(20),co_name varchar(20),mobile varchar(12),email varchar(30),event_address varchar(100),event_date varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table eventdata2 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table eventdata2 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)

        except:
            strr = 'use eventmanagementsystem2'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
   
    dbroot.resizable(False,False)
    dbroot.config(bg='skyblue')
    #-------------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='skyblue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='skyblue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='skyblue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-------------------------------- Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='skyblue',bd=5,width=20,activebackground='skyblue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###########################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
##########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title('Event Management System')
root.config(bg='skyblue')
root.geometry('1174x700+200+50')
# root.iconbitmap('mana.ico')
root.resizable(False,False)
############################################################################################################  Frames
##---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=550)
frontlabel = Label(DataEntryFrame,text='--------------Welcome--------------',width=30,font=('arial',22,'italic bold'),bg='skyblue')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame, text='1. Add Event', width=25, font=('times', 20, 'bold'), bd=6, bg='skyblue',
                activebackground='skyblue3', relief=RIDGE,
                activeforeground='white', command=addevent)
addbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='2. Delete Event', width=25, font=('times', 20, 'bold'), bd=6, bg='skyblue',
                   activebackground='skyblue3', relief=RIDGE,
                   activeforeground='white', command=deleteevent)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='3. Update Event', width=25, font=('times', 20, 'bold'), bd=6, bg='skyblue',
                   activebackground='skyblue3', relief=RIDGE,
                   activeforeground='white', command=updateevent)
updatebtn.pack(side=TOP, expand=True)

showallbtn = Button(DataEntryFrame, text='4. Show All', width=25, font=('times', 20, 'bold'), bd=6, bg='skyblue',
                    activebackground='skyblue3', relief=RIDGE,
                    activeforeground='white', command=showevent)
showallbtn.pack(side=TOP, expand=True)

exportbtn = Button(DataEntryFrame, text='5. Export data', width=25, font=('times', 20, 'bold'), bd=6, bg='skyblue',
                   activebackground='skyblue3', relief=RIDGE,
                   activeforeground='white', command=exportevent)
exportbtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='6.  Exit', width=25, font=('times', 20, 'bold'), bd=6, bg='skyblue',
                 activebackground='skyblue3', relief=RIDGE,
                 activeforeground='white', command=exitsevent)
exitbtn.pack(side=TOP, expand=True)

##-----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='skyblue',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=550)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',15,'bold'),foreground='black')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
eventtable = Treeview(ShowDataFrame,columns=('Id','Event_Name','Co-Ordinator_Name','Mobile No','Email','Event_Address','Event_Date','Added Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=eventtable.xview)
scroll_y.config(command=eventtable.yview)
eventtable.heading('Id',text='Id')
eventtable.heading('Event_Name',text='Event_Name')
eventtable.heading('Co-Ordinator_Name',text='Co-Ordinator_Name')
eventtable.heading('Mobile No',text='Mobile No')
eventtable.heading('Email',text='Email')
eventtable.heading('Event_Address', text='Event_Address')
eventtable.heading('Event_Date', text='Event_date')
eventtable.heading('Added Date', text='Added Date')
eventtable.heading('Added Time', text='Added Time')
eventtable['show'] = 'headings'
eventtable.column('Id',width=100)
eventtable.column('Event_Name',width=200)
eventtable.column('Co-Ordinator_Name',width=400)
eventtable.column('Mobile No',width=200)
eventtable.column('Email',width=300)
eventtable.column('Event_Address',width=300)
eventtable.column('Event_Date',width=170)
eventtable.column('Added Date',width=170)
eventtable.column('Added Time',width=170)
eventtable.pack(fill=BOTH,expand=1)

################################################################################################################  Slider
ss = 'Event Management System'
count = 0
text = ''
##################################
SliderLabel = Label(root, text=ss, font=('times', 25, 'italic bold'), relief=RIDGE, borderwidth=5, width=30,
                    bg='skyblue')
SliderLabel.place(x=0, y=0)
############################################################################################################### clock
clock = Label(root, font=('times', 15, 'bold'), relief=RIDGE, borderwidth=4, bg='white')
clock.place(x=1020, y=0)
tick()
################################################################################################################## ConnectDatabaseButton
connectbutton = Button(root, text='Admin Login', width=15, font=('times', 20, 'italic bold'), relief=RIDGE,
                       borderwidth=4, bg='white',
                       activebackground='skyblue', activeforeground='white', command=Connectdb)
connectbutton.place(x=750, y=0)
root.mainloop()