## tkinter 사용방법 설명

# (정확하지 않은 설명일 수 있습니다.)

# App 클래스는 Tk 클래스를 상속하여 객체(프로그램 화면의 껍데기라고 생각하면 된다.)를 생성한다.
# App.switch_frame을 통해 프레임(껍데기 안을 구현할 공간)을 손쉽게 교체할 수 있다.
# 프레임은 tk.Frame을 상속하여 구현한다.

# Toplevel(새창)을 지원하기 위한 App.open_toplevel.
# 새 창은 Toplevel을 상속하여 클래스로 구현한다.

# Toplevel 클래스와 Frame 클래스는 생성자에 master라는 변수를 가지며
# 이는 App 클래스로 생성된 객체를 의미한다.
# 추가적으로 만든 기능들(User, Info 클래스)의 객체를 해당 master의 변수에 할당하면
# 전역에서 해당 객체를 사용할 수 있게 된다.

import tkinter as tk
import ctypes
from tkinter.ttk import Combobox
import random
import tkinter.messagebox as box
import os


class User:
    """유저의 회원가입 정보를 저장 및 수정하는 객체를 생성한다."""

    def __init__(self):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.check_already_file()
        self._ids = self.get_user_id()
        self._pws = self.get_user_pw()

    def check_already_file(self):
        """user.txt파일이 있으면 넘기고 없으면 만드는 함수"""
        if 'user.txt' not in os.listdir(os.getcwd()):
            with open("user.txt", 'w', encoding='UTF8') as f:
                f.write('\n\n\n')

    def read_users(self):
        self._ids = self.user_id
        self._pws = self.user_pw

    def get_user_id(self):
        """user.txt파일에서 id, pw줄을 읽어와 공백으로 분할한 리스트로 변환하는 함수"""
        with open('user.txt', 'r', encoding='UTF8') as f:
            self._lines = f.readlines()
            return list(filter(lambda x: x != '', self._lines[0].strip().split(sep="|")))

    def add_id(self, u_id):
        self._ids.append(u_id)

    def get_user_pw(self):
        with open('user.txt', 'r', encoding='UTF8') as f:
            self._lines = f.readlines()
            return list(filter(lambda x: x != '', self._lines[1].strip().split(sep="|")))

    def add_pw(self, u_pw):
        self._pws.append(u_pw)

    def check_already_id(self, i):
        if i in self._ids:
            return True
        return False

    def save(self):
        with open('user.txt', 'w', encoding='UTF-8') as f:
            f.write("|".join(self._ids) + "\n")
            f.write("|".join(self._pws) + "\n")

    def check_pw(self, i, p):
        """id와 pw를 받아 동일한 위치에 i, p가 있는지 확인하는 함수"""
        if self._pws[self._ids.index(i)] == p:
            return True
        return False

    def get_user_index(self, i):
        return self._ids.index(i)


