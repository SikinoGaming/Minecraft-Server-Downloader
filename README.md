# Minecraft-Server-Downloader

## 1. Version Python de Minecraft Server Downloader.

Cette version est disponible sous forme d'un fichier python et sous forme de fichiers exeutables AMD64 et ARM64 Windows et Linux.

SI VOUS SOUHAITEZ UTILISER UN FICHIER SUR PLUSIEURS ORDINATEURS DIFFÉRENTS, UTILISEZ LE SCRIPT .py OU LES .jar POUR ÊTRE SUR QU'ILS SOIENT EXECUTÉS SANS PROBLÈMES !

## 2. Roadmap

[✔️] Téléchargement des fichiers
[✔️] Acceptation du CLUF
[✔️] Différentes langues
[❌] Allocation de mémoire
[❌] Configuration du serveur (server.properties)
[❌] Version CLI (**C**ommand **L**ine **I**nterface)
[❌] Téléchagement automatique de la dernière version de Minecraft Download Manager

Versions :
    [✔️] Vanila (de la 1.8 à la 1.19)
    [❌] Bukkit
    [❌] Spigot
    [❌] Forge
    [❌] Fabric
    [❌] Modpack CurseForge

## 3. Problèmes

Si les liens ne dirigent pas sur le bon jar (exemple : serveur 1.17 voulu et 1.17.1 téléchargé), faites une "Issue" avec le lien la version qui ne va pas.

Exemple d'Issue :
``PROBLÈME DE LIEN : VANILLA 1.17``

## 4. Traductions

### 4.1 Conditions et moyen d'envoi

Vous pouvez aider la traduction du projet en faisant un pull request ou en m'envoyant le fichier en MP ou par mail.
Merci de ne pas mettre de traduction troll (ce sera vérifié avec Google Traduction et Deepl).

### 4.2 Forme du fichier

Respectez la convention de nommage suivante pour le fichier : ``langue_REGION.lang`` (ex: "fr_FR.lang", "en_UK.lang", "en_US.lang", "es_ES.lang"...)
Pareil pour les indices (ex:"all.name="), veillez à ne pas les modifier et à bien mettre votre traduction entre les guillemets (je suis assez tolérant et testerai avant pour modifier s'il y a un problème).

### 4.3 Pull Request

Si vous voulez un pull request, mettez votre fichier ``.lang`` dans le dossier [/assets/translations/](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/assets/translations/) et d'ajouter le nom (nom du fichier sans le ``.lang``) à la variable self.langs de [src/utils/translations.py](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/src/utils/translations.py) en l'ajoutant avant le ] de cette façon : ``, "nom"`` (ex: ``, "en_UK"``).

### 4.4 Autre forme d'envoi

Vous pouvez m'envoyer le fichier ``.lang`` en envoyant un message sur mon [Discord](https://discord.gg/NaV9vwaUdx) dans le salon [#général](https://discord.com/channels/529301599143723008/807293011452231720) en précisant que c'est pour Minecraft Server Downloader.
Si tu n'as pas Discord (qui n'a pas Discord mais bon ça arrive), tu peux m'envoyer un email à [sikino.gaming@gmail.com](mailto:sikino.gaming@gmail.com) en me mettant comme sujet ``Traduction Minecraft Server Downloader`` et ton ficher en pièce jointe.

### 4.5 Traducteurs

Remerciment a ceux qui ont traduit :

Sikino : [Français (France)](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/assets/translations/fr_FR.lang), [Anglais (United Kingdom)](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/assets/translations/en_UK.lang)
[YouTube](https://www.youtube.com/channel/UC08jBD4MwfhkNOR2gUS06CQ), [Instagram](https://www.instagram.com/sikinogaming/), [GitHub](https://github.com/SikinoGaming), [Discord](https://discord.gg/NaV9vwaUdx)