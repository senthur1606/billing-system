from tkinter import *

from numpy.ma.core import product
from win32comext.adsi.demos.search import search
#heading frame
root=Tk()
root.title('billing system')
root.geometry('1270x685')
root.iconbitmap('bill icon.ico')
headingLabel=Label(root,text='Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief='groove')
headingLabel.pack(fill=X)
#1.cutomer details frame
customer_details_frame=LabelFrame(root,text='Customer Details',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
customer_details_frame.pack(fill=X,pady=10)
#name label column
nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,)
nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)
#phone number column
phoneLabel=Label(customer_details_frame,text='phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)
phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)
#billnumber column
billnumberLabel=Label(customer_details_frame,text='bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)
billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)
#searchbutton column
searchbutton=Button(customer_details_frame,text='SEARCH',font=('arial',10,'bold'),bd=7,width=10,command=search,padx=10)
searchbutton.grid(row=0,column=6,padx=10,pady=8)
#2.products frame
productsFrame=Frame(root)
productsFrame.pack()
#cosmetics column
cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
cosmeticsFrame.grid(row=0,column=0,padx=20,pady=10)
bathsoapLable=Label(cosmeticsFrame,text='Bath soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLable.grid(row=0,column=0)
bathsoapEntry=Entry(cosmeticsFrame)
bathsoapEntry.grid(row=0,column=1)
root.mainloop()