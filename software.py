from tkinter import *
from tkinter import ttk, messagebox
import time
import os


class File_App:
    def __init__(self, root):
        self.root=root
        self.root.title('Record System App')
        self.root.geometry('1350x700+0+0')

        title=Label(self.root, text='Record System App', font=('Times New Roman', 35, 'bold'), bd=10, relief=GROOVE, pady=10)
        title.pack(fill=X)

        frame_st=Frame(self.root, bd=10, relief=GROOVE)
        frame_st.place(x=20, y=100, height=400)

        title_st=Label(frame_st, text='Student details', font=('Times New Roman', 26, 'bold'))
        lbl_sid=Label(frame_st, text='Student ID', font=('Times New Roman', 18, 'bold'))
        txt_sid=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_name=Label(frame_st, text='Name', font=('Times New Roman', 18, 'bold'))
        txt_name=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_phone=Label(frame_st, text='Phone number', font=('Times New Roman', 18, 'bold'))
        txt_phone=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_date=Label(frame_st, text='Date (dd/mm/yyyy)', font=('Times New Roman', 18, 'bold'))
        txt_date=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_course=Label(frame_st, text='Course', font=('Times New Roman', 18, 'bold'))
        txt_course=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_address=Label(frame_st, text='Address', font=('Times New Roman', 18, 'bold'))
        txt_address=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_city=Label(frame_st, text='City', font=('Times New Roman', 18, 'bold'))
        txt_city=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15, justify='center')
        lbl_deg=Label(frame_st, text='Select degree', font=('Times New Roman', 18, 'bold'))
        combo_deg=ttk.Combobox(frame_st, font=('Arial', 15, 'bold'), state='readonly', width=14)
        combo_deg['values']=('No degree', 'Bch', 'MSc', 'PHD', 'Prof')
        lbl_id_p=Label(frame_st, text='ID proof', font=('Times New Roman', 18, 'bold'))
        combo_id_p=ttk.Combobox(frame_st, font=('Arial', 15, 'bold'), state='readonly', width=14)
        combo_id_p['values']=('ID Card', 'Driver licence', 'Student ID card', 'Military ID card')
        lbl_payment=Label(frame_st, text='Payment mode', font=('Times New Roman', 18, 'bold'))
        combo_payment=ttk.Combobox(frame_st, font=('Arial', 15, 'bold'), state='readonly', width=14)
        combo_payment['values']=('Cash', 'Debit card', 'Credit card', 'Bank transfer', 'Blik')

        title_st.grid(row=0, column=0, padx=5, pady=20, columnspan=4)
        lbl_sid.grid(row=1, column=0, padx=5, pady=20)
        txt_sid.grid(row=1, column=1, padx=10, pady=5)
        lbl_name.grid(row=2, column=0, padx=5, pady=10)
        txt_name.grid(row=2, column=1, padx=10, pady=5)
        lbl_phone.grid(row=1, column=2, padx=5, pady=10)
        txt_phone.grid(row=1, column=3, padx=10, pady=5)
        lbl_date.grid(row=2, column=2, padx=5, pady=10)
        txt_date.grid(row=2, column=3, padx=10, pady=5)
        lbl_course.grid(row=3, column=0, padx=5, pady=10)
        txt_course.grid(row=3, column=1, padx=10, pady=5)
        lbl_address.grid(row=4, column=0, padx=5, pady=10)
        txt_address.grid(row=4, column=1, padx=10, pady=5)
        lbl_city.grid(row=5, column=0, padx=5, pady=10)
        txt_city.grid(row=5, column=1, padx=10, pady=5)
        lbl_deg.grid(row=3, column=2, padx=5, pady=10)
        combo_deg.grid(row=3, column=3, padx=5, pady=10)
        lbl_id_p.grid(row=4, column=2, padx=5, pady=10)
        combo_id_p.grid(row=4, column=3, padx=5, pady=10)
        lbl_payment.grid(row=5, column=2, padx=5, pady=10)
        combo_payment.grid(row=5, column=3, padx=5, pady=10)


root=Tk()
obj=File_App(root)
root.mainloop()