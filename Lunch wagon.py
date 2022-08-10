from tkinter import *
import tkinter as tk
root=tk.Tk()
root.title('Menu')
root.geometry('950x600')
root.configure(background='#000225')
def Food():
    w=e.get()
    Label(root, text=w).grid(row=1)

Sum = []
def fries ():
   a= str()
   Sum.append(150)
   s= sum (Sum)
   a = "YOU PAY:" + str (s)
   label_ord.config(text = a)

def stks ():
   a= str()
   Sum.append(250)
   s= sum (Sum)
   a = "YOU PAY :" + str (s)
   label_ord.config(text = a)

def baked ():
   a= str()
   Sum.append(200)
   s= sum (Sum)
   a = "YOU PAY :" + str (s)
   label_ord.config(text = a)
def pizza ():
   a= str()
   Sum.append(200)
   s= sum (Sum)
   a = "YOU PAY:" + str (s)
   label_ord.config(text = a)
def prawn ():
   a= str()
   Sum.append(300)
   s= sum (Sum)
   a = "YOU PAY :" + str (s)
   label_ord.config(text = a)
def pp():
   a= str()
   Sum.append(250)
   s= sum (Sum)
   a = "YOU PAY :" + str (s)
   label_ord.config(text = a)
def pr():
   a= str()
   Sum.append(300)
   s= sum (Sum)
   a = "YOU PAY:" + str (s)
   label_ord.config(text = a)
def r():
   a= str()
   Sum.append(150)
   s= sum (Sum)
   a = "YOU PAY:" + str (s)
   label_ord.config(text = a)
def bb():
   a= str()
   Sum.append(250)
   s= sum (Sum)
   a = "YOU PAY:" + str (s)
   label_ord.config(text = a)
def reset():
    l=[]
    Sum=l
    s=sum(Sum)
    a='CART EMPTY :)   :' + str(s)
    label_ord.config(text=a)
def disc():
   txt= Label(text = 'NO DISCOUNT', font = 30, fg = 'white', bg= '#000225').grid(column=20, row=24)  

#label text
label_app=Label(root, text = ' Lunch-wagon',fg='white',bg='black', font=('Algerian',40))
but_food1=Button(root, text='Fries  :      150',font=20,fg='white',width=30, borderwidth = 5, bg='Black', command = fries)                            
but_food2=Button(root, text='Mozarella Sticks :   250',font= 20,fg='white',width=30 ,borderwidth = 5,bg='Black', command = stks)
but_food3=Button(root, text='Baked potato    :200',font= 20,fg='white',width=30,borderwidth = 5,bg='Black', command = baked)
but_food4=Button(root, text='Pizza Rolls :  200',font= 20,width=30 ,fg='white',borderwidth = 5, bg='Black',command = pizza)
but_food5=Button(root,text='Prawns  :  300',font=20,width=30,borderwidth = 5,fg='white',bg='Black',command = prawn)
but_food6=Button(root,text='BBQ chicken  : 250',font=20, width=30,borderwidth = 5,fg='white',bg='Black', command=bb)
but_food7=Button(root,text='Peri Peri chicken: 250',font=20, width=30,borderwidth = 5,fg='white',bg='Black', command=pp)
but_food8=Button(root,text='Pork ribs  : 300',font=20, width=30,borderwidth = 5,fg='white', bg='Black',command=pr)
but_food9=Button(root,text='Risotto  : 150',font=20, width=30,borderwidth = 5,fg='white', bg='Black', command=r)
reset=Button(root,text='CLEAR ORDER',font=25,width=35,bg='green', command =reset)
Discount=Button(root,text='PRESS FOR DISCOUNT!',width=35,bg='green',font= ('chiller', 20),  command =disc)
label_ord = Label (root, text='CART EMPTY:', font=('Comic Sans MS',35,))

#label grid
label_app.grid(row=0,column=20)

but_food1.grid(row=4,column=4)

but_food2.grid(row=6,column=4)

but_food3.grid(row=8,column=4)
but_food4.grid(row=10,column=4)

but_food5.grid(row=12,column=4)
but_food6.grid(row=14,column=4)
but_food7.grid(row=16,column=4)
but_food8.grid(row=18,column=4)
but_food9.grid(row=20,column=4)
reset.grid(row=18,column=20)
Discount.grid(row=12,column=20)

label_app=Label(root, text = 'ITS GOOD MOOD FOOD',bg='light pink',fg='black', font=('Algerian',40)).grid(column=20,row=1)
label_ord.grid(row = 24 , column = 4)


