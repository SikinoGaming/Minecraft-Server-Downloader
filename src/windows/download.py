import tkinter
from tkinter import *
from tkinter.constants import *
from typing import final
from PIL import Image, ImageTk
from utils.file_manager import FileManager
from windows.eula import EULAWindow

class DownloadWindow:

    def __init__(self, window, logger):
        self.logger = logger
        self.logger.log("DOWNLOAD", "Creating Window")
        self.widget_list = []
        self.window = window
        self.window.title("Minecraft Server Downloader")
        self.window.geometry("640x480")
        self.window.minsize(640, 480)
        self.window.maxsize(1440, 1080)
        #self.window.iconbitmap("../assets/server.ico")
        self.bg = Image.open("../assets/background.png").resize((640, 480))
        self.bg = ImageTk.PhotoImage(self.bg)
        bg_label = Label(self.window, image = self.bg)
        bg_label.place(x=0, y=0)

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

        self.create_DOWNLOAD_window()
        self.create_next_button()

    def create_DOWNLOAD_window(self):
        self.logger.log("DOWNLOAD", "Creating DOWNLOAD window widgets")
        # TITLE
        self.name = tkinter.Label(text="Minecraft Server Downloader Python Edition", background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.name.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        # SERVER TYPE
        self.variable_server = tkinter.StringVar(self.window)
        self.variable_server.set("Choisissez le Type de Serveur")
        self.server_version_button = tkinter.OptionMenu(
            self.window,
            self.variable_server,
            *self.server_versions
        )
        self.server_version_button.config(background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.server_version_button['menu'].config(background='#2E2E2E', relief=SOLID, fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10))
        self.server_version_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.server_version_button)

        self.variable_server.trace("w", self.choise_version_server)

        # MINECRAFT VERSION
        self.variable_mc = tkinter.StringVar(self.window)
        self.variable_mc.set("Choisissez la Version de Minecraft")
        self.minecraft_version_button = tkinter.OptionMenu(
            self.window,
            self.variable_mc,
            *self.minecraft_versions
        )
        self.minecraft_version_button.config(background='#2E2E2E', relief=SOLID, fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.minecraft_version_button['menu'].config(background='#2E2E2E', relief=SOLID, fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10))
        self.minecraft_version_button.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.minecraft_version_button)

        self.variable_mc.trace("w", self.choise_version_mc)
        
        # PATH FIELD
        self.path_name = tkinter.Label(text="Emplacement du Serveur", background='#2E2E2E', fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 14))
        self.path_name.place(relx=0.5, rely=0.6, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.path_name)

        self.path_field = tkinter.Entry(background='#2E2E2E', borderwidth=1, relief=SOLID, width=60, fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 12))
        self.path_field.insert(1, "/home/kali/Documents/Minecraft-Server-Downloader/Python/run")
        self.path_field.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.path_field)

        # LAUNCH DOWNLOAD BUTTON
        self.start_button = tkinter.Button(background='#2E2E2E', text="Télécharger le serveur", relief=SOLID, fg="#DADADA", command=self.init_download, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.start_button.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.start_button)
        self.logger.log("DOWNLOAD", "Created widgets of DOWNLOAD window")

    def choise_version_server(self, *args):
        self.current_version_server = self.variable_server.get()
        self.logger.log("DOWNLOAD", self.current_version_server)


    def choise_version_mc(self, *args):
        self.current_version = self.variable_mc.get()
        self.logger.log("DOWNLOAD", self.current_version)

    def init_download(self):
        if self.current_version_server == "0":
            self.error = tkinter.Label(text="ERREUR : Il vous faut sélectionner un type de serveur", background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.error)

        elif self.current_version == "0":
            self.error = tkinter.Label(text="ERREUR : Il vous faut sélectionner une version de Minecraft", background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.error)

        elif self.path_field.get() == "":
            self.error = tkinter.Label(text="ERREUR : Le chemin d'arrivé n'est pas spécifié.", background="#FF8C00", relief=SOLID, font=('Roboto', 14))
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)
            self.widget_list.insert(len(self.widget_list), self.error)

        else:
            FileManager(self.current_version_server, self.current_version, self.path_field.get(), self.logger)

    def create_next_button(self):
        # NEXT BUTTON
        self.next_button = tkinter.Button(background='#2E2E2E', text="Suivant", relief=SOLID, fg="#DADADA", command=self.change_eula_window, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 14))
        self.next_button.place(relx=0.9, rely=0.93, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.next_button)

    def change_eula_window(self):
        EULAWindow(self.window, self.logger, self.path_field.get())
        self.unload_window()
        self.logger.log("EULA", "Changed window to EULA")

    def unload_window(self):
        i=0
        for widget in self.widget_list:
            widget_name = [ i for i, a in locals().items() if a == widget][0]
            self.logger.log("DOWNLOAD", "Removed " + widget_name + " from the screen (" + str(i + 1) + "/" + str(len(self.widget_list)) + ")")
            widget.destroy()
            i += 1