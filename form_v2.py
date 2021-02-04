import sqlite3
from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox 

conn = sqlite3.connect('Marksheet.db')
cur = conn.cursor()

cur.executescript('''

CREATE TABLE IF NOT EXISTS STUDENT(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    un TEXT UNIQUE,
    password VARCHAR(15),
    confpassword VARCHAR(15),
    m1 INTEGER,
    m2 INTERGER,
    m3 INTEGER,
    m4 INTEGER,
    m5 INTEGER,
    per INTEGER,
    result VARCHAR(15)


);
''')

def main():
    app=Tk()
    app.title("Registration Form")
    app.geometry("1175x650")
    app.resizable(0,0)

    image = Image.open('login/pic.jpg')
    photo_image = ImageTk.PhotoImage(image)
    label = Label(app, image = photo_image)
    label.pack()

    username=StringVar()
    password=StringVar()
    cnf_pass=StringVar()
    sub_one=DoubleVar()
    sub_two=DoubleVar()
    sub_three=DoubleVar()
    sub_four=DoubleVar()
    sub_five=DoubleVar()
    u=StringVar()
    p=StringVar()
    r1=IntVar()
    r2=StringVar()
    
    sub_one.set(" ")
    sub_two.set(" ")
    sub_three.set(" ")
    sub_four.set(" ")
    sub_five.set(" ")
    r1.set(" ")
    def rem():
        user=username.get()
        pasw=password.get()
        cnfpasw=cnf_pass.get()
        s1=sub_one.get()
        s2=sub_two.get()
        s3=sub_three.get()
        s4=sub_four.get()
        s5=sub_five.get()
        print(s1,s2,s3,s4,s5)

        t=(s1+s2+s3+s4+s5)/5
        
        if t<100 and t >= 90:
            tos="OUTSTANDING"
        elif t<90 and t>=80:
            tos="EXCELLENT"
        elif t<80 and t>=70:
            tos="GOOD"
        elif t<70 and t>=60:
            tos="ABOVE AVERAGE"
        elif t<60 and t>=50:
            tos="AVERAGE"
        elif t<50 and t>=40:
            tos="BELOW AVERAGE"
        else:
            tos="FAIL"     
        print(tos)
        print(t)     

        if(len(user)!=0 and pasw==cnfpasw):
            cur.execute('''INSERT OR REPLACE INTO STUDENT(un,password,confpassword,m1,m2,m3,m4,m5,per,result) VALUES (?,?,?,
                                                       ?,?,?,?,?,?,?)''',(str(user),str(pasw),str(cnfpasw),s1,s2,s3,s4,s5,t,tos))

            messagebox.showinfo("Registered","Registration Successfull")
            username.set(" ")
            password.set(" ")
            cnf_pass.set(" ")
            sub_one.set(" ")
            sub_two.set(" ")
            sub_three.set(" ")
            sub_four.set(" ")
            sub_five.set(" ")
            
        else:
            messagebox.showerror("Error","Password or Username Entry Error")    
        conn.commit()
    

    def login():
        u1=u.get()
        p1=p.get()

        if u1=="" or p1=="":
            messagebox.showerror("Error","Fill all the required fields")
        else:
            cur.execute('SELECT * FROM STUDENT WHERE un = ? and password= ?',[u1,p1])
            row=cur.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")


            else:
                print(row)
                r1.set((row[9]))
                r2.set(str(row[10]))
                p.set("")



    register=Label(app,text="Register Here",font=("verdana",30,"bold"),fg="green")
    register.place(x="150",y="25")
    log=Label(app,text="Login Here",font=("verdana",30,"bold"),fg="dark blue")
    log.place(x="750",y="25")
    marks=Label(app,text="Enter Your Marks",font=("verdana",20,"bold"))
    marks.place(x="50",y="250")

    firstrow=Label(app,text="Username-",font=("verdana",16))
    firstrow.place(x="650",y="100")
    user2=Entry(app,textvariable=u,font=("verdana",13))
    user2.place(x="800",y="100",height="40",width="300")
    secondrow=Label(app,text="Password-",font=("verdana",16))
    secondrow.place(x="650",y="175")
    pass2=Entry(app,show='*',textvariable=p,font=("verdana",13))
    pass2.place(x="800",y="175",height="40",width="300")
    b2=Button(app,text="Show Result",font=("verdana",15,"bold"),command=login)
    b2.place(x="850",y="235")

    firstrow=Label(app,text="Username-",font=("verdana",16))
    firstrow.place(x="50",y="100")
    user1=Entry(app,textvariable=username,font=("verdana",13))
    user1.place(x="250",y="100",height="30",width="300")
    secondrow=Label(app,text="Password-",font=("verdana",16))
    secondrow.place(x="50",y="150")
    pass2=Entry(app,textvariable=password,font=("verdana",13))
    pass2.place(x="250",y="200",height="30",width="300")
    secrow=Label(app,text="Conf. Password-",font=("verdana",16))
    secrow.place(x="50",y="200")
    cnf_password=Entry(app,textvariable=cnf_pass,font=("verdana",13))
    cnf_password.place(x="250",y="150",height="30",width="300")
    thirdrow=Label(app,text="subject 1-",font=("verdana",16))
    thirdrow.place(x="50",y="300")
    subject1=Entry(app,textvariable=sub_one,font=("verdana",13))
    subject1.place(x="250",y="300",height="30",width="300")
    fourthrow=Label(app,text="subject 2-",font=("verdana",16))
    fourthrow.place(x="50",y="350")
    subject2=Entry(app,textvariable=sub_two,font=("verdana",13))
    subject2.place(x="250",y="350",height="30",width="300")
    fiverow=Label(app,text="subject 3-",font=("verdana",16))
    fiverow.place(x="50",y="400")
    subject3=Entry(app,textvariable=sub_three,font=("verdana",13))
    subject3.place(x="250",y="400",height="30",width="300")
    sixrow=Label(app,text="subject 4-",font=("verdana",16))
    sixrow.place(x="50",y="450")
    subject4=Entry(app,textvariable=sub_four,font=("verdana",13))
    subject4.place(x="250",y="450",height="30",width="300")
    sevenrow=Label(app,text="subject 5-",font=("verdana",16))
    sevenrow.place(x="50",y="500")
    subject5=Entry(app,textvariable=sub_five,font=("verdana",13))
    subject5.place(x="250",y="500",height="30",width="300")
    b1=Button(app,text="Register",font=("verdana",15,"bold"),command=rem)
    b1.place(x="250",y="550",height="50")

    firstrow=Label(app,text="Percantage-",font=("verdana",16))
    firstrow.place(x="650",y="350")
    per=Entry(app,state="readonly",font=("verdana",16,"bold"),textvariable=r1,width="50")
    per.place(x="800",y="350",height="30",width="300")
    secondrow=Label(app,text="Remarks-",font=("verdana",16))
    secondrow.place(x="650",y="425")
    remark=Entry(app,state="readonly",font=("verdana",16,"bold"),textvariable=r2,width="50")
    remark.place(x="800",y="425",height="30",width="300")
    mainloop()    


if __name__=="__main__":
    main()