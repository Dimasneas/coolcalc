import gettext
from __main__ import root, app, expand, set_theme, set_new_lang
from tkinter import Menu

from coolcalc.menu_command import *

import coolcalc.settings as glob

menus = []
""" Список меню """

main_menu = Menu(root)
""" Главное меню """
menus.append(main_menu)
file_menu = Menu(main_menu, tearoff=0)
""" Меню "Файл" """
menus.append(file_menu)
theme_menu = Menu(main_menu, tearoff=0)
""" Подменю темы """
menus.append(theme_menu)
lang_menu = Menu(main_menu, tearoff=0)
""" подменю языков """
menus.append(lang_menu)
view_menu = Menu(main_menu, tearoff=0)
""" Меню "Вид" """
menus.append(view_menu)
about_menu = Menu(main_menu, tearoff=0)
""" Меню "О программе" """
menus.append(about_menu)

_ = gettext.gettext


def translate(new_lang: str) -> None:
    """
    Устанавливает язык lang в меню приложения
    :param new_lang: язык для установки('ru', 'en').
    :return: None
    """
    global _
    lang = gettext.translation(domain='menu', localedir=glob.LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext
    rename_menu()


def set_menu_theme(theme: str):
    """
    Устанавливает тему theme в меню приложения
    :param theme: тема для установки('dark', 'light', 'kids').
    :return: None
    """
    th = glob.THEMES[theme]['menu']
    for menu in menus:
        menu.config(background=th['bg'],
                    foreground=th['fg'],
                    activebackground=th['abg'],
                    activeforeground=th['afg']
                    )


def create_menu():
    """
    Создаёт меню приложения
    :return: None
    """

    # Файл
    file_menu.add_command(command=lambda: app.entry.event_generate("<<Copy>>"), accelerator='Ctrl+C')
    file_menu.add_command(command=lambda: app.entry.event_generate("<<Paste>>"), accelerator='Ctrl+V')
    root.config(menu=file_menu)

    # Вид
    view_menu.add_command(command=lambda: expand('expand'),
                          # accelerator='Ctrl+X'
                          )
    view_menu.add_command(command=lambda: expand('basic'),
                          # accelerator='Ctrl+C'
                          )

    view_menu.add_separator()
    # Темы
    theme_menu.add_command(command=lambda: set_theme('dark'))
    theme_menu.add_command(command=lambda: set_theme('light'))
    theme_menu.add_command(command=lambda: set_theme('kids'))

    view_menu.add_cascade(menu=theme_menu)
    view_menu.add_separator()
    # Языки
    lang_menu.add_command(command=lambda: set_new_lang('ru'))
    lang_menu.add_command(command=lambda: set_new_lang('en'))

    view_menu.add_cascade(menu=lang_menu)

    # О программе
    about_menu.add_command(command=menu_help, accelerator='Ctrl+I')
    about_menu.add_command(command=about, accelerator='Ctrl+P')

    # Добавление списков меню
    main_menu.add_cascade(menu=file_menu)
    main_menu.add_cascade(menu=view_menu)
    main_menu.add_cascade(menu=about_menu)
    root.config(menu=main_menu)


def rename_menu():
    """
    Переименовывает объекты меню
    :return: None
    """
    # Файл
    file_menu.entryconfig(0, label=_('Copy'))
    file_menu.entryconfig(1, label=_('Paste'))

    # Правка
    view_menu.entryconfig(0, label=_('Expend'))
    view_menu.entryconfig(1, label=_('Basic'))
    view_menu.entryconfig(3, label=_('Theme'))
    view_menu.entryconfig(5, label=_('Language'))

    theme_menu.entryconfig(0, label=_('Dark'))
    theme_menu.entryconfig(1, label=_('Light'))
    theme_menu.entryconfig(2, label=_('Kids'))

    lang_menu.entryconfig(0, label='Русский')
    lang_menu.entryconfig(1, label='Английский')

    # Поиск
    about_menu.entryconfig(0, label=_('Help'))
    about_menu.entryconfig(1, label=_('About'))

    # Основное меню
    main_menu.entryconfig(1, label=_('Calculator'))
    main_menu.entryconfig(2, label=_('View'))
    main_menu.entryconfig(3, label=_('About'))
