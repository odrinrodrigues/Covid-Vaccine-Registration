import tkinter
from datetime import datetime, date
from tkinter import*

import bcrypt
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta
# from start app
from loggperson import new_signup_user
from conn import Conndb

# homepage admin and user

class Homae_page_:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1280x600')
        self.root.title('Home Page')
        self.label_1 = Label(root, text="VACCINATION:YOUR BEST SHOT", width=30,fg="ORANGE", font=("CHARLESWORTH", 30, "bold"))
        self.label_1.place(x=300, y=50)

        self.Admin_btn=tkinter.Button(self.root,cursor="hand2",command=self.Admin_login_btn_action,text="ADMIN",font=("CHARLESWORTH",30,"bold"),fg="black")
        self.Admin_btn.place(x=550,y=240,width =180)
        self.user_btn=tkinter.Button(self.root,cursor="hand2",text="USER",command=self.User_btn_Action,font=("CHARLESWORTH",30,"bold"),fg="black")
        self.user_btn.place(x=550,y=470,width=180)

# # admin login & sign up

    def home_btn_action(self):
        root=Tk()
        self.root.destroy()
        new_homepage=Homae_page_(root)
        root.mainloop()

    def User_btn_Action(self):
        self.Admin_btn.destroy()
        self.user_btn.destroy()
        self.label_1.destroy()
        #User page call
        self.user_page()

    def Admin_page(self):
        self.root.title('Admin')
        self.label_2 = Label(self.root, text="VACCINATION:YOUR BEST SHOT", width=30, fg="ORANGE", font=("CHARLESWORTH", 30, "bold"))
        self.label_2.place(x=300, y=50)

        self.Signup_btn = Button(self.root, cursor="hand2",command=self.Admin_signup_btn_action, text="Signup", font=("CHARLESWORTH", 30, "bold"), fg="black")
        self.Signup_btn.place(x=550, y=240, width=180)
        self.login_btn = Button(self.root, cursor="hand2", command=self.Admin_login_btn_action, text="Login",
                                font=("CHARLESWORTH", 30, "bold"), fg="black")

        self.login_btn.place(x=550, y=470, width=180)


    def Admin_signup_btn_action(self):
        tkinter.messagebox.showinfo(title='Center empty', message='This form is unavailble ')

    def Admin_login_btn_action(self):

        self.Admin_btn.destroy()
        self.user_btn.destroy()
        self.label_1.destroy()
      # admin login
        self.root.title('Admin Login')
        label_3 = Label(self.root, text="ADMIN LOGIN", width=30, font=("CHARLESWORTH", 40, "bold"))
        label_3.place(x=200, y=100)

        label_4 = Label(self.root, text="ID Number", width=30, font=("garamond", 30, "bold"))
        label_4.place(x=100, y=200)
        self.entry_1 = Entry(self.root, width=35, font=("garamond", 18, "bold"))
        self.entry_1.place(x=650, y=215)

        label_5 = Label(self.root, text="Password", width=30, font=("garamond", 30, "bold"))
        label_5.place(x=100, y=350)
        self.entry_2 = Entry(self.root, width=35, font=("garamond", 18, "bold"))
        self.entry_2.place(x=650, y=365)

        self.login_btn = Button(self.root, cursor="hand2", command=self.Admin_login_check_action, text="Login",
                                font=("CHARLESWORTH", 30, "bold"), fg="black")
        self.login_btn.place(x=550, y=470, width=180)


        self.home_btn=tkinter.Button(self.root,cursor="hand2",text="Home",command=self.home_btn_action,font=("CHARLESWORTH",13,"bold"),fg="black")
        self.home_btn.place(x=1080,y=10)

        self.close_btn=tkinter.Button(self.root,cursor="hand2",text="Exit",command=self.root.destroy,font=("CHARLESWORTH",13,"bold"),fg="black")
        self.close_btn.place(x=1180,y=10,width=80)
    def Admin_login_check_action(self):
        print('Logged In')
        ###Slq login Check
    def user_page(self):
        # user login & sign up
        self.Admin_btn.destroy()
        self.user_btn.destroy()
        self.label_1.destroy()
        self.root.title('User')

        self.label_17 = Label(self.root, text="VACCINATION:YOUR BEST SHOT", width=30, fg="ORANGE", font=("CHARLESWORTH", 30, "bold"))
        self.label_17.place(x=300, y=50)

        self.user_Signup_btn = tkinter.Button(self.root, cursor="hand2",command=self.user_signup_button_action, text="Signup", font=("CHARLESWORTH", 30, "bold"), fg="black")
        self.user_Signup_btn.place(x=550, y=240, width=180)

        self.user_login_btn = tkinter.Button(self.root, cursor="hand2", command=self.user_login_btn_action, text="Login", font=("CHARLESWORTH", 30, "bold"),
                           fg="black")
        self.user_login_btn.place(x=550, y=470, width=180)
        self.home_btn=tkinter.Button(self.root,cursor="hand2",text="Home",command=self.home_btn_action,font=("CHARLESWORTH",13,"bold"),fg="black")
        self.home_btn.place(x=1080,y=10)

        self.close_btn=tkinter.Button(self.root,cursor="hand2",text="Exit",command=self.root.destroy,font=("CHARLESWORTH",13,"bold"),fg="black")
        self.close_btn.place(x=1180,y=10,width=80)
        self.var = StringVar()
    def user_signup_button_action(self):
        # destroy old widgets
        self.label_17.destroy()
        self.user_Signup_btn.destroy()
        self.user_login_btn.destroy()

        #user signup
        self.root.geometry('1280x720')
        self.root.title('User Signup')
        self.label_21 = Label(self.root, text="USER SIGN UP",width=30,font=("CHARLESWORTH",30,"bold"))
        self.label_21.place(x=300,y=15)

        self.label_22 = Label(self.root, text="First Name",width=30,font=("garamond",20,"bold"))
        self.label_22.place(x=150,y=100)
        self.entry_14 = Entry(self.root,width=40)
        self.entry_14.place(x=600,y=110)

        self.label_23 = Label(self.root, text="Middle Name",width=30,font=("garamond",20,"bold"))
        self.label_23.place(x=150,y=150)
        self.entry_15 = Entry(self.root,width=40)
        self.entry_15.place(x=600,y=160)

        self.label_24 = Label(self.root, text="Last  Name",width=30,font=("garamond",20,"bold"))
        self.label_24.place(x=150,y=200)
        self.entry_16 = Entry(self.root,width=40)
        self.entry_16.place(x=600,y=210)

        self.label_25 = Label(self.root, text="UID Number",width=30,font=("garamond",20,"bold"))
        self.label_25.place(x=150,y=250)
        self.entry_17 = Entry(self.root,width=40)
        self.entry_17.place(x=600,y=260)

        self.label_26 = Label(self.root, text="Phone number",width=30,font=("garamond",20,"bold"))
        self.label_26.place(x=150,y=300)
        self.entry_18 = Entry(self.root,width=40)
        self.entry_18.place(x=600,y=310)

        self.label_27 = Label(self.root, text="Email",width=30,font=("garamond",20,"bold"))
        self.label_27.place(x=150,y=350)
        self.entry_19 = Entry(self.root,width=40)
        self.entry_19.place(x=600,y=360)

        self.label_28 = Label(self.root, text="Gender",width=30,font=("garamond",20,"bold"))
        self.label_28.place(x=150,y=400)
        # global var

        self.gendermale=Radiobutton(self.root, text="Male",padx = 20, variable=self.var, value='Male',font=("garamond",20,"bold"))
        self.gendermale.place(x=550,y=410)
        self.genderfemale=Radiobutton(self.root, text="Female",padx = 20, variable=self.var, value='Female',font=("garamond",20,"bold"))
        self.genderfemale.place(x=660,y=410)
        self.genderother=Radiobutton(self.root, text="Other",padx = 20, variable=self.var, value='Other',font=("garamond",20,"bold"))
        self.genderother.place(x=820,y=410)

        self.label_29 = Label(self.root, text="Date of Birth:",width=30,font=("garamond",20,"bold"))
        self.label_29.place(x=150,y=450)

        self.entry_20= DateEntry(self.root, width=12, year=date.today().year-1, month=date.today().month, day=date.today().day,date_pattern='dd/mm/yyyy',
        background='darkblue', foreground='white', borderwidth=2)
        self.entry_20.place(x=600,y=460)
        print(self.entry_20.get_date())

                #PASSWORD
        self.label_30 = Label (self.root,text="Password",width=30,font=("garamond",20,"bold"))
        self.label_30.place(x=150,y=500)
        self.entry_21 = Entry(self.root,width=40)
        self.entry_21.place(x=600,y=510)

        self.label_31 = Label (self.root,text="Confirm Password",width=30,font=("garamond",20,"bold"))
        self.label_31.place(x=150,y=550)
        self.entry_22 = Entry(self.root,width=40)
        self.entry_22.place(x=600,y=560)

        self.user_signup_form_submit_btn=tkinter.Button(self.root, command=self.user_signup_form_submit_btn_action,text='Submit',width=10,bg='Yellow',fg='black',font=("CHARLESWORTH",15,"bold"))
        self.user_signup_form_submit_btn.place(x=400,y=600)

        self.user_signup_form_cancel_btn=tkinter.Button(self.root, text='Cancel',command=self.user_signup_form_cancel_btn_action,width=10,bg='Yellow',fg='black',font=("CHARLESWORTH",15,"bold"))
        self.user_signup_form_cancel_btn.place(x=800,y=600)

    def user_signup_form_submit_btn_action(self):
        new_signup=new_signup_user

        new_signup.user_detail['fname']=self.entry_14.get()
        new_signup.user_detail['mname']=self.entry_15.get()
        new_signup.user_detail['lname']=self.entry_16.get()
        new_signup.user_detail['uid']=self.entry_17.get()
        new_signup.user_detail['phone_number']=self.entry_18.get()
        birth_date=self.entry_20.get_date()
        new_signup.user_detail['birth_date']=birth_date
        new_signup.user_detail['gendder']=self.var.get()
        new_signup.user_detail['e_mail']=self.entry_19.get()
        print(birth_date)

        print(list(new_signup.user_detail.values()))


        new_conn = Conndb

        try:
            ##--Checking existing uid
            insert_flag =None
            if new_signup.user_detail['uid'] is not None:
                check_uid="""select uid from userdata where uid=%s"""
                new_conn.curs.execute(check_uid,(new_signup.user_detail['uid'],))
                uid_found=new_conn.curs.fetchone()
                print(uid_found)
                if uid_found is  None:
                    insert_flag = 1
                else:
                    insert_flag=0
                    MsgBox = tkinter.messagebox.askquestion('User already exist', f'UID {uid_found[0]} already registered !\n Proceed to Login',
                                                            icon='warning')
                    if MsgBox == 'yes':
                        self.user_signup_form_cancel_btn_action()
                        self.user_page()
        except:
            print('Error while checking user')
        try:
            # ------------ Prepared statement

            new_user = """insert into userdata values(%s,%s,%s,%s,%s,%s,%s,%s)"""
            new_conn.curs.execute(new_user, list(new_signup_user.user_detail.values()))
            new_conn.conn.commit()

            # ##--Hashing Pass
            hashed = bcrypt.hashpw(self.entry_21.get().encode('utf8'), bcrypt.gensalt())
            user_login=(new_signup_user.user_detail['uid'],hashed)
            #--inserting login data
            insert_paas="""insert into user_login values(%s,%s)"""
            new_conn.curs.execute(insert_paas,user_login)
            new_conn.conn.commit()

        except:
            print('error inserting')

    def user_signup_form_cancel_btn_action(self):


    def user_login_btn_action(self):
        #destroy old widgets
        self.label_17.destroy()
        self.user_Signup_btn.destroy()
        self.user_login_btn.destroy()

        # user login
        self.root.title('user Login')
        self.label_18 = Label(self.root, text="USER Login",width=30,font=("CHARLESWORTH",40,"bold"))
        self.label_18.place(x=200,y=100)

        self.label_19 = Label(self.root, text="UID Number",width=30,font=("garamond",30,"bold"))
        self.label_19.place(x=150,y=200)
        self.entry_12 = Entry(self.root,width=50)
        self.entry_12.place(x=700,y=215)

        self.label_20 = Label(self.root, text="Password",width=30,font=("garamond",30,"bold"))
        self.label_20.place(x=150,y=350)
        self.entry_13 = Entry(self.root,width=50)
        self.entry_13.place(x=700,y=365)
        self.user_login_btn = tkinter.Button(self.root, cursor="hand2", command=self.user_login_check, text="Login", font=("CHARLESWORTH", 20, "bold"),
                           fg="black")
        self.user_login_btn.place(x=850, y=470, width=100)

        self.user_back_btn = tkinter.Button(self.root, cursor="hand2", command=self.user_back_btn_action, text="Back", font=("CHARLESWORTH", 20, "bold"),
                           fg="black")
        self.user_back_btn.place(x=550, y=470, width=100)

    def user_login_check(self):
        pass

    def user_back_btn_action(self):
        self.label_18.destroy()
        self.label_19.destroy()
        self.label_20.destroy()
        self.entry_12.destroy()
        self.entry_13.destroy()
        self.user_login_btn.destroy()
        self.user_back_btn.destroy()
        self.user_page()

