import argparse
import os
import json
from datetime import datetime

try:
    from pySmartDL import SmartDL
except ImportError as e:
    print("Can't import library " + str(e.name) + ", try \"pip install pySmartDL\" and retry")
    exit(1)

class CommandLineInterface:

    def __init__(self):
    # ----------------  CLI part  ----------------

        parser = argparse.ArgumentParser()
        parser.add_argument("type", help="Server type (Vanilla only supported now),")
        parser.add_argument("version", help="Server version (1.12.2, 1.16.5, ...),")
        parser.add_argument("path", help="Path to download server (/etc/games/minecraft/server, ../server/, ~/servers/mc/1.12.2),")
        parser.add_argument("--eula", help="Do you accept the Mojang's EULA ?.", action="count")

        args = parser.parse_args()

    # ----------------  Download part  ----------------

        self.server_version = args.type
        self.mc_version = args.version

        if args.path.endswith("/"):
            self.loca = args.path
        else:
            self.loca = args.path + "/"

        files_in_folder = os.listdir(path=self.loca)
        if not "links.json" in files_in_folder:
            print("Links.json not found, downloading it.")
            SmartDL("https://raw.githubusercontent.com/SikinoGaming/Minecraft-Server-Downloader/Python/links.json", self.loca + "links.json").start(True)
        
        try:
            with open("links.json", "r") as file:
                self.link = json.loads(file.read())[self.server_version][self.mc_version]
                file.close()
        except KeyError as e:
            print("There is the problem with your server type or version. Try search (Ctrl + F) in links.json to see if the link is registered.")
            exit(1)

        self.file = SmartDL(self.link, self.loca + "server.jar")

        files_in_folder = os.listdir(path=self.loca)
        if not "server.properties" in files_in_folder:
            print("Downloading server file.")
            self.file.start(True)
        else:
            print("There is a server in this folder, empty or change it.")

    # ----------------  Config part  ----------------

        if not args.eula:
            while True:
                answer = input("Do you accept Mojang's EULA (https://account.mojang.com/documents/minecraft_eula) [y/yes or server can't start] ")
                if answer == "y" or answer == "yes":
                    break

        with open(self.loca + "eula.txt", "w") as eula_file:
            current = datetime.now()

            days = ["Mon", "Tue", "Wen", "thu", "Fri", "Sat", "Sun"]
            weekday = days[current.weekday()]

            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month = months[current.month]

            eula_file.write(
                "#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n" +
                f"#{weekday} {month} {self.my_format(current.day)} {self.my_format(current.hour)}:{self.my_format(current.minute)}:{self.my_format(current.second)} CEST {current.year}\neula=true")
            eula_file.close()

    def my_format(self, txt, *args) -> str:
        txt = str(txt)
        if len(txt) == 1:
            return "0" + txt
        else:
            return txt


if __name__ == "__main__":
    CommandLineInterface()
