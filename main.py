from tkinter import *
from tkinter import messagebox
import random
import os
import tempfile
import smtplib

#functionality part
#clear button functionality part
def clear():
    bathsoapEntry.delete(0,END)
    facecreamEntry.delete(0,END)
    facewashEntry.delete(0,END)
    hairsprayEntry.delete(0,END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugerEntry.delete(0, END)
    teapowderEntry.delete(0, END)

    maazaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    fizzEntry.delete(0, END)
    frootiEntry.delete(0, END)
    cococolaEntry.delete(0, END)

    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    facewashEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    bodylotionEntry.insert(0,0)

    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    sugerEntry.insert(0,0)
    teapowderEntry.insert(0,0)

    maazaEntry.insert(0,0)
    pepsiEntry.insert(0,0)
    spriteEntry.insert(0,0)
    fizzEntry.insert(0,0)
    frootiEntry.insert(0,0)
    cococolaEntry.insert(0,0)

    cousmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    cousmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)

#email
def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),reciverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is sent successfully')
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again')
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title("send gmail")
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text="SENDER",font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLable=Label(senderFrame,text="sender's Email",font=('arial',16,'bold'),bg='gray20',fg='white')
        senderLable.grid(row=0,column=0,padx=10,pady=8)
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLable=Label(senderFrame,text="Password",font=('arial',16,'bold'),bg='gray20',fg='white')
        passwordLable.grid(row=1,column=0,padx=10,pady=8)
        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text="RECIPIENT",font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        reciverLable=Label(recipientFrame,text="Email Address",font=('arial',16,'bold'),bg='gray20',fg='white')
        reciverLable.grid(row=0,column=0,padx=10,pady=8)
        reciverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        reciverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLable=Label(recipientFrame,text="Message",font=('arial',16,'bold'),bg='gray20',fg='white')
        messageLable.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendbutton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendbutton.grid(row=2,column=0,pady=20)
        root1.mainloop()



def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')



if not os.path.exists('saved bills'):
    os.mkdir('saved bills')

def search_bill():
    bill_number = billnumberEntry.get()
    bill_file = f'saved bills/{bill_number}.txt'

    if os.path.exists(bill_file):
        with open(bill_file, 'r') as file:
            bill_content = file.read()
            textarea.delete('1.0', END)
            textarea.insert(END, bill_content)
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')
#bill save file creation
def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get('1.0', END)
        bill_file = f'saved bills/{billnumber}.txt'

        with open(bill_file, 'w') as file:
            file.write(bill_content)

        messagebox.showinfo('Success', f'Bill number {billnumber} is saved successfully')
        billnumber = random.randint(100, 1000)

# Generate initial random bill number
billnumber = random.randint(100, 1000)

#error mesg set path
def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error', 'customer detail are required')
    elif cousmetictaxEntry.get() == '' or grocerypriceEntry.get() == '' or drinkspriceEntry.get() == '':
        messagebox.showerror('Error', 'No products are selected')
    elif cousmetictaxEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and drinkspriceEntry.get() == '0 Rs':
        messagebox.showerror('Error', 'No products are selected')
    else:
        textarea.delete('1.0',END)


        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number:{billnumber}\n')
        textarea.insert(END, f'\ncustomer Number:{nameEntry.get()}\n')
        textarea.insert(END,f'\ncustomer phone Number:{phoneEntry.get()}\n')
        textarea.insert(END,'\n===================================================')
        textarea.insert(END,'product\t\tQty\t\t\tprice')
        textarea.insert(END,'\n===================================================')
#cousmetic items set to print in a bill
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'Bath Soap\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs\n')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'Face Cream\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs\n')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'Face Wash\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs\n')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'Hair Spray\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs\n')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'Hair Gel\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs\n')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'Body Lotion\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs\n')

#grocery items set to print in a bill
        if riceEntry.get()!='0':
            textarea.insert(END,f'Rice\t\t{riceEntry.get()}\t\t\t{riceprice} Rs\n')
        if oilEntry.get()!='0':
            textarea.insert(END,f'Oil\t\t{oilEntry.get()}\t\t\t{oilprice} Rs\n')
        if daalEntry.get()!='0':
            textarea.insert(END,f'Daal\t\t{daalEntry.get()}\t\t\t{daalprice} Rs\n')
        if wheatEntry.get()!= '0':
            textarea.insert(END, f'Wheat\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs\n')
        if sugerEntry.get() != '0':
            textarea.insert(END, f'Suger\t\t{sugerEntry.get()}\t\t\t{sugerprice} Rs\n')
        if teapowderEntry.get() != '0':
            textarea.insert(END, f'Tea Powder\t\t{teapowderEntry.get()}\t\t\t{teapowderprice} Rs\n')

