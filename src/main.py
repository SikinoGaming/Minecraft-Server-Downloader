import tkinter
from tkinter.constants import *
from file_manager import FileManager

window = tkinter.Tk()

class Application:

    def __init__(self, window):
        self.window = window
        self.window.title("Minecraft Server Downloader")
        self.window.geometry("720x480")
        self.window.minsize(720, 480)
        self.window.maxsize(1440, 1080)
        #self.window.iconbitmap("server.ico")
        self.window.config(background='#576574')

        self.minecraft_versions = [
            "1.18.2",
            "1.18.1",
            "1.18",
            "1.17.2",
            "1.17.1",
            "1.17",
            "1.16.5",
            "1.16.4",
            "1.16.3",
            "1.16.2",
            "1.16.1",
            "1.16",
            "1.15.2",
            "1.15.2",
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

        self.create_assets()

    def create_assets(self):
        # TITLE
        self.name = tkinter.Label(text="Minecraft Server Downloader Python Edition", background="#576574")
        self.name.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        # SERVER TYPE
        self.variable_server = tkinter.StringVar(self.window)
        self.variable_server.set("Choisissez le Type de Serveur")
        self.server_version_button = tkinter.OptionMenu(
            window,
            self.variable_server,
            *self.server_versions
        )
        self.server_version_button.config(background="#576574", activebackground="#576574", relief=SOLID, highlightbackground="#576574")
        self.server_version_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.variable_server.trace("w", self.choise_version_server)

        # MINECRAFT VERSION
        self.variable_mc = tkinter.StringVar(self.window)
        self.variable_mc.set("Choisissez la Version de Minecraft")
        self.minecraft_version_button = tkinter.OptionMenu(
            window,
            self.variable_mc,
            *self.minecraft_versions
        )
        self.minecraft_version_button.config(background="#576574", activebackground="#576574", relief=SOLID, highlightbackground="#576574")
        self.minecraft_version_button.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.variable_mc.trace("w", self.choise_version_mc)
        
        # PATH FIELD
        self.path_name = tkinter.Label(text="Emplacement du Serveur", background="#576574")
        self.path_name.place(relx=0.5, rely=0.6, anchor=CENTER)

        self.path_field = tkinter.Entry(background="#576574", borderwidth=2, relief=SOLID, width=60)
        self.path_field.insert(1, "/home/kali/Documents/Minecraft-Server-Downloader/Python/run")
        self.path_field.place(relx=0.5, rely=0.7, anchor=CENTER)

        # LAUNCH DOWNLOAD BUTTON
        self.start_button = tkinter.Button(text="Télécharger le serveur", background="#95afc0", relief=SOLID, activebackground="#576574", command=self.download)
        self.start_button.place(relx=0.5, rely=0.8, anchor=CENTER)

    def choise_version_mc(self, *args):
        self.current_version = self.variable_mc.get()
        print(self.current_version)

    def choise_version_server(self, *args):
        self.current_version_server = self.variable_server.get()
        print(self.current_version_server)

    def download(self):
        if self.current_version_server == "0":
            self.error = tkinter.Label(text="ERREUR : Il vous faut sélectionner un type de serveur", background="#eb2f06")
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)

        elif self.current_version == "0":
            self.error = tkinter.Label(text="ERREUR : Il vous faut sélectionner une version de Minecraft", background="#eb2f06")
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)

        elif self.path_field.get() == "":
            self.error = tkinter.Label(text="ERREUR : Le chemin d'arrivé est vide.", background="#eb2f06")
            self.error.place(relx=0.5, rely=0.9, anchor=CENTER)

        else:
            FileManager(self.current_version_server, self.current_version, self.path_field.get())

Application(window)
window.mainloop()