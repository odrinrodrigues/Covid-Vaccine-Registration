import tkinter
from datetime import datetime, date
from tkinter import *
from tkinter import ttk, messagebox

import bcrypt
import mysql
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta
# from start app
from loggperson import new_signup_user
from conn import Conndb
from registrationpage import Registration_frame


# homepage admin and user

class Homae_page_:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1280x600')
        self.root.title('Home Page')
        self.__init__frame = Frame(root)
        self.__init__frame.place(x=0, y=0, width=1300, height=780)
        self.__init__frame.config(bg='lightgrey')

        self.label_1 = Label(self.__init__frame, text="VACCINATION:YOUR BEST SHOT", width=30, fg="ORANGE",
                             font=("CHARLESWORTH", 30, "bold"),bg='lightgrey')

        self.label_1.place(x=300, y=50)
        self.Admin_btn = tkinter.Button(self.__init__frame, cursor="hand2",
                                        text="ADMIN", font=("CHARLESWORTH", 30, "bold"), fg="black",bg='lightgrey',command=self.Admin_login_btn_action)
        self.Admin_btn.place(x=550, y=240, width=180)
        self.user_btn = tkinter.Button(self.__init__frame, cursor="hand2", text="USER",
                                       font=("CHARLESWORTH", 30, "bold"), fg="black",bg='lightgrey',command=self.User_btn_Action)
        self.user_btn.place(x=550, y=470, width=180)
        # # admin login & sign up

    def home_btn_action(self):
        root = Tk()
        self.root.destroy()
        new_homepage = Homae_page_(root)
        root.mainloop()

    def User_btn_Action(self):
        self.__init__frame.destroy()
        self.user_page_frame()

