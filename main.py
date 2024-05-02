import tkinter as tk


def on_button_click(label ):
    print("hello world")
    #label.config(text="Excect")

# button click event 


def main():
    #print("Hello World!")
    win = tk.Tk() # 如果使用直譯器的話，在這行Enter後就會先看到一個視窗了！
    win.title("supercake")
    win.iconbitmap('cupcake.ico')  # load icon 
    win.resizable(False, False)
    win.minsize(width=500, height=500)

    
    mylabel = tk.Label(win,
                  text='歡迎使用supercake',
                  font=('Arial',20,'bold'),
                  bg='#ff0')
    
    mylabel.pack(padx=0, pady=20,anchor='ne') 
    #anchor means position original position
    
    # botton set
    exectbtn = tk.StringVar() # 初始化tk的字串變數
    exectbtn.set('執行')
    exectbtn = tk.Button(
                win,
                text='執行',
                font=('Arial',10,'bold'),
                #width=20,
                #height=20,
                padx=20,
                pady=20,
                activeforeground='#f00'
                ,
                command=lambda: on_button_click(mylabel)
              )    
    exectbtn.pack( pady=50,anchor='ne')
    #button 
    entry = tk.Entry(width=30, font=("Arial", 14, "bold"), bg="red", fg="yellow", state='normal')
    entry.insert(string="some text")
    entry.pack()
    #print(entry.get())
    # text field 
    win.mainloop() # 在一般python xxx.py的執行方式中，呼叫mainloop()才算正式啟動

# main funtion 
if __name__ == "__main__":
    main()