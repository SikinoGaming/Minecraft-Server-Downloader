import requests
import threading
import os

from utils.logger import Logger

class FileManager(threading.Thread):

    def __init__(self, server_version:str, mc_version:str, location:str, logger:Logger):
        self.logger = logger
        self.thread = threading.Thread(name="Download Thread", target=self.start(server_version, mc_version, location))
        self.thread.start()

    def start(self, server_version:str, mc_version:str, location:str):

        self.server_version = str(server_version)
        self.mc_version = str(mc_version)

        if self.server_version == "Vanilla":
            if self.mc_version   == "1.19":   self.page = requests.get("https://launcher.mojang.com/v1/objects/e00c4052dac1d59a1188b2aa9d5a87113aaf1122/server.jar")
            elif self.mc_version == "1.18.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar")
            elif self.mc_version == "1.18.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar")
            elif self.mc_version == "1.18":   self.page = requests.get("https://launcher.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar")
            elif self.mc_version == "1.17.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar")
            elif self.mc_version == "1.17":   self.page = requests.get("https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar")
            elif self.mc_version == "1.16.5": self.page = requests.get("https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar")
            elif self.mc_version == "1.16.4": self.page = requests.get("https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar")
            elif self.mc_version == "1.16.3": self.page = requests.get("https://launcher.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar")
            elif self.mc_version == "1.16.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar")
            elif self.mc_version == "1.16.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar")
            elif self.mc_version == "1.16":   self.page = requests.get("https://launcher.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar")
            elif self.mc_version == "1.15.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar")
            elif self.mc_version == "1.15.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar")
            elif self.mc_version == "1.15":   self.page = requests.get("https://launcher.mojang.com/v1/objects/e9f105b3c5c7e85c7b445249a93362a22f62442d/server.jar")
            elif self.mc_version == "1.14.4": self.page = requests.get("https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar")
            elif self.mc_version == "1.14.3": self.page = requests.get("https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar")
            elif self.mc_version == "1.14.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/808be3869e2ca6b62378f9f4b33c946621620019/server.jar")
            elif self.mc_version == "1.14.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/ed76d597a44c5266be2a7fcd77a8270f1f0bc118/server.jar")
            elif self.mc_version == "1.14":   self.page = requests.get("https://launcher.mojang.com/v1/objects/f1a0073671057f01aa843443fef34330281333ce/server.jar")
            elif self.mc_version == "1.13.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar")
            elif self.mc_version == "1.13.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/fe123682e9cb30031eae351764f653500b7396c9/server.jar")
            elif self.mc_version == "1.13":   self.page = requests.get("https://launcher.mojang.com/v1/objects/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar")
            elif self.mc_version == "1.12.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar")
            elif self.mc_version == "1.12.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/561c7b2d54bae80cc06b05d950633a9ac95da816/server.jar")
            elif self.mc_version == "1.12":   self.page = requests.get("https://launcher.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar")
            elif self.mc_version == "1.11.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar")
            elif self.mc_version == "1.11.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/1f97bd101e508d7b52b3d6a7879223b000b5eba0/server.jar")
            elif self.mc_version == "1.11":   self.page = requests.get("https://launcher.mojang.com/v1/objects/48820c84cb1ed502cb5b2fe23b8153d5e4fa61c0/server.jar")
            elif self.mc_version == "1.10.2": self.page = requests.get("https://launcher.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar")
            elif self.mc_version == "1.10.1": self.page = requests.get("https://launcher.mojang.com/v1/objects/cb4c6f9f51a845b09a8861cdbe0eea3ff6996dee/server.jar")
            elif self.mc_version == "1.10":   self.page = requests.get("https://launcher.mojang.com/v1/objects/a96617ffdf5dabbb718ab11a9a68e50545fc5bee/server.jar")
            elif self.mc_version == "1.9.4":  self.page = requests.get("https://launcher.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar")
            elif self.mc_version == "1.9.3":  self.page = requests.get("https://launcher.mojang.com/v1/objects/8e897b6b6d784f745332644f4d104f7a6e737ccf/server.jar")
            elif self.mc_version == "1.9.2":  self.page = requests.get("https://launcher.mojang.com/v1/objects/2b95cc7b136017e064c46d04a5825fe4cfa1be30/server.jar")
            elif self.mc_version == "1.9.1":  self.page = requests.get("https://launcher.mojang.com/v1/objects/bf95d9118d9b4b827f524c878efd275125b56181/server.jar")
            elif self.mc_version == "1.9":    self.page = requests.get("https://launcher.mojang.com/v1/objects/b4d449cf2918e0f3bd8aa18954b916a4d1880f0d/server.jar")
            elif self.mc_version == "1.8.9":  self.page = requests.get("https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar")
            elif self.mc_version == "1.8.8":  self.page = requests.get("https://launcher.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar")
            elif self.mc_version == "1.8.7":  self.page = requests.get("https://launcher.mojang.com/v1/objects/35c59e16d1f3b751cd20b76b9b8a19045de363a9/server.jar")
            elif self.mc_version == "1.8.6":  self.page = requests.get("https://launcher.mojang.com/v1/objects/2bd44b53198f143fb278f8bec3a505dad0beacd2/server.jar")
            elif self.mc_version == "1.8.5":  self.page = requests.get("https://launcher.mojang.com/v1/objects/ea6dd23658b167dbc0877015d1072cac21ab6eee/server.jar")
            elif self.mc_version == "1.8.4":  self.page = requests.get("https://launcher.mojang.com/v1/objects/dd4b5eba1c79500390e0b0f45162fa70d38f8a3d/server.jar")
            elif self.mc_version == "1.8.3":  self.page = requests.get("https://launcher.mojang.com/v1/objects/163ba351cb86f6390450bb2a67fafeb92b6c0f2f/server.jar")
            elif self.mc_version == "1.8.2":  self.page = requests.get("https://launcher.mojang.com/v1/objects/a37bdd5210137354ed1bfe3dac0a5b77fe08fe2e/server.jar")
            elif self.mc_version == "1.8.1":  self.page = requests.get("https://launcher.mojang.com/v1/objects/68bfb524888f7c0ab939025e07e5de08843dac0f/server.jar")
            elif self.mc_version == "1.8":    self.page = requests.get("https://launcher.mojang.com/v1/objects/a028f00e678ee5c6aef0e29656dca091b5df11c7/server.jar")

        elif self.server_version == "Bukkit":
            pass

        elif self.server_version == "Spigot":
            pass

        elif self.server_version == "Forge":
            pass

        elif self.server_version == "Fabric":
            pass

        elif self.server_version == "Modpack CurseForge":
            pass

        if location.endswith("/"):
            self.base_loca = location
        
        else:
            self.base_loca = location + "/"
        location = location + "/Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar"
        self.download(location)

    def download(self, location:str):
        files_in_folder = os.listdir()

        if not "server.properties" in files_in_folder:
            with open(self.base_loca + "Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar", "wb") as server_file:
                self.logger.log("File Manager", "Downloading server " + self.mc_version + " " + self.server_version + " at " + location)
                server_file.write(self.page.content)
                server_file.close()

            with open(self.base_loca + "start.bat", "w") as start_file:
                self.logger.log("File Manager", "Creating start file (bat)")
                start_file.write(
"""@echo off
java -jar -Xmx2048M "Serveur Minecraft """ + self.mc_version + " " + self.server_version + """.jar
pause""")

            with open(self.base_loca + "start.sh", "w") as start_file:
                self.logger.log("File Manager", "Creating start file (shell)")
                start_file.write(
"""#! /bin/bash
java -jar Xmx2048M "Serveur Minecraft """ + self.mc_version + " " + self.server_version + ".jar")
                start_file.close()
                self.logger.log("File Manager", 'Download Ended')
