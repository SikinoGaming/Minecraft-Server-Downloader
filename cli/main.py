import argparse
import os
import json
import datetime

try:
    from pySmartDL import SmartDL
except ImportError as e:
    print("Can't import library " + str(e.name) + ", try \"pip install -r ../gui-requirements.txt\" and retry")
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
        
        try:
            with open("links.json", "r") as file:
                self.link = json.loads(file.read())[self.server_version][self.mc_version]
                file.close()
        except KeyError as e:
            print("There is the problem with your server type or version. Try search (Ctrl + F) in links.json to see if the link is registered.")
        
        self.file = SmartDL(self.link, self.loca + "Serveur Minecraft " + self.mc_version + " " + self.server_version + ".jar")

        files_in_folder = os.listdir(path=self.loca)
        if not "server.properties" in files_in_folder:
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
            current = datetime.datetime.now()
            weekday = ""
            if current.weekday() == 0: weekday = "Mon"
            elif current.weekday() == 1: weekday = "Tue"
            elif current.weekday() == 2: weekday = "Wen"
            elif current.weekday() == 3: weekday = "Thu"
            elif current.weekday() == 4: weekday = "Fri"
            elif current.weekday() == 5: weekday = "Sat"
            elif current.weekday() == 6: weekday = "Sun"

            if current.month == 1: month = "Jan"
            elif current.month == 2: month = "Feb"
            elif current.month == 3: month = "Mar"
            elif current.month == 4: month = "Apr"
            elif current.month == 5: month = "May"
            elif current.month == 6: month = "Jun"
            elif current.month == 7: month = "Jul"
            elif current.month == 8: month = "Aug"
            elif current.month == 9: month = "Sep"
            elif current.month == 10: month = "Oct"
            elif current.month == 11: month = "Nov"
            elif current.month == 12: month = "Dec"

            eula_file.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#" +
            weekday+ " " + month + " " + str(current.day) + " " + str(current.hour) + ":" + str(current.minute) + ":" + str(current.second) +" CEST "+ str(current.year) + "\neula=true")
            eula_file.close()


if __name__ == "__main__":
    CommandLineInterface()