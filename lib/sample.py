# class JSS:
#     def __init__(self):
#         self.name = input("name:")
#         self.age = input("age:")
        
#     def show(self):
#         print("name : {}, age : {}.".format(self.name, self.age))
        
        
        
# class JSS2(JSS):
#     def __init__(self):
#         # super().__init__()
#         self.gender = input("gender:")
        
        
# b = JSS2()
# b.name = '123'
# b.age = '456'

# b.show()
import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_value.set(combo.get())

# tkinter 창 생성
window = tk.Tk()
window.title("드롭다운 목록 예제")

# 드롭다운 목록을 위한 문자열 변수 생성
selected_value = tk.StringVar()

# 드롭다운 목록 생성
combo = ttk.Combobox(window, textvariable=selected_value)
combo['values'] = ('항목 1', '항목 2', '항목 3', '항목 4')
combo.pack()

# 드롭다운 목록에서 항목 선택 시 이벤트 처리
combo.bind('<<ComboboxSelected>>', on_select)

# 선택된 항목 표시를 위한 레이블 생성
selected_label = tk.Label(window, textvariable=selected_value)
selected_label.pack()

# 창 실행
window.mainloop()
