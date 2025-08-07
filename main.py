from tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root=root
        self.root.title('Record System')
        self.root.geometry('1350x700+0+0')

        # Logging frame
        frame1=Frame(self.root, bd=10, relief=GROOVE)
        frame1.place(x=450, y=150, width=450, height=400)

        self.user=StringVar()
        self.password=StringVar()

        title=Label(frame1, text='Login System', font=('Times New Roman', 28, 'bold'))
        user_lbl=Label(frame1, text='User', font=('Times New Roman', 20, 'bold'))
        password_lbl=Label(frame1, text='Password', font=('Times New Roman', 20, 'bold'))
        user_ent=Entry(frame1, textvariable=self.user, font=('Arial', 14, 'bold'), bd=7, relief=GROOVE, width=15)
        password_ent=Entry(frame1, textvariable=self.password, show='·', font=('Arial', 14, 'bold'), bd=7, relief=GROOVE, width=15)
        log_btn=Button(frame1, text='Login', font=('Arial', 16, 'bold'), bd=7, width=7, command=self.logging)
        reset_btn=Button(frame1, text='Reset', font=('Arial', 16, 'bold'), bd=7, width=7, command=self.reset)
        exit_btn=Button(frame1, text='Exit', font=('Arial', 16, 'bold'), bd=7, width=7, command=self.exit)

        title.grid(row=0, column=0, columnspan=2, padx=(0, 110), pady=(20, 10))
        user_lbl.grid(row=1, column=0, padx=(5, 0), pady=(50, 5))
        password_lbl.grid(row=2, column=0, padx=(60, 0), pady=1)
        user_ent.grid(row=1, column=1, padx=(0, 200), pady=(50, 5))
        password_ent.grid(row=2, column=1, padx=(0, 200), pady=1)
        log_btn.grid(row=3, column=0, columnspan=2, padx=(0, 110), pady=20)
        reset_btn.place(x=100, y=310)
        exit_btn.place(x=230, y=310)