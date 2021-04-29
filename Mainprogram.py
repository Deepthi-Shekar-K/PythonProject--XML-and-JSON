from tkinter import *


root = Tk()
root.geometry("500x300")
root.configure(bg="#ccffff")
root.title("PARSING WINDOW")
root.iconbitmap('parsingimg.ico')

def openwindow():
    new_window=Toplevel(root)
    new_window.geometry("500x370")
    new_window.configure(bg="#ffe6f3")
    new_window.iconbitmap('json2.ico')
    new_window.title("DATA")
    new_window.resizable(False,False)
    import json
    x=[]
    b=[]
    myrecord=json.load(open("jsonfile.json"))

    a=myrecord
    for i in a:
        x.append(i)
        b.append(a[i])


    Label(new_window,text="JSON DATA",font=('arial',16,'bold'),bg="#ffe6f3",fg='#0d0d0d',justify='center').place(x=160,y=50)
    Label(new_window,text=x[0],bg="#ffe6f3",font=('arial',15)).place(x=100,y=100)
    Label(new_window,text=x[1],bg="#ffe6f3",font=('arial',15)).place(x=100,y=150)
    Label(new_window,text=x[2],bg="#ffe6f3",font=('arial',15)).place(x=100,y=200)
    Label(new_window,text=x[3],bg="#ffe6f3",font=('arial',15)).place(x=100,y=250)
    Label(new_window,text=x[4],bg="#ffe6f3",font=('arial',15)).place(x=100,y=300)
    Label(new_window,text=b[0],bg="#ffe6f3",font=('arial',15)).place(x=220,y=100)
    Label(new_window,text=b[1],bg="#ffe6f3",font=('arial',15)).place(x=220,y=150)
    Label(new_window,text=b[2],bg="#ffe6f3",font=('arial',15)).place(x=220,y=200)
    Label(new_window,text=b[3],bg="#ffe6f3",font=('arial',15)).place(x=220,y=250)
    Label(new_window,text=b[4],bg="#ffe6f3",font=('arial',15)).place(x=220,y=300)



import xml.etree.ElementTree as ET
data= '''
<XML_DATA>
    <data>
        <City_name> : Mysore</City_name>
        <latitude> : 12.295</latitude>
        <longitude> : 76.639</longitude>
        <temperature> : 22</temperature>
        <humidity> : 90%</humidity>
    </data>
</XML_DATA>
'''
a=[]
c=[]
myroot=ET.fromstring(data)
#print(myroot.tag)
#print(myroot[0].attrib)
for i in myroot[0]:
    a.append(i.tag)
    c.append(i.text)
#for i in myroot[0]:
    #print(i.text)
def openwindow1():
    new_window1=Toplevel(root)
    new_window1.geometry("500x370")
    new_window1.configure(bg="#ffe6f3")
    new_window1.iconbitmap('xml3.ico')
    new_window1.title("DATA")
    new_window1.resizable(False,False)
    Label(new_window1,text="XML DATA",font=('arial',16,'bold'),bg="#ffe6f3",fg='#0d0d0d',justify='center').place(x=160,y=50)
    Label(new_window1,text=a[0],bg="#ffe6f3",font=('arial',15)).place(x=100,y=100)
    Label(new_window1,text=a[1],bg="#ffe6f3",font=('arial',15)).place(x=100,y=150)
    Label(new_window1,text=a[2],bg="#ffe6f3",font=('arial',15)).place(x=100,y=200)
    Label(new_window1,text=a[3],bg="#ffe6f3",font=('arial',15)).place(x=100,y=250)
    Label(new_window1,text=a[4],bg="#ffe6f3",font=('arial',15)).place(x=100,y=300)
    Label(new_window1,text=c[0],bg="#ffe6f3",font=('arial',15)).place(x=220,y=100)
    Label(new_window1,text=c[1],bg="#ffe6f3",font=('arial',15)).place(x=220,y=150)
    Label(new_window1,text=c[2],bg="#ffe6f3",font=('arial',15)).place(x=220,y=200)
    Label(new_window1,text=c[3],bg="#ffe6f3",font=('arial',15)).place(x=220,y=250)
    Label(new_window1,text=c[4],bg="#ffe6f3",font=('arial',15)).place(x=220,y=300)


w=Label(root,text="PARSING XML AND JSON DATA",fg='black',justify='center',font=('arial',16,'bold')).place(x=90,y=50)

btn1=Button(root,text="Parsing  XML  Data",width = 20,justify='center',bg="lightpink",fg="black",font=('arial',12),
            command=openwindow1).place(x=150,y=120)

btn2=Button(root,text="Parsing JSON Data", width = 20,justify='center',bg="lightpink",fg="black",font=('arial',12),
            command=openwindow).place(x=150,y=170)

root.mainloop()




