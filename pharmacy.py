from tkinter import *
from tkinter import messagebox
import os
import random
from datetime import date
import sys
import time

def hospital():
    coming = Toplevel()
    coming.geometry('500x500+100+100')
    space = Label(coming,text="         ")
    space.pack() 
    com = Label(coming,text = "Coming Soon!")
    com.config(font = ('Lucida Console', 30,'bold'))
    com.pack()
def reset_patient():
    ref_e.config(state=NORMAL)
    ref_e.delete(0,END)
    num = random.randint(100000,999999)
    ref_e.insert(0,str(num))
    ref_e.config(state=DISABLED)

    fname_e.delete(0,END)
    sname_e.delete(0,END)
    address_e.delete(0,END)
    tele_e.delete(0,END)

    payment.set("Master Card")
    member.set("Annual membership")
    proof.set("PAN Card")
    
def receipt_print():
    reference_num = ref_e.get()
    first_name = fname_e.get()
    last_name = sname_e.get()
    address = address_e.get()
    date = str(today)
    telephone_num = tele_e.get()
    fees = fees_e.get()
    if payment == "Master Card" or "Credit Card" or "Debit Card":
        pay_status = "Paid"
    elif payment == "Manual":
        pay_status = "Not Paid"

    space = "                      "
    rec.insert(1,reference_num+space+first_name+space+last_name+space+address+space+date+space+telephone_num+space+pay_status+space+fees)



def exit_c():
    patient_reg.destroy()
    