#     def Admin_signup_btn_action(self):
#         tkinter.messagebox.showinfo(title='Center empty', message='This form is unavailble ')
    def Admin_login_btn_action(self):

        # admin login
        self.Admin_login_fram=Frame(self.root)
        self.Admin_login_fram.place(x=0, y=0, width=1300, height=780)
        label_3 = Label(self.Admin_login_fram, text="ADMIN LOGIN", width=30, font=("CHARLESWORTH", 40, "bold"))
        label_3.place(x=200, y=100)

        label_4 = Label(self.Admin_login_fram, text="ID Number", width=30, font=("garamond", 30, "bold"))
        label_4.place(x=100, y=200)
        self.entry_1 = Entry(self.Admin_login_fram, width=35, font=("garamond", 18, "bold"))
        self.entry_1.place(x=650, y=215)

        label_5 = Label(self.Admin_login_fram, text="Password", width=30, font=("garamond", 30, "bold"))
        label_5.place(x=100, y=350)
        self.entry_2 = Entry(self.Admin_login_fram, width=35, font=("garamond", 18, "bold"))
        self.entry_2.place(x=650, y=365)

        self.login_btn = Button(self.Admin_login_fram, cursor="hand2", text="Login",
                                font=("CHARLESWORTH", 30, "bold"), fg="black")
        self.login_btn.place(x=550, y=470, width=180)

        self.home_btn = tkinter.Button(self.Admin_login_fram, cursor="hand2", text="Home",
                                       font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.home_btn_action)
        self.home_btn.place(x=1080, y=10)

        self.close_btn = tkinter.Button(self.Admin_login_fram, cursor="hand2", text="Exit",
                                        font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.root.destroy)
        self.close_btn.place(x=1180, y=10, width=80)



    def Admin_login_check_action(self):
        print('Logged In')
        ###Slq login Check
        pass

    def user_page_frame(self):
        # user login & sign up
            self.user_page = Frame(self.root)

            self.user_page.place(x=0, y=0, width=1300, height=780)

            self.label_17 = Label(self.user_page, text="VACCINATION:YOUR BEST SHOT", width=30, fg="ORANGE",
                                  font=("CHARLESWORTH", 30, "bold"))
            self.label_17.place(x=300, y=50)

            self.user_Signup_btn = tkinter.Button(self.user_page, cursor="hand2",
                                                  text="Signup", font=("CHARLESWORTH", 30, "bold"), fg="black",command=self.user_signup_button_action)
            self.user_Signup_btn.place(x=550, y=240, width=180)

            self.user_login_btn = tkinter.Button(self.user_page, cursor="hand2",
                                                 text="Login", font=("CHARLESWORTH", 30, "bold"),
                                                 fg="black",command=self.user_login_btn_action)
            self.user_login_btn.place(x=550, y=470, width=180)
            self.home_btn = tkinter.Button(self.user_page, cursor="hand2", text="Home",
                                           font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.home_btn_action)
            self.home_btn.place(x=1080, y=10)

            self.close_btn = tkinter.Button(self.user_page, cursor="hand2", text="Exit",
                                            font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.root.destroy)
            self.close_btn.place(x=1180, y=10, width=80)

    def user_signup_button_action(self):
        # self.new_login_frame.destroy()
        self.new_signup_page_frame = Frame(self.root)
        self.new_signup_page_frame.place(x=0, y=0, width=1300, height=780)
        # user signup

        self.label_21 = Label(self.new_signup_page_frame, text="USER SIGN UP", width=30, font=("CHARLESWORTH", 30, "bold"))
        self.label_21.place(x=300, y=15)

        self.label_22 = Label(self.new_signup_page_frame, text="First Name", width=30, font=("garamond", 20, "bold"))
        self.label_22.place(x=150, y=100)
        self.entry_14 = Entry(self.new_signup_page_frame, width=40)
        self.entry_14.place(x=600, y=110)

        self.label_23 = Label(self.new_signup_page_frame, text="Middle Name", width=30, font=("garamond", 20, "bold"))
        self.label_23.place(x=150, y=150)
        self.entry_15 = Entry(self.new_signup_page_frame, width=40)
        self.entry_15.place(x=600, y=160)

        self.label_24 = Label(self.new_signup_page_frame, text="Last  Name", width=30, font=("garamond", 20, "bold"))
        self.label_24.place(x=150, y=200)
        self.entry_16 = Entry(self.new_signup_page_frame, width=40)
        self.entry_16.place(x=600, y=210)

        self.label_25 = Label(self.new_signup_page_frame, text="UID Number", width=30, font=("garamond", 20, "bold"))
        self.label_25.place(x=150, y=250)
        self.entry_17 = Entry(self.new_signup_page_frame, width=40)
        self.entry_17.place(x=600, y=260)

        self.label_26 = Label(self.new_signup_page_frame, text="Phone number", width=30, font=("garamond", 20, "bold"))
        self.label_26.place(x=150, y=300)
        self.entry_18 = Entry(self.new_signup_page_frame, width=40)
        self.entry_18.place(x=600, y=310)

        self.label_27 = Label(self.new_signup_page_frame, text="Email", width=30, font=("garamond", 20, "bold"))
        self.label_27.place(x=150, y=350)
        self.entry_19 = Entry(self.new_signup_page_frame, width=40)
        self.entry_19.place(x=600, y=360)

        self.label_28 = Label(self.new_signup_page_frame, text="Gender", width=30, font=("garamond", 20, "bold"))
        self.label_28.place(x=150, y=400)

        # self.var = tkinter.StringVar()
        self.gender = ttk.Combobox(self.new_signup_page_frame, width=15,state='readonly')
        self.gender.place(x=600, y=410)

        self.gender['values'] = ('Male','Female','Other'
                                )

        self.label_29 = Label(self.new_signup_page_frame, text="Date of Birth:", width=30, font=("garamond", 20, "bold"))
        self.label_29.place(x=150, y=450)

        self.entry_20 = DateEntry(self.new_signup_page_frame, width=12, year=date.today().year - 1,
                                  month=date.today().month,
                                  day=date.today().day, date_pattern='dd/mm/yyyy',
                                  background='darkblue', foreground='white', borderwidth=2)
        self.entry_20.place(x=600, y=460)

        # PASSWORD
        self.label_30 = Label(self.new_signup_page_frame, text="Password", width=30, font=("garamond", 20, "bold"))
        self.label_30.place(x=150, y=500)
        self.entry_21 = Entry(self.new_signup_page_frame, width=40)
        self.entry_21.place(x=600, y=510)

        self.label_31 = Label(self.new_signup_page_frame, text="Confirm Password", width=30, font=("garamond", 20, "bold"))
        self.label_31.place(x=150, y=550)
        self.entry_22 = Entry(self.new_signup_page_frame, width=40)
        self.entry_22.place(x=600, y=560)

        self.user_signup_form_submit_btn = tkinter.Button(self.new_signup_page_frame,
                                                          command=self.user_signup_form_submit_btn_action,
                                                          text='Submit', width=10, bg='Yellow', fg='black',
                                                          font=("CHARLESWORTH", 15, "bold"))
        self.user_signup_form_submit_btn.place(x=400, y=600)

        self.user_signup_form_cancel_btn = tkinter.Button(self.new_signup_page_frame, text='Cancel',
                                                           width=10,
                                                          bg='Yellow', fg='black', font=("CHARLESWORTH", 15, "bold"),command=self.user_signup_form_cancel_btn_action)
        self.user_signup_form_cancel_btn.place(x=800, y=600)

        self.home_btn = tkinter.Button(self.new_signup_page_frame, cursor="hand2", text="Home",
                                       font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.home_btn_action)
        self.home_btn.place(x=1080, y=10)

        self.close_btn = tkinter.Button(self.new_signup_page_frame, cursor="hand2", text="Exit",
                                        font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.root.destroy)
        self.close_btn.place(x=1180, y=10, width=80)


    def user_signup_form_submit_btn_action(self):
        new_signup = new_signup_user

        new_signup.user_detail['fname'] = self.entry_14.get()
        new_signup.user_detail['mname'] = self.entry_15.get()
        new_signup.user_detail['lname'] = self.entry_16.get()
        new_signup.user_detail['uid'] = self.entry_17.get()
        new_signup.user_detail['phone_number'] = self.entry_18.get()
        birth_date = self.entry_20.get_date()
        new_signup.user_detail['birth_date'] = birth_date
        new_signup.user_detail['gendder'] = self.gender.get()
        new_signup.user_detail['e_mail'] = self.entry_19.get()

        new_conn = Conndb

        try:
            ##--Checking existing uid
            if new_signup.user_detail['uid'] is not None:
                check_uid = """select uid from userdata where uid=%s"""
                new_conn.curs.execute(check_uid, (new_signup.user_detail['uid'],))
                uid_found = new_conn.curs.fetchone()
                print(uid_found)
                if ((self.entry_17.get() is None or self.entry_17 =="") or len(self.entry_17.get())<12 or len(self.entry_17.get())>12):
                    tkinter.messagebox.showinfo(title='Invalid input', message='Invalid UID!')
                else:
                    if uid_found==None:

                        ##--Start inserting
                        try:
                            # ------------ Prepared statement

                            new_user = """insert into userdata values(%s,%s,%s,%s,%s,%s,%s,%s)"""
                            new_conn.curs.execute(new_user, list(new_signup_user.user_detail.values()))
                            new_conn.conn.commit()

                            # ##--Hashing Pass
                            hashed = bcrypt.hashpw(self.entry_21.get().encode('utf8'), bcrypt.gensalt())
                            user_login = (new_signup_user.user_detail['uid'], hashed)
                            # --inserting login data
                            insert_paas = """insert into user_login values(%s,%s)"""
                            new_conn.curs.execute(insert_paas, user_login)
                            new_conn.conn.commit()

                            messagebox.showinfo("Success", 'Registeration Completed',
                                                parent=self.new_signup_page_frame)


                        except:
                            print('error inserting')

                        finally:
                            new_conn.conn.close()


                    elif uid_found is not None:

                        MsgBox = tkinter.messagebox.askquestion('User already exist',
                                                                f'UID {uid_found[0]} already registered !\n Proceed to Login',
                                                                icon='warning')
                        if MsgBox == 'yes':
                            self.user_login_btn_action()
        except:
            print('Error while checking user')


    def user_signup_form_cancel_btn_action(self):
        self.new_signup_page_frame.destroy()
        self.user_page_frame()
        ## code for sql data insert

