from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

def generate():
    poor=string.ascii_uppercase+string.ascii_lowercase
    average=poor+string.digits
    advanced=average+" "+string.punctuation

    try:
        choice=x.get()
        length=int(lenField.get())

        if choice==1:
            pwd="".join(random.sample(poor,length))
        elif choice==2:
            pwd="".join(random.sample(average,length))
        elif choice==3:
            pwd="".join(random.sample(advanced,length))
        else:
            messagebox.showwarning(title="WARNING!",message="Please Choose Password Strength!")
            pwd=""

        pwdField.delete(0,END)
        pwdField.insert(0,pwd)
        
    except ValueError:
        messagebox.showerror(title="Value Error",message="Enter a Valid Length!")

def accept():
    if pwdField.get()=="":
        messagebox.showerror(title="Password Error",message="Generate the Password to Accept it!")
    elif len(nameField.get())==0:
        messagebox.showwarning(title="WARNING!",message="Please Specify User Name!")
    elif pwdField.get()!="" and nameField.get():
        msg=nameField.get()+" !  Your Password is : "+pwdField.get()
        acpt_label.config(text=msg)
    
def reset():
    nameField.delete(0,END)
    lenField.delete(0,END)
    pwdField.delete(0,END)
    x.set(0)
    acpt_label.config(text="")
    paste_label.config(text="")

def copy():
    if pwdField.get():
        pyperclip.copy(pwdField.get())
        paste_label.config(text="Copied Password is : "+pyperclip.paste())
    else:
        messagebox.showerror(title="Password Error",message="Generate the Password to Copy it")



if __name__=="__main__":

    window=Tk()

    window.title("Random Password Generator")
    window.geometry("600x600")
    window.config(bg="#FFF4E6")

    font1=("Baskerville Old Face",17)

    title_label=Label(window,text="Random Password Generator",font=("Baskerville Old Face",30,"bold"),fg="light yellow",bg="#1D4D6B",width=50,height=2)
    title_label.pack()

    name_label=Label(window,text="Enter your Name  ",font=font1,bg="#FFF4E6")
    name_label.place(x=350,y=140)

    nameField=Entry(window,width=40,font=font1,fg="#242528")
    nameField.place(x=850,y=140)

    len_label=Label(window,text="Enter Length of the Password  ",font=font1,bg="#FFF4E6")
    len_label.place(x=350,y=200)

    lenField=Spinbox(window,from_=4,to_=32,font=font1,width=38,fg="#242528")
    lenField.place(x=850,y=200)

    strength_label=Label(window,text="Password Strength ",font=font1,bg="#FFF4E6")
    strength_label.place(x=350,y=260)

    x=IntVar()
    weak_pw=Radiobutton(window,text="Poor",font=("Bell MT",16,"bold"),variable=x,value=1,fg="#242528",bg="#FFF4E6")

    medium_pw=Radiobutton(window,text="Average",font=("Bell MT",16,"bold"),variable=x,value=2,fg="#242528",bg="#FFF4E6")

    strong_pw=Radiobutton(window,text="Advanced",font=("Bell MT",16,"bold"),variable=x,value=3,fg="#242528",bg="#FFF4E6")

    weak_pw.place(x=850,y=260)
    medium_pw.place(x=850,y=290)
    strong_pw.place(x=850,y=320)

    generate_button=Button(window,text="Generate",font=("Goudy Old Style",14,"bold"),bg="lime green",width=15,command=generate)
    generate_button.place(x=350,y=380)

    accept_button=Button(window,text="Accept",font=("Goudy Old Style",14,"bold"),bg="tomato",width=15,command=accept)
    accept_button.place(x=600,y=380)

    reset_button=Button(window,text="Reset",font=("Goudy Old Style",14,"bold"),bg="blue",fg="white",width=15,command=reset)
    reset_button.place(x=850,y=380)

    copy_button=Button(window,text="Copy",font=("Goudy Old Style",14,"bold"),bg="#f80bcb",width=15,command=copy)
    copy_button.place(x=1100,y=380)

    pwd_label=Label(window,text="Generated Password ",font=font1,bg="#FFF4E6")
    pwd_label.place(x=350,y=470)

    pwdField=Entry(window,width=40,font=font1)
    pwdField.place(x=850,y=470)

    acpt_label=Label(window,text="",font=("Goudy Old Style",18,"bold"),fg="#1D4D6B",bg="#FFF4E6")
    acpt_label.place(x=350,y=530)

    paste_label=Label(window,text="",font=("Goudy Old Style",18,"bold"),fg="#f80bcb",bg="#FFF4E6")
    paste_label.place(x=350,y=570)

    window.mainloop()
