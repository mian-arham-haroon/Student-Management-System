from tkinter import *
from datetime import datetime
import ttkthemes
import time
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass    

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is Save succesfully')


def update_student():
    def update_data():
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get()
                                ,addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
        conn.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()
        show_student()

    
    update_window=Toplevel()
    update_window.grab_set()
    update_window.resizable(0,0)
    update_window.title('Update Student')
    idLabel=Label(update_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(update_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    phoneLabel=Label(update_window,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(update_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    emailLabel=Label(update_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel=Label(update_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(update_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel=Label(update_window,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(update_window,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    update_student_button=ttk.Button(update_window,text='UPDATE STUDENT',command=update_data)
    update_student_button.grid(row=7,columnspan=2,pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdate=content['values']
    idEntry.insert(0,listdate[0])
    nameEntry.insert(0,listdate[1])
    phoneEntry.insert(0,listdate[2])
    emailEntry.insert(0,listdate[3])
    addressEntry.insert(0,listdate[4])
    genderEntry.insert(0,listdate[5])
    dobEntry.insert(0,listdate[6])
    



def show_student():
    query='select* from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data )

def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    connent_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,connent_id)
    conn.commit()
    messagebox.showinfo('Deleted',f'Id {connent_id} is deleted succesfully')
    query='select* from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data )





def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s' 
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()   
        for data in fetched_data:
            studentTable.insert('',END,values=data )




    search_window=Toplevel()
    search_window.grab_set()
    search_window.resizable(0,0)
    search_window.title('Search Student')
    idLabel=Label(search_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(search_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    phoneLabel=Label(search_window,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(search_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    emailLabel=Label(search_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel=Label(search_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(search_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel=Label(search_window,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(search_window,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    search_student_button=ttk.Button(search_window,text='SEARCH STUDENT',command=search_data)
    search_student_button.grid(row=7,columnspan=2,pady=15)


    



def connect_database():

    def connect():
        global mycursor,conn
        try:
            conn=pymysql.connect(host='localhost',user='root',password='arham@12345678@')
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)    
            return
        try:
            query='create database studentmanagementsystem' 
            mycursor.execute(query)   
            query='use studentmanagementsystem' 
            mycursor.execute(query)   
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(11),email varchar(30),\
                address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))' 
            mycursor.execute(query)   
        except:
            query='use studentmanagementsystem' 
            mycursor.execute(query)   
        messagebox.showinfo('Success','Database Connection is successful',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state='normal')
        searchstudentButton.config(state='normal')
        updatestudentButton.config(state='normal')
        showstudentButton.config(state='normal')
        exportButton.config(state='normal')
        deletestudentButton.config(state='normal')
            


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0)

    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0)

    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=55,pady=20)

    connect_Button=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connect_Button.grid(row=3,columnspan=2)

def add_student():

    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All Feilds are reqired',parent=add_window)
        else:
            date=time.strftime('%d/%m/%Y')
            currenttime=time.strftime('%H:%M:%S')
            try:
                # query = 'INSERT INTO student (name, mobile, email, address, gender, dob, date, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                # mycursor.execute(query, (nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                #                           addressEntry.get(), genderEntry.get(), dobEntry.get(), date, currenttime))
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))  
                conn.commit()
                result=messagebox.askyesno('Confirm','Date added successfully. Do you want to clean the form?')            
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass 
            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_window) 
                return

            query='select * from student'
            mycursor.execute(query)
            fetched_date=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for date in fetched_date:
                studentTable.insert('',END,values=date)



    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    idLabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel=Label(add_window,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    phoneLabel=Label(add_window,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(add_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    emailLabel=Label(add_window,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)

    addressLabel=Label(add_window,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(add_window,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    dobLabel=Label(add_window,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)

count=0
text=''

def slider():
    global text
    global count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(1000,slider)


def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f' Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.title('Student Management System')
root.resizable(False,False)

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)

clock()

s='Student Management System'
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)

slider()

connectButton=ttk.Button(root,text='Connect Database',command=connect_database)
connectButton.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state='disabled',command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state='disabled',command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state='disabled',command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state='disabled',command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state='disabled',command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportButton=ttk.Button(leftFrame,text='Export Data',width=25,state='disabled',command=export_data)
exportButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25)
exitButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollbarY=Scrollbar(rightFrame,orient=VERTICAL)


studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender'
                                             ,'D.O.B','Added Date','Added Time'),xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
scrollbarX.config(command=studentTable.xview)
scrollbarY.config(command=studentTable.yview)

scrollbarX.pack(side=BOTTOM,fill=X)
scrollbarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No')
studentTable.heading('Email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')
studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=30,font=('arial',12,'bold'),fg='black',bg='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',13,'bold'))

studentTable.config(show='headings')


root.mainloop()