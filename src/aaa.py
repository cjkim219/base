from tkinter import *
from tkinter import ttk
# import mysql.connector
import pymysql

import student_data as stu_data
import account_data as acc_data
import config_set as con


# mariaDB 접속 정보
config = con.config

# tkinter 객체 생성
login_wd = Tk()


main_wd = Tk()
main_wd.bind("<F11>", lambda event: main_wd.attributes("-fullscreen", not main_wd.attributes("-fullscreen")))
main_wd.bind("<Escape>", lambda event: main_wd.attributes("-fullscreen", False))
main_wd.title("하이어 수학학원")
main_wd.geometry("1080x720")
# main_wd.iconphoto(False, PhotoImage(file = "photo.png"))


# main화면 접속계정 정보
account_info = acc_data.account_info

# login화면의 사용자 id와 password를 저장하는 변수 생성
user_id, user_password = StringVar(), StringVar()




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
    
    cur.execute(sql)

    clear_entry(edt1)
    clear_entry(edt2)
    clear_entry(edt3)
    clear_entry(edt4)
    
    conn.commit()
    conn.close()
    
        
def selectData():
    strData1, strData2, strData3, strData4 = [], [], [], []
    
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM main_table")
    
    strData1.append("이름")
    strData2.append("나이")
    strData3.append("날짜")
    strData4.append("내용")
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
    
    

def run_main_screen():
    
    btnInsert = Button(edtFrame, text="입력", command=insertData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)

    btnInsert = Button(edtFrame, text="조회", command=selectData)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    
    btnInsert = Button(edtFrame, text="종료", command = main_wd.destroy)
    btnInsert.pack(side=LEFT, padx=10, pady=10)
    


### Login 화면 ###
def check_data():
    login_result = [False, False]
    for acc_id in account_info.keys():
        if user_id.get() == acc_id:
            login_result[0] = True
            
            if user_password.get() == account_info[user_id.get()]:
                login_result[1] = True
                login_wd.destroy()
                run_main_screen()
                
            else:
                ttk.Label(main_wd, text="Check your password").grid(row = 0, column = 0, padx = 10, pady = 10)
                ttk.Button(main_wd, text="확인", command = main_wd.destroy).grid(row = 1, column = 0, padx = 10, pady = 10)
                break
            
    if login_result[0] == False:
        ttk.Label(main_wd, text="Check your ID").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Button(main_wd, text="확인", command = main_wd.destroy).grid(row = 1, column = 0, padx = 10, pady = 10)




# 정보 입력 화면
ttk.Label(login_wd, text = "아이디 : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(login_wd, text = "비밀번호 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(login_wd, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(login_wd, textvariable = user_password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(login_wd, text = "로그인", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)
ttk.Button(login_wd, text = "종료", command = login_wd.destroy).grid(row = 2, column = 2, padx = 10, pady = 10)




edtFrame = Frame(main_wd)
edtFrame.pack()
listFrame = Frame(main_wd)
listFrame.pack(side = BOTTOM, fill=BOTH, expand=1)

edt1 = Entry(edtFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

listData1 = Listbox(listFrame)
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame)
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame)
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame)
listData4.pack(side=LEFT, fill=BOTH, expand=1)
    
    

# py 파일 추가해서 3줄만 다른곳으로 옮겨보기.
# window.attributes("-fullscreen", True)


login_wd.mainloop()



# # py 파일 추가해서 3줄만 다른곳으로 옮겨보기.
# # window.attributes("-fullscreen", True)
# login_wd.bind("<F11>", lambda event: login_wd.attributes("-fullscreen", not login_wd.attributes("-fullscreen")))
# login_wd.bind("<Escape>", lambda event: login_wd.attributes("-fullscreen", False))