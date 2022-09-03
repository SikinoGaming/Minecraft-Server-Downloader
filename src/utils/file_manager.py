import threading
import os
import json

from pySmartDL import SmartDL

class FileManager():

    def __init__(self, download_window):
        self.download_window = download_window
        self.logger = self.download_window.logger
        self.server_version = self.download_window.current_version_server
        self.mc_version = self.download_window.current_version
        base_path = self.download_window.path_field.get()
        if base_path.endswith("/"):
            self.loca = base_path
        else:
            self.loca = base_path + "/"
        url = self.get_url()
        loca = self.loca + "Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar"
        self.file = SmartDL(url, loca)
        self.thread = threading.Thread(target=self.download, args=())
        self.thread.start()

    def get_url(self) -> str:
        files_in_folder = os.listdir(path=self.loca)
        if not "links.json" in files_in_folder:
            print("Links.json not found, downloading it.")
            SmartDL("https://raw.githubusercontent.com/SikinoGaming/Minecraft-Server-Downloader/Python/links.json", self.loca + "links.json").start()
        
        try:
            with open("links.json", "r") as file:
                self.link = json.loads(file.read())[self.server_version][self.mc_version]
                file.close()
        except KeyError as e:
            print("There is the problem with your server type or version. Try search (Ctrl + F) in links.json to see if the link is registered.")
            exit(1)

    def download(self):
        files_in_folder = os.listdir(path=self.loca)

        if not "server.properties" in files_in_folder:
            self.file.start()
        else:
            self.logger.log("File Manager", "There is a server in this directory")
            self.download_window.show_dir_error()
