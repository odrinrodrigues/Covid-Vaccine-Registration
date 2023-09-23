#####---Registration Form
import tkinter
from datetime import datetime
from tkinter import*

from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta
import calendar
from tkinter import messagebox
from tkinter import ttk
from conn import Conndb
from loggperson import login_userdata
from scheduler import schedul_date_check

class Registration_frame:
    def __init__(self, root):

        self.root=root
        self.root.title("Registration Form")
        self.root.geometry('1200x680')


        ##########--Form
        # global self.Form
        self.Form=Frame(root)
        self.Form.place(x=0,y=0,width=1200,height=680)
        self.Form.config(bg='lightgrey')

        ##--Fetching data  DATE_FORMAT(birth_date,'%m-%d-%Y')
    def get_user_data(self,i_uid):

        self.i_uid=i_uid
        userdat_table = """select * from userdata where uid=%s """
        self.new_db_con = Conndb
        self.new_db_con.curs.execute(userdat_table, (self.i_uid,))
        login_result = self.new_db_con.curs.fetchone()
        self.new_login=login_userdata
        data_lenght=0
        for i in self.new_login.user_detail.keys():
            if data_lenght <=len(login_result):
                self.new_login.user_detail[i]=login_result[data_lenght]
                data_lenght=data_lenght+1



        ##--Lables

        # name_lbl=Label(Form,text="Name",bg='lightgrey',font=("garamond",15,"bold")).place(x=100,y=30)6++
        first_name = Label(self.Form, text='First Name',bg='lightgrey', font=("garamond", 15, "bold")).place(x=100,y=50)
        middle_name = Label(self.Form, text='Middel Name',bg='lightgrey', font=("garamond", 15, "bold")).place(x=100,y=100)
        last_name = Label(self.Form, text='Last Name',bg='lightgrey', font=("garamond", 15, "bold")).place(x=100, y=150)

        ##--Entryname

        self.first_name_entry=Entry(self.Form,width=20,font=("garamond",15,"bold"))
        self.first_name_entry.insert(0,self.new_login.user_detail['fname'])
        self.first_name_entry.config(state='disabled')
        self.first_name_entry.place(x=240,y=50)
        self.middle_name_entry=Entry(self.Form,width=20,font=("garamond",15,"bold"))
        self.middle_name_entry.insert(0,self.new_login.user_detail['mname'])
        self.middle_name_entry.config(state='disabled')
        self.middle_name_entry.place(x=240,y=100)
        self.last_name_entry=Entry(self.Form,width=20,font=("garamond",15,"bold"))
        self.last_name_entry.insert(0,self.new_login.user_detail['lname'])
        self.last_name_entry.config(state='disabled')
        self.last_name_entry.place(x=240,y=150)



        ##--UID
        uid_lbl = Label(self.Form, text="Adhar Number", bg='lightgrey', font=("garamond", 15, "bold")).place(x=100, y=200)
        self.uid_entry = Entry(self.Form, width=20, font=("garamond", 15, "bold"))
        self.uid_entry.insert(0,self.new_login.user_detail['uid'])
        self.uid_entry.config(state='disabled')
        self.uid_entry.place(x=240, y=200)


        ##--phone
        phone_lbl = Label(self.Form, text="Phone Number", bg='lightgrey', font=("garamond", 15, "bold")).place(x=100, y=250)

        self.phone_entry = Entry(self.Form, width=20, font=("garamond", 15, "bold"))
        self.phone_entry.insert(0,self.new_login.user_detail['phone_number'])
        self.phone_entry.config(state='disabled')
        self.phone_entry.place(x=240, y=250)


        #--DOB
        dob_lbl = Label(self.Form, text="Date Of Birth", bg='lightgrey', font=("garamond", 15, "bold")).place(x=100, y=300)
        Dob=self.new_login.user_detail['birth_date'].strftime('%d-%m-%Y')
        self.Dob_entry = DateEntry(self.Form,day=int(self.new_login.user_detail['birth_date'].strftime('%d')),month=
                                   int(self.new_login.user_detail['birth_date'].strftime('%m')),
                                   year=int(self.new_login.user_detail['birth_date'].strftime('%Y'))
                                   , width=15,date_pattern='dd-mm-yyyy',
        background='black', foreground='white', borderwidth=3,
                            )
        self.Dob_entry.config(state='disabled')
        # self.Dob_entry.insert(0,Dob)
        self.Dob_entry.place(x=240, y=300)


        ##-Gender

        gender_lable=Label(self.Form,text='Gender',font=("garamond", 15, "bold")
                           ,bg='lightgrey').place(x=100, y=350)
        self.gender = StringVar(value=self.new_login.user_detail['gendder'])


        Radiobutton(self.Form, text="Male",selectcolor='red', padx=5, variable=self.gender, value="Male" ,font=("garamond", 10, "bold")
                           ,bg='lightgrey',state='disabled').place(x=240, y=350)



        Radiobutton(self.Form, text="Female", padx=20,selectcolor='red',state='disabled', variable=self.gender, value="Female",font=("garamond", 10, "bold")
                           ,bg='lightgrey').place(x=300, y=350)



        Radiobutton(self.Form, text="Other", padx=20 ,selectcolor='red',state='disabled', variable=self.gender, value="Other",font=("garamond", 10, "bold")
                           ,bg='lightgrey').place(x=385, y=350)



        ##---Email
        email_lbl=Label(self.Form,text='Email',font=("garamond", 15, "bold")
                           ,bg='lightgrey').place(x=100, y=400)

        self.email_entry = Entry(self.Form, width=30, font=("garamond", 13, "bold"))
        self.email_entry.insert(0,self.new_login.user_detail['e_mail'])
        self.email_entry.config(state='disabled')
        self.email_entry.place(x=240, y=400)

        ##---Address
        addrs_lbl=Label(self.Form,text='Address',font=("garamond", 15, "bold")
                           ,bg='lightgrey').place(x=100, y=450)

        self.street_ddrs_entry1 = Entry(self.Form, width=30, font=("garamond", 13, "bold"))

        self.street_ddrs_entry1.place(x=240, y=450)
        self.street_ddrs_entry2 = Entry(self.Form, width=15, font=("garamond", 13, "bold"))

        self.street_ddrs_entry2.place(x=240, y=480)
        self.street_ddrs_entry3 = Entry(self.Form, width=20, font=("garamond", 13, "bold"))

        self.street_ddrs_entry3.place(x=240, y=510)
        self.street_ddrs_entry4 = Entry(self.Form, width=15, font=("garamond", 13, "bold"))
        self.street_ddrs_entry4.place(x=240, y=540)


        ##-Submit Button
        self.Continue_bttn1=Button(self.Form,text='Confirm Address',width=15,height=1,command=self.Continue_button1,font=("garamond", 13, "bold"),bg='green')
        self.Continue_bttn1.place(x=270, y=580)
        self.Form.update()
        

    def Continue_button1(self):
        if ((self.street_ddrs_entry1.get() != 'street' and self.street_ddrs_entry2.get() != 'city')
                and (
                        self.street_ddrs_entry3.get() != 'state') and self.street_ddrs_entry4.get() != 'Pincode'):

            self.new_login.user_address['street'] = self.street_ddrs_entry1.get()
            self.new_login.user_address['city'] = self.street_ddrs_entry2.get()
            self.new_login.user_address['state'] = self.street_ddrs_entry3.get()
            self.new_login.user_address['pincode'] = self.street_ddrs_entry4.get()
            self.new_login.user_address['uid'] = self.i_uid
            #
            # self.street_ddrs_entry1.config(state='disabled')
            # self.street_ddrs_entry2.config(state='disabled')
            # self.street_ddrs_entry3.config(state='disabled')
            # self.street_ddrs_entry4.config(state='disabled')
            MsgBox = tkinter.messagebox.askquestion('Confirm Details', 'You are about to confirm given details',
                                                    icon='warning')
            if MsgBox == 'yes':
                    print('None inserting')
                    try:
                        insert_addrss_conn=Conndb
                        insert_addrss = """insert into user_address values(%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE street=%s,city=%s,state=%s,pincode=%s """
                        insert_addrss_conn.curs.execute(insert_addrss, list(self.new_login.user_address.values()))
                        self.new_db_con.conn.commit()
                        print('Inserted')
                        self.select_center()
                        self.Continue_bttn1.destroy()
                        print(list(self.new_login.user_address.values()))
                    except:
                        print('Insert Error')
                    finally:
                        insert_addrss_conn.conn.close()

        else:
            tkinter.messagebox.showinfo(title='Address invalid',
                                        message='All Address field are required!', icon='info')



    def select_center(self):

        select_type_lble=Label(self.Form,text='Select Vaccine center',font=("garamond", 15, "bold")
                           ,bg='lightgrey')
        select_type_lble.place(x=600,y=50)

        select_center_type=Label(self.Form,text='Private / Gov',font=("garamond", 12, "bold")
                           ,bg='lightgrey')
        select_center_type.place(x=600,y=80)


        self.center_type_value = tkinter.StringVar()
        self.center_type = ttk.Combobox(self.Form, width=15, textvariable=self.center_type_value,state='readonly')
        self.center_type.place(x=600,y=110)

        self.center_type['values'] = ('Private','Gov'
                                )
        self.center_type_next_btn=Button(self.Form,text='Next',width=10,height=1,command=self.next_Button_hsptl,font=("garamond", 13, "bold"),bg='green')
        self.center_type_next_btn.place(x=720, y=160)

    def next_Button_hsptl(self):
        if self.center_type.get()=="":
            print("No type selected")
        elif self.center_type.get() is not None:
            self.center_type_next_btn.destroy()
            self.center_type.config(state='disabled')
            self.center_hsptl_btn = Button(self.Form, text='Next', width=10, height=1,
                                               command=self.Continue_button2, font=("garamond", 13, "bold"),
                                               bg='green')

            ###--Fetch Hospitals
            fetch_hsptl_centers="""Select * from hospital where h_type=%s and h_city=%s"""
            center_pref=(self.center_type_value.get(),self.new_login.user_address['city'])
            self.new_db_con.curs.execute(fetch_hsptl_centers,(center_pref))
            self.center_data=self.new_db_con.curs.fetchall()
            print(self.center_data)

            self.center_hsptl_btn.place(x=720, y=160)
            select_center_hsptl = Label(self.Form, text='Center', font=("garamond", 12, "bold")
                                        , bg='lightgrey')
            select_center_hsptl.place(x=800, y=80)
            self.center_name = tkinter.StringVar()

            self.center_selection = ttk.Combobox(self.Form, width=28, textvariable=self.center_name, state='readonly')
            self.center_selection.place(x=800, y=110)
            self.center_names=[]
            for i in range(len(self.center_data)):
                i=self.center_data[i][1]
                self.center_names.append(i)
            # print(self.center_names)
            self.center_selection['values'] = self.center_names


    def Continue_button2(self):
        if self.center_selection.get() == '':
            tkinter.messagebox.showinfo(title='Center empty', message='Please select center near you.')

        elif self.center_selection.get() is not None:
            MsgBox = tkinter.messagebox.askquestion('Confirm Center', 'You are about to confirm this Centre',
                                                    icon='warning')
            if MsgBox == 'yes':
                print("details not saved"
                      "")
                self.center_selection.config(state='disabled')
                self.center_hsptl_btn.destroy()

            else:
                print("details not saved"
                      "")


    def dose_date(self):



        select_dose_lbl = Label(self.Form, text="Select suitable date for 1st dose", bg='lightgrey', font=("garamond", 15, "bold")).place(x=600, y=210)

        dose_date = Label(self.Form, text="1st Dose date", bg='lightgrey', font=("garamond", 15, "bold")).place(x=600, y=250)
        self.dose_date_entry = DateEntry(self.Form, width=15,date_pattern='dd-mm-yyyy',
        background='black', foreground='white', borderwidth=3,weekendbackground = 'yellow',state='readonly',
                              todaybackground='red')
        self.dose_date_entry.place(x=780,y=255)

        self.center_type_next_btn=Button(self.Form,text='Check',width=9,height=1,command=self.validate_date,font=("garamond", 10, "bold"),bg='green')
        self.center_type_next_btn.place(x=910,y=252)

    def validate_date(self):
        print('selected date',self.dose_date_entry.get_date().strftime('%d-%m-%Y'))
        if self.dose_date_entry.get_date()< datetime.today().date() or\
                (self.dose_date_entry.get_date()-datetime.today().date()).days>28:
            tkinter.messagebox.showinfo(title='Holiday', message=f'Please select Valid Date')

        else:
            newdate=schedul_date_check
            selected_date,status=newdate.check_new_date(self.dose_date_entry.get_date())
            if (status=='Holiday'):
                tkinter.messagebox.showinfo(title='Holiday', message=f'Selected day is a weekend holiday ')
            elif status=='Working':
                MsgBox = tkinter.messagebox.askquestion('Confirm ', 'For vaccine shot you have to visit selected center between 11:00 AM to 3:00 PM',
                                                        icon='info')
                if MsgBox == 'yes':
                    print("details not saved"
                          "")
                    self.center_type_next_btn.destroy()
                    self.finish_btn = Button(self.Form, text='Finish', width=15, height=1,
                                             command=self.confirm_registration, font=("garamond", 13, "bold"), bg='green')
                    self.finish_btn.place(x=700, y=400)
                else:
                    print("details not saved"
                          "")

            print(status)

    def confirm_registration(self):
        insert_reg_detail="""insert in """
        # self.new_db_con.







