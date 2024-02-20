import gettext
import os
import platform
import sys


LOCALE_DIR = 'src/coolcalc/locales'
""" Директория расположения файлов перевода"""

if sys.stdin and sys.stdin.isatty():  # Если запуск с консоли
    LOCALE_DIR = 'src/coolcalc/locales'
else:
    LOCALE_DIR = 'locales'

WIDTH = 400
HEIGHT = 550

theme = 'dark'
""" Текущая тема приложения """

_ = gettext.gettext


def translate(new_lang: str):
    """
    Устанавливает язык для текста в настройках
    :param new_lang: новый язык для приложения.
    :return: None
    """

    global _, about_info, help_info, error_text
    lang = gettext.translation(domain='settings', localedir=LOCALE_DIR, languages=[new_lang])
    _ = lang.gettext
    about_info = get_about_info()
    help_info = get_help_info()
    error_text = get_error_text()


def get_about_info() -> dict:
    """
    Обрабатывает текстовую информацию окна "О программе"
    :return: Словарь с информацией об окне "О программе"
    """

    return {
        "title": _('About'),
        "body": _(
            'The calculator has two modes: simple and advanced.\n'
            'In simple mode, the calculator can perform operations such as: arithmetic operations, sign change, '
            'percentages, squaring, square root.\n'
            'In advanced mode, the calculator can perform such operations as: functions of a simple calculator, '
            'trigonometric functions, exponentiation, ogarithms (natural and decimal), modulus of a number, '
            'factorial of a number, translation into number systems (2, 3, 4, 5, 6, 7, 8)\n'
            'The calculator has several themes for design, among which there is a kids. \n'
            'You can also change the interface language to Russian.\n'
            'The program was created and has an MIT license.\n'
            'Creators:'
            'Glushenkov Dmitrii Alekseevich'
        ),
        "version": _('Operating system: ') + platform.platform(),
        "user": _('Username: ') + os.getlogin(),
        "cnl": _('Quit'),
    }


def get_help_info() -> dict:
    """
    Обрабатывает текстовую информацию окна "Справка"
    :return: Словарь с информацией об окне "Справка"
    """

    return {
        "title": _('Help'),
        "body": _(
            'This window is designed to answer some questions about the application. \n\n'
            'СALCULATOR\n\n'
            'In this tab, you can copy or paste the values. To copy the item you need, select it with the left '
            'mouse button, go to the "Calculator" tab and click "Copy". To insert the element you need, select it with '
            'the left mouse button, go to the Calculator tab and click "Paste".\n\n'
            'VIEW\n\n'
            'To switch the calculator view, go to the "View" tab and select the mode you need. '
            'If you want to find out how the modes differ from each other, go to the "About" tab and select "About". '
            'To change the theme of the calculator, go to the "View" tab, then hover over the "View" tab and select '
            'the topic you are interested in. You can also change the language to English in this tab. Go to the '
            '"View" tab, then hover over the "Language" tab and select the language you are interested in.\n\n'
            'ABOUT\n\n'
            'In this tab, you can read this manual in the Help tab. If you want to learn more about the program, '
            'open the About tab.\n\n'
            'Some functions:\n'
            'ln(x) — natural logarithm\n'
            'log(x) - logarithm\n'
            'abs(x) — module\n'
            'sqrt(x) — root\n'
            'x^y — x power y \n'
            'of x! — factorial(x)\n'
        ),
    }


def get_error_text() -> dict:
    """
    Обрабатывает текст ошибок
    :return: Словарь с текстом ошибок
    """

    return {
            "syntax": _('Wrong input'),
            "overflow": _('Too big answer'),
            "zero_division": _('Zero division'),
            "value": _('Too much nesting'),
           }


about_info = get_about_info()
""" Словарь с информацией о странице "О приложении" """

help_info = get_help_info()
""" Словарь с информацией о странице "Справка" """

error_text = get_error_text()
""" Словарь с текстом ошибок """

