from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo

root = Tk()
root.title("Меню авторизации")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
wh = (w // 2) - 700
hh = (h // 2) - 400
root.geometry(f"1384x753+{wh}+{hh}")
root.resizable(False, False)
canvas = Canvas(root, bg='white', width=1384, height=753)
canvas.place(x=0, y=0)
img = PhotoImage(file='C:/Users/tipoya/Desktop/ti/Frame 1.png')
enabled = IntVar()
x0, y0 = 50, 50
x1, y1 = 150, 150
radius = 20
log_registr = StringVar()
passwr_register = StringVar()
login = StringVar()
passw = StringVar()
n = 0
def igra():
    igr = Tk()
    igr.title("Шашки Артамонова")
    igr.geometry(f"1384x753+{wh}+{hh}")
    igr.resizable(False, False)
    canvas = Canvas(igr, bg='white', width=1384, height=753)
    canvas.place(x=0, y=0)
    igr.mainloop()
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
    global n
    f = open('base.txt', 'r')
    while TRUE:
        line = f.readline()
        line = line.split()
        if len(line) == 0:
            showerror(title="Ошибка", message="Логин и пароль не найдены")
            break
        elif line[0] == login.get() and line[1] == passw.get():
            f.close()
            showinfo(title="Информация", message="Авторизация успешно пройдена")
            root.destroy()
            igra()
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
    # Окно логина
    login_text = canvas.create_text(600, 325, text="Логин:", font=("Compact 15 bold"), fill="black")
    log_block = canvas.create_rectangle(550, 299, 649, 350, fill="white", outline="black")
    canvas.tag_lower(log_block,login_text)
    login = Entry(canvas, font=("Compact 18 bold"),relief = 'flat',textvariable = login)
    canvas.create_window(650, 300, anchor=NW, window=login, width=180, height=50)
    # Окно пароля
    passw_text = canvas.create_text(600, 390, text="Пароль:", font=("Compact 15 bold"), fill="black")
    passw_block = canvas.create_rectangle(550, 364, 649, 415, fill="white", outline="black")
    canvas.tag_lower(passw_block, passw_text)
    passw = Entry(canvas, font=("Compact 18 bold"),relief = 'flat',textvariable = passw,show = '*')
    canvas.create_window(650, 365, anchor=NW, window=passw, width=180, height=50)
    enabled_checkbutton = Checkbutton(text="", bg="#525252", activebackground="#525252", variable=enabled,
                                      command=lambda: paf(passw))
    canvas.create_window(830, 380, anchor=NW, window=enabled_checkbutton, width=0, height=0)
    # Кнопка авторизации
    but_one = Button(root,text="Авторизация",bg ="white",fg="black",activebackground="white",font=("Compact 11 bold"),relief = 'flat', cursor="hand2",command=avtor)
    canvas.create_window(595, 430, anchor=NW, window=but_one, width=200, height=30)
    # Кнопка регистрации
    log_block = canvas.create_rectangle(550, 480, 700, 510, fill="white", outline="black")
    login_text = canvas.create_text(625, 495, text="Первый раз в игре?", font=("Compact 11 bold"), fill="black")
    but_two = Button(root, text="Зарегистрируйся!!!", bg="white", fg="black", activebackground="white", font=("Compact 11 bold"),
                 relief='flat',command=registr, cursor="hand2")
    canvas.create_window(701, 480, anchor=NW, window=but_two, width=150, height=30)
reg(login,passw)
root.mainloop()
