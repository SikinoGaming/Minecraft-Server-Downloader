import tkinter 
import webbrowser
import datetime
from tkinter import *

class EULAWindow:

    def __init__(self, window, logger, path):
        self.logger = logger
        self.window = window
        self.widget_list = []
        self.create_eula_window()
        if path.endswith("/"):
            self.path = path
        else:
            self.path = path + "/"

    def create_eula_window(self):
        # EULA LINK
        self.link = tkinter.Label(text="Lien vers le Contrat de Licence Utilisateur Final de Mojang", background="#2E2E2E", fg="#0288d1", font=('Roboto', 14, 'underline'))
        self.link.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.link)
        self.link.bind("<Button-1>", self.callback)

        # AGREE CHECKBOX
        self.agree = Checkbutton(self.window)
        self.agree.configure(text="J'ai lu et j'accepte le Contrat de License Utilisateur Final de Mojang", command=self.create_eula_file, background="#2E2E2E", fg="#DADADA", font=('Roboto', 12, 'underline'), activebackground="#252525", activeforeground="#DADADA")
        self.agree.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.agree)

    def callback(self, *args):
        webbrowser.open_new_tab("https://account.mojang.com/documents/minecraft_eula")
        self.logger.log("EULA", "Open EULA link")

    def create_eula_file(self):
        # Creating Label for waiting
        self.logger.log("EULA", "Creating EULA File")
        self.creating_eula = Label(text="Création du fichier EULA requis pour lancer un serveur...", background="#2E2E2E", fg="#FF8C00", font=('Roboto', 14))
        self.creating_eula.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.widget_list.insert(len(self.widget_list), self.creating_eula)

        # Creating eula.txt file
        with open(self.path + "eula.txt", "w") as start_file:
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

            self.logger.log("EULA", "Creating eula.txt")
            start_file.write("#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#" +
            weekday+ " " + month + " " + str(current.day) + " " + str(current.hour) + ":" + str(current.minute) + ":" + str(current.second) +" CEST "+ str(current.year) + "\neula=true")
            start_file.close()
        
        self.logger.log("EULA", 'eula.txt created')
        self.creating_eula.configure(text='Le fichier "eula.txt" à été créé."')

    def unload_window(self):
        i=0
        for widget in self.widget_list:
            widget_name = [ i for i, a in locals().items() if a == widget][0]
            self.logger.log("MAIN", "Removed " + widget_name + " from the screen (" + str(i + 1) + "/" + str(len(self.widget_list)) + ")")
            widget.destroy()
            i += 1