class Info:
    """유저마다의 pw, 메모 저장 공간을 읽어오고 수정 및 저장하는 객체를 생성한다."""

    def __init__(self, i):
        self.index = i
        self._pws = self.read_pws().strip().split("|")
        self._memos = self.read_memos().strip().split("|")

    @staticmethod
    def set_info_space():   # 새로운 계정이 만들어졌을 때에만 사용된다.
        """새로 계정을 생성할 때 마다 info.txt 끝에 두 줄의 정보 공간을 추가한다."""
        with open('info.txt', 'a', encoding='UTF8') as f:
            f.write("||\n||\n")

    def get_memos(self):
        return self._memos

    def get_pws(self):
        return self._pws

    def read_pws(self):
        """info.txt파일의 i 유저 정보에 해당하는 줄 읽어오기"""
        with open('info.txt', 'r', encoding='UTF8') as f:
            return f.readlines()[self.index*2]

    def read_memos(self):
        """info.txt파일의 i 유저 정보에 해당하는 줄 읽어오기"""
        with open('info.txt', 'r', encoding='UTF8') as f:
            return f.readlines()[self.index*2+1]

    def save_file(self):
        """유저 정보에 해당되는 줄에 info.txt를 기록하는 함수"""
        with open('info.txt', 'r', encoding='UTF8') as f:
            sf = f.readlines()
            sf[self.index*2] = "|".join(self._pws) + "\n"
            sf[(self.index*2)+1] = "|".join(self._memos) + "\n"
        with open('info.txt', 'w', encoding='UTF8') as f:
            f.writelines(sf)

    def set_pw(self, pw):
        """빈 자리에 pw를 입력하고 True를 리턴한다. 빈 자리가 없다면 False를 반환한다."""
        if all(map(lambda x: x != '', self._pws)):
            return False
        for i in range(0, len(self._pws)):
            if self._pws[i] == '':
                self._pws[i] = pw
                return True

    def set_memos(self, m1, m2, m3):
        """self._memos의 각 자리와 m1, m2, m3를 교체한다."""
        self._memos[0] = m1
        self._memos[1] = m2
        self._memos[2] = m3

    def del_info(self, c1, c2, c3):
        """체크박스에 해당되는 자리를 삭제한다."""
        if c1:
            self._memos[0] = ""
            self._pws[0] = ""
        if c2:
            self._memos[1] = ""
            self._pws[1] = ""
        if c3:
            self._memos[2] = ""
            self._pws[2] = ""


class Tool:
    @staticmethod
    def display_setting(app, width, height):
        user32 = ctypes.windll.user32
        s_width = user32.GetSystemMetrics(0)
        s_height = user32.GetSystemMetrics(1)
        s_x = int((s_width/2)-(width/2))
        s_y = int((s_height/2)-(height/2))
        app.resizable(False, False)
        app.geometry("{}x{}+{}+{}".format(width, height, s_x, s_y))

    @staticmethod
    def create_password(i, sa, ba, n, s):
        if i == "":
            return "길이 선택"
        sa, ba, n, s = sa != False, ba != False, n != False, s != False
        if sa+ba+n+s == 0:
            return "구성문자 선택"
        s_alpha = [chr(x) for x in range(ord('a'), ord('z')+1)]
        b_alpha = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        number = [str(i) for i in range(0, 9+1)]
        special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
                   ';', '<', '=', '>', '?', '@', '[', '＼', ']', '^', '_', '`', '{', '}', '~', '\'']  # 구분자로 '|'를 사용해서, 제외.
        return "".join(random.sample(s_alpha*sa+b_alpha*ba+number*n+special*s, int(i)))


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def open_toplevel(self, toplevel_class):
        toplevel_class(self)


class LoginPage(tk.Frame):

    def login(self, master):
        u_id = self.e_id.get()
        u_pw = self.e_pw.get()
        if u_id == "":
            box.showinfo('오류', '아이디를 입력하세요.', parent=self)
        elif u_pw == "":
            box.showinfo('오류', '비밀번호를 입력하세요.', parent=self)
        elif u_id.count("|")+u_pw.count("|") != 0:
            box.showinfo('오류', '"|" 특수문자는 사용될 수 없습니다.', parent=self)
        elif not (master.user.check_already_id(u_id) and master.user.check_pw(u_id, u_pw)):
            box.showinfo('오류', '아이디 또는 비밀번호가 틀렸습니다.', parent=self)
        else:
            # 유저 인덱스를 저장해놓는다.
            master.user_index = master.user.get_user_index(u_id)
            master.switch_frame(MainPage)

    def __init__(self, master):

        master.user = User()

        master.title('로그인')
        tk.Frame.__init__(self, master)
        Tool.display_setting(master, 350, 250)
        tk.Label(self, text='　').pack(side="top", fill="x", pady=10)

        tk.Label(self, text="아이디 ").pack(anchor='w', expand='False')
        self.e_id = tk.Entry(self, text='', width=20)
        self.e_id.pack()

        tk.Label(self, text="비밀번호 ").pack(anchor='w')
        self.e_pw = tk.Entry(self, text='', width=20)
        self.e_pw.pack()

        tk.Button(self, text="로그인", command=lambda: self.login(
            master)).pack(side=tk.LEFT, pady=6, padx=6)
        tk.Button(self, text="회원가입", command=lambda: master.open_toplevel(
            JoinPage)).pack(side=tk.LEFT, pady=6, padx=10)


