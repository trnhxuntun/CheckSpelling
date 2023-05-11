import tkinter as tk
import tkinter.ttk as ttk
import re


class DatnGui1App:
    def __init__(self, master, maingui):
        # build ui
        self.frmFind = ttk.Frame(master)
        self.txt_Find = ttk.Entry(self.frmFind)
        self.txt_Find.place(anchor='nw', relheight='0.1', relwidth='0.9', relx='0.05', rely='0.15', x='0', y='0')
        self.txt_Replace = ttk.Entry(self.frmFind)
        self.txt_Replace.place(anchor='nw', relheight='0.1', relwidth='0.9', relx='0.05', rely='0.5', x='0', y='0')
        self.lb_Find = ttk.Label(self.frmFind)
        self.lb_Find.configure(anchor='n', compound='top', font='TkTextFont', text='Tìm kiếm:')
        self.lb_Find.place(anchor='nw', relheight='0.1', relwidth='0.09', relx='0.02', rely='0.03', x='0', y='0')
        self.lb_Replace = ttk.Label(self.frmFind)
        self.lb_Replace.configure(anchor='n', compound='top', font='TkTextFont', text='Thay thế bằng:')
        self.lb_Replace.place(anchor='nw', relheight='0.1', relwidth='0.16', relx='0.02', rely='0.4', x='0', y='0')
        self.btnFind = ttk.Button(self.frmFind)
        self.btnFind.configure(text='Tìm kiếm')
        self.btnFind.place(anchor='nw', relx='0.65', rely='0.7', x='0', y='0')
        self.btnFind.configure(command=self.find_text)
        self.btnReplace = ttk.Button(self.frmFind)
        self.btnReplace.configure(text='Thay thế tất cả')
        self.btnReplace.place(anchor='nw', relx='0.85', rely='0.7', x='0', y='0')
        self.btnReplace.configure(command=self.replace_text)
        self.lb_Message = ttk.Label(self.frmFind)
        self.lb_Message.place(anchor='nw', relheight='0.1', relwidth='0.55', relx='0.05', rely='0.7', x='0', y='0')
        self.frmFind.configure(height='250', width='600')
        self.frmFind.pack(side='top')
        self.maingui = maingui
        self.findtext = ''
        self.replacetext = ''

        # Main widget
        self.mainwindow = self.frmFind

    def run(self):
        self.mainwindow.mainloop()

    def to_coord(self, stline, stto):
        return '%s.%s' % (str(stline), str(stto))

    def find_text(self):
        content = self.maingui.txt_file.get("1.0", tk.END)
        marked_tag = 'Tìm kiếm'
        self.maingui.txt_file.tag_remove(marked_tag, "1.0", tk.END)
        self.maingui.txt_file.tag_remove("here", "1.0", tk.END)
        r = re.compile(self.txt_Find.get())
        line = 1
        count = 0
        for val in content.split('\n'):
            for m in r.finditer(val):
                count += 1
                self.maingui.txt_file.tag_add(marked_tag, self.to_coord(line, m.start()),
                                              self.to_coord(line, m.end()))
            line += 1
        self.lb_Message.config(text='Tìm thấy %s từ' % str(count))
        self.maingui.txt_file.tag_config(marked_tag, background='blue', foreground='white', wrap=tk.WORD)

    def replace_text(self):
        content = self.maingui.txt_file.get("1.0", tk.END)
        marked_tag = 'find'
        self.maingui.txt_file.tag_remove(marked_tag, "1.0", tk.END)
        self.maingui.txt_file.delete('1.0', tk.END)
        self.maingui.txt_file.insert(tk.INSERT, content.replace(self.txt_Find.get(), self.txt_Replace.get()))
        self.lb_Message.config(text='Thay thế tất cả thành công')