def patient():
    global patient_reg
    global ref_e
    global date_e
    global frame3
    global ref_num
    global fname_e
    global sname_e
    global address_e
    global tele_e
    global today
    global payment
    global fees_e
    global rec
    global proof
    global member
    
    patient_reg = Toplevel(win)
    patient_reg.title("Patient Registration System")
    patient_reg.geometry("1350x700+0+0")
    
    patient_label = Label(patient_reg,text = "Patient Registration System",font=('arial',50,'bold'))
    patient_label.pack()
    
    frame1 = Frame(patient_reg,height=1000,width=1500,bd=20,relief='ridge')
    frame1.pack()
    
    frame2 = Frame(frame1,height=570,width=430,bd=15,relief='ridge')
    frame2.grid(row=1,column=1)
    
    frame3 = Frame(frame1,height=570,width=870,bd=15,relief='ridge')
    frame3.grid(row=1,column=2)

    ref_num = random.randint(100000,999999)
    
    reference_num = Label(frame2,text = "Reference Number",font=('arial',15,'bold'))
    reference_num.grid(row=1,column=1,sticky=W)
    
    ref_e = Entry(frame2,bd=8,font=('arial',15,'bold'))
    ref_e.insert(0,str(ref_num))
    ref_e.config(state=DISABLED)
    ref_e.grid(row=1,column=2,pady=5)

    fname_l = Label(frame2,text="First Name",font=('arial',15,'bold'))
    fname_l.grid(row=2,column=1,sticky=W)

    fname_e = Entry(frame2,bd=8,font=('arial',15,'bold'))
    fname_e.grid(row=2,column=2,pady=5)

    
    sname_l = Label(frame2,text="Last Name",font=('arial',15,'bold'))
    sname_l.grid(row=3,column=1,sticky=W)

    sname_e = Entry(frame2,bd=8,font=('arial',15,'bold'))
    sname_e.grid(row=3,column=2,pady=5)

    address_l = Label(frame2,text="Address",font=('arial',15,'bold'))
    address_l.grid(row=4,column=1,sticky=W)

    address_e = Entry(frame2,bd=8,font=('arial',15,'bold'))
    address_e.grid(row=4,column=2,pady=5)

    tele_l = Label(frame2,text="Telephone",font=('arial',15,'bold'))
    tele_l.grid(row=5,column=1,sticky=W)

    tele_e = Entry(frame2,bd=8,font=('arial',15,'bold'))
    tele_e.grid(row=5,column=2,pady=5)

    today = str(date.today())

    date_l = Label(frame2,text="Date",font=('arial',15,'bold'))
    date_l.grid(row=6,column=1,sticky=W)

    date_e = Entry(frame2,bd=8,font=('arial',15,'bold'))
    date_e.insert(0,today)
    date_e.config(state=DISABLED)
    date_e.grid(row=6,column=2,pady=5)

    proof_l = Label(frame2,text = "ID Proof",font=('arial',15,'bold'))
    proof_l.grid(row=7,column=1,sticky=W)

    
    proof = StringVar()


    proof.set("PAN Card")
    proof_s = OptionMenu(frame2,proof,"Driving Liscence","PAN Card","Aadhar Card","Passport")
    proof_s.config(width=18, font=('arial', 15))
    proof_s.grid(row=7,column=2)

    membership_l = Label(frame2,text = "Membership",font=('arial',15,'bold'))
    membership_l.grid(row=8,column=1,sticky=W)

    member = StringVar()

    member.set("Annual membership")
    
    membership_s = OptionMenu(frame2,member,"annual membership","monthly membership","one time membership")
    membership_s.config(width=18, font=('arial', 15))
    membership_s.grid(row=8,column=2)

    payment_l = Label(frame2,text = "Mode Of Payment",font=('arial',15,'bold'))
    payment_l.grid(row=9,column=1)

    payment = StringVar()

    payment.set("Master Card")

    payment_s = OptionMenu(frame2,payment,"Credit Card","Manual","Debit Card","Master Card")
    payment_s.config(width=18, font=('aria;',15))
    payment_s.grid(row=9,column=2)

    fees_l = Label(frame2,text = "Payment Fees",font=('arial',15,"bold"))
    fees_l.grid(row=10,column=1,sticky=W)

    fees_e = Entry(frame2,font=('arial',15,'bold'))
    fees_e.insert(0,"₹500")
    fees_e.config(state=DISABLED)
    fees_e.grid(row=10,column=2)





    
   
    pat_ref_l = Label(frame3,text = "Patient Ref",bg = "gainsboro",padx=15,pady=20)
    pat_ref_l.grid(row=1,column=1)

    fname_l = Label(frame3,text = "First Name",bg = "gainsboro",padx=15,pady=20)
    fname_l.grid(row=1,column=2)

    sname_l = Label(frame3,text = "Last Name",bg = "gainsboro",padx=15,pady=20)
    sname_l.grid(row=1,column=3)

    addre_l = Label(frame3,text = "Address",bg = "gainsboro",padx=15,pady=20)
    addre_l.grid(row=1,column=4)

    reg_date_l = Label(frame3,text = "Reg Date",bg = "gainsboro",padx=15,pady=20)
    reg_date_l.grid(row=1,column=5)

    telephone_l = Label(frame3,text = "Telephone",bg = "gainsboro",padx=15,pady=20)
    telephone_l.grid(row=1,column=6)

    payment_sta_l = Label(frame3,text = "Payment Status",bg = "gainsboro",padx=15,pady=20)
    payment_sta_l.grid(row=1,column=7)

    fees_l = Label(frame3,text = "Fees",bg = "gainsboro",padx=15,pady=20)
    fees_l.grid(row=1,column=8)


    rec = Listbox(frame3,height=25,width=112)

    rec.grid(row=2,column=1,columnspan=8)

    exit_b = Button(frame3,text = "Exit",font=('arial',20),padx=50,command=exit_c)
    exit_b.grid(row=3,column=1,columnspan=2)

    receipt_b = Button(frame3,text="Receipt",font=("arial",20),padx=30,command=receipt_print)
    receipt_b.grid(row=3,column=3,columnspan=4)

    reset_b = Button(frame3, text="Reset",font=("arial",20),padx=50,command=reset_patient)
    reset_b.grid(row=3,column=6,columnspan=4)
    
def button_active():
    patient_info.config(state=ACTIVE)
    hospital_info.config(state=ACTIVE)
def login():
  
    username = user_entry.get()
    password = pass_entry.get()
    list_of_files = os.listdir()
    user_entry.delete(0,END)
    pass_entry.delete(0,END)
  
    if username in list_of_files:
        file = open(username,"r")
        verify = file.read().splitlines()
        if password in verify:
            button_active()
            messagebox.showinfo("Success","Login Succesful")
        else:
            messagebox.showerror("Error","The password you have entered is invalid")
    else:
        messagebox.showerror("Error","The Username you have entered is invalid")
        
def reset_sign():
    user_entry1.delete(0,END)
    pass_entry1.delete(0,END)
    