#
    def user_login_btn_action(self):
        # user login
        self.user_page.destroy()
        self.new_login_frame=Frame(self.root)
        self.new_login_frame.place(x=0, y=0, width=1300, height=780)
        self.label_18 = Label(self.new_login_frame, text="USER Login", width=30, font=("CHARLESWORTH", 40, "bold"))
        self.label_18.place(x=200, y=100)

        self.label_19 = Label(self.new_login_frame, text="UID Number", width=30, font=("garamond", 30, "bold"))
        self.label_19.place(x=150, y=200)
        self.entry_12 = Entry(self.new_login_frame, width=50)
        self.entry_12.place(x=700, y=215)

        self.label_20 = Label(self.new_login_frame, text="Password", width=30, font=("garamond", 30, "bold"))
        self.label_20.place(x=150, y=350)
        self.entry_13 = Entry(self.new_login_frame, width=50)
        self.entry_13.place(x=700, y=365)
        self.user_login_btn = tkinter.Button(self.new_login_frame, cursor="hand2", text="Login",
                                             font=("CHARLESWORTH", 20, "bold"),
                                             fg="black",command=self.user_login_check)
        self.user_login_btn.place(x=850, y=470, width=100)

        self.user_back_btn = tkinter.Button(self.new_login_frame, cursor="hand2", text="Back",
                                            font=("CHARLESWORTH", 20, "bold"),
                                            fg="black",command=self.user_page_frame)
        self.user_back_btn.place(x=550, y=470, width=100)

        self.home_btn = tkinter.Button(self.new_login_frame, cursor="hand2", text="Home",
                                       font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.home_btn_action)
        self.home_btn.place(x=1080, y=10)

        self.close_btn = tkinter.Button(self.new_login_frame, cursor="hand2", text="Exit",
                                        font=("CHARLESWORTH", 13, "bold"), fg="black",command=self.root.destroy)
        self.close_btn.place(x=1180, y=10, width=80)


    def user_login_check(self):
        try:
            login_sql = """select uid,user_password from user_login where uid=%s """
            new_login = Conndb
            new_login.curs.execute(login_sql, (self.entry_12.get(),))
            login_result = new_login.curs.fetchone()
            if login_result is not None:
                hashesdpass = login_result[1]
                if bcrypt.checkpw(self.entry_13.get().encode('utf-8'), hashesdpass.encode('utf-8')):

                    if login_result is not None:
                        messagebox.showinfo("Success", 'Log in Success',
                                            parent=self.new_login_frame)

                        new_registration=Registration_frame(self.root)
                        new_registration.get_user_data(self.entry_12.get())
                        self.new_login_frame.destroy()
                else:
                    login_status=0
                    messagebox.showerror("Error", "Invalid username or password", parent=self.root)
        except mysql.connector.Error as error:
            messagebox.showerror("Internal Error", "To reset your paasword click on forgot password ", parent=self.root)

