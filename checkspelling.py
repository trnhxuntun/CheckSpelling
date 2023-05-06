import re

# The class of the program
class SpellingChecker:
    def __init__(self):
        self.ignore_dict_list = None
        self.dict_list = []
        self.content = None
        self.error_list = []
        self.fi = None
        self.di = None

    # General file loading function
    def load_file(self, file_path):
        file = open(file_path, 'r', encoding='utf-8')
        content = file.read()
        file.close()
        return content

    # Load dictionaries into a list
    def load_dict(self, dict_path):
        self.dict_list.append(self.load_file(dict_path).split('\n'))
    
    # Load content of the text file
    def load_content(self, file_path):
        self.content = self.load_file(file_path)

    def load_ignore_dict(self, file_path):
        self.ignore_dict_list = self.load_file(file_path).split('\n')

    def pre_processing(self):
        fi = self.content
        fi = fi.split('\n')
        di = ''
        for val in self.dict_list:
            di += " " + " ".join(val).lower()

        self.fi = fi
        self.di = di

    def remove_char_from_ignore_dict(self, word):
        if self.ignore_dict_list is not None:
            for char in self.ignore_dict_list:
                #print(word)
                word = word.replace(char, ' ')
            return word
            
    # Check is there is a space behind punctuation
    def func_check_punct(self):
        error_list = []
        rex = '(\s+[\.,!?])|([\.,!?]\s\s+)'

        count = 0
        for line in self.content.split('\n'):
            result = re.finditer(rex, line)
            p = re.compile(rex)
            for m in p.finditer(line):
                error_list.append((count, m.start(), m.group()))
            count += 1
        print(error_list)
        return error_list

    def func_check_single_word(self):
        error_list = []
        count = 0
        if (self.di  and self.fi and self.ignore_dict_list) is not None:
            for dong in self.fi:
                # Lay dong
                line = dong
                # Lay vi tri hien tai
                vt = 0
                # Lay tung chu trong cau
                for word in re.split('[\t\s]', line):
                    # Xoa het ki tu trong ignore dictionary va dau cach o dau va cuoi cai tu nay
                    altword = self.remove_char_from_ignore_dict((word.lower())).strip()
                    # Tim vi tri cua tu trong cau goc
                    ll = line.find(word) + vt
                    # Kiem tra xem tu do co rong hay khong
                    if len(word) == 0:
                        them = 1
                    else:
                        them = len(word) + 1
                        # Kiem tra xem tu co trong tu dien hay khong
                        if altword not in self.di and len(altword) > 0:
                            # Neu khong thi them vao danh sach loi
                            error_list.append((count, ll,  word))
                    # Cap nhap vi tri tren cau goc
                    vt += them
                    # Xoa tu vua tim duoc
                    line = line[them:]
                # Dem so dong
                count += 1
        return error_list

    def remove_http(self, error_list):
        outlist = []
        for i in range(len(error_list)):
            if not error_list[i][2].startswith('http'):
                outlist.append(error_list[i])
        return outlist

def runtest():
    sc = SpellingChecker()
    sc.load_content('test (2).txt')
    sc.load_dict('tudien.txt')
    sc.load_dict('vi-DauMoi.txt')
    sc.load_dict('eng-words.txt')
    sc.load_ignore_dict('ignore_dict.txt')
    sc.pre_processing()
    sc.func_check_punct()
    w = sc.func_check_single_word()
    sc.remove_http(w)
    
#runtest()