#

#
# # health report
#
#         label_0 = Label(root,bg='light grey', text="HEALTH REPORT", width=30,fg="BLACK", font=("CHARLESWORTH", 30, "bold"))
#         label_0.place(x=250, y=10)
#
#         disease_bp = Label(root,bg='light grey', text="Do you have Blood Pressure?", width=30, font=("garamond", 25, "bold"))
#         disease_bp.place(x=10, y=100)
#         self.var = StringVar()
#         Radiobutton(root,bg='light grey', text="YES", padx=20, variable=self.var, value=1, font=("garamond", 15, "bold")).place(x=580,y=103)
#         Radiobutton(root,bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700,y=103)
#         Radiobutton(root,bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820,y=103)
#
#         disease_cancer = Label(root, bg='light grey', text="Do you have any type of Cancer?", width=30, font=("garamond", 25, "bold"))
#         disease_cancer.place(x=10, y=160)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580,y=163)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700,y=163)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820,y=163)
#
#         disease_diabetes = Label(root, bg='light grey', text="Do you have Diabetes Mellitus?", width=30,font=("garamond", 25, "bold"))
#         disease_diabetes.place(x=10, y=220)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=223)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=223)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=223)
#
#         disease_lipid = Label(root, bg='light grey', text="Do you have Lipid Disorder?", width=30,font=("garamond", 25, "bold"))
#         disease_lipid.place(x=10, y=280)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=283)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700, y=283)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820, y=283)
#
#         disease_kidney = Label(root, bg='light grey', text="Do you have Kidney Disease?", width=30,font=("garamond", 25, "bold"))
#         disease_kidney.place(x=10, y=340)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=343)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=343)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=343)
#
#         disease_heart = Label(root, bg='light grey', text="Do you have any type heart disease?", width=30, font=("garamond", 25, "bold"))
#         disease_heart.place(x=10, y=400)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=403)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700, y=403)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820, y=403)
#
#         disease_allergies = Label(root, bg='light grey', text="Do you have any type allergies?", width=30,font=("garamond", 25, "bold"))
#         disease_allergies.place(x=10, y=460)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=463)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=463)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=463)
#
#         disease_allergies = Label(root, bg='light grey', text="Are you tested covid positive before?", width=30,font=("garamond", 25, "bold"))
#         disease_allergies.place(x=10, y=520)
#         self.var = StringVar()
#         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=523)
#         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=523)
#         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=523)
#
#         Button(root, text='Cancel', width=10, bg='Yellow', fg='black', font=("CHARLESWORTH", 15, "bold")).place(x=400, y=590)
#         Button(root, text='Submit', width=10, bg='Yellow', fg='black', font=("CHARLESWORTH", 15, "bold")).place(x=750, y=590)
#
#
