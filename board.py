from tkinter import *
import tkinter.messagebox
import random
from PIL import Image,ImageTk

tk=Tk()
tk.geometry("1000x770+0+0")

image1 = Image.open('Wallpaper1.bmp')
img = ImageTk.PhotoImage(image1)

label0=Label(tk,image=img).place(x=0,y=0)

tkinter.messagebox.showinfo("Mine Game","Welcome To Mine Game")
label2=Label(tk,text="Player Score",width=15,height=3,font=("Courier 14 bold"),fg="blue",bg="white")
label2.grid(row=0,column=11,padx=2,pady=2)
label1=Label(tk,text="XX = -100\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label1.grid(row=2,column=11,padx=2,pady=2)

label3=Label(tk,text="+ = +5\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label3.grid(row=3,column=11,padx=2,pady=2)

label4=Label(tk,text="- = -5\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label4.grid(row=4,column=11,padx=2,pady=2)

label5=Label(tk,text="++ = +10\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label5.grid(row=5,column=11,padx=2,pady=2)

label6=Label(tk,text="-- = -10\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label6.grid(row=6,column=11,padx=2,pady=2)

label7=Label(tk,text="* = Score * 2\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label7.grid(row=7,column=11,padx=2,pady=2)

label8=Label(tk,text="X = -50\nPoints",width=15,height=3,font=("Courier 14 bold"),fg="red",bg="white")
label8.grid(row=8,column=11,padx=2,pady=2)

global count
count=100

text1=Text(tk,width=6,height=1,font=("Courier 45 bold"),fg="red")
text1.grid(row=2,column=11,padx=2,pady=2)
text1.insert(END,count)

e2=["-","+","--","++","*","X"]
e=["-","+","--","++","*","X","XX"]
e1=["-","--","++","+","X","XX"]
e3=["-","+","XX","X","XX","--","++","XX"]

def checkcount():
    if count<=0:
        tkinter.messagebox.showinfo("Game Over","Your Score Is : "+str(count))
        exit()
        
click=0

def allbutton():
    if click==100:
        tkinter.messagebox.showinfo("Game Over","Your Score Is : "+str(count))
        exit()  

def check(button):
    global count
    global click
    if count<=500:
        button.configure(text=random.choice(e2),bg="white",state="disabled")
        click += 1
    elif count<=1000:
        button.configure(text=random.choice(e),bg="#98fc71",state="disabled")
        click += 1
    elif count<=1500:
        button.configure(text=random.choice(e1),bg="#ffff75",state="disabled")
        click += 1
    else:
        button.configure(text=random.choice(e3),bg="#ff6363",state="disabled")
        click += 1
    txt=str(button["text"])
    if txt == '+':
        count += 5
        text1.delete(0.0,END)
        text1.insert(END,count)
    elif txt=='-':
        count -= 5
        text1.delete(0.0,END)
        text1.insert(END,count)
    elif txt=='++':
        count += 10
        text1.delete(0.0,END)
        text1.insert(END,count)
    elif txt=='--':
        count -= 10
        text1.delete(0.0,END)
        text1.insert(END,count)
    elif txt=='*':
        count *= 2
        text1.delete(0.0,END)
        text1.insert(END,count)
    elif txt=='X':
        count -= 50
        text1.delete(0.0,END)
        text1.insert(END,count)
    elif txt=='XX':
        count -= 100
        text1.delete(0.0,END)
        text1.insert(END,count)
    allbutton()
    checkcount()
        
def onclick_exitg():
    tkinter.messagebox.showinfo("Thank You For Playing","Your Score Is : "+str(count))
    exit()

button1=Button(tk,text="EXIT",command=onclick_exitg,width=15,height=2,font=("Courier 12 bold"),fg="red",bg="#E1E7E4")
button1.grid(row=9,column=11,padx=2,pady=2)

tk.title("Demo Project")
button=StringVar()
button00=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button00))
button00.grid(row=0,column=0,padx=2,pady=2)
button01=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button01))
button01.grid(row=0,column=1,padx=2,pady=2)
button02=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button02))
button02.grid(row=0,column=2,padx=2,pady=2)
button03=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button03))
button03.grid(row=0,column=3,padx=2,pady=2)
button04=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button04))
button04.grid(row=0,column=4,padx=2,pady=2)
button05=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button05))
button05.grid(row=0,column=5,padx=2,pady=2)
button06=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button06))
button06.grid(row=0,column=6,padx=2,pady=2)
button07=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button07))
button07.grid(row=0,column=7,padx=2,pady=2)
button08=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button08))
button08.grid(row=0,column=8,padx=2,pady=2)
button09=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button09))
button09.grid(row=0,column=9,padx=2,pady=2)