#grocery items set to print in a bill
        if maazaEntry.get()!='0':
            textarea.insert(END,f'Maaza\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs\n')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'Pepsi\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs\n')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'Sprite\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs\n')
        if fizzEntry.get() != '0':
            textarea.insert(END, f'Fizz\t\t{fizzEntry.get()}\t\t\t{fizzprice} Rs\n')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'Frooti\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs\n')
        if cococolaEntry.get() != '0':
            textarea.insert(END, f'Cococola\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs\n')
        textarea.insert(END,'\n---------------------------------------------------')
# Strip spaces and handle 'Rs' or any similar currency suffix in the input
        cousmetic_tax = cousmetictaxEntry.get().replace('Rs','').strip()
        grocery_tax = grocerytaxEntry.get().replace('Rs','').strip()
        drinks_tax = drinkstaxEntry.get().replace('Rs','').strip()
# Check and insert tax columns if the numeric value is greater than 0
        if float(cousmetic_tax) > 0:
            textarea.insert(END, f'\nCosmetic Tax\t\t\t{cousmetictaxEntry.get()}')
        if float(grocery_tax) >  0:
            textarea.insert(END, f'\nGrocery Tax\t\t\t{grocerytaxEntry.get()}')
        if float(drinks_tax) > 0:
            textarea.insert(END, f'\nDrinks Tax\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,f'\nTotal Bill\t\t\t{totalbill} Rs')
        textarea.insert(END, '\n---------------------------------------------------')
        save_bill()
def total():
    global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
    global riceprice,oilprice,daalprice,wheatprice,sugerprice,teapowderprice
    global maazaprice,pepsiprice,spriteprice,fizzprice,frootiprice,cococolaprice
    global totalbill
#cousmetics price calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice = int(facewashEntry.get())*100
    hairsprayprice = int(hairsprayEntry.get())*150
    hairgelprice = int(hairgelEntry.get())*80
    bodylotionprice = int(bodylotionEntry.get())*60
    totalcousmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cousmeticpriceEntry.delete(0,END)
    cousmeticpriceEntry.insert(0,str(totalcousmeticprice)+'Rs')
#cousmetic tax calculation
    cousmetictax=totalcousmeticprice*0.05
    cousmetictaxEntry.delete(0,END)
    cousmetictaxEntry.insert(0,str(cousmetictax)+'Rs')
#grocery price calculation
    riceprice = int(riceEntry.get()) * 200
    oilprice = int(oilEntry.get()) * 90
    daalprice = int(daalEntry.get()) * 120
    wheatprice = int(wheatEntry.get()) * 130
    sugerprice = int(sugerEntry.get()) * 75
    teapowderprice = int(teapowderEntry.get()) * 90
    totalgroceryprice = riceprice + oilprice + daalprice + wheatprice + sugerprice + teapowderprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,str(totalgroceryprice)+'Rs')
#grocerytax calculation
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,str(grocerytax)+'Rs')

#coal drinks price calculation
    maazaprice = int(maazaEntry.get()) * 200
    pepsiprice = int(pepsiEntry.get()) * 90
    spriteprice = int(spriteEntry.get()) * 120
    fizzprice = int(fizzEntry.get()) * 130
    frootiprice = int(frootiEntry.get()) * 75
    cococolaprice = int(cococolaEntry.get()) * 90
    totalcoaldrinksprice = maazaprice + pepsiprice + spriteprice + fizzprice + frootiprice + cococolaprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0,str(totalcoaldrinksprice)+'Rs')
#cousmetictax calculation
    drinkstax=totalcoaldrinksprice*0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,str(drinkstax)+'Rs')
#total calculation of all products
    totalbill=totalcousmeticprice+totalgroceryprice+totalcoaldrinksprice+cousmetictax+grocerytax+drinkstax