def sign_new():
    
        
    username = user_entry1.get()
    password = pass_entry1.get()
    list_file = os.listdir()
    if username in list_file:
        user_same = Label(sign_in, text = "Username already exists", fg = "red")
        user_same.config(font= ("Arial Tur","15"))
        user_same.grid(row=6,column=1)
    else:
        file = open(username, "w")
        file.write(username)
        space = " \n"
        file.write(space)
        file.write(password)
        file.close()
        user_entry1.delete(0,END)
        pass_entry1.delete(0,END)

        reg_success = Label(sign_in, text = "Registration Success!",fg = "Green")
        reg_success.config(font= ("Arial Tur","15"))
        reg_success.grid(row=6,column=1)
    
        
def sign_up():
    global user_entry1
    global pass_entry1
    
    global sign_in
    sign_in = Toplevel(win)
    sign_in.title("Sign Up")
    sign_in.geometry("500x300+0+0")
    
    sign_heading = Label(sign_in,text = "Fill the following details",font=('arial',25,'bold'))
    sign_heading.grid(row=1,column=1,columnspan=2)

    user_label = Label(sign_in, text = "Enter Username",font=('arial',15,'bold'))
    user_label.grid(row=2,column=1)

    user_entry1 = Entry(sign_in, bd=10,font=('arial',15,'bold'))
    user_entry1.grid(row=2,column=2)

    pass_label = Label(sign_in, text = "Enter Password",font=('arial',15,'bold'))
    pass_label.grid(row=3,column=1)
    
    pass_entry1 = Entry(sign_in, bd=10,font=('arial',15,'bold'),show = "\u2022")
    pass_entry1.grid(row=3,column=2)

    reset_b = Button(sign_in,text = "Reset", bd=10,font=('arial',15,'bold'),command = reset_sign)
    reset_b.grid(row=5,column=1)

    show_b = Button(sign_in,text = "Sign Up",bd=10,font=('arial',15,'bold'),command = sign_new)
    show_b.grid(row=5,column=2)
def reset():
    user_entry.delete(0,END)
    pass_entry.delete(0,END)
    patient_info.config(state=DISABLED)
    hospital_info.config(state=DISABLED)
def main_scr():
    global user_entry
    global pass_entry
    global win
    global patient_info
    global hospital_info
    win = Tk()
    win.title("Hospital Registration System")
    win.geometry("1350x750+0+0")
    heading = Label(win,text = "Pharmacy Management System",font=("arial",50,"bold"),bd=20)
    heading.pack()
    
    login_frame = Frame(win,bd=20,relief='ridge',height=300,width=1350)
    login_frame.pack()
    
    button_frame = Frame(win,bd=20,relief='ridge',height=100,width=500)
    button_frame.pack()

    button_frame1 = Frame(win,bd=20,relief='ridge',height=100,width=700)
    button_frame1.pack()
    
    user_label = Label(login_frame,text = "Enter Username ",font=("arial",25),bd=20)
    user_label.grid(row=1,column=1)
    
    user_entry = Entry(login_frame,bd=13,font=('arial',25,"bold"))
    user_entry.grid(row=1,column=2,padx=70,pady=5)
    
    pass_label = Label(login_frame,text = "Enter Password ",font=('arial',25),bd=20)
    pass_label.grid(row=2,column=1)
    
    pass_entry = Entry(login_frame,bd=13,font=('aria;',25,'bold'),show = "\u2022")
    pass_entry.grid(row=2,column=2,padx=70,pady=5)

    login_b = Button(button_frame,text = "LOGIN",width=10,pady=10,font=('arial',20,'bold'),command = login)
    login_b.grid(row=0,column=0)

    sign_up_b = Button(button_frame,text = "SIGN UP",width=10,pady=10,font=('arial',20,'bold'),command = sign_up)
    sign_up_b.grid(row=0,column=1)

    reset_b = Button(button_frame,text = "RESET",width=10,pady=10,font=('arial',20,'bold'),command = reset)
    reset_b.grid(row=0,column=2)

    patient_info = Button(button_frame1,text = "Patients Registration System",state = DISABLED,font=('arial',20,'bold')
                          ,command = patient)
    patient_info.grid(row=1,column=1)
    
    hospital_info = Button(button_frame1,text = "Hospital Management Systems",state = DISABLED,font=('arial',20,'bold')
                           ,command=hospital)
    hospital_info.grid(row=1,column=2)
    win.mainloop()
    
    
main_scr()


