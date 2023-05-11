from tkinter import scrolledtext
import tkinter as tk
import tkinter.ttk as ttk

class DatnGui1App:
    def __init__(self, master, maingui, destroy=False):
        # build ui
        self.maingui = maingui
        self.frmAutofix = ttk.Frame(master)
        self.lb_Input = ttk.Label(self.frmAutofix)
        self.lb_Input.configure(text='Input')
        self.lb_Input.place(anchor='nw', relx='0.25', rely='0.11', x='0', y='0')
        self.lb_Output = ttk.Label(self.frmAutofix)
        self.lb_Output.configure(text='Output')
        self.lb_Output.place(anchor='nw', relx='0.7', rely='0.11', x='0', y='0')
        self.txt_Input = scrolledtext.ScrolledText(self.frmAutofix)
        self.txt_Input.configure(height='9', width='30', wrap='word')
        self.txt_Input.place(anchor='nw', relx='0.075', rely='0.22', x='0', y='0')
        self.txt_Output = scrolledtext.ScrolledText(self.frmAutofix)
        self.txt_Output.configure(height='9', width='30', wrap='word')
        self.txt_Output.place(anchor='nw', relx='0.52', rely='0.22', x='0', y='0')
        self.btnOk = ttk.Button(self.frmAutofix, command=self.save_file)
        self.btnOk.configure(text='Save')
        self.btnOk.place(anchor='nw', relx='0.82', rely='0.85', x='0', y='0')
        self.lb_Autofix = ttk.Label(self.frmAutofix)
        self.lb_Autofix.configure(text='Từ điển sửa')
        self.lb_Autofix.place(anchor='nw', relx='0.01', rely='0.01', x='0', y='0')
        self.frmAutofix.configure(height='250', width='600')
        self.frmAutofix.pack(side='top')
        from os import getcwd
        self.file_path = getcwd() + '\\cdict\\custom_autofix.txt'
        self.load_file()

        self.mainwindow = self.frmAutofix
        if destroy:
            master.destroy()
    
    def run(self):
        self.mainwindow.mainloop()

    def load_file(self):
        f = open(self.file_path, 'r', encoding='utf-8')
        self.content = f.readlines()
        f.close()
        ipn_txt = ''
        opn_txt = ''
        if len(self.content) > 0 and len(self.content) % 2 == 0:
            for i in range(0 , len(self.content), 2):
                ipn_txt += self.content[i].strip() + '\n'
                opn_txt += self.content[i+1].strip() + '\n'

        self.txt_Input.delete('1.0', tk.END)
        self.txt_Input.insert(tk.INSERT, ipn_txt[:-1])

        self.txt_Output.delete('1.0', tk.END)
        self.txt_Output.insert(tk.INSERT, opn_txt[:-1])
        self.maingui.autofix_inp = ipn_txt[:-1].split('\n')
        self.maingui.autofix_onp = opn_txt[:-1].split('\n')


    def save_file(self):
        f = open(self.file_path, 'w', encoding='utf-8')
        cinpt = self.txt_Input.get("1.0", tk.END)
        conpt = self.txt_Output.get("1.0", tk.END)
        cinpt = cinpt.split('\n')
        conpt = conpt.split('\n')
        if len(cinpt) == len(conpt) and len(conpt) > 0:
            final_out = ''
            for i in range(len(cinpt)):
                final_out += cinpt[i] + '\n' + conpt[i] + '\n'

            f.write(final_out[:-1].strip())

            self.maingui.autofix_inp = cinpt
            self.maingui.autofix_onp = conpt
        f.close()