#GUI part
#heading frame
root=Tk()
root.title('billing system')
root.geometry('1270x685')
root.iconbitmap('bill icon.ico')
headingLabel=Label(root,text='Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief='groove')
headingLabel.pack(fill=X)
#1.cutomer details frame
customer_details_frame=LabelFrame(root,text='Customer Details',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
customer_details_frame.pack(fill=X)
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
searchbutton=Button(customer_details_frame,text='SEARCH',font=('arial',10,'bold'),bd=7,width=10,command=search_bill)
searchbutton.grid(row=0,column=6,padx=10,pady=8)
#2.products frame
productsFrame=Frame(root)
productsFrame.pack()
#cosmetics column
cousmeticsFrame=LabelFrame(productsFrame,text='Cousmetics',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
cousmeticsFrame.grid(row=0,column=0)

bathsoapLable=Label(cousmeticsFrame,text='Bath soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLable.grid(row=0,column=0,pady=9,padx=10,sticky=W)
bathsoapEntry=Entry(cousmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLable=Label(cousmeticsFrame,text='face cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLable.grid(row=1,column=0,pady=9,padx=10,sticky=W)
facecreamEntry=Entry(cousmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLable=Label(cousmeticsFrame,text='face wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLable.grid(row=2,column=0,pady=9,padx=10,sticky=W)
facewashEntry=Entry(cousmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLable=Label(cousmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLable.grid(row=3,column=0,pady=9,padx=10,sticky=W)
hairsprayEntry=Entry(cousmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLable=Label(cousmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLable.grid(row=4,column=0,pady=9,padx=10,sticky=W)
hairgelEntry=Entry(cousmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLable=Label(cousmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionLable.grid(row=5,column=0,pady=9,padx=10,sticky=W)
bodylotionEntry=Entry(cousmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

#grocery column
groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLable=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLable.grid(row=0,column=0,pady=9,padx=10,sticky=W)
riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLable=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLable.grid(row=1,column=0,pady=9,padx=10,sticky=W)
oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLable=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLable.grid(row=2,column=0,pady=9,padx=10,sticky=W)
daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLable=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLable.grid(row=3,column=0,pady=9,padx=10,sticky=W)
wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugerLable=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugerLable.grid(row=4,column=0,pady=9,padx=10,sticky=W)
sugerEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugerEntry.grid(row=4,column=1,pady=9,padx=10)
sugerEntry.insert(0,0)

teapowderLable=Label(groceryFrame,text='Tea Powder',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teapowderLable.grid(row=5,column=0,pady=9,padx=10,sticky=W)
teapowderEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teapowderEntry.grid(row=5,column=1,pady=9,padx=10)
teapowderEntry.insert(0,0)

#coldrinks column
drinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
drinksFrame.grid(row=0,column=2)

maazaLable=Label(drinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maazaLable.grid(row=0,column=0,pady=9,padx=10,sticky=W)
maazaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepsiLable=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLable.grid(row=1,column=0,pady=9,padx=10,sticky=W)
pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLable=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLable.grid(row=2,column=0,pady=9,padx=10,sticky=W)
spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

fizzLable=Label(drinksFrame,text='Fizz',font=('times new roman',15,'bold'),bg='gray20',fg='white')
fizzLable.grid(row=3,column=0,pady=9,padx=10,sticky=W)
fizzEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fizzEntry.grid(row=3,column=1,pady=9,padx=10)
fizzEntry.insert(0,0)

frootiLable=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLable.grid(row=4,column=0,pady=9,padx=10,sticky=W)
frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLable=Label(drinksFrame,text='Coco Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cococolaLable.grid(row=5,column=0,pady=9,padx=10,sticky=W)
cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)

#billframe column
billframe=Frame(productsFrame,bd=8,relief='groove')
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief='groove')
billareaLabel.pack(fill=X)

#scrollbar column
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=51,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)
#billmenu column
billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times to roman',15,'bold'),fg='gold',bd=8,relief='groove',bg='gray20')
billmenuFrame.pack()
cousmeticpriceLable=Label(billmenuFrame,text='Cousmetic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cousmeticpriceLable.grid(row=0,column=0,pady=6,padx=10,sticky=W)
cousmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cousmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLable=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerypriceLable.grid(row=1,column=0,pady=6,padx=10,sticky=W)
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLable=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkspriceLable.grid(row=2,column=0,pady=6,padx=10,sticky=W)
drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cousmetictaxLable=Label(billmenuFrame,text='Cousmetic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cousmetictaxLable.grid(row=0,column=2,pady=6,padx=10,sticky=W)
cousmetictaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cousmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLable=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerytaxLable.grid(row=1,column=2,pady=6,padx=10,sticky=W)
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLable=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkstaxLable.grid(row=2,column=2,pady=6,padx=10,sticky=W)
drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)

#buttonframe
buttonframe=Frame(billmenuFrame,bd=8,relief='groove')
buttonframe.grid(row=0,column=4,rowspan=3)

totalbutton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalbutton.grid(row=0,column=0,pady=20,padx=5)

billbutton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billbutton.grid(row=0,column=1,pady=20,padx=5)

emailbutton=Button(buttonframe,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailbutton.grid(row=0,column=2,pady=20,padx=5)

printbutton=Button(buttonframe,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printbutton.grid(row=0,column=3,pady=20,padx=5)

clearbutton=Button(buttonframe,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)
root.mainloop()