#     def user_back_btn_action(self):
#         self.label_18.destroy()
#         self.label_19.destroy()
#         self.label_20.destroy()
#         self.entry_12.destroy()
#         self.entry_13.destroy()
#         self.user_login_btn.destroy()
#         self.user_back_btn.destroy()
#         self.user_page()
#
# #
#
# #
# # # health report
# #
# #         label_0 = Label(root,bg='light grey', text="HEALTH REPORT", width=30,fg="BLACK", font=("CHARLESWORTH", 30, "bold"))
# #         label_0.place(x=250, y=10)
# #
# #         disease_bp = Label(root,bg='light grey', text="Do you have Blood Pressure?", width=30, font=("garamond", 25, "bold"))
# #         disease_bp.place(x=10, y=100)
# #         self.var = StringVar()
# #         Radiobutton(root,bg='light grey', text="YES", padx=20, variable=self.var, value=1, font=("garamond", 15, "bold")).place(x=580,y=103)
# #         Radiobutton(root,bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700,y=103)
# #         Radiobutton(root,bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820,y=103)
# #
# #         disease_cancer = Label(root, bg='light grey', text="Do you have any type of Cancer?", width=30, font=("garamond", 25, "bold"))
# #         disease_cancer.place(x=10, y=160)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580,y=163)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700,y=163)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820,y=163)
# #
# #         disease_diabetes = Label(root, bg='light grey', text="Do you have Diabetes Mellitus?", width=30,font=("garamond", 25, "bold"))
# #         disease_diabetes.place(x=10, y=220)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=223)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=223)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=223)
# #
# #         disease_lipid = Label(root, bg='light grey', text="Do you have Lipid Disorder?", width=30,font=("garamond", 25, "bold"))
# #         disease_lipid.place(x=10, y=280)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=283)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700, y=283)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820, y=283)
# #
# #         disease_kidney = Label(root, bg='light grey', text="Do you have Kidney Disease?", width=30,font=("garamond", 25, "bold"))
# #         disease_kidney.place(x=10, y=340)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=343)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=343)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=343)
# #
# #         disease_heart = Label(root, bg='light grey', text="Do you have any type heart disease?", width=30, font=("garamond", 25, "bold"))
# #         disease_heart.place(x=10, y=400)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=403)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2, font=("garamond", 15, "bold")).place(x=700, y=403)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3, font=("garamond", 15, "bold")).place(x=820, y=403)
# #
# #         disease_allergies = Label(root, bg='light grey', text="Do you have any type allergies?", width=30,font=("garamond", 25, "bold"))
# #         disease_allergies.place(x=10, y=460)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=463)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=463)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=463)
# #
# #         disease_allergies = Label(root, bg='light grey', text="Are you tested covid positive before?", width=30,font=("garamond", 25, "bold"))
# #         disease_allergies.place(x=10, y=520)
# #         self.var = StringVar()
# #         Radiobutton(root, bg='light grey', text="YES", padx=20, variable=self.var, value=1,font=("garamond", 15, "bold")).place(x=580, y=523)
# #         Radiobutton(root, bg='light grey', text="NO", padx=20, variable=self.var, value=2,font=("garamond", 15, "bold")).place(x=700, y=523)
# #         Radiobutton(root, bg='light grey', text="DON'T KNOW", padx=20, variable=self.var, value=3,font=("garamond", 15, "bold")).place(x=820, y=523)
# #
# #         Button(root, text='Cancel', width=10, bg='Yellow', fg='black', font=("CHARLESWORTH", 15, "bold")).place(x=400, y=590)
# #         Button(root, text='Submit', width=10, bg='Yellow', fg='black', font=("CHARLESWORTH", 15, "bold")).place(x=750, y=590)
# #
# #
