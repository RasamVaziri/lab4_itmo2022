import tkinter as tk
import random
import pygame
window = tk.Tk()
window.title('Ps5+ key ')
window.geometry('600x400')
window.resizable(width='False', height='False')


Picture = tk.PhotoImage(file='Call of Duty.png')
Wallpaper = tk.Label(window, image=Picture, bg='#000000')
Wallpaper.place(x=0, y=0, width=600, height=400)

Collection = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def close():
    window.destroy()


def GenerateKey():
    a = FirstPart.get()
    first_part = ''
    second_part = ''
    third_part = ''

    if len(a) == 6:
        a = str.upper(a)

        for i in range(0, 3):
            first_part += a[i]
            second_part += a[i + 3]

        for i in range(0, 2):
            index = random.randint(0, 35)
            first_part += Collection[index]
            index2 = random.randint(0, 35)
            second_part += Collection[index2]

        for i in range(0, 4):
            index3 = random.randint(0, 35)
            third_part += Collection[index3]

        lbl_roots.configure(text=first_part + '---' + second_part + '---' + third_part)

    else:
        lbl_roots.configure(text='The inpute must be 6 icon')

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Glimmer Of - Mahdyar.mp3")
lblFirstPart = tk.Label(window, text='First part of key', font=('Arial',40), bg='#FFFF45')
lblFirstPart.place(relx=0.5, rely=0.8, anchor='center')
FirstPart = tk.Entry(window, width=10)
FirstPart.place(relx=0.5, rely=0.4, anchor='center')

lbl_roots = tk.Label(window, text='', font=('Arial', 15))
lbl_roots.place(relx=0.5, rely=0.5, anchor='center')

btn_calc = tk.Button(window, text='Gain', font=('Arial', 17), command=GenerateKey, bg='#952233')
btn_calc.place(relx=0.2, rely=0.6, anchor='center')
btn_exit = tk.Button(window, text=' Cancel  ', font=('Arial', 15), command=close,bg='#0000FF')
btn_exit.place(relx=0.8, rely=0.6, anchor='center')
pygame.mixer.music.play(-1)
window.mainloop()