button10=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button10))
button10.grid(row=1,column=0,padx=2,pady=2)
button11=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button11))
button11.grid(row=1,column=1,padx=2,pady=2)
button12=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button12))
button12.grid(row=1,column=2,padx=2,pady=2)
button13=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button13))
button13.grid(row=1,column=3,padx=2,pady=2)
button14=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button14))
button14.grid(row=1,column=4,padx=2,pady=2)
button15=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button15))
button15.grid(row=1,column=5,padx=2,pady=2)
button16=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button16))
button16.grid(row=1,column=6,padx=2,pady=2)
button17=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button17))
button17.grid(row=1,column=7,padx=2,pady=2)
button18=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button18))
button18.grid(row=1,column=8,padx=2,pady=2)
button19=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button19))
button19.grid(row=1,column=9,padx=2,pady=2)

button20=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button20))
button20.grid(row=2,column=0,padx=2,pady=2)
button21=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button21))
button21.grid(row=2,column=1,padx=2,pady=2)
button22=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button22))
button22.grid(row=2,column=2,padx=2,pady=2)
button23=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button23))
button23.grid(row=2,column=3,padx=2,pady=2)
button24=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button24))
button24.grid(row=2,column=4,padx=2,pady=2)
button25=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button25))
button25.grid(row=2,column=5,padx=2,pady=2)
button26=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button26))
button26.grid(row=2,column=6,padx=2,pady=2)
button27=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button27))
button27.grid(row=2,column=7,padx=2,pady=2)
button28=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button28))
button28.grid(row=2,column=8,padx=2,pady=2)
button29=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button29))
button29.grid(row=2,column=9,padx=2,pady=2)

button30=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button30))
button30.grid(row=3,column=0,padx=2,pady=2)
button31=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button31))
button31.grid(row=3,column=1,padx=2,pady=2)
button32=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button32))
button32.grid(row=3,column=2,padx=2,pady=2)
button33=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button33))
button33.grid(row=3,column=3,padx=2,pady=2)
button34=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button34))
button34.grid(row=3,column=4,padx=2,pady=2)
button35=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button35))
button35.grid(row=3,column=5,padx=2,pady=2)
button36=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button36))
button36.grid(row=3,column=6,padx=2,pady=2)
button37=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button37))
button37.grid(row=3,column=7,padx=2,pady=2)
button38=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button38))
button38.grid(row=3,column=8,padx=2,pady=2)
button39=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button39))
button39.grid(row=3,column=9,padx=2,pady=2)

button40=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button40))
button40.grid(row=4,column=0,padx=2,pady=2)
button41=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button41))
button41.grid(row=4,column=1,padx=2,pady=2)
button42=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button42))
button42.grid(row=4,column=2,padx=2,pady=2)
button43=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button43))
button43.grid(row=4,column=3,padx=2,pady=2)
button44=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button44))
button44.grid(row=4,column=4,padx=2,pady=2)
button45=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button45))
button45.grid(row=4,column=5,padx=2,pady=2)
button46=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button46))
button46.grid(row=4,column=6,padx=2,pady=2)
button47=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button47))
button47.grid(row=4,column=7,padx=2,pady=2)
button48=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button48))
button48.grid(row=4,column=8,padx=2,pady=2)
button49=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button49))
button49.grid(row=4,column=9,padx=2,pady=2)

