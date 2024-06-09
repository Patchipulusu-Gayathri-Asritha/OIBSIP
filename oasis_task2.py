from tkinter import *
from tkinter import messagebox


def compute_bmi():
    try:
        height=float(height_entry.get())
        weight=float(weight_entry.get())
        if x.get()=="lbs":
            weight*=0.453592
        if x.get()!="lbs" and x.get()!="kgs":
            messagebox.showwarning("Specify Units!","Please Choose Units for Weight")
            return None
        if y.get()=="ft":
            height*=30.48
        if y.get()!="ft" and y.get()!="cms":
            messagebox.showwarning("Specify Units!","Please Choose Units for Height")
            return None
    
        bmi=round(weight/((height/100)**2),6)

        if bmi<16:
            comment="Severely Underweight"
        elif bmi<18.5:
            comment="Underweight"
        elif bmi<25:
            comment="Healthy"
        elif bmi<30:
            comment="Overweight"
        else:
            comment="Obesity"

        result_label.config(text="BMI is : "+str(round(bmi,4))+"\nBMI Category : \n"+comment)
            
        
    except ValueError:
        messagebox.showerror(title="Error",message="Enter a Valid Number")
    except ZeroDivisionError:
        messagebox.showerror(title="Error",message="Height cannot be 0!")
    
        
    
        
window=Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.config(background="#223333")
title_label=Label(window,
            text="BMI Calculator",
            font=("Baskerville Old Face",30,"bold"),
            bg="#223333",
            fg="lime"
            )
title_label.place(x=20,y=20)

weight_label=Label(window,
              text="Weight",
              font=("Arial",18,"bold"),
              bg="#223333",
              fg="white"
              )
weight_label.place(x=20,y=90)

height_label=Label(window,
                   text="Height",
                   font=("Arial",18,"bold"),
                   bg="#223333",
                   fg="white"
                   )
height_label.place(x=20,y=160)

weight_entry=Entry(window,
                   font=("Times New Roman",12,"bold"),
                   bg="white",
                   fg="black"
                   )
weight_entry.place(x=20,y=125)

height_entry=Entry(window,
                   font=("Times New Roman",12,"bold"),
                   bg="white",
                   fg="black"
                   )
height_entry.place(x=20,y=195)

x=StringVar()
y=StringVar()
x.set("Weight Units")
y.set("Height Units")
weight_drop=OptionMenu(window,x,"kgs","lbs")
height_drop=OptionMenu(window,y,"ft","cms")

weight_drop.place(x=250,y=125)
height_drop.place(x=250,y=195)

button=Button(window,text="Calculate BMI",
              font=("Arial",12,"bold"),
              fg="white",
              bg="dodger blue",
              command=compute_bmi
              )
button.place(x=142,y=260)

result_label=Label(window,
                   font=("Goudy Old Style",15,"bold"),
                   fg="light yellow",
                   bg="#223333")
result_label.place(x=130,y=310)
status_label=Label(window,
                   font=("Goudy Old Style",15,"bold"),
                   fg="light yellow",
                   bg="#223333")
status_label.place(x=90,y=330)

window.mainloop()






