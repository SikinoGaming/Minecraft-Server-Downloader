import requests
import threading
import os

class FileManager(threading.Thread):

    def __init__(self, server_version, mc_version, location):
        self.thread = threading.Thread(name="Download Thread", target=self.start(server_version, mc_version, location))
        self.thread.start()

    def start(self, server_version, mc_version, location):

        self.server_version = str(server_version)
        self.mc_version = str(mc_version)

        if self.server_version == "Vanilla":
            if self.mc_version == "1.17.1":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar")
            elif self.mc_version == "1.16.5":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar")
            elif self.mc_version == "1.15.2":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar")
            elif self.mc_version == "1.14.4":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar")
            elif self.mc_version == "1.13.2":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar")
            elif self.mc_version == "1.12.2":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar")
            elif self.mc_version == "1.11.2":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar")
            elif self.mc_version == "1.10.2":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar")
            elif self.mc_version == "1.9.4":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar")
            elif self.mc_version == "1.8.9":
                self.page = requests.get("https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar")

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
            location = location + "Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar"
            self.download(location)

        else:
            self.base_loca = location + "/"
            location = location + "/Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar"
            self.download(location)

    def download(self, location):
        files_in_folder = os.listdir()

        if not "server.properties" in files_in_folder:
            with open(location, "wb") as server_file:
                print("Downloading server " + self.mc_version + " " + self.server_version + " at " + location)
                server_file.write(self.page.content)
                server_file.close()

            with open(self.base_loca + "start.bat", "w") as start_file:
                print("Creating start file (bat)")
                start_file.write(
"""@echo off
java -jar "Serveur Minecraft """ + self.mc_version + """ """ + self.server_version + """.jar" -Xmx1024M -Xms4096M
pause
exit""")

            with open(self.base_loca + "start.sh", "w") as start_file:
                print("Creating start file (shell)")
                start_file.write(
"""java -jar "Serveur Minecraft """ + self.mc_version + """ """ + self.server_version + """.jar" -Xmx1024M -Xms4096M
pause
exit""")
                start_file.close()