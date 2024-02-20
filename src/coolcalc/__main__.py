import gettext
from tkinter import *


from coolcalc import calculate
from coolcalc.graph_calc import Calculator
import coolcalc.settings as glob
import sys


def translate(new_lang: str) -> None:
    """
    Меняет язык на new_lang
    :param new_lang: новый язык.
    :return: None
    """

    global _
    lang = gettext.translation(domain='app', localedir=glob.LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext


def set_new_lang(lang: str):
    """
    Переводит приложение на new_lang
    :param lang: новый язык.
    :return: None
    """

    translate(lang)
    menu.translate(lang)
    glob.translate(lang)
    root.title(_('Calculator'))


def set_theme(theme):
    """
    Меняет тему приложения на theme
    :param theme: название темы приложения.
    :return: None
    """

    glob.theme = theme
    app.set_theme(theme)
    root["bg"] = glob.THEMES[theme]['root']['bg']
    menu.set_menu_theme(theme)


def expand(mode):
    """
    Меняет размер окна
    :param mode: размер окна.
    :return: None
    """

    if mode == 'basic':
        app.basic()
        root.geometry("%dx%d" % (glob.WIDTH, glob.HEIGHT))
    elif mode == 'expand':
        app.expend()
        root.geometry("%dx%d" % (glob.WIDTH + glob.WIDTH / 2 + 10, glob.HEIGHT))


if __name__ == '__main__':

    # Подключаем перевод
    _ = gettext.gettext
    translate("ru")
    glob.translate('ru')

    # Если в командной строке есть аргументы, выдаём ответ в командную строку, иначе запускаем графическую оболочку
    if len(sys.argv) > 1:
        expr = ''
        for arg in sys.argv[1:]:
            expr += str(arg)
        print(calculate(expr))
    else:
        root = Tk()
        app = Calculator(root)
        import coolcalc.menu as menu

        menu.create_menu()
        set_theme('dark')
        set_new_lang('ru')

        root.geometry("%dx%d+700+200" % (glob.WIDTH, glob.HEIGHT))
        root.resizable(False, False)

        app.pack(pady=10, padx=10, fill=BOTH, expand=True)
        root.mainloop()
