from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
root= Tk()
root.title("Меню авторизации")
w = root.winfo_screenwidth();h = root.winfo_screenheight()
wh = (w // 2) - 700;hh = (h // 2) - 400
root.geometry(f"1384x753+{wh}+{hh}")
root.resizable(False, False)
canvas = Canvas(root, bg='white', width=1384, height=753)
canvas.place(x=0, y=0)
img = PhotoImage(file='background.png')
enabled = IntVar()
x0, y0 = 50, 50
x1, y1 = 150, 150
x_pred = 77;y_pred = 77
log_registr = StringVar();passwr_register = StringVar()
login = StringVar();passw = StringVar()
ngo = 1
score_igrok = 0;score_bot = 0;chet_do_konca = 15
hodim = -1
i_last_last = 0;x_last_last = 0;y_last_last = 0
check_dal = 0;check_bliz = 0;check_hod_mat = 0;ch = 0
global rastanovka
rastanovka = []
global mat_knopok,ves
mat_knopok = []
ves = [[1,2,3,4,5,6,7,8],
        [9,10,11,12,13,14,15,16],
        [17,18,19,20,21,22,23,24],
        [25,26,27,28,29,30,31,32],
        [33,34,35,36,37,38,39,40],
        [41,42,43,44,45,46,47,48],
        [49,50,51,52,53,54,55,56],
        [57,58,59,60,61,62,63,64]]
suma_dal = 0;suma_bliz = 0;poz_bot_x = 0;poz_bot_y = 0
max_poz = 0;win_igr = 0;win_bot = 0;nich = 0
def proverka_na_conec(a, b):
    global win_igr,win_bot,nich,hodim,score_bot,score_igrok,chet_do_konca
    suma= 0
    chek_tup= 0
    kol_mat = 0
    for i in range(8):
        for j in range(8):
            if rastanovka[i][j] == 1 or rastanovka[i][j] == -1:
                suma += 1
                if i == 0:
                    chek_tup += 1
                else:
                    chek_tup= 0
    if (suma == 1) or (suma == 0) or(suma > 0 and chek_tup >0 and chek_tup<5) or chet_do_konca == 0:
        if a > b:
            igr.destroy()
            glavmenu.deiconify()
            showinfo(title="", message="Выйграл игрок")
            win_igr +=1
        elif a < b:
            igr.destroy()
            glavmenu.deiconify()
            showinfo(title="", message="Выйграл бот")
            win_bot += 1
        else:
            igr.destroy()
            glavmenu.deiconify()
            showinfo(title="", message="Ничья")
            nich +=1
        hodim = -1
        score_bot = 0
        score_igrok = 0
        chet_do_konca = 15

def smena_hoda():
    #-------------------------------смена номера хода-------------------------------
    global hodim
    if hodim == 1:
        hodim = -1
    else:
        hodim = 1
def bot():
    #-------------------------------бот-------------------------------
    global return_check
    for io in range(8):
        for jo in range(8):
            if mat_knopok[io][jo]['state'] == NORMAL and mat_knopok[io][jo]['image'] != '' and mat_knopok[io][jo]['bg'] != 'white':
                if return_check == 1:
                    return_check = 0
                    break
                elif return_check == 0:
                    pokaz_dostup_hodov(io, jo, 0, 1, rastanovka[io][jo])
        if return_check == 1:
            break
    click_check(0, poz_bot_x, poz_bot_y, 0);click_check(0, poz_bot_x_next, poz_bot_y_next, 1)
def pokaz_dostup_hodov(x, y, clear, bot, k):
    global ch,suma_bliz,suma_dal,poz_bot_x_next ,poz_bot_y_next ,max_poz,poz_bot_x,poz_bot_y,fash,score,suma_hod_mat,return_check
    fash = 0;score = 0
    chek_M_1 = 0;chek_M_2 = 0;chek_M_3 = 0;chek_M_4 = 0
    if clear == 1:
        max_poz = 0
        #-------------------------------очистка клеток от красного у шашки-------------------------------
        if k == -1 or k == 1:
            for i in range(((x + x_last) // 2) - 1, ((x + x_last) // 2) + 2):
                for j in range(((y + y_last) // 2) - 1, ((y + y_last) // 2) + 2):
                    if i >= 0 and j >= 0 and i<8 and j<8 and i != x and j !=y and mat_knopok[i][j]['bg'] == '#8B2323':
                        mat_knopok[i][j]['bg'] = 'black'
                    elif i >= 0  and j>=0 and i<8 and j<8 and i != x and j !=y and mat_knopok[i][j]['image'] != '' and mat_knopok[i][j]['bg'] == 'black':
                        if (i + (i - x) >= 0) and (j + (j - y) >= 0) and (i + (i - x)) < 8 and (j + (j - y)) < 8 and i != x and j != y and mat_knopok[i + (i - x)][j + (j - y)]['bg'] == '#8B2323':
                            mat_knopok[i + (i - x)][j + (j - y)]['bg'] = 'black'
        elif k == 2:
            #-------------------------------очистка клеток от красного у дамки + удаление съеденых-------------------------------
            for i in range(7, 0,-1):
                if x + i >= 0 and y + i >= 0 and x + i < 8 and y + i < 8:
                    if mat_knopok[x + i][y + i]['image'] == str(shash_M) and chek_M_1 == 0:
                        chek_M_1 = 1
                    elif mat_knopok[x + i][y + i]['image'] == str(shash_M) and chek_M_1 == 1:
                        mat_knopok[x + i][y + i]['image'] = ''
                        rastanovka[x - i][y + i] = 0
                        score += 1
                    if (mat_knopok[x + i][y + i]['image'] == str(shash)) and chek_M_1 == 1:
                        mat_knopok[x + i][y + i]['image'] = ''
                        rastanovka[x + i][y + i] = 0
                        score += 1
                    mat_knopok[x + i][y + i]['bg'] = 'black'
                if x - i >= 0 and y + i >= 0 and x - i < 8 and y + i < 8:
                    if mat_knopok[x - i][y + i]['image'] == str(shash_M) and chek_M_2 == 0:
                        chek_M_2 = 1
                    elif mat_knopok[x - i][y + i]['image'] == str(shash_M) and chek_M_2 == 1:
                        mat_knopok[x - i][y + i]['image'] = ''
                        rastanovka[x - i][y + i] = 0
                        score += 1
                    if (mat_knopok[x - i][y + i]['image'] == str(shash)) and chek_M_2 == 1:
                        mat_knopok[x - i][y + i]['image'] = ''
                        rastanovka[x - i][y + i] = 0
                        score += 1
                    mat_knopok[x - i][y + i]['bg'] = 'black'
                if x + i >= 0 and y - i >= 0 and x + i < 8 and y - i < 8:
                    if mat_knopok[x + i][y - i]['image'] == str(shash_M) and chek_M_3 == 0:
                        chek_M_3 = 1
                    elif mat_knopok[x + i][y - i]['image'] == str(shash_M) and chek_M_3 == 1:
                        mat_knopok[x + i][y - i]['image'] = ''
                        rastanovka[x + i][y - i] = 0
                        score += 1
                    if (mat_knopok[x + i][y - i]['image'] == str(shash)) and chek_M_3 == 1:
                        mat_knopok[x + i][y - i]['image'] = ''
                        rastanovka[x + i][y - i] = 0
                        score += 1
                    mat_knopok[x + i][y - i]['bg'] = 'black'
                if x - i >= 0 and y - i >= 0 and x - i < 8 and y - i < 8:
                    if mat_knopok[x - i][y - i]['image'] == str(shash_M):
                        chek_M_4 = 1
                    elif mat_knopok[x - i][y - i]['image'] == str(shash_M) and chek_M_4 == 1:
                        mat_knopok[x - i][y - i]['image'] = ''
                        rastanovka[x - i][y - i] = 0
                        score += 1
                    if (mat_knopok[x - i][y - i]['image'] == str(shash))and chek_M_4 == 1:
                        mat_knopok[x - i][y - i]['image'] = ''
                        rastanovka[x - i][y - i] = 0
                        score+=1
                    mat_knopok[x - i][y - i]['bg'] = 'black'
    elif clear == 0:
            #-------------------------------подсветка доступных ходов-------------------------------
            suma_hod_mat = 0;suma_bliz = 0;suma_dal = 0;max_poz = 0;return_check = 0
            if k == -1 or k == 1:
                #-------------------------------для шашки-------------------------------
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if (i >= 0 and j >= 0 and i != x and j != y and i < 8 and j < 8 and mat_knopok[i][j]['image'] == '' and mat_knopok[i][j]['bg'] == 'black') and check_dal == 0 and check_bliz == 0:
                            if (x - i) != hodim:
                                if bot == 0:
                                    mat_knopok[i][j]['bg'] = '#8B2323'
                                    suma_bliz += 1
                                    poz_bot_x_next = i
                                    poz_bot_y_next = j
                                else:
                                    suma_bliz += 1
                                if max_poz < ves[i][j] and suma_bliz > 0 and mat_knopok[i][j]['state'] == NORMAL and mat_knopok[x][y]['state'] == NORMAL:
                                    max_poz = ves[i][j]
                                    poz_bot_x = x
                                    poz_bot_y = y
                                    poz_bot_x_next = i
                                    poz_bot_y_next = j
                        elif i >= 0 and j>=0 and i != x and j !=y and i<8 and j<8 and mat_knopok[i][j]['image'] != '' and  mat_knopok[i][j]['bg'] == 'black':
                            if ((i+(i-x) >= 0) and (j+(j-y)>=0) and (i+(i-x)) < 8 and (j+(j-y)) < 8 and i != x and j != y and mat_knopok[i + (i - x)][j + (j - y)]['image'] == '') and check_bliz == 0:
                                if bot == 0:
                                    mat_knopok[i + (i - x)][j + (j - y)]['bg'] = '#8B2323'
                                    suma_dal += 1
                                    poz_bot_x_next = i + (i - x)
                                    poz_bot_y_next = j + (j - y)
                                else:
                                    suma_dal += 1
                                if suma_dal>0 and mat_knopok[i][j]['state'] == NORMAL and mat_knopok[x][y]['state'] == NORMAL:
                                    max_poz = ves[i+(i-x)][j+(j-y)]
                                    poz_bot_x = x
                                    poz_bot_y = y
                                    poz_bot_x_next = i+(i-x)
                                    poz_bot_y_next = j+(j-y)
                                    return_check =1
            elif k == 2:
                #-------------------------------для дамки-------------------------------
                for i in range(1, 7):
                    if x + i >= 0 and y + i >= 0 and x + i < 8 and y + i < 8:
                        if mat_knopok[x + i][y + i]['image'] == '':
                            fash = 0
                            if bot == 1:
                                max_poz = 9999
                                poz_bot_x = x;poz_bot_y = y;poz_bot_x_next = x + i;poz_bot_y_next = y + i
                            else:
                                mat_knopok[x + i][y + i]['bg'] = '#8B2323'
                        if mat_knopok[x + i][y + i]['image'] != '' and fash == 0:
                            fash += 1
                            suma_hod_mat +=1
                        elif mat_knopok[x + i][y + i]['image'] != '' and fash == 1:
                            suma_hod_mat = 0
                            break
                fash = 0
                for i in range(1, 7):
                    if x - i >= 0 and y + i >= 0 and x - i < 8 and y + i < 8:
                        if mat_knopok[x - i][y + i]['image'] == '':
                            fash = 0
                            if bot == 1:
                                max_poz = ves[x - i][y + i];poz_bot_x = x;poz_bot_y = y
                                poz_bot_x_next = x - i;poz_bot_y_next = y + i
                            else:
                                mat_knopok[x - i][y + i]['bg'] = '#8B2323'
                        if mat_knopok[x - i][y + i]['image'] != '' and fash == 0:
                            fash += 1
                            suma_hod_mat += 1
                        elif mat_knopok[x - i][y + i]['image'] != '' and fash == 1:
                            fash = 0
                            suma_hod_mat = 0
                            break
                fash = 0
                for i in range(1, 7):
                    if x + i >= 0 and y - i >= 0 and x + i < 8 and y - i < 8:
                        if mat_knopok[x + i][y - i]['image'] == '':
                            fash = 0
                            if bot == 1:
                                max_poz = ves[x + i][y - i]
                                poz_bot_x = x;poz_bot_y = y
                                poz_bot_x_next = x + i;poz_bot_y_next = y - i
                            else:
                                mat_knopok[x + i][y - i]['bg'] = '#8B2323'
                        if mat_knopok[x + i][y - i]['image'] != '' and fash == 0:
                            fash += 1
                            suma_hod_mat += 1
                        elif mat_knopok[x + i][y - i]['image'] != '' and fash == 1:
                            fash = 0
                            suma_hod_mat = 0
                            break
                fash = 0
                for i in range(1, 7):
                    if x - i >= 0 and y - i >= 0 and x - i < 8 and y - i < 8:
                        if mat_knopok[x - i][y - i]['image'] == '':
                            fash = 0
                            if bot == 1:
                                max_poz = ves[x - i][y - i]
                                poz_bot_x = x;poz_bot_y = y
                                poz_bot_x_next = x - i;poz_bot_y_next = y - i
                            else:
                                mat_knopok[x - i][y - i]['bg'] = '#8B2323'
                        if mat_knopok[x - i][y - i]['image'] != '' and fash == 0:
                            fash += 1
                            suma_hod_mat += 1
                        elif mat_knopok[x - i][y - i]['image'] != '' and fash == 1:
                            fash = 0
                            suma_hod_mat = 0
                            break

def click_check(i, x, y, boti):
    global ngo, i_last,x_last,y_last,score_igrok,score_bot,chet_do_konca,i_last_last,hodim,x_last_last,y_last_last,ch,suma_dal,suma_bliz,igr,check_dal,check_bliz,check_hod_mat
    #-------------------------------первое нажатие-------------------------------
    if ngo == 1 and mat_knopok[x][y]['image'] != '':
        ngo = 2
        i_last = i
        x_last = x
        y_last = y
        pokaz_dostup_hodov(x, y, 0, 0, rastanovka[x][y])
        if suma_dal == 0 and suma_bliz == 0 and rastanovka[x][y] != 2:
            showerror(title="Not", message="Ходов 0")
            ngo = 1
            ch = 0
            return
        if boti == 1:
            ngo = 2
            click_check(i, poz_bot_x_next, poz_bot_y_next, 1)
    #-------------------------------второе нажатие-------------------------------
    elif ngo == 2 and mat_knopok[x_last][y_last]['image'] != '':
        #-------------------------------если ход на две клетки-------------------------------
        if abs(y - y_last) == 2 and mat_knopok[(x + x_last) // 2][(y + y_last) // 2]['image'] != '' and mat_knopok[x][y]['image'] == '':
            mat_knopok[(x + x_last) // 2][(y + y_last) // 2]['image'] = ''
            rastanovka[(x + x_last) // 2][(y + y_last) // 2] = 0
            check_dal += 1
            #-------------------------------добавление к результату-------------------------------
            if hodim == -1:
                score_igrok += 1
                canvas_igr.itemconfigure(sc_1, text=f"Cчёт первого игрока: {score_igrok}")
                chet_do_konca = 16
                canvas_igr.itemconfigure(hodi, text=f'До конца{chet_do_konca}')
            elif hodim == 1:
                score_bot += 1
                canvas_igr.itemconfigure(sc_2, text=f"Cчёт второго игрока: {score_bot}")
                chet_do_konca = 16
                canvas_igr.itemconfigure(hodi, text=f'До конца{chet_do_konca}')
        #-------------------------------если ход на более двух клеток-------------------------------
        if abs(y-y_last) > 2 and mat_knopok[x][y]['image'] == '':
            if hodim == -1:
                score_igrok += score
                canvas_igr.itemconfigure(sc_1, text=f"Cчёт первого игрока: {score_igrok}")
                chet_do_konca = 16
                canvas_igr.itemconfigure(hodi, text=f'До конца{chet_do_konca}')
            elif hodim == 1:
                score_bot += score
                canvas_igr.itemconfigure(sc_2, text=f"Cчёт второго игрока: {score_bot}")
                chet_do_konca = 16
                canvas_igr.itemconfigure(hodi, text=f'До конца{chet_do_konca}')
            check_hod_mat += 1
        #-------------------------------если нажата даже клетка-------------------------------
        if x == x_last and y == y_last:
            mat_knopok[x_last][y_last]['bg'] = 'black'
            pokaz_dostup_hodov(x_last, y_last, 1, 0, rastanovka[x][y])
            if check_dal != 0:
                smena_hoda()
                ngo = 1
                ch = 0
                check_dal = 0
                check_bliz = 0
                x_last = 0
                y_last = 0
                bot()
                return
            else:
                ngo = 1
                return
        #-------------------------------если нажата кнопка с подсветкой-------------------------------
        if mat_knopok[x][y]['bg'] == '#8B2323':
            if abs(x-x_last) == 1:
                check_bliz =1
            chet_do_konca -=1
            canvas_igr.itemconfigure(hodi, text=f'До конца{chet_do_konca}')
            mat_knopok[x_last_last][y_last_last]['state'] = NORMAL
            if rastanovka[x_last][y_last] == 2:
                mat_knopok[x][y]['image'] = shash_M
            else:
                mat_knopok[x][y]['image'] = shash
            mat_knopok[x][y]['bg'] = 'black'
            mat_knopok[x_last][y_last]['image']= ''
            rastanovka[x][y] = rastanovka[x_last][y_last]
            rastanovka[x_last][y_last] = 0
            pokaz_dostup_hodov(x_last, y_last, 1, 0, rastanovka[x][y])
            if rastanovka[x][y] != 2:
                pokaz_dostup_hodov(x, y, 0, 0, rastanovka[x][y])
            if suma_dal == 0 and suma_bliz == 0 or (check_hod_mat == 1 and suma_hod_mat == 1):
                x_last_last = x;y_last_last = y
                smena_hoda()
                ngo = 1
                ch = 0
                pokaz_dostup_hodov(x_last, y_last, 1, 0, rastanovka[x][y])
                check_dal = 0;check_bliz = 0
                x_last = 0;y_last = 0
                if y in [0, 1, 2, 3, 4, 5, 6, 7] and ((x == 0) or (x == 7)):
                    mat_knopok[x][y]['image'] = shash_M
                    rastanovka[x][y] = 2
                mat_knopok[x][y]['state'] = DISABLED
                if boti != 1:
                    bot()
                proverka_na_conec(score_igrok, score_bot)
            elif ((suma_dal > 0 and suma_bliz == 0) or check_hod_mat == 0) and boti == 0:
                ngo = 1
                click_check(i, x, y, 0)
            elif suma_dal > 0 and suma_bliz == 0 and boti == 1:
                ngo = 1
                click_check(i, x, y, 1)
        #-------------------------------если нажата кнопка без подсветка-------------------------------
        elif mat_knopok[x][y]['bg'] != '#8B2323':
            showerror(title="Not", message="Запрещено")
            ngo = 2
            return
        #-------------------------------проверка на конец-------------------------------

def otris(canvas_igr,igr):
    global rastanovka
    rastanovka = [[0, 1, 0, 1, 0, 1, 0, 1],
                  [1, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [-1, 0, -1, 0, -1, 0, -1, 0],
                  [0, -1, 0, -1, 0, -1, 0, -1],
                  [-1, 0, -1, 0, -1, 0, -1, 0]]
    for i in range(8):
        mat_knopok.append([0] * 8)
    global sc_1,sc_2,hodi
    #-------------------------------отрисовка фона поля и текста-------------------------------
    canvas_igr.create_rectangle(2, 200, 200, 400, fill="white", outline="black")
    sc_1 = canvas_igr.create_text(105, 230, text=f"Cчёт игрока: {score_igrok}", font=("Compact 18 bold"), fill="black")
    sc_2 = canvas_igr.create_text(110, 300, text=f"Cчёт бота: {score_bot}", font=("Compact 18 bold"), fill="black")
    hodi = canvas_igr.create_text(105, 370, text=f'До конца: {chet_do_konca}', font=("Compact 18 bold"), fill="black")
    canvas_igr.create_rectangle(340, 10, 1033, 705, fill="black", outline="black")
    canvas_igr.create_text(695, 720, text=f'a        b        c        d        e        f        g       h', font=("Compact 25 bold"), fill="black")
    canvas_igr.create_text(320, 660, text=f'1', font=("Compact 25 bold"), fill="black");canvas_igr.create_text(320, 570, text=f'2', font=("Compact 25 bold"), fill="black")
    canvas_igr.create_text(320, 480, text=f'3', font=("Compact 25 bold"), fill="black");canvas_igr.create_text(320, 400, text=f'4', font=("Compact 25 bold"), fill="black")
    canvas_igr.create_text(320, 310, text=f'5', font=("Compact 25 bold"), fill="black");canvas_igr.create_text(320, 230, text=f'6', font=("Compact 25 bold"), fill="black")
    canvas_igr.create_text(320, 150, text=f'7', font=("Compact 25 bold"), fill="black");canvas_igr.create_text(320, 65, text=f'8', font=("Compact 25 bold"), fill="black")
    n = 350;w = 20
    color = 'white'
    #-------------------------------отрисовка поля и раставление шашек-------------------------------
    for i1 in range(8):
        for j1 in range(8):
            i = i1 * 8 + j1
            if i1 % 2 != 0:
                if i % 2 != 0:
                    color = "white"
                else:
                    color = "black"
            elif i1 % 2 == 0:
                if i % 2 == 0:
                    color = "white"
                else:
                    color = "black"
            if rastanovka[i1][j1] == 1 or rastanovka[i1][j1] == -1:
                mat_knopok[i1][j1] = (Button(igr, bg=color, fg="black", activebackground="white", relief="flat", command=lambda i =i, i1=i1, j1=j1: click_check(i, i1, j1, 0)))
            else:
                mat_knopok[i1][j1] = (Button(igr, bg=color, fg="white", activebackground="white", relief="flat", command=lambda i=i, i1=i1, j1=j1: click_check(i, i1, j1, 0)))
            if mat_knopok[i1][j1]['bg'] == 'white':
                mat_knopok[i1][j1]['state'] = DISABLED
            canvas_igr.create_window(n, w, anchor=NW, window=mat_knopok[i1][j1], width=80, height=80)
            if i in [1,3,5,7,8,10,12,14,17,19,21,23,40,42,44,46,49,51,53,55,56,58,58, 65,60,62,62, 69]:
                mat_knopok[i1][j1].config(image=shash)
            n += 85
        n = 350;w += 85
def igra(glavmenu):
    #-------------------------------создание окна игры-------------------------------
    global color,igr
    glavmenu.withdraw()
    igr = Tk()
    igr.title("Шашки Артамонова")
    igr.geometry(f"1384x753+{wh}+{hh}")
    igr.resizable(False, False)
    global canvas_igr
    canvas_igr = Canvas(igr, bg='white', width=1384, height=753)
    canvas_igr.place(x=0, y=0)
    img_igr = PhotoImage(master=canvas_igr, file='background.png')
    global shash,shash_M
    shash = PhotoImage(master=canvas_igr, file='shashka.png')
    shash = shash.subsample(2, 2)
    shash_M = PhotoImage(master=canvas_igr, file='shashka_damka.png')
    shash_M = shash_M.subsample(2, 2)
    canvas_igr.create_image(0, 0, anchor='nw', image=img_igr)
    otris(canvas_igr,igr)
    igr.mainloop()
def rezul(canvas_glav,igr):
    #-------------------------------окно результатов-------------------------------
    canvas_glav.create_rectangle(920, 210, 1320, 250, fill="white", outline="black",tags='nastr')
    canvas_glav.create_text(1120, 230, text="Результаты", font=("Compact 18 bold"), fill="black",tags='nastr')
    canvas_glav.create_rectangle(920, 250, 1320, 580, fill="#525252", outline="black",tags='nastr')
    canvas_glav.create_rectangle(1030, 330, 1230, 430, fill="white", outline="black", tags='nastr')
    canvas_glav.create_text(1130, 350, text=f"Выйграно {win_igr}", font=("Compact 18 bold"), fill="black", tags='nastr')
    canvas_glav.create_text(1130, 380, text=f"Проиграно {win_bot}", font=("Compact 18 bold"), fill="black", tags='nastr')
    canvas_glav.create_text(1130, 410, text=f"Ничья {nich}", font=("Compact 18 bold"), fill="black", tags='nastr')
    but_zak = Button(igr,text="Закрыть", bg="white", fg="black", activebackground="white",
                      font=("Compact 15 bold"), relief='flat', cursor="hand2",command= lambda: canvas_glav.delete('nastr'))
    canvas_glav.create_window(1030, 500, anchor=NW, window=but_zak, width=200, height=35,tags='nastr')
def vih():
    exit()
def glav_menu():
    #-------------------------------создание окна-------------------------------
    global glavmenu
    glavmenu = Tk()
    glavmenu.title("Главное меню")
    glavmenu.geometry(f"1384x753+{wh}+{hh}")
    glavmenu.resizable(False, False)
    canvas_glav_menu = Canvas(glavmenu, bg='white', width=1384, height=753)
    canvas_glav_menu.place(x=0, y=0)
    # -------------------------------фон-------------------------------
    img_menu = PhotoImage(master = canvas_glav_menu,file='background.png')
    canvas_glav_menu.create_image(0, 0, anchor='nw', image=img_menu)
    # -------------------------------размещение блоков-------------------------------
    canvas_glav_menu.create_rectangle(500, 210, 900, 250, fill="white", outline="black")
    canvas_glav_menu.create_text(700, 230, text="Главное меню", font=("Compact 18 bold"), fill="black")
    canvas_glav_menu.create_rectangle(500, 250, 900, 580, fill="#525252", outline="black")
    # -------------------------------размещение кнопок-------------------------------
    but_nach = Button(glavmenu, text="Начать игру", bg="white", fg="black", activebackground="white",
                      font=("Compact 15 bold"), relief='flat', cursor="hand2", command= lambda:igra(glavmenu)) # начло игры
    canvas_glav_menu.create_window(550, 300, anchor=NW, window=but_nach, width=300, height=50)
    but_nastr = Button(glavmenu, text="Результаты", bg="white", fg="black", activebackground="white",
                       font=("Compact 15 bold"), relief='flat', cursor="hand2", command= lambda: rezul(canvas_glav_menu, glavmenu)) # настройки
    canvas_glav_menu.create_window(550, 370, anchor=NW, window=but_nastr, width=300, height=50)
    but_vih = Button(glavmenu, text="Выход", bg="white", fg="black", activebackground="white",
                     font=("Compact 15 bold"), relief='flat', cursor="hand2", command=vih) # выход
    canvas_glav_menu.create_window(550, 440, anchor=NW, window=but_vih, width=300, height=50)
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
reg(login,passw)
root.mainloop()
