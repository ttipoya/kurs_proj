from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
from functools import partial
root= Tk()
root.title("Меню авторизации")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
wh = (w // 2) - 700
hh = (h // 2) - 400
root.geometry(f"1384x753+{wh}+{hh}")
root.resizable(False, False)
canvas = Canvas(root, bg='white', width=1384, height=753)
canvas.place(x=0, y=0)
img = PhotoImage(file='Frame 1.png')
root.withdraw()
enabled = IntVar()
x0, y0 = 50, 50
x1, y1 = 150, 150
radius = 20
k = 77
log_registr = StringVar()
passwr_register = StringVar()
login = StringVar()
passw = StringVar()
rastanovka = [[1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0]]
n = 0
def check(y):
    global k
    if  pol[y - 1]['image'] == 'pyimage5':
        if k == 77:
            pol[y - 1]['bg'] = 'red'
            k = y
        else:
            pol[k - 1]['bg'] = 'black'
            pol[y-1]['bg'] = 'red'
            k = y
        print(k,y)
        if pol[y - 10]['image'] == '':
            pol[y - 10]['bg'] = 'red'
        if pol[y - 8]['image'] == '':
            pol[y - 8]['bg'] = 'red'
        if pol[y+8]['image'] == '':
            pol[y+8]['bg'] = 'red'
        if pol[y+6]['image'] == '':
            pol[y+6]['bg'] = 'red'
    if pol[y - 1]['image'] == '' and pol[y - 1]['bg'] == 'red':
        pol[k -1]['image'] = ''
        pol[y - 1]['image'] = 'pyimage5'
        pol[k - 1]['bg'] = 'black'
        pol[y - 1]['bg'] = 'black'
        pol[k+8]['bg'] = 'black'
        pol[k + 6]['bg'] = 'black'
        pol[k -8]['bg'] = 'black'
        pol[k -10]['bg'] = 'black'
def otris(canvas_igr,igr):
    canvas_igr.create_rectangle(340, 10, 1033, 705, fill="black", outline="black", tags='nastr')
    global color
    l = 0
    global pol
    pol = []
    n = 350
    w = 20
    for i in range(1, 9):
        for j in range(1, 9):
            l += 1
            if i % 2 == 0:
                if l % 2 ==0:
                    color = "white"
                else:
                    color = "black"
            elif i % 2 != 0:
                if l % 2 !=0 :
                    color = "white"
                else:
                    color = "black"
            pol.append(Button(igr,bg=color, fg="white", activebackground="white", relief="flat",command= partial(check,l)))
            if pol[l-1]['bg'] == 'white':
                pol[l-1]['state'] = DISABLED
            canvas_igr.create_window(n, w, anchor=NW, window=pol[l-1], width=80, height=80)
            if l in [2,4,6,8,18,20,22,24,9,11,13,15,41,43,45,47,50,52,54,56,57,59,61,63]:
                pol[l-1].config(image = shash)
            n += 85
        n = 350
        w += 85
def igra(glavmenu):
    global color
    glavmenu.destroy()
    igr = Tk()
    igr.title("Шашки Артамонова")
    igr.geometry(f"1384x753+{wh}+{hh}")
    igr.resizable(False, False)
    global canvas_igr
    canvas_igr = Canvas(igr, bg='white', width=1384, height=753)
    canvas_igr.place(x=0, y=0)
    img_igr = PhotoImage(master=canvas_igr, file='Frame 1.png')
    global shash
    shash = PhotoImage(master=canvas_igr, file='Group 8.png')
    shash = shash.subsample(2, 2)
    canvas_igr.create_image(0, 0, anchor='nw', image=img_igr)
    otris(canvas_igr,igr)
    igr.mainloop()
def nastr(canvas_glav,igr):
    canvas_glav.create_rectangle(530, 210, 930, 250, fill="white", outline="black",tags='nastr')
    canvas_glav.create_text(730, 230, text="Настройки", font=("Compact 18 bold"), fill="black",tags='nastr')
    canvas_glav.create_rectangle(530, 250, 930, 580, fill="#525252", outline="black",tags='nastr')
    but_zak = Button(igr,text="Закрыть", bg="white", fg="black", activebackground="white",
                      font=("Compact 15 bold"), relief='flat', cursor="hand2",command= lambda: canvas_glav.delete('nastr'))
    canvas_glav.create_window(630, 500, anchor=NW, window=but_zak, width=200, height=35,tags='nastr')
def vih():
    exit()
def glav_menu():
    #-------------------------------создание окна-------------------------------
    glavmenu = Tk()
    glavmenu.title("Главное меню")
    glavmenu.geometry(f"1384x753+{wh}+{hh}")
    glavmenu.resizable(False, False)
    canvas_glav_menu = Canvas(glavmenu, bg='white', width=1384, height=753)
    canvas_glav_menu.place(x=0, y=0)
    # -------------------------------фон-------------------------------
    img_menu = PhotoImage(master = canvas_glav_menu,file='Frame 1.png')
    canvas_glav_menu.create_image(0, 0, anchor='nw', image=img_menu)
    # -------------------------------размещение блоков-------------------------------
    canvas_glav_menu.create_rectangle(100, 210, 500, 250, fill="white", outline="black")
    canvas_glav_menu.create_text(290, 230, text="Главное меню", font=("Compact 18 bold"), fill="black")
    canvas_glav_menu.create_rectangle(100, 250, 500, 580, fill="#525252", outline="black")
    # -------------------------------размещение кнопок-------------------------------
    but_nach = Button(glavmenu, text="Начать игру", bg="white", fg="black", activebackground="white",
                      font=("Compact 15 bold"), relief='flat', cursor="hand2", command= lambda:igra(glavmenu)) # начло игры
    canvas_glav_menu.create_window(150, 300, anchor=NW, window=but_nach, width=300, height=50)
    but_nastr = Button(glavmenu, text="Настройки", bg="white", fg="black", activebackground="white",
                       font=("Compact 15 bold"), relief='flat', cursor="hand2", command= lambda: nastr(canvas_glav_menu, glavmenu)) # настройки
    canvas_glav_menu.create_window(150, 370, anchor=NW, window=but_nastr, width=300, height=50)
    but_vih = Button(glavmenu, text="Выход", bg="white", fg="black", activebackground="white",
                     font=("Compact 15 bold"), relief='flat', cursor="hand2", command=vih) # выход
    canvas_glav_menu.create_window(150, 440, anchor=NW, window=but_vih, width=300, height=50)
    glavmenu.mainloop()
def paf(par_ent):
    if enabled.get() == 1:
        par_ent['show'] = ''
    if enabled.get() == 0:
        par_ent['show'] = '*'
def ok():
    if (len(passwr_register.get()) >= 4 and len(passwr_register.get()) <=10) and (log_registr.get().count(' ') == 0 and passwr_register.get().count(' ') == 0):
        showinfo(title="Информация", message="Регистрация успешно пройдена")
        f = open('base.txt', 'a+')
        canvas.delete("reg")
        f.write(log_registr.get() +' '+ passwr_register.get()+'\n')
        f.close()
        log_registr.set('')
        passwr_register.set('')
    else:
        showerror(title="Ошибка", message="Пароль должен быть от 4 до 8 символов")
def avtor():
    if (len(login.get()) == 0 or len(passw.get()) == 0) or (len(login.get()) == 0 and len(passw.get()) == 0):
        showerror(title="Ошибка", message="Поля не должны быть пустыми")
    else:
        f = open('base.txt', 'r')
        while TRUE:
            line = f.readline()
            line = line.split()
            if len(line) == 0:
                f.close()
                showerror(title="Ошибка", message="Логин и пароль не найдены")
                break
            elif line[0] == login.get() and line[1] == passw.get():
                f.close()
                showinfo(title="Информация", message="Авторизация успешно пройдена")
                root.destroy()
                glav_menu()
                break

def registr():
    block_naz = canvas.create_rectangle(890, 210, 1200, 250, fill="white", outline="black",tags= "reg")
    block_one = canvas.create_rectangle(890, 250, 1200, 550, fill="#525252", outline="black",tags= "reg")
    leib1 = canvas.create_text(1050, 230, text="Регистрация", font=("Compact 18 bold"), fill="black",tags= "reg")
    log_block = canvas.create_rectangle(950, 280, 1150, 320, fill="white", outline="black",tags= "reg")
    log_reg = canvas.create_text(1050, 300, text="Введите логин\n без пробелов", font=("Compact 13 bold"), fill="black",tags= "reg")
    login_reg = Entry(canvas, font=("Compact 18 bold"), relief='flat',textvariable = log_registr)
    canvas.create_window(950, 325, anchor=NW, window=login_reg, width=201, height=30,tags= "reg")
    passw_block = canvas.create_rectangle(950, 370, 1150, 410, fill="white", outline="black", tags="reg")
    passw_reg = canvas.create_text(1050, 390, text="    Введите пароль\n от 4 до 8 символов", font=("Compact 13 bold"), fill="black", tags="reg")
    passwor_reg = Entry(canvas, font=("Compact 18 bold"), relief='flat',textvariable = passwr_register)
    canvas.create_window(950, 415, anchor=NW, window=passwor_reg, width=201, height=30, tags="reg")
    but_two = Button(root, text="Зарегистрироваться", bg="white", fg="black", activebackground="white",
                     font=("Compact 11 bold"),
                     relief='flat', command= ok, cursor="hand2")
    canvas.create_window(980, 460, anchor=NW, window=but_two, width=150, height=30, tags="reg")

def reg(login,passw):
    image = canvas.create_image(0, 0, anchor='nw', image=img)
    canvas.create_rectangle(500, 210, 884, 250, fill="white", outline="black")
    leib = canvas.create_text(695, 230, text="Авторизация", font=("Compact 18 bold"), fill="black")
    block_one = canvas.create_rectangle(500, 250, 884, 550, fill="#525252", outline="black")
    # -------------------------------Окно логина-------------------------------
    login_text = canvas.create_text(600, 325, text="Логин:", font=("Compact 15 bold"), fill="black")
    log_block = canvas.create_rectangle(550, 299, 649, 350, fill="white", outline="black")
    canvas.tag_lower(log_block,login_text)
    login = Entry(canvas, font=("Compact 18 bold"),relief = 'flat',textvariable = login)
    canvas.create_window(650, 300, anchor=NW, window=login, width=180, height=50)
    # -------------------------------Окно пароля-------------------------------
    passw_text = canvas.create_text(600, 390, text="Пароль:", font=("Compact 15 bold"), fill="black")
    passw_block = canvas.create_rectangle(550, 364, 649, 415, fill="white", outline="black")
    canvas.tag_lower(passw_block, passw_text)
    passw = Entry(canvas, font=("Compact 18 bold"),relief = 'flat',textvariable = passw,show = '*')
    canvas.create_window(650, 365, anchor=NW, window=passw, width=180, height=50)
    enabled_checkbutton = Checkbutton(text="", bg="#525252", activebackground="#525252", variable=enabled,
                                      command=lambda: paf(passw))
    canvas.create_window(830, 380, anchor=NW, window=enabled_checkbutton, width=0, height=0)
    # -------------------------------Кнопка авторизации-------------------------------
    but_one = Button(root,text="Авторизация",bg ="white",fg="black",activebackground="white",font=("Compact 11 bold"),relief = 'flat', cursor="hand2",command=avtor)
    canvas.create_window(595, 430, anchor=NW, window=but_one, width=200, height=30)
    # -------------------------------Кнопка регистрации-------------------------------
    log_block = canvas.create_rectangle(550, 480, 700, 510, fill="white", outline="black")
    login_text = canvas.create_text(625, 495, text="Первый раз в игре?", font=("Compact 11 bold"), fill="black")
    but_two = Button(root, text="Зарегистрируйся!!!", bg="white", fg="black", activebackground="white", font=("Compact 11 bold"),
                 relief='flat',command=registr, cursor="hand2")
    canvas.create_window(701, 480, anchor=NW, window=but_two, width=150, height=30)
glav_menu()
#reg(login,passw)
root.mainloop()
