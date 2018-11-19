'''Restaurant Management System'''

from tkinter import *
import time
import random

root = Tk()
root.title('Restaurant Management System')

text_input = StringVar()
button_input = ''
#---------------------------Creating the Frames--------------------------
TopFrame = Frame(root,width=1600,height=50,bg='midnightblue',relief=SUNKEN)
TopFrame.pack(side=TOP)

LeftFrame = Frame(root,width=800,height=700,relief=SUNKEN)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(root,width=300,height=700,relief=SUNKEN)
RightFrame.pack(side=RIGHT)
#-------------Setting the time------------------------------------
time = time.asctime(time.localtime(time.time()))
#-------------Setting the title and time Label--------------------
title = Label(TopFrame,font=('Tahoma',50,'italic'),
              text='Restaurant Management System',fg='firebrick')
title.grid(row=0,column=0)

timeLabel = Label(TopFrame,font=('Tahoma',20,'bold','italic'),
              text=time,fg='dimgrey',)
timeLabel.grid(row=1,column=0)

#--------------------------------Calculator---------------------------------
def buttonClick(number):
    global button_input
    button_input += str(number)
    text_input.set(button_input)

def clearDisplay():
    global button_input
    button_input = ''
    text_input.set('')

def eq():
    global button_input
    result = str(eval(button_input))
    text_input.set(result)
    button_input = ''

def Total():
    a = random.randint(98767,467242)
    b = str(a)
    ref.set(b)

    cost_of_fries = float(fries.get()) * 40
    cost_of_burger = float(burger.get()) * 80
    cost_of_fillet = float(fillet.get()) * 100
    cost_of_chicken = float(chicken.get()) * 120
    cost_of_cheese = float(cheese.get()) * 110
    cost_of_drinks = float(drinks.get()) * 30

    cost_of_meal = 'Rs.',str('%.2f'%(cost_of_fries +cost_of_burger +cost_of_fillet
                                      +cost_of_chicken +cost_of_cheese +
                                      cost_of_drinks))

    service_charge = (cost_of_fries +cost_of_burger +cost_of_fillet
                                      +cost_of_chicken +cost_of_cheese +
                                      cost_of_drinks) * 0.025

    gstax = round(((cost_of_fries +cost_of_burger +cost_of_fillet
                                      +cost_of_chicken +cost_of_cheese +
                                      cost_of_drinks) * 0.18),2)

    stotal = (cost_of_fries +cost_of_burger +cost_of_fillet
                                      +cost_of_chicken +cost_of_cheese +
                                      cost_of_drinks)+service_charge

    gtotal = 'Rs.'+str(stotal+gstax)

    cost.set(cost_of_meal)
    service.set(service_charge)
    GST.set(gstax)
    sub_total.set(stotal)
    grand.set(gtotal)

def Reset():
    ref.set('')
    fries.set('')
    burger.set('')
    fillet.set('')
    chicken.set('')
    cheese.set('')
    drinks.set('')
    cost.set('')
    service.set('')
    GST.set('')
    sub_total.set('')
    grand.set('')

display = Entry(RightFrame,font=('Helvetica',20,'bold'),textvariable=text_input,
                bd=30,insertwidth=4,bg='slateblue',justify='right')
display.grid(columnspan=4)
#-------------------------------First Row Buttons---------------------
button9 = Button(RightFrame,text='9',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(9))
button9.grid(row=2,column=0)

button8 = Button(RightFrame,text='8',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(8))
button8.grid(row=2,column=1)

button7 = Button(RightFrame,text='7',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(7))
button7.grid(row=2,column=2)

Add = Button(RightFrame,text='+',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick('+'))
Add.grid(row=2,column=3)
#--------------------------------Second Row Buttons-----------------------
button6 = Button(RightFrame,text='6',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(6))
button6.grid(row=3,column=0)

button5 = Button(RightFrame,text='5',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(5))
button5.grid(row=3,column=1)

button4 = Button(RightFrame,text='4',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(4))
button4.grid(row=3,column=2)

Sub = Button(RightFrame,text='-',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick('-'))
Sub.grid(row=3,column=3)
#-------------------------------Third Row Buttons---------------------------
button3 = Button(RightFrame,text='3',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(3))
button3.grid(row=4,column=0)

button2 = Button(RightFrame,text='2',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(2))
button2.grid(row=4,column=1)

button1 = Button(RightFrame,text='1',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(1))
button1.grid(row=4,column=2)

Mul = Button(RightFrame,text='*',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick('*'))
Mul.grid(row=4,column=3)
#----------------------------Fourth Row Buttons-------------------------------
button0 = Button(RightFrame,text='0',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick(0))
button0.grid(row=5,column=0)

