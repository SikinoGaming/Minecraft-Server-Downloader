import threading
import os
import json

from pySmartDL import SmartDL

class FileManager():

    def __init__(self, download_window):
        self.download_window = download_window
        self.logger = self.download_window.logger
        base_path = self.download_window.path_field.get()
        if base_path.endswith("/"):
            self.loca = base_path
        else:
            self.loca = base_path + "/"
        url = self.get_url(self.download_window.current_version_server, self.download_window.current_version)
        loca = self.loca + "Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar"
        self.file = SmartDL(url, loca)
        self.thread = threading.Thread(target=self.download, args=())
        self.thread.start()

    def get_url(self, server_version:str, mc_version:str) -> str:
        with open("utils/links.json", "r") as file:
            link = json.loads(file.read())[server_version][mc_version]
            file.close()
            return link

    def download(self):
        files_in_folder = os.listdir(path=self.loca)

        if not "server.properties" in files_in_folder:
            self.file.start()
        else:
            self.logger.log("File Manager", "There is a server in this directory")
            self.download_window.show_dir_error()