class JoinPage(tk.Toplevel):

    def dialog(self, master):
        value_0 = tk.Entry.get(self.entry_0)
        value_1 = tk.Entry.get(self.entry_1)
        value_2 = tk.Entry.get(self.entry_2)
        if value_0 == '' or value_1 == '' or value_2 == '':
            box.showinfo('오류', '값을 입력하세요', parent=self)
        elif value_1 != value_2:
            box.showinfo('오류', '비밀번호를 다시 확인해주세요.', parent=self)
        elif master.user.check_already_id(value_0):
            box.showinfo('오류', '이미 사용중인 아이디입니다.', parent=self)
        else:
            box.showinfo('완료', '비밀번호가 설정되었습니다', parent=self)
            master.user.add_id(value_0)
            master.user.add_pw(value_1)
            master.user.save()
            Info.set_info_space()
            self.destroy()

    def __init__(self, master):

        # self는 Toplevel 객체이다.
        tk.Toplevel.__init__(self, master)
        self.title("JoinPage")
        Tool.display_setting(self, 300, 250)

        tk.Label(self, text='아이디').pack()
        self.entry_0 = tk.Entry(self)
        self.entry_0.pack(padx=10, pady=10)

        tk.Label(self, text='비밀번호').pack()
        self.entry_1 = tk.Entry(self)
        self.entry_1.pack(padx=10, pady=10)

        tk.Label(self, text='비밀번호 확인').pack()
        self.entry_2 = tk.Entry(self)
        self.entry_2.pack(padx=10)

        btn = tk.Button(self, text='비밀번호 저장',
                        command=lambda: self.dialog(master))
        btn_2 = tk.Button(self, text='나가기', command=self.destroy)
        btn.pack(side=tk.LEFT, padx=40)
        btn_2.pack(side=tk.RIGHT, padx=40)


class MainPage(tk.Frame):

    def set_password(self):
        self.entry.delete(0, "end")
        self.entry.insert(0, Tool.create_password(self.combo_box.get(
        ), self.v1.get(), self.v2.get(), self.v3.get(), self.v4.get()))

    def save_password(self, master):
        if self.entry.get().count("|") != 0:
            box.showinfo('오류', '사용될 수 없는 특수문자("|")가 사용되었습니다.', parent=self)
        elif master.info.set_pw(self.entry.get()):
            box.showinfo('완료', '비밀번호가 저장되었습니다.', parent=self)
            master.info.save_file()
        else:
            box.showinfo('오류', '비밀번호를 저장할 공간이 부족합니다.', parent=self)

    def __init__(self, master):
        # self는 Frame 객체이다.
        tk.Frame.__init__(self, master)
        master.title('MainPage')
        Tool.display_setting(master, 300, 220)
        master.info = Info(master.user_index)

        tk.Label(self, text=" ").grid(row=0, column=0)

        tk.Label(self, text="길이 : ").grid(row=1, column=0)
        self.combo_box = Combobox(self, width=12, values=[
                                  i for i in range(8, 13)])
        self.combo_box.grid(row=1, column=1)
        tk.Button(self, text='생성', command=lambda: self.set_password()).grid(
            row=1, column=4)

        self.v1, self.v2, self.v3, self.v4 = tk.IntVar(
        ), tk.IntVar(), tk.IntVar(), tk.IntVar()
        tk.Checkbutton(self, text="소문자", variable=self.v1).grid(
            row=2, column=1, sticky='w')
        tk.Checkbutton(self, text="대문자", variable=self.v2).grid(
            row=3, column=1, sticky='w')
        tk.Checkbutton(self, text="숫자", variable=self.v3).grid(
            row=4, column=1, sticky='w')
        tk.Checkbutton(self, text="특수문자", variable=self.v4).grid(
            row=5, column=1, sticky='w')

        tk.Label(self, text="출력 : ").grid(row=6, column=0)
        self.entry = tk.Entry(self, width=14)
        self.entry.grid(row=6, column=1)
        tk.Button(self, text='저장', command=lambda: self.save_password(master)).grid(
            row=6, column=4, padx=5)

        tk.Button(self, text='PW 관리', command=lambda: master.open_toplevel(
            DBPage)).grid(row=7, column=5, pady=15, sticky='e')


