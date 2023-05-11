from tkinter import scrolledtext
import tkinter as tk
import tkinter.ttk as ttk



class DatnGui1App:
    def __init__(self, master, maingui, destroy=False):
        # build ui
        self.maingui = maingui
        self.frmIgnore = ttk.Frame(master)
        self.lb_Word = ttk.Label(self.frmIgnore)
        self.lb_Word.configure(text='Danh sách')
        self.lb_Word.place(anchor='nw', relx='0.44', rely='0.11', x='0', y='0')
        self.txtInput = scrolledtext.ScrolledText(self.frmIgnore)
        self.txtInput.configure(autoseparators='false', height='9', width='50', wrap='word')
        self.txtInput.place(anchor='nw', relx='0.17', rely='0.22', x='0', y='0')
        self.lb_Ignore = ttk.Label(self.frmIgnore)
        self.lb_Ignore.configure(text='Từ điển riêng')
        self.lb_Ignore.place(anchor='nw', relx='0.01', rely='0.01', x='0', y='0')
        self.btnSave = ttk.Button(self.frmIgnore)
        self.btnSave.configure(text='Save', command=self.save_file)
        self.btnSave.place(anchor='nw', relx='0.735', rely='0.85', x='0', y='0')
        self.frmIgnore.configure(height='250', width='600')
        self.frmIgnore.pack(side='top')
        from os import getcwd
        self.file_path = getcwd() + '\\cdict\\custom_ignore.txt'
        self.load_file()

        # Main widget
        self.mainwindow = self.frmIgnore
        if destroy:
            master.destroy()
    
    def run(self):
        self.mainwindow.mainloop()

    def load_file(self):
        f = open(self.file_path, 'r', encoding='utf-8')
        self.content = f.readlines()
        f.close()
        ipn_txt = ''
        if len(self.content) > 0:
            for i in range(0 , len(self.content), 1):
                ipn_txt += self.content[i].strip() + '\n'

        self.txtInput.delete('1.0', tk.END)
        self.txtInput.insert(tk.INSERT, ipn_txt[:-1])

        self.maingui.ignore_inp = ipn_txt[:-1].split('\n')
        # print(self.maingui.ignore_inp)
        

    def save_file(self):
        f = open(self.file_path, 'w', encoding='utf-8')
        cinpt = self.txtInput.get("1.0", tk.END)
        if cinpt.strip() != '':
            cinpt = cinpt.split('\n')
            final_out = ''
            for i in range(len(cinpt)):
                final_out += cinpt[i] + '\n'
            f.write(final_out[:-1].strip())
            self.maingui.ignore_inp = cinpt
        f.close()