button50=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button50))
button50.grid(row=5,column=0,padx=2,pady=2)
button51=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button51))
button51.grid(row=5,column=1,padx=2,pady=2)
button52=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button52))
button52.grid(row=5,column=2,padx=2,pady=2)
button53=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button53))
button53.grid(row=5,column=3,padx=2,pady=2)
button54=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button54))
button54.grid(row=5,column=4,padx=2,pady=2)
button55=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button55))
button55.grid(row=5,column=5,padx=2,pady=2)
button56=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button56))
button56.grid(row=5,column=6,padx=2,pady=2)
button57=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button57))
button57.grid(row=5,column=7,padx=2,pady=2)
button58=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button58))
button58.grid(row=5,column=8,padx=2,pady=2)
button59=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button59))
button59.grid(row=5,column=9,padx=2,pady=2)

button60=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button60))
button60.grid(row=6,column=0,padx=2,pady=2)
button61=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button61))
button61.grid(row=6,column=1,padx=2,pady=2)
button62=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button62))
button62.grid(row=6,column=2,padx=2,pady=2)
button63=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button63))
button63.grid(row=6,column=3,padx=2,pady=2)
button64=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button64))
button64.grid(row=6,column=4,padx=2,pady=2)
button65=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button65))
button65.grid(row=6,column=5,padx=2,pady=2)
button66=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button66))
button66.grid(row=6,column=6,padx=2,pady=2)
button67=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button67))
button67.grid(row=6,column=7,padx=2,pady=2)
button68=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button68))
button68.grid(row=6,column=8,padx=2,pady=2)
button69=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button69))
button69.grid(row=6,column=9,padx=2,pady=2)

button70=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button70))
button70.grid(row=7,column=0,padx=2,pady=2)
button71=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button71))
button71.grid(row=7,column=1,padx=2,pady=2)
button72=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button72))
button72.grid(row=7,column=2,padx=2,pady=2)
button73=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button73))
button73.grid(row=7,column=3,padx=2,pady=2)
button74=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button74))
button74.grid(row=7,column=4,padx=2,pady=2)
button75=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button75))
button75.grid(row=7,column=5,padx=2,pady=2)
button76=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button76))
button76.grid(row=7,column=6,padx=2,pady=2)
button77=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button77))
button77.grid(row=7,column=7,padx=2,pady=2)
button78=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button78))
button78.grid(row=7,column=8,padx=2,pady=2)
button79=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button79))
button79.grid(row=7,column=9,padx=2,pady=2)

button80=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button80))
button80.grid(row=8,column=0,padx=2,pady=2)
button81=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button81))
button81.grid(row=8,column=1,padx=2,pady=2)
button82=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button82))
button82.grid(row=8,column=2,padx=2,pady=2)
button83=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button83))
button83.grid(row=8,column=3,padx=2,pady=2)
button84=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button84))
button84.grid(row=8,column=4,padx=2,pady=2)
button85=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button85))
button85.grid(row=8,column=5,padx=2,pady=2)
button86=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button86))
button86.grid(row=8,column=6,padx=2,pady=2)
button87=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button87))
button87.grid(row=8,column=7,padx=2,pady=2)
button88=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button88))
button88.grid(row=8,column=8,padx=2,pady=2)
button89=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button89))
button89.grid(row=8,column=9,padx=2,pady=2)

button90=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button90))
button90.grid(row=9,column=0,padx=2,pady=2)
button91=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button91))
button91.grid(row=9,column=1,padx=2,pady=2)
button92=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button92))
button92.grid(row=9,column=2,padx=2,pady=2)
button93=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button93))
button93.grid(row=9,column=3,padx=2,pady=2)
button94=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button94))
button94.grid(row=9,column=4,padx=2,pady=2)
button95=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button95))
button95.grid(row=9,column=5,padx=2,pady=2)
button96=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button96))
button96.grid(row=9,column=6,padx=2,pady=2)
button97=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button97))
button97.grid(row=9,column=7,padx=2,pady=2)
button98=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button98))
button98.grid(row=9,column=8,padx=2,pady=2)
button99=Button(tk,text=" ",font=('Times 26 bold'),height=1,width=3,command=lambda:check(button99))
button99.grid(row=9,column=9,padx=2,pady=2)
tk.mainloop()