Clear = Button(RightFrame,text='C',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=clearDisplay)
Clear.grid(row=5,column=1)

Div = Button(RightFrame,text='/',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=lambda:buttonClick('/'))
Div.grid(row=5,column=2)

Equal = Button(RightFrame,text='=',padx=16,pady=16,bd=8,fg='black',bg='limegreen',
                 font=('Times',20,'bold'),command=eq)
Equal.grid(row=5,column=3)

#-----------------------------Labels and Entries-I--------------------------------
ref = StringVar()
fries = StringVar()
burger = StringVar()
fillet = StringVar()
chicken = StringVar()
cheese = StringVar()

lref = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Reference',bd=16,anchor='w')
lref.grid(row=0,column=0)
tref = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=ref,bd=10,
           insertwidth=4,bg='plum',justify='right')
tref.grid(row=0,column=1)

lfries = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Indian Fries',bd=16,
                anchor='w')
lfries.grid(row=1,column=0)
tfries = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=fries,bd=10,
           insertwidth=4,bg='plum',justify='right')
tfries.grid(row=1,column=1)

lburger = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Burger Meal',bd=16,
                anchor='w')
lburger.grid(row=2,column=0)
tburger = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=burger,bd=10,
           insertwidth=4,bg='plum',justify='right')
tburger.grid(row=2,column=1)

lfillet = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Fillet Meal',bd=16,
                anchor='w')
lfillet.grid(row=3,column=0)
tfillet = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=fillet,bd=10,
           insertwidth=4,bg='plum',justify='right')
tfillet.grid(row=3,column=1)

lchicken = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Chicken Meal',bd=16,
                anchor='w')
lchicken.grid(row=4,column=0)
tchicken = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=chicken,bd=10,
           insertwidth=4,bg='plum',justify='right')
tchicken.grid(row=4,column=1)

lcheese = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Cheese Meal',bd=16,
                anchor='w')
lcheese.grid(row=5,column=0)
tcheese = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=cheese,bd=10,
           insertwidth=4,bg='plum',justify='right')
tcheese.grid(row=5,column=1)

#----------------------------Labels and Entries-II---------------------------

drinks = StringVar()
cost = StringVar()
service = StringVar()
GST = StringVar()
sub_total = StringVar()
grand = StringVar()

ldrinks = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Drinks',bd=16,
                anchor='w')
ldrinks.grid(row=0,column=2)
tdrinks = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=drinks,bd=10,
           insertwidth=4,bg='plum',justify='right')
tdrinks.grid(row=0,column=3)

lcost = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Cost of Meal',bd=16,
                anchor='w')
lcost.grid(row=1,column=2)
tcost = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=cost,bd=10,
           insertwidth=4,bg='plum',justify='right')
tcost.grid(row=1,column=3)

lservice = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Service Charge',bd=16,
                anchor='w')
lservice.grid(row=2,column=2)
tservice = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=service,bd=10,
           insertwidth=4,bg='plum',justify='right')
tservice.grid(row=2,column=3)

lGST = Label(LeftFrame,font=('Helvetica',16,'bold'),text='GST',bd=16,
                anchor='w')
lGST.grid(row=3,column=2)
tGST = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=GST,bd=10,
           insertwidth=4,bg='plum',justify='right')
tGST.grid(row=3,column=3)

lsubt = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Sub Total',bd=16,
                anchor='w')
lsubt.grid(row=4,column=2)
tsubt = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=sub_total,bd=10,
           insertwidth=4,bg='plum',justify='right')
tsubt.grid(row=4,column=3)

lgrand = Label(LeftFrame,font=('Helvetica',16,'bold'),text='Grand Total',bd=16,
                anchor='w')
lgrand.grid(row=5,column=2)
tgrand = Entry(LeftFrame,font=('Helvetica',16,'bold'),textvariable=grand,bd=10,
           insertwidth=4,bg='plum',justify='right')
tgrand.grid(row=5,column=3)

#----------------------------Buttons-------------------------------
total = Button(LeftFrame,padx=16,pady=8,fg='black',font=('arial',16,'bold'),
               width=10,text='Total',bg='gold',command=Total,bd=16)
total.grid(row=8,column=1)

reset = Button(LeftFrame,padx=16,pady=8,fg='black',font=('arial',16,'bold'),
               width=10,text='Reset',bg='gold',command=Reset,bd=16)
reset.grid(row=8,column=2)

destroy = Button(LeftFrame,padx=16,pady=8,fg='black',font=('arial',16,'bold'),
               width=10,text='Exit',bg='gold',command=root.destroy,bd=16)
destroy.grid(row=8,column=3)

root.geometry('1600x800+0+0')
root.mainloop()
