from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("Lucky Country and capital")

entry_name1=Entry(root)
entry_name1.place(relx=0.5,rely=0.1,anchor=CENTER)
entry_name2=Entry(root)
entry_name2.place(relx=0.5,rely=0.2,anchor=CENTER)

country_label=Label(root)
capital_label=Label(root)
random_country=Label(root)
random_capital=Label(root)

list1=[]
list2=[]

def place_name():
    country_name=entry_name1.get()
    capital_name=entry_name2.get()
    list1.append(country_name)
    list2.append(capital_name)
    country_label["text"]="Your country list: "+str(list1)
    capital_label["text"]="Your capital list: "+str(list2)

def random_place():
    length1=len(list1)
    length2=len(list2)
    random_number1=random.randint(0,length1-1)
    random_number2=random.randint(0,length2-1)
    random_n1=list1[random_number1]
    random_n2=list2[random_number2]
    random_country["text"]="Your country is: "+str(random_n1)
    random_capital["text"]="Your capital is: "+str(random_n2)

btn1=Button(root,text="Your capitals and countries are:",command=place_name)
btn1.place(relx=0.5,rely=.4,anchor=CENTER)
country_label.place(relx=0.5,rely=0.5,anchor=CENTER)
capital_label.place(relx=0.5,rely=0.6,anchor=CENTER)
btn2=Button(root,text="Your capital and country are:",command=random_place)
btn2.place(relx=0.5,rely=.7,anchor=CENTER)
random_country.place(relx=0.5,rely=0.8,anchor=CENTER)
random_capital.place(relx=0.5,rely=0.9,anchor=CENTER)
root.mainloop()

