from utils.logger import Logger

class TranslationsManager:

    def __init__(self, logger:Logger):
        self.logger = logger
        self.langs = ["fr_FR", "en_UK"]
        self.lang = "en_UK"

    def get_trans(self, id:str) -> str:
        with open("../assets/translations/" + self.lang + ".lang", "r") as trans_file:
            for count, line in enumerate(trans_file):
                if line.startswith(id):
                    return line[len(id)+2:-2]
            # if trad is 404:Not Found
            self.logger.log("Translations Manager", "Translation " + id + " not found")
            if self.lang == "fr_FR":
                return "Si tu vois ça, crée une Issue sur le GitHub du projet / envoyer un message a Sikino et de garder ton dernier fichier log (dans le dossier logs)"
            elif self.lang == "en_UK":
                return "If you see that, create an Issue at the project's GitHub / tell it to Sikino and keep the last log file (in the logs folder)"

    def change_lang(self):
        # Check if current lang isn't the last
        if not self.langs.index(self.lang) + 1 == len(self.langs):
            # Change to the next lang
            self.lang = self.langs[self.langs.index(self.lang) + 1]
        else:
            # Change to the first lang
            self.lang = self.langs[0]
        self.logger.log("Translation Manager", "Changed to lang " + self.lang)
