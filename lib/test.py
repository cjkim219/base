import config_set as conf
import pymysql
from tkinter import *
from tkinter import ttk



config = conf.config


def clear_entry(target):
    target.delete(0, END)
    

def insertData():
    con, cur = None, None
    data1, data2, data3, data4 = "", "", "", ""
    sql=""
    
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    
    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()
    
    sql = "INSERT INTO main_table VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', '" + data4 + "')"
    
    clear_entry(edt1)
    clear_entry(edt2)
    clear_entry(edt3)
    clear_entry(edt4)
    
    cur.execute(sql)
    
    
    conn.commit()
    conn.close()
    
        
def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM main_table")
    
    strData1.append("ID")
    strData2.append("name")
    strData3.append("e-mail")
    strData4.append("birth")
    strData1.append("-------")
    strData2.append("-------")
    strData3.append("-------")
    strData4.append("-------")
    
    while(True):
        row = cur.fetchone()
        if row == None:
            break
        
        strData1.append(row[0])
        strData2.append(row[1])
        strData3.append(row[2])
        strData4.append(row[3])
        
    listData1.delete(0, listData1.size() - 1)
    listData2.delete(0, listData2.size() - 1)
    listData3.delete(0, listData3.size() - 1)
    listData4.delete(0, listData4.size() - 1)
    
    for item1, item2, item3, item4 in zip(strData1, strData2, strData3, strData4):
        listData1.insert(END, item1)
        listData2.insert(END, item2)
        listData3.insert(END, item3)
        listData4.insert(END, item4)
    
    conn.close()
    
    
    
window = Tk()
window.geometry("1080x720")
window.title("GUI 데이터 입력")


edtFrame = Frame(window)
edtFrame.pack()
listFrame = Frame(window)
listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnInsert = Button(edtFrame, text="조회", command=selectData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame, bg='yellow')
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg='yellow')
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg='yellow')
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg='yellow')
listData4.pack(side=LEFT, fill=BOTH, expand=1)



window.mainloop()