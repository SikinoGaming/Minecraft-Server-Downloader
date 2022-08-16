import tkinter
import psutil

from utils.logger import Logger
from utils.translations import TranslationsManager
from tkinter.constants import *


class ConfigurationWindow:

    def __init__(self, window:tkinter.Tk, eula_window):
        self.window = window
        self.eula_window = eula_window
        self.logger = self.eula_window.logger
        self.translations = self.eula_window.translations
        self.server_path = self.eula_window.path
        self.widget_list = []
        self.nogui_accepted = False
        self.load()

    def load(self):
        # TITLE
        self.title = tkinter.Label(text=self.translations.get_trans("all.title"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.title)

        # TITLE MEMORY
        self.memory = tkinter.Label(text=self.translations.get_trans("conf.memory"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.memory.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.memory)

        # MEMORY SLIDER
        self.slider = tkinter.Scale(self.window, from_=1, to=str(int(psutil.virtual_memory().total) / (1024 * 1024 * 1024))[:1], orient=HORIZONTAL, background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", activebackground="#252525", font=('Roboto', 14))
        self.slider.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.title)

        # NOGUI CHECKBOX
        self.nogui = tkinter.Checkbutton(self.window)
        self.nogui.configure(text=self.translations.get_trans("conf.nogui"), command=self.switch_nogui , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12, 'underline'), activebackground="#252525", activeforeground="#DADADA")
        self.nogui.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.nogui)

        # CREATE server.properties
        self.apply_button = tkinter.Button(background='#2E2E2E', text=self.translations.get_trans("conf.create"), relief=SOLID, fg="#DADADA", command=self.create_files, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.apply_button.place(relx=0.5, rely=0.93, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.apply_button)

        self.logger.log("CONFIGURATION", "Created Configuration's widgets")

    def switch_nogui(self):
        self.nogui_accepted = not self.nogui_accepted

    def create_files(self):

        args = " "
        if self.nogui_accepted:
            args += "nogui"

        with open(self.server_path + "start.bat", "w") as start_bat:
            self.logger.log("CONFIGURATION", "Creating start file (bat)")
            start_bat.write(
"""@echo off
java -jar -Xmx""" + str(self.slider.get()*1024) + """M "Serveur Minecraft """ + self.eula_window.download_window.current_version + " " + self.eula_window.download_window.current_version_server + '.jar"' + args + "\npause")
            start_bat.close()

        with open(self.server_path + "start.sh", "w") as start_sh:
            self.logger.log("CONFIGURATION", "Creating start file (shell)")
            start_sh.write(
"""#! /bin/bash
java -jar -Xmx""" + str(self.slider.get()*1024) + """M "Serveur Minecraft """ + self.eula_window.download_window.current_version + " " + self.eula_window.download_window.current_version_server + '.jar"' + args)
            start_sh.close()

            self.info = tkinter.Label(text=self.translations.get_trans("conf.file"), background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.info.place(relx=0.5, rely=0.85, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.info)

    def unload_window(self):
        i=0
        for widget in self.widget_list:
            widget_name = [ i for i, a in locals().items() if a == widget][0]
            self.logger.log("CONFIGURATION", "Removed " + widget_name + " from the screen (" + str(i + 1) + "/" + str(len(self.widget_list)) + ")")
            widget.destroy()
            i += 1
