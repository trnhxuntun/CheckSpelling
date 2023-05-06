from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
import checkspelling as cs
from tkinter import scrolledtext
from findreplacegui import DatnGui1App as FindReplaceGUI
from ignoregui import DatnGui1App as IgnoreGUI
from autofixgui import DatnGui1App as AutoFixGUI
from ttkthemes import ThemedTk

class DatnGui1App:
    def __init__(self, master=None, sc=None):
        self.master = master
        self.sc = sc
        self.marked_tag = "here"
        self.file_path = ''
        self.autofix_inp = []
        self.autofix_onp = []
        self.ignore_inp = []
        self.frmWorking = ttk.Frame(master)
        self.label1 = ttk.Label(self.frmWorking)
        self.img_image = tk.PhotoImage(file="bg.png")
        self.label1.configure(image=self.img_image)
        self.label1.place(anchor='nw', relheight='1', relwidth='1', relx='0', rely='0', x='0', y='0')
        self.lb_bgr = ttk.Label(self.frmWorking)
        self.lb_bgr.place(anchor='nw', relwidth='1', relheight='0.03', relx='0', rely='0', x='0', y='0')
        self.__tkvar1 = tk.StringVar(value='File')
        self.__tkvar2 = tk.StringVar(value='Edit')
        self.__tkvar3 = tk.StringVar(value='Quản lý')
        __values = ['File mới', 'Open', 'Save', 'Save as']
        self.opt_file_working = tk.OptionMenu(self.frmWorking, self.__tkvar1, *__values, command=self.opt_filepicked)
        self.opt_file_working.place(anchor='nw', relwidth='0.052', x='0', y='0')
        __values = ['Tìm kiếm']
        self.opt_tool_woking = tk.OptionMenu(self.frmWorking, self.__tkvar2, *__values, command=self.opt_editpicked)
        self.opt_tool_woking.place(anchor='nw', relwidth='0.052', relx='0.052', x='0', y='0')
        __values = ['Từ điển sửa', 'Từ điển riêng']
        self.opt_add_working = tk.OptionMenu(self.frmWorking, self.__tkvar3, *__values, command=self.opt_managepicked)
        self.opt_add_working.place(anchor='nw', relx='0.104', width='85', x='0', y='0')
        self.lb_ErrorNumber = ttk.Label(self.frmWorking)
        self.lb_ErrorNumber.configure(text='Tìm thấy 0 lỗi')
        self.lb_ErrorNumber.place(anchor='nw', relwidth='0.69', relx='0.03', rely='0.91', width='500', x='0', y='0')
        self.txt_file = scrolledtext.ScrolledText(self.frmWorking)
        # self.txt_file = scrolledtext.ScrolledText(self.frmWorking, font=("Arial", 25))
        self.txt_file.configure(blockcursor=False, state='normal', takefocus=False, wrap=tk.WORD)
        self.txt_file.configure(undo=True, wrap=tk.WORD, bg="white", foreground='black')
        self.txt_file.place(anchor='nw', relx='0.03', rely='0.06', x='0', y='0', relheight='0.85', relwidth='0.95')
        self.btn_Check = ttk.Button(self.frmWorking, command=self.run_check)
        self.btn_Check.configure(text='Kiểm tra (F5)')
        self.btn_Check.place(anchor='nw', relx='0.80', rely='0.95', x='0', y='0')
        self.txt_file.bind('<Control-s>', lambda event: self.opt_filepicked('Save'))
        self.txt_file.bind('<Control-Shift-S>', lambda event: self.opt_filepicked('Save as'))
        self.txt_file.bind('<F5>', lambda event: self.run_check(None))
        # self.txt_file.bind('<space>', lambda event: self.run_check(None))
        # self.txt_file.bind('<Return>', lambda event: self.run_check(None))
        self.lb_StatusSave = ttk.Label(self.frmWorking)
        self.lb_StatusSave.place(anchor='nw', relwidth='0.0', relx='0.4', rely='0.91', width='500', x='0', y='0')
        #self.btn_next_word = ttk.Button(self.frmWorking, command=None)
        #self.btn_next_word.configure(text='Next Word')
        #self.btn_next_word.place(anchor='nw', relx='0.90', rely='0.95', x='0', y='0')
        self.frmWorking.configure(height='1465', width='1600')
        self.frmWorking.pack(fill='both', side='top')

        self.last_cursor_loc = self.txt_file.index(tk.INSERT)
        self.err_punc_list = None
        self.err_word_list = None
        # Main widget
        self.mainwindow = self.frmWorking

    def opt_filepicked(self, option):
        if option == 'Open':
            files = [('Text Document', ['*.txt', '*.docx', '*.doc'])]
            file_path = filedialog.askopenfilename(filetypes = files)
            self.file_path = file_path
            if file_path is not None and file_path != '':
                self.run_check(file_path)
        elif option == 'File mới':
            self.txt_file.delete('1.0', tk.END)
            self.file_path = ''
        elif option == 'Save':
            if self.file_path is not None and self.file_path != '':
                try:
                    f = open(self.file_path, 'w', encoding='utf-8')
                    f.write(self.txt_file.get("1.0", tk.END))
                    f.close()
                    self.lb_StatusSave.configure(text='File saved')
                except Exception as e:
                    self.lb_StatusSave.configure(text=e)
                # finally:
                #     t = Thread(target=time.sleep(3); self.lb_StatusSave.configure(text='', args=()))
                #     time.sleep(3)
                #     self.lb_StatusSave.configure(text='')
        elif option == 'Save as':
            files = [('Text Document', ['*.txt'])]
            file_path = filedialog.asksaveasfile(filetypes=files, defaultextension='.txt', mode='wb')
            if file_path is not None and file_path != '':
                pass
            try:
                file_path.write((self.txt_file.get("1.0", tk.END)).encode('utf-8'))
                file_path.close()
                self.lb_StatusSave.configure(text='File saved')
            except Exception as e:
                self.lb_StatusSave.configure(text=e)
        #     finally:
        #         time.sleep(3)
        #         self.lb_StatusSave.configure(text='')
        # self.__tkvar1.set('File')

    def opt_editpicked(self, option):
        if option == '':
            pass
        elif option == 'Place':
            FindReplaceGUI(tk.Toplevel(self.master), self)
        elif option == 'Tìm kiếm':
            FindReplaceGUI(tk.Toplevel(self.master), self)
        self.__tkvar2.set('Edit')

    def opt_managepicked(self, option):
        if option == 'Từ điển sửa':
            AutoFixGUI(tk.Toplevel(self.master), self)
        elif option == 'Từ điển riêng':
            IgnoreGUI(tk.Toplevel(self.master), self)
        self.__tkvar3.set('Manage')

    def run(self):
        self.mainwindow.mainloop()

    def load_def_dicts(self):
        from os import getcwd
        self.sc.load_dict(getcwd() + '\\dict\\tudien.txt')
        self.sc.load_dict(getcwd() + '\\dict\\vi-DauCuoi.txt')
        # self.sc.load_dict(getcwd() + '\\dict\\vi-DauMoi.txt')
        # self.sc.load_dict(getcwd() + '\\dict\\vi-DauCu.txt')
        #self.sc.load_dict(getcwd() + '\\dict\\eng-words.txt')
        self.sc.load_ignore_dict(getcwd() + '\\dict\\ignore_dict.txt')

    def to_coord(self, stline, stto):
        return '%s.%s' % (str(stline), str(stto))

    def next_word(self):
        self.last_cursor_loc = self.txt_file.index(tk.INSERT)
        if self.err_punc_list and self.err_word_list is not None:
            pass
    
    def run_check_threaded(self, file=None):
        if file is None:
            self.sc.content = self.txt_file.get("1.0", tk.END)
        else:
            self.sc.load_content(file)
        AutoFixGUI(tk.Toplevel(self.master), self, True)
        IgnoreGUI(tk.Toplevel(self.master), self, True)

        for i in range(len(self.autofix_inp)):
            self.sc.content = self.sc.content.replace(self.autofix_inp[i], self.autofix_onp[i])


        if self.sc.content.strip() != '' or True:
            self.last_cursor_loc = self.txt_file.index(tk.INSERT)
            self.load_def_dicts()
            self.sc.pre_processing()
            err_punc_list = self.sc.func_check_punct()
            err_word_list = self.sc.remove_http(self.sc.func_check_single_word())

            self.err_punc_list = err_punc_list
            self.err_word_list = err_word_list

            self.txt_file.delete('1.0', tk.END)
            self.txt_file.insert(tk.INSERT, self.sc.content)
            soloi = 0
            replacelist = '.,()"''{}[]:'
            for err_word in err_word_list:
                err_word = list(err_word)
                for charc in replacelist:
                    err_word[-1] = err_word[-1].replace(charc, " ")
                if err_word[-1].strip() not in self.ignore_inp:
                    self.txt_file.tag_add(self.marked_tag, self.to_coord(err_word[0]+1, err_word[1]), self.to_coord(err_word[0]+1, err_word[1]  +len(err_word[2])))
                    soloi +=1
                    print(err_word)

            for err_word in err_punc_list:
                soloi+=1
                self.txt_file.tag_add(self.marked_tag, self.to_coord(err_word[0]+1, err_word[1]), self.to_coord(err_word[0]+1, err_word[1] + len(err_word[2])))
            self.txt_file.tag_config(self.marked_tag, background='red', foreground='white', wrap=tk.WORD)
            #self.txt_file.tag_config(self.marked_tag, underline=True, wrap=tk.WORD)

            self.txt_file.mark_set(tk.INSERT, str(self.last_cursor_loc))
            self.lb_ErrorNumber.configure(text='Tìm thấy %s lỗi' % soloi)

    def run_check(self, file=None):
        # t = Thread(target=self.run_check_threaded, args=(file,))
        # t.start()
        self.run_check_threaded(file)
        
if __name__ == '__main__':
    root = ThemedTk(theme="plastik")
    root.title('Kiểm tra lỗi chính tả')
    photo = tk.PhotoImage(file=r"image.png")
    root.iconphoto(False, photo)
    sc = cs.SpellingChecker()
    app = DatnGui1App(root, sc)
    app.run()
