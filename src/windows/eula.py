import tkinter 
import webbrowser
import datetime

from tkinter.constants import *
from windows.configuration import ConfigurationWindow

class EULAWindow:

    def __init__(self, window:tkinter.Tk, download_window):
        self.download_window = download_window
        self.logger = self.download_window.logger
        self.window = window
        self.translations = self.download_window.translations
        self.widget_list = []
        self.load()
        self.create_next_button()
        self.path = self.download_window.path_field.get()
        if not self.path.endswith("/"):
            self.path += "/"

    def load(self):
        # TITLE
        self.title = tkinter.Label(text=self.translations.get_trans("all.title"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.title)

        # EULA LINK
        self.link = tkinter.Label(text=self.translations.get_trans("eula.link"), background="#2E2E2E", fg="#0288d1", font=('Roboto', 14, 'underline'))
        self.link.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.link)
        self.link.bind("<Button-1>", self.callback)

        # AGREE CHECKBOX
        self.agree = tkinter.Checkbutton(self.window)
        self.agree.configure(text=self.translations.get_trans("eula.agree"), command=self.create_eula_file, background="#2E2E2E", fg="#DADADA", font=('Roboto', 12, 'underline'), activebackground="#252525", activeforeground="#DADADA")
        self.agree.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.agree)

        self.logger.log("EULA", "Created EULA's widgets")

    def callback(self, *args):
        webbrowser.open_new_tab("https://account.mojang.com/documents/minecraft_eula")
        self.logger.log("EULA", "Open EULA link")

    def create_eula_file(self):
        # Creating Label for waiting
        self.creating_eula = tkinter.Label(text=self.translations.get_trans("eula.creating"), background="#2E2E2E", fg="#FF8C00", font=('Roboto', 14))
        self.creating_eula.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.creating_eula)

        # Creating eula.txt file
        with open(self.path + "eula.txt", "w") as eula_file:
            current = datetime.datetime.now()
            days = ["Mon", "Tue", "Wen", "thu", "Fri", "Sat", "Sun"]
            weekday = days[current.weekday()]

            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month = months[current.month]

            eula_file.write(
                "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n" +
                f"#{weekday} {month} {self.my_format(current.day)} {self.my_format(current.hour)}:{self.my_format(current.minute)}:{self.my_format(current.second)} CEST {current.year}\neula=true")
            eula_file.close()
        
        self.logger.log("EULA", 'eula.txt created')
        self.creating_eula.configure(text=self.translations.get_trans("eula.created"))
        self.create_next_button()

    def unload_window(self):
        i=0
        for widget in self.widget_list:
            self.logger.log("EULA", "Removed one widget from the screen (" + str(i + 1) + "/" + str(len(self.widget_list)) + ")")
            widget.destroy()
            i += 1

    def create_next_button(self):
        # NEXT BUTTON
        self.next_button = tkinter.Button(background='#2E2E2E', text=self.translations.get_trans("all.next"), relief=SOLID, fg="#DADADA", command=self.change_conf_window, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.next_button.place(relx=0.9, rely=0.93, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.next_button)

    def change_conf_window(self):
        ConfigurationWindow(self.window, self)
        self.unload_window()
        self.logger.log("CONFIGURATION", "Changed window to CONFIGURATION")

    def my_format(self, txt, *args) -> str:
        txt = str(txt)
        if len(txt) == 1:
            return "0" + txt
        else:
            return txt
