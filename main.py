from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
window=Tk()
window.geometry('1280x700+0+0')
window.resizable(False,False)
window.title('Login System Of Student Management System')

def login():
    if usernameEntry.get()=='' or passwordEntry=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='admin' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Wellcome') 
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Enter correct credentials')


backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='student.png')
logoLabel=Label(loginFrame,image=logoImage,bg='white')
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='darkblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='darkblue',show='*')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='white',bg='cornflowerblue',activebackground='cornflowerblue',activeforeground='white'
                   ,cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()