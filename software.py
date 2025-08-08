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
        frame_st.place(x=20, y=100, width=800, height=400)

        title_st=Label(frame_st, text='Student details', font=('Times New Roman', 18, 'bold'))
        lbl_sid=Label(frame_st, text='Student ID', font=('Times New Roman', 18, 'bold'))
        txt_sid=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15)
        lbl_name=Label(frame_st, text='Name', font=('Times New Roman', 18, 'bold'))
        txt_name=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15)
        lbl_phone=Label(frame_st, text='Phone number', font=('Times New Roman', 18, 'bold'))
        txt_phone=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15)
        lbl_date=Label(frame_st, text='Date (dd/mm/yyyy)', font=('Times New Roman', 18, 'bold'))
        txt_date=Entry(frame_st, font=('Arial', 15, 'bold'), bd=7, relief=GROOVE, width=15)

        title_st.grid(row=0, column=0, padx=5, pady=20)
        lbl_sid.grid(row=1, column=0, padx=5, pady=20)
        txt_sid.grid(row=1, column=1, padx=10, pady=5)
        lbl_name.grid(row=2, column=0, padx=5, pady=10)
        txt_name.grid(row=2, column=1, padx=10, pady=5)
        lbl_phone.grid(row=1, column=2, padx=5, pady=10)
        txt_phone.grid(row=1, column=3, padx=10, pady=5)
        lbl_date.grid(row=2, column=2, padx=5, pady=10)
        txt_date.grid(row=2, column=3, padx=10, pady=5)


root=Tk()
obj=File_App(root)
root.mainloop()