from tkinter import *

from __main__ import root
from typing import Tuple

import coolcalc.settings as glob


def create_win(info: str) -> Tuple[Toplevel, dict]:
    """
    Функция создаёт окно с заголовком info
    :param info: заголовок окна.
    :returns: Возвращает виджет-окно для размещения информации и тему
    """

    theme = glob.THEMES[glob.theme]['settings']
    # Создание дочернего окна
    win = Toplevel(root)
    win.title(info)

    x = root.winfo_rootx()
    y = root.winfo_rooty()
    root_height = root.winfo_height()
    root_width = root.winfo_width()

    height = 650
    width = 520

    x = x + root_width / 2 - width / 2
    y = y + root_height / 2 - height / 2

    win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    win.resizable(width=False, height=False)
    win.grab_set()

    win['bg'] = theme['bg']

    return win, theme


def menu_help() -> None:
    """
    Создаёт окно "Помощь"
    :return: None
    """

    info = glob.help_info
    win_help, theme = create_win(info['title'])

    lbs = Frame(win_help)
    lbs.pack(side=TOP)

    body = Label(lbs,
                 text=info['body'],
                 font='Times 12',
                 anchor='w',
                 justify=LEFT,
                 wraplength=500,
                 bg=theme['bg'],
                 fg=theme['fg'])

    body.pack(fill=BOTH)

    win_help.mainloop()


def about() -> None:
    """
    Создаёт окно раздела "О программе"
    :return: None
    """

    info = glob.about_info
    win_about, theme = create_win(info)
    lbs = Frame(win_about, bg=theme['bg'])
    btn = Frame(win_about, bg=theme['bg'])
    lbs.pack(side=TOP)
    btn.pack(side=BOTTOM)

    def cancel():
        win_about.destroy()

    bg = theme['bg']
    fg = theme['fg']
    top = Label(lbs,
                text=root.title(),
                font='Times 14',
                bg=bg, fg=fg)
    body = Label(lbs,
                 text=info['body'],
                 font='Times 12',
                 anchor='w',
                 justify=LEFT,
                 wraplength=500,
                 bg=bg, fg=fg)
    user = Label(lbs,
                 text=info['user'] + '\n' + info['version'],
                 font='Times 12',
                 anchor='w',
                 justify=LEFT,
                 bg=bg, fg=fg)
    quite_btn = Button(btn,
                       text=info['cnl'],
                       command=cancel,
                       bg=theme['btn']['bg'],
                       fg=theme['btn']['fg'],
                       )
    top.pack(fill=BOTH)
    body.pack(fill=BOTH)
    user.pack(fill=BOTH)
    quite_btn.pack(side=BOTTOM, pady=(0, 5))

    win_about.mainloop()
