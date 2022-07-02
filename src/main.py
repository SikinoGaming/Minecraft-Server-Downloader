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
        self.window.iconbitmap("server.ico")
        self.window.config(background='#576574')

        self.minecraft_versions = [
            "1.8.9",
            "1.9.4",
            "1.10.2",
            "1.11.2",
            "1.12.2",
            "1.13.2",
            "1.14.4",
            "1.15.2",
            "1.16.5",
            "1.17.1"
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
        self.name = tkinter.Label(text="Minecraft Server Downloader", background="#576574")
        self.name.place(x=290, y=25)
        
        self.create_server_version()
        self.create_minecraft_version()
        #self.create_path_field()

        self.start_button = tkinter.Button(text="Télécharger le serveur", background="#95afc0", relief=SOLID, activebackground="#576574", command=self.download)
        self.start_button.place(x=300, y=380)


    def create_minecraft_version(self):

        self.variable_mc = tkinter.StringVar(self.window)
        self.variable_mc.set("Choisissez la Version de Minecraft")

        self.minecraft_version_button = tkinter.OptionMenu(
            window,
            self.variable_mc,
            *self.minecraft_versions
        )
        self.minecraft_version_button.config(background="#576574", activebackground="#576574", relief=SOLID, highlightbackground="#576574")

        self.minecraft_version_button.place(x=255, y=100)

        self.variable_mc.trace("w", self.choise_version_mc)

    def create_server_version(self):
        self.variable_server = tkinter.StringVar(self.window)
        self.variable_server.set("Choisissez le Type de Serveur")

        self.server_version_button = tkinter.OptionMenu(
            window,
            self.variable_server,
            *self.server_versions
        )
        self.server_version_button.config(background="#576574", activebackground="#576574", relief=SOLID, highlightbackground="#576574")

        self.server_version_button.place(x=270, y=180)

        self.variable_server.trace("w", self.choise_version_server)

    def choise_version_mc(self, *args):
        self.current_version = self.variable_mc.get()
        print(self.current_version)

    def choise_version_server(self, *args):
        self.current_version_server = self.variable_server.get()
        print(self.current_version_server)

    def create_path_field(self):
        self.path_name = tkinter.Label(text="Emplacement du Serveur", background="#576574")
        self.path_field = tkinter.Entry(background="#576574", borderwidth=2, relief=SOLID, width=60)
        self.path_field.insert(1, "E:/Ethan/Minecraft Server Downloader/run/")

        self.path_name.place(x=293, y=260)
        self.path_field.place(x=190, y=290)

    def download(self):
        if not self.current_version_server == "0" and not self.current_version == "0":
            FileManager(self.current_version_server, self.current_version, "./server")
        elif self.current_version_server == "0":
            self.error = tkinter.Label(text="ERREUR : Il vous faut sélectionner un type de serveur", background="#eb2f06")
            self.error.place(x=222, y=450)
        elif self.current_version == "0":
            self.error = tkinter.Label(text="ERREUR : Il vous faut sélectionner une version de Minecraft", background="#eb2f06")
            self.error.place(x=222, y=450)

Application(window)
window.mainloop()