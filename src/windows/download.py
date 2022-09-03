import tkinter
import threading
import os

from time import sleep
from tkinter.constants import *
from math import log
from PIL import Image, ImageTk
from utils.file_manager import FileManager
from utils.logger import Logger
from windows.eula import EULAWindow
from utils.translations import TranslationsManager

class DownloadWindow():

    def __init__(self, window:tkinter.Tk, logger:Logger):
        self.logger = logger
        self.translations = TranslationsManager(self.logger)
        self.logger.log("DOWNLOAD", "Creating Window")
        self.widget_list = []
        self.window = window
        self.window.title(self.translations.get_trans("all.name"))
        self.window.geometry("640x480")
        self.window.minsize(640, 480)
        self.window.maxsize(1440, 1080)
        #self.window.iconbitmap("../assets/server.ico")
        self.bg = Image.open("../assets/background.png").resize((640, 480))
        self.bg_copy= self.bg.copy()
        self.bg_image = ImageTk.PhotoImage(self.bg)
        self.bg_label = tkinter.Label(self.window, image = self.bg_image)
        self.bg_label.place(x=0, y=0)
        self.window.bind("<Configure>", self.resize_bg)

        self.minecraft_versions = [
            "1.19",
            "1.18.2",
            "1.18.1",
            "1.18",
            "1.17.1",
            "1.17",
            "1.16.5",
            "1.16.4",
            "1.16.3",
            "1.16.2",
            "1.16.1",
            "1.16",
            "1.15.2",
            "1.15.1",
            "1.15",
            "1.14.4",
            "1.14.3",
            "1.14.2",
            "1.14.1",
            "1.14",
            "1.13.2",
            "1.13.1",
            "1.13",
            "1.12.2",
            "1.12.1",
            "1.12",
            "1.11.2",
            "1.11.1",
            "1.11",
            "1.10.2",
            "1.10.1",
            "1.10",
            "1.9.4",
            "1.9.3",
            "1.9.2",
            "1.9.1",
            "1.9",
            "1.8.9",
            "1.8.8",
            "1.8.7",
            "1.8.6",
            "1.8.5",
            "1.8.4",
            "1.8.3",
            "1.8.2",
            "1.8.1",
            "1.8",
        ]

        self.server_versions = [
            "Vanilla",
            #"Bukkit",
            #"Spigot",
            #"Forge",
            #"Fabric",
            #"Modpack CurseForge"
        ]

        self.current_version = "0"
        self.current_version_server = "0"

        self.load()
        self.create_next_button()

    def load(self):
        self.logger.log("DOWNLOAD", "Creating DOWNLOAD window widgets")

        # TITLE
        self.title = tkinter.Label(text=self.translations.get_trans("all.title"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.title)

        # FLAG
        self.flag_image = Image.open("../assets/flags/" + self.translations.lang + ".png").resize((100,75))
        self.flag_image = ImageTk.PhotoImage(self.flag_image)
        self.flag = tkinter.Button(self.window, image=self.flag_image, command=self.change_lang, background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.flag['image'] = self.flag_image
        self.flag.place(relx=0.1, rely=0.1, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.flag)
        
        # SERVER TYPE
        self.variable_server = tkinter.StringVar(self.window)
        self.variable_server.set(self.translations.get_trans("main.choose_type"))
        self.server_version_button = tkinter.OptionMenu(
            self.window,
            self.variable_server,
            *self.server_versions
        )
        self.server_version_button.config(background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14), cursor="hand2")
        self.server_version_button['menu'].config(background='#2E2E2E', relief=SOLID, fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10), cursor="hand2")
        self.server_version_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.server_version_button)

        self.variable_server.trace("w", self.choise_version_server)

        # MINECRAFT VERSION
        self.variable_mc = tkinter.StringVar(self.window)
        self.variable_mc.set(self.translations.get_trans("main.choose_mc"))
        self.minecraft_version_button = tkinter.OptionMenu(
            self.window,
            self.variable_mc,
            *self.minecraft_versions
        )
        self.minecraft_version_button.config(background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14), cursor="hand2")
        self.minecraft_version_button['menu'].config(background='#2E2E2E', relief=SOLID, fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10), cursor="hand2")
        self.minecraft_version_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.minecraft_version_button)

        self.variable_mc.trace("w", self.choise_version_mc)
        
        # PATH FIELD
        self.path_name = tkinter.Label(text=self.translations.get_trans("main.path_text"), background='#2E2E2E', fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 14))
        self.path_name.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.path_name)

        self.path_field = tkinter.Entry(background='#2E2E2E', borderwidth=1, relief=SOLID, width=60, fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 12))
        self.path_field.insert(1, os.getcwd()[:-3] + "run")
        self.path_field.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.path_field)

        # LAUNCH DOWNLOAD BUTTON
        self.start_button = tkinter.Button(background='#2E2E2E', text=self.translations.get_trans("main.download"), relief=SOLID, fg="#DADADA", command=self.init_download, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14), cursor="hand2")
        self.start_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.start_button)
        self.logger.log("DOWNLOAD", "Created widgets of DOWNLOAD window")

    def choise_version_server(self, *args):
        self.current_version_server = self.variable_server.get()
        self.logger.log("DOWNLOAD", "Selected type : " + self.current_version_server)


    def choise_version_mc(self, *args):
        self.current_version = self.variable_mc.get()
        self.logger.log("DOWNLOAD", "Selected version : " + self.current_version)

    def init_download(self):
        if self.current_version_server == "0":
            self.error = tkinter.Label(text=self.translations.get_trans("main.error_type"), background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.error)

        elif self.current_version == "0":
            self.error = tkinter.Label(text=self.translations.get_trans("main.error_mc"), background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.error)

        elif self.path_field.get() == "":
            self.error = tkinter.Label(text=self.translations.get_trans("main.error_path"), background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.error)

        else:
            self.file_manager = FileManager(self)
            self.track_thread = threading.Thread(target=self.track_download, args=())
            self.track_thread.start()
            self.create_next_button()

    def create_next_button(self):
        # NEXT BUTTON
        self.next_button = tkinter.Button(background='#2E2E2E', text=self.translations.get_trans("all.next"), relief=SOLID, fg="#DADADA", command=self.change_eula_window, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14), cursor="hand2")
        self.next_button.place(relx=0.9, rely=0.93, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.next_button)

    def change_eula_window(self):
        EULAWindow(self.window, self)
        self.unload_window()
        self.logger.log("EULA", "Changed window to EULA")

    def unload_window(self):
        i=0
        for widget in self.widget_list:
            self.logger.log("DOWNLOAD", "Removed one widget from the screen (" + str(i + 1) + "/" + str(len(self.widget_list)) + ")")
            widget.destroy()
            i += 1
        self.widget_list = []

    def change_lang(self):
        self.translations.change_lang()
        self.unload_window()
        self.load()

    def show_dir_error(self):
        self.error = tkinter.Label(text=self.translations.get_trans("main.error_dir"), background="#FF8C00", relief=SOLID, font=('Roboto', 14))
        self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.error)

    def track_download(self):
        self.error = tkinter.Label(text="Starting download", background="#FF8C00", relief=SOLID, font=('Roboto', 14))
        self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.error)
        sleep(0.3)
        while self.file_manager.file.get_status() == "downloading":
            file = self.file_manager.file
            self.error.configure(text=str(self.sizeof_human(file.get_dl_size())) + "/" + str(self.sizeof_human(file.get_final_filesize())) + " (" + str(file.get_progress() * 100)[:5] + "%) @ " + str(self.sizeof_human(round(file.get_speed(), 2))) + "/s, " + str(self.time_human(file.get_dl_time())))
            sleep(0.5)
        self.error.configure(text="Download Finished")

    def resize_bg(self, e):
        if e.widget == self.window:
            self.bg = self.bg_copy.resize((e.width, e.height))
            self.bg_image = ImageTk.PhotoImage(self.bg)
            self.bg_label.configure(image = self.bg_image)


    # Code from https://github.com/iTaybb/pySmartDL/blob/master/pySmartDL/utils.py

    def sizeof_human(self, num):
        '''
        Human-readable formatting for filesizes. Taken from `here <http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size>`_.

        >>> sizeof_human(175799789)
        '167.7 MB'

        :param num: Size in bytes.
        :type num: int

        :rtype: string
        '''
        unit_list = list(zip(['B', 'kB', 'MB', 'GB', 'TB', 'PB'], [0, 0, 1, 2, 2, 2]))

        if num > 1:
            exponent = min(int(log(num, 1024)), len(unit_list) - 1)
            quotient = float(num) / 1024**exponent
            unit, num_decimals = unit_list[exponent]

            format_string = '{:,.%sf} {}' % (num_decimals)
            return format_string.format(quotient, unit)

        if num == 0:
            return '0 bytes'
        if num == 1:
            return '1 byte'

    def time_human(self, duration, fmt_short=False, show_ms=False):
        '''
        Human-readable formatting for timing. Based on code from `here <http://stackoverflow.com/questions/6574329/how-can-i-produce-a-human-readable-difference-when-subtracting-two-unix-timestam>`_.

        >>> time_human(175799789)
        '6 years, 2 weeks, 4 days, 17 hours, 16 minutes, 29 seconds'
        >>> time_human(589, fmt_short=True)
        '9m49s'

        :param duration: Duration in seconds.
        :type duration: int/float
        :param fmt_short: Format as a short string (`47s` instead of `47 seconds`)
        :type fmt_short: bool
        :param show_ms: Specify milliseconds in the string.
        :type show_ms: bool
        :rtype: string
        '''
        ms = int(duration % 1 * 1000)
        duration = int(duration)
        if duration == 0 and (not show_ms or ms == 0):
            return "0s" if fmt_short else "0 seconds"

        INTERVALS = [1, 60, 3600, 86400, 604800, 2419200, 29030400]
        if fmt_short:
            NAMES = ['s'*2, 'm'*2, 'h'*2, 'd'*2, 'w'*2, 'y'*2]
        else:
            NAMES = [
                ('second', 'seconds'),
                ('minute', 'minutes'),
                ('hour', 'hours'),
                ('day', 'days'),
                ('week', 'weeks'),
                ('month', 'months'),
                ('year', 'years')
            ]

        result = []

        for i in range(len(NAMES)-1, -1, -1):
            a = duration // INTERVALS[i]
            if a > 0:
                result.append( (a, NAMES[i][1 % a]) )
                duration -= a * INTERVALS[i]

        if show_ms and ms > 0:
            result.append((ms, "ms" if fmt_short else "milliseconds"))

        if fmt_short:
            return "".join(["%s%s" % x for x in result])
        return ", ".join(["%s %s" % x for x in result])