# Задание разных тем для приложения
THEMES = {
    # светлая
    'light': {
        'root': {
            'bg': "#D0DABE",
            'fg': "black",
        },
        'menu': {
            'bg': "#B3E0C4",  # фон
            'fg': "black",  # текст
            'abg': '#68D490',  # фон при наведении
            'afg': 'black',  # текст при наведении

        },
        'calc': {
            'actions': {
                'bg': '#78DBE2',
                'fg': '#000',
            },
            'numbers': {
                'bg': "#9FE2BF",
                'fg': '#000',
            },
            'num_sys': {
                'bg': "#AFDAFC",
                'fg': '#000',
            },
            'ex_actions': {
                'bg': '#AFDAFC',
                'fg': '#000',
            },
            'font': ('Times New Roman', 17),
            'custom': {
                '=': {
                    'bg': "#9FE2BF",
                    'fg': '#000',
                },

            },
            'labels': {
                'font': ('Times New Roman', 30),
            },

        },
        'settings': {
            'bg': '#D0DABE',
            'fg': 'black',
            'btn': {
                'bg': 'white',
                'fg': 'black'
            }
        }
    },
    # темная
    'dark': {  # ТЁМНАЯ
        'root': {
            'bg': "#303030",
            'fg': "#fff",
        },
        'menu': {
            'bg': "#303030",  # фон
            'fg': "white",  # текст
            'abg': '#1F1F1F',  # фон при наведении
            'afg': 'white',  # текст при наведении

        },
        'calc': {
            'actions': {
                'bg': '#7D7D7D',
                'fg': '#000',
            },
            'numbers': {
                'bg': "#fff",
                'fg': '#000',
            },
            'num_sys': {
                'bg': "#07c",
                'fg': '#000',
            },
            'ex_actions': {
                'bg': '#07c',
                'fg': '#000',
            },
            'font': ('Times New Roman', 17),
            'custom': {
                '=': {
                    'bg': "#fff",
                    'fg': '#000',
                },

            },
            'labels': {
                'font': ('Times New Roman', 30),
            },

        },
        'settings': {
            'bg': '#303030',
            'fg': '#fff',
            'btn': {
                'bg': 'white',
                'fg': 'black'
            }
        }
    },
    # детская
    'kids': {  # Детская
        'root': {
            'bg': "#AFDAFC",
            'fg': "#2939FF",
        },
        'menu': {
            'bg': "#AFDAFC",  # фон
            'fg': "#000000",  # текст
            'abg': '#29A7FF',  # фон при наведении
            'afg': 'black',  # текст при наведении

        },
        'calc': {
            'actions': {
                'bg': '#ccc',
                'fg': '#000',
            },
            'numbers': {
                'bg': "#fff",
                'fg': '#000',
            },
            'num_sys': {
                'bg': "#07c",
                'fg': '#000',
            },
            'ex_actions': {
                'bg': '#aaa',
                'fg': '#000',
            },
            'font': ('Arial', 25),
            'custom': {
                ')': {
                    'bg': "#FFA152",
                    'fg': '#000',
                },
                '(': {
                    'bg': "#FF5F52",
                    'fg': '#000',
                },
                'C': {
                    'bg': "#FFEC52",
                    'fg': '#000',
                },
                'Del': {
                    'bg': "#5EFF52",
                    'fg': '#000',
                },
                'log': {
                    'bg': "#42AAFF",
                    'fg': '#000',
                },
                'ln': {
                    'bg': "#525FFF",
                    'fg': '#000',
                },
                '%': {
                    'bg': "#8C52FF",
                    'fg': '#000',
                },
                '^': {
                    'bg': "#525FFF",
                    'fg': '#000',
                },
                u"\u221a": {
                    'bg': "#42AAFF",
                    'fg': '#000',
                },
                '/': {
                    'bg': "#FFA152",
                    'fg': '#000',
                },
                '!': {
                    'bg': "#FFEC52",
                    'fg': '#000',
                },
                'abs': {
                    'bg': "#FFA152",
                    'fg': '#000',
                },
                '7': {
                    'bg': "#42AAFF",
                    'fg': '#000',
                },
                '8': {
                    'bg': "#FF5F52",
                    'fg': '#000',
                },
                '9': {
                    'bg': "#FFEC52",
                    'fg': '#000',
                },
                '*': {
                    'bg': "#8C52FF",
                    'fg': '#000',
                },
                'dec': {
                    'bg': "#525FFF",
                    'fg': '#000',
                },
                'bin': {
                    'bg': "#5EFF52",
                    'fg': '#000',
                },
                '4': {
                    'bg': "#5EFF52",
                    'fg': '#000',
                },
                '5': {
                    'bg': "#525FFF",
                    'fg': '#000',
                },
                '6': {
                    'bg': "#FFA152",
                    'fg': '#000',
                },
                '-': {
                    'bg': "#42AAFF",
                    'fg': '#000',
                },
                'oct': {
                    'bg': "#FFEC52",
                    'fg': '#000',
                },
                'ter': {
                    'bg': "#8C52FF",
                    'fg': '#000',
                },
                '1': {
                    'bg': "#FFEC52",
                    'fg': '#000',
                },
                '2': {
                    'bg': "#8C52FF",
                    'fg': '#000',
                },
                '3': {
                    'bg': "#5EFF52",
                    'fg': '#000',
                },
                '+': {
                    'bg': "#525FFF",
                    'fg': '#000',
                },
                'qua': {
                    'bg': "#FFA152",
                    'fg': '#000',
                },
                'fiv': {
                    'bg': "#FF5F52",
                    'fg': '#000',
                },
                '+-': {
                    'bg': "#525FFF",
                    'fg': '#000',
                },
                '0': {
                    'bg': "#FFA152",
                    'fg': '#000',
                },
                '.': {
                    'bg': "#42AAFF",
                    'fg': '#000',
                },
                '=': {
                    'bg': "#FF5F52",
                    'fg': '#000',
                },
                'six': {
                    'bg': "#5EFF52",
                    'fg': '#000',
                },
                'sep': {
                    'bg': "#42AAFF",
                    'fg': '#000',
                },

            },
            'labels': {
                'font': ('Times New Roman', 35),
            },

        },
        'settings': {
            'bg': "#AFDAFC",
            'fg': "#2939FF",
            'btn': {
                'bg': 'blue',
                'fg': 'black'
            }
        }
    },
}
""" Задаёт темы для приложения """
