from tkinter import *

import pymysql

con = pymysql.connect(host='127.0.0.1', user='root', passwd='djh660993', db='SMMS', charset='utf8')
c = con.cursor()
sql1 = "SELECT sum(stockQuantity),stockID FROM stock where stockDate>=%s and stockDate<=%s"
sql2 = "SELECT sum(saleQuantity) FROM sale where saleDate>=%s and saleDate<=%s"
root = Tk()
frame = Frame(root, width=230, height=150)
frame.pack(fill=BOTH, expand=1)
label=Label(frame,text='请输入查询起止日期:',anchor='nw')
label.place(x=5,y=5,width=130,height=50)
entry = Entry(frame)
entry.place(x=10, y=40, width=70, height=20)
label1=Label(frame,text='至')
label1.place(x=85,y=40,width=10,height=20)
entry1 = Entry(frame)
entry1.place(x=100, y=40, width=70, height=20)
label2=Label(frame,text='进货总量为：')
label2.place(x=10,y=65,width=75,height=20)
label3=Label(frame,text='销售总量为：')
label3.place(x=10,y=90,width=75,height=20)
text1=Text(frame)
text1.place(x=90,y=65,width=75,height=20)
text2=Text(frame)
text2.place(x=90,y=90,width=75,height=20)
def check():
    text1.delete('0.0', 'end')
    text2.delete('0.0', 'end')
    d = entry.get()
    e=entry1.get()
    c.execute(sql1, (d,e))
    a = c.fetchall()
    c.execute(sql2, (d,e))
    b = c.fetchall()
    text1.insert(INSERT,a[0][0])
    text2.insert(INSERT,b[0][0])
    print(a[0][0])

    print(b[0][0])


button = Button(frame, text='check', command=check)
button.place(x=175, y=40, width=40, height=20)
root.mainloop()

# d=input('输入起始时间')
# e=input('输入终止时间')