class DBPage(tk.Toplevel):

    def load_text(self, master):
        self.pw1.configure(state='normal')
        self.pw2.configure(state='normal')
        self.pw3.configure(state='normal')
        self.pw1.delete(0, 'end')
        self.pw2.delete(0, 'end')
        self.pw3.delete(0, 'end')
        self.pw1.insert(0, master.info._pws[0])
        self.pw2.insert(0, master.info._pws[1])
        self.pw3.insert(0, master.info._pws[2])
        self.pw1.configure(state='readonly')
        self.pw2.configure(state='readonly')
        self.pw3.configure(state='readonly')
        self.memo1.delete(0, 'end')
        self.memo2.delete(0, 'end')
        self.memo3.delete(0, 'end')
        self.memo1.insert(0, master.info._memos[0])
        self.memo2.insert(0, master.info._memos[1])
        self.memo3.insert(0, master.info._memos[2])

    def save_file(self, master):
        box.showinfo('완료', '모든 변경사항이 저장되었습니다.', parent=self)
        self.set_memos(master)
        master.info.save_file()
        self.load_text(master)

    def del_text(self, master):
        if self.v1.get() == 1:
            master.info._pws[0] = ""
            master.info._memos[0] = ""
        if self.v2.get() == 1:
            master.info._pws[1] = ""
            master.info._memos[1] = ""
        if self.v3.get() == 1:
            master.info._pws[2] = ""
            master.info._memos[2] = ""
        self.load_text(master)

    def set_memos(self, master):
        master.info._memos[0] = self.memo1.get()
        master.info._memos[1] = self.memo2.get()
        master.info._memos[2] = self.memo3.get()

    def __init__(self, master):
        # self는 Toplevel 객체이다.
        tk.Toplevel.__init__(self, master)
        self.title("DBPage")
        Tool.display_setting(self, 270, 200)

        tk.Label(self, text="P W").place(x=90, y=20, width=40)
        tk.Label(self, text="MEMO").place(x=190, y=20)

        self.v1, self.v2, self.v3 = tk.IntVar(), tk.IntVar(), tk.IntVar()
        self.c_b1 = tk.Checkbutton(self, bd=2, relief='flat',
                                   variable=self.v1)
        self.c_b2 = tk.Checkbutton(self, bd=2, relief='flat',
                                   variable=self.v2)
        self.c_b3 = tk.Checkbutton(self, bd=2, relief='flat',
                                   variable=self.v3)
        self.c_b1.place(x=10, y=50)
        self.c_b2.place(x=10, y=90)
        self.c_b3.place(x=10, y=130)

        self.pw1 = tk.Entry(self, width=17, state='readonly')
        self.pw2 = tk.Entry(self, width=17, state='readonly')
        self.pw3 = tk.Entry(self, width=17, state='readonly')
        self.pw1.place(x=50, y=53)
        self.pw2.place(x=50, y=93)
        self.pw3.place(x=50, y=133)

        self.memo1 = tk.Entry(self, text='', width=8)
        self.memo2 = tk.Entry(self, text='', width=8)
        self.memo3 = tk.Entry(self, text='', width=8)
        self.memo1.place(x=190, y=53)
        self.memo2.place(x=190, y=93)
        self.memo3.place(x=190, y=133)

        self.b_save = tk.Button(
            self, text='저장', command=lambda: self.save_file(master))
        self.b_save.place(x=175, y=160)
        self.b_del = tk.Button(
            self, text='삭제', command=lambda: self.del_text(master))
        self.b_del.place(x=220, y=160)

        self.load_text(master)


if __name__ == "__main__":
    app = App()
    app.mainloop()