import tkinter
import datetime

class PropertiesWindow:

    def __init__(self, window:tkinter.Tk, conf_window):
        self.window = window
        self.conf = conf_window
        self.logger = self.conf.logger
        self.translations = self.conf.translations
        self.widget_list = []

        self.cmd_blocks = "false"
        self.pvp = "true"
        self.structures = "true"
        self.crack = "false"
        self.max_players = 20
        self.render_distance = 10
        self.flight = "false"
        self.nether = "true"
        self.hardcore = "false"
        self.whitelist = "false"
        self.monsters = "true"

        self.load()

    def load(self):
        # TITLE
        self.title = tkinter.Label(text=self.translations.get_trans("all.title"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 14))
        self.title.place(relx=0.35, rely=0.1, anchor="center")
        self.widget_list.insert(len(self.widget_list), self.title)

        # CREATE BUTTON
        self.create_button = tkinter.Button(background='#2E2E2E', text=self.translations.get_trans("prop.create"), relief="solid", fg="#DADADA", command=self.create_file, highlightbackground="#7A7A7A", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 12), cursor="hand2")
        self.create_button.place(relx=0.85, rely=0.1, anchor="center")
        self.widget_list.insert(len(self.widget_list), self.create_button)

        # SEED FIELD
        self.seed_field = tkinter.Entry(background='#2E2E2E', borderwidth=1, relief="solid", width=29, fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 12))
        self.seed_field.place(relx=0.25, rely=0.18, anchor="n")
        self.seed_field.insert(0, self.translations.get_trans("prop.seed_text"))
        self.seed_field.bind("<FocusIn>", self.clear_seed_text)
        self.widget_list.insert(len(self.widget_list), self.seed_field)

        # WORLD NAME FIELD
        self.world_field = tkinter.Entry(background='#2E2E2E', borderwidth=1, relief="solid", width=29, fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 12))
        self.world_field.place(relx=0.75, rely=0.18, anchor="n")
        self.world_field.insert(0, self.translations.get_trans("prop.world_text"))
        self.world_field.bind("<FocusIn>", self.clear_world_text)
        self.widget_list.insert(len(self.widget_list), self.world_field)

        # GAMEMODE MENU
        self.gamemodes = tkinter.StringVar(self.window)
        self.gamemodes.set(self.translations.get_trans("prop.choose_gamemode"))
        self.gamemode_menu = tkinter.OptionMenu(
            self.window,
            self.gamemodes,
            *["survival", "creative", "adventure", "spectator"]
        )
        self.gamemode_menu.config(background='#2E2E2E', relief="solid", fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 12), cursor="hand2")
        self.gamemode_menu['menu'].config(background='#2E2E2E', relief="solid", fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10), cursor="hand2")
        self.gamemode_menu.place(relx=0.25, rely=0.25, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.gamemode_menu)

        # DIFFICULTY MENU
        self.difficulties = tkinter.StringVar(self.window)
        self.difficulties.set(self.translations.get_trans("prop.choose_difficulty"))
        self.difficulty_menu = tkinter.OptionMenu(
            self.window,
            self.difficulties,
            *["peaceful", "easy", "normal", "hard"]
        )
        self.difficulty_menu.config(background='#2E2E2E', relief="solid", fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 12), cursor="hand2")
        self.difficulty_menu['menu'].config(background='#2E2E2E', relief="solid", fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10), cursor="hand2")
        self.difficulty_menu.place(relx=0.75, rely=0.25, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.difficulty_menu)

        # COMMAND BLOCKS CHECKBOX
        self.cmd_blocks_check = tkinter.Checkbutton(self.window)
        self.cmd_blocks_check.configure(text=self.translations.get_trans("prop.cmd_blocks"), command=self.switch_cmd_blocks , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), justify="center", activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.cmd_blocks_check.place(relx=0.25, rely=0.34, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.cmd_blocks_check)

        # CRACK CHECKBOX
        self.crack_check = tkinter.Checkbutton(self.window)
        self.crack_check.configure(text=self.translations.get_trans("prop.crack"), command=self.switch_crack , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.crack_check.place(relx=0.75, rely=0.34, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.crack_check)

        # PvP CHECKBOX
        self.pvp_check = tkinter.Checkbutton(self.window)
        self.pvp_check.configure(text=self.translations.get_trans("prop.pvp"), command=self.switch_pvp , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.pvp_check.place(relx=0.25, rely=0.42, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.pvp_check)
        self.pvp_check.select()
        self.switch_pvp()

        # STRUCTURES CHECKBOX
        self.structures_check = tkinter.Checkbutton(self.window)
        self.structures_check.configure(text=self.translations.get_trans("prop.structures"), command=self.switch_strucures , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.structures_check.place(relx=0.75, rely=0.42, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.structures_check)
        self.structures_check.select()
        self.switch_strucures()

        # Max Player Text
        self.players_text = tkinter.Label(text=self.translations.get_trans("prop.players"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 10))
        self.players_text.place(relx=0.25, rely=0.49, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.players_text)
        # Max Player SpinBox
        self.player_spinbox = tkinter.Spinbox(self.window, from_=1, to=6969, textvariable=self.max_players)
        self.player_spinbox.configure(background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525")
        self.player_spinbox.place(relx=0.25, rely=0.54, anchor="n")

        # Render Distance Text
        self.render_distance_text = tkinter.Label(text=self.translations.get_trans("prop.render_distance"), background="#2E2E2E", fg="#DADADA", font=('Roboto', 10))
        self.render_distance_text.place(relx=0.75, rely=0.49, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.render_distance_text)
        # Render Distance SpinBox
        self.render_distances_pinbox = tkinter.Spinbox(self.window, from_=2, to=32, textvariable=self.render_distance)
        self.render_distances_pinbox.configure(background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525")
        self.render_distances_pinbox.place(relx=0.75, rely=0.54, anchor="n")

        # FIGHT CHECKBOX
        self.flight_check = tkinter.Checkbutton(self.window)
        self.flight_check.configure(text=self.translations.get_trans("prop.flight"), command=self.switch_flight , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.flight_check.place(relx=0.25, rely=0.63, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.flight_check)

        # NETHER CHECKBOX
        self.nether_check = tkinter.Checkbutton(self.window)
        self.nether_check.configure(text=self.translations.get_trans("prop.nether"), command=self.switch_nether , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.nether_check.place(relx=0.75, rely=0.63, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.nether_check)
        self.nether_check.select()
        self.switch_nether()

        # HARDCORE CHECKBOX
        self.hardcore_check = tkinter.Checkbutton(self.window)
        self.hardcore_check.configure(text=self.translations.get_trans("prop.hardcore"), command=self.switch_hardcore , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.hardcore_check.place(relx=0.25, rely=0.70, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.hardcore_check)

        # WHITELIST CHECKBOX
        self.whitelist_check = tkinter.Checkbutton(self.window)
        self.whitelist_check.configure(text=self.translations.get_trans("prop.whitelist"), command=self.switch_whitelist , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.whitelist_check.place(relx=0.75, rely=0.70, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.whitelist_check)

        # MONSTERS CHECKBOX
        self.monsters_check = tkinter.Checkbutton(self.window)
        self.monsters_check.configure(text=self.translations.get_trans("prop.monsters"), command=self.switch_monsters , background="#2E2E2E", fg="#DADADA", font=('Roboto', 12), activebackground="#252525", activeforeground="#DADADA", cursor="hand2")
        self.monsters_check.place(relx=0.25, rely=0.77, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.monsters_check)
        self.monsters_check.select()
        self.switch_monsters()

        # LEVEL TYPES MENU
        self.types = tkinter.StringVar(self.window)
        self.types.set(self.translations.get_trans("prop.choose_difficulty"))
        self.types_menu = tkinter.OptionMenu(
            self.window,
            self.types,
            *["normal", "large_biomes", "flat", "amplified"]
        )
        self.types_menu.config(background='#2E2E2E', relief="solid", fg="#DADADA", highlightbackground="#7A7A7A", highlightthickness=1, activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 12), cursor="hand2")
        self.types_menu['menu'].config(background='#2E2E2E', relief="solid", fg="#DADADA", activebackground="#252525", activeforeground="#DADADA", font=('Roboto', 10), cursor="hand2")
        self.types_menu.place(relx=0.75, rely=0.77, anchor="n")
        self.widget_list.insert(len(self.widget_list), self.types_menu)

        # Ressource Pack
        self.ressource_pack = tkinter.Text(background='#2E2E2E', borderwidth=1, relief="solid", width=60, height=1, fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 12))
        self.ressource_pack.place(relx=0.5, rely=0.84, anchor="n")
        self.ressource_pack.insert("end", self.translations.get_trans("prop.ressource_pack"))
        self.widget_list.insert(len(self.widget_list), self.ressource_pack)

        # Message Of The Day
        self.motd = tkinter.Text(background='#2E2E2E', borderwidth=1, relief="solid", width=60, height=2, fg="#DADADA", highlightbackground="#7A7A7A", font=('Roboto', 12))
        self.motd.place(relx=0.5, rely=0.9, anchor="n")
        self.motd.insert("end", self.translations.get_trans("prop.motd"))
        self.widget_list.insert(len(self.widget_list), self.motd)

    def clear_seed_text(self, *args):
        self.seed_field.delete(0, tkinter.END)
    
    def clear_world_text(self, *args):
        self.world_field.delete(0,tkinter.END)

    def switch_cmd_blocks(self):
        if self.cmd_blocks == "true":
            self.cmd_blocks = "false"
        else:
            self.cmd_blocks = "true"

    def switch_crack(self):
        if self.crack == "true":
            self.crack = "false"
        else:
            self.crack = "true"

    def switch_pvp(self):
        if self.pvp == "true":
            self.pvp = "false"
        else:
            self.pvp = "true"

    def switch_strucures(self):
        if self.structures == "true":
            self.structures = "false"
        else:
            self.structures = "true"

    def switch_flight(self):
        if self.flight == "true":
            self.flight = "false"
        else:
            self.flight = "true"

    def switch_nether(self):
        if self.nether == "true":
            self.nether = "false"
        else:
            self.nether = "true"

    def switch_hardcore(self):
        if self.hardcore == "true":
            self.hardcore = "false"
        else:
            self.hardcore = "true"

    def switch_whitelist(self):
        if self.whitelist == "true":
            self.whitelist = "false"
        else:
            self.whitelist = "true"

    def switch_monsters(self):
        if self.monsters == "true":
            self.monsters = "false"
        else:
            self.monsters = "true"

    def create_file(self):

        with open(self.conf.server_path + "server.properties", "w") as properties_file:
            self.logger.log("PROPERTIES", "Creating server.properties file")

            current = datetime.datetime.now()
            weekday = ""
            if current.weekday() == 0: weekday = "Mon"
            elif current.weekday() == 1: weekday = "Tue"
            elif current.weekday() == 2: weekday = "Wed"
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

            if self.seed_field.get() == self.translations.get_trans("prop.seed_text"):
                self.seed_field.delete(0, tkinter.END)
            if self.world_field.get() == self.translations.get_trans("prop.world_text"):
                self.world_field.delete(0,tkinter.END)
            if self.gamemodes.get() == self.translations.get_trans("prop.choose_gamemode"):
                self.gamemodes.set("survival")
            if self.motd.get("end") == self.translations.get_trans("prop.motd"):
                self.motd.set("A Simple Minecraft Server, Created with Minecraft Server Downloader by Sikino, search it in GitHub!")
            if self.difficulties.get() == self.translations.get_trans("prop.choose_difficulty"):
                self.difficulties.set("normal")

            seed = self.seed_field.get()
            gamemode = self.gamemodes.get()
            cmd_block = self.cmd_blocks
            level_name = self.world_field.get()
            motd = self.motd.get('end')
            pvp = self.pvp
            structures = self.structures
            difficulty = self.difficulties.get()
            max_players = self.max_players
            crack = self.crack
            allow_flight = self.flight
            render_distance = self.render_distance
            nether = self.nether
            ressource_pack = self.ressource_pack.get('end')
            hardcore = self.hardcore
            whitelist = self.whitelist
            level_type = self.types.get()
            monsters = self.monsters

            properties_file.write("#Minecraft server properties\n" +
            f"#{weekday} {month} {self.my_format(current.day)} {self.my_format(current.hour)}:{self.my_format(current.minute)}:{self.my_format(current.second)} CEST {current.year}\n" +
            f"level-seed={seed}\n"
            f"gamemode={gamemode}\n" +
            f"enable-command-block={cmd_block}\n" +
            f"level-name={level_name}\n" +
            f"motd={motd}\n" +
            f"pvp={pvp}\n" +
            f"generate-structures={structures}\n" +
            f"difficulty={difficulty}\n" +
            f"max-players=20{max_players}\n" +
            f"online-mode={crack}\n" +
            f"allow-flight={allow_flight}\n" +
            f"view-distance={render_distance}\n" +
            f"allow-nether={nether}\n" +
            f"resource-pack={ressource_pack}\n" +
            f"hardcore={hardcore}\n" +
            f"white-list={whitelist}\n" +
            f"level-type={level_type}\n" +
            f"spawn-monsters={monsters}\n")
            properties_file.close()

    def my_format(self, txt, *args) -> str:
        txt = str(txt)
        if len(txt) == 1:
            return "0" + txt
        else:
            return txt
