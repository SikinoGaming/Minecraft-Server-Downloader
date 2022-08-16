import tkinter
import os
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
        self.load()

    def load(self):
        # TITLE
        self.title = tkinter.Label(text=self.translations.get_trans("all.title"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.title.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.title)

        # TITLE MEMORY
        self.memory = tkinter.Label(text=self.translations.get_trans("conf.memory"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.memory.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.memory)

        # MEMORY SLIDER
        self.slider = tkinter.Scale(self.window, from_=1, to=str(int(psutil.virtual_memory().total) / (1024 * 1024 * 1024))[:1], orient=HORIZONTAL, background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", activebackground="#252525", font=('Roboto', 14))
        self.slider.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.title)

        # CREATE server.properties
        self.apply_button = tkinter.Button(background='#2E2E2E', text=self.translations.get_trans("conf.create"), relief=SOLID, fg="#DADADA", command=self.create_files, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.apply_button.place(relx=0.5, rely=0.93, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.apply_button)

        self.logger.log("CONFIGURATION", "Created Configuration's widgets")

    def create_files(self):
        with open(self.server_path + "start.bat", "w") as start_bat:
            self.logger.log("CONFIGURATION", "Creating start file (bat)")
            start_bat.write(
"""@echo off
java -jar -Xmx""" + str(self.slider.get()*1024) + """M "Serveur Minecraft """ + self.eula_window.download_window.current_version + " " + self.eula_window.download_window.current_version_server + '''.jar"
pause''')
            start_bat.close()

        with open(self.server_path + "start.sh", "w") as start_sh:
            self.logger.log("CONFIGURATION", "Creating start file (shell)")
            start_sh.write(
"""#! /bin/bash
java -jar -Xmx""" + str(self.slider.get()*1024) + """M "Serveur Minecraft """ + self.eula_window.download_window.current_version + " " + self.eula_window.download_window.current_version_server + '.jar"')
            start_sh.close()

            self.info = tkinter.Label(text=self.translations.get_trans("conf.file"), background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.info.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.info)

    def unload_window(self):
        i=0
        for widget in self.widget_list:
            widget_name = [ i for i, a in locals().items() if a == widget][0]
            self.logger.log("CONFIGURATION", "Removed " + widget_name + " from the screen (" + str(i + 1) + "/" + str(len(self.widget_list)) + ")")
            widget.destroy()
            i += 1
