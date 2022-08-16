
# Minecraft-Server-Downloader

## 1. Version Python de Minecraft Server Downloader.

Cette version est disponible sous forme d'un fichier python et sous forme de fichiers exeutables AMD64 et ARM64 Windows et Linux.

SI VOUS SOUHAITEZ UTILISER UN FICHIER SUR PLUSIEURS ORDINATEURS DIFFÉRENTS, UTILISEZ LE SCRIPT .py OU LES .jar POUR ÊTRE SUR QU'ILS SOIENT EXECUTÉS SANS PROBLÈMES !

## 2. Roadmap

[✔️] Téléchargement des fichiers<br>
[✔️] Acceptation du CLUF<br>
[✔️] Différentes langues<br>
[✔️] Allocation de mémoire<br>
[✔️] Amélioration du téléchargement<br>
[❌] Version CLI (**C**ommand **L**ine **I**nterface)<br>
[❌] Configuration du serveur (server.properties)<br>
[❌] Téléchagement automatique de la dernière version de Minecraft Download Manager<br>
[❌] Amélioration du GUI<br>

Versions :
- [✔️] Vanila (de la 1.8 à la 1.19)<br>
- [❌] Bukkit<br>
- [❌] Spigot<br>
- [❌] Forge<br>
- [❌] Fabric<br>
- [❌] Modpack CurseForge

## 3. Problèmes

### 3.1 Liens

Si les liens ne dirigent pas sur le bon jar (exemple : serveur 1.17 voulu et 1.17.1 téléchargé), faites une "Issue" avec le lien la version qui ne va pas.

Exemple d'Issue :

``PROBLÈME DE LIEN : VANILLA 1.17``

### 3.2 Autres bugs

Si vous avez trouvé un bug, merci de faire une Issue avec un screenshot (ou une vidéo qui filme les étapes c'est encore mieux) du bug et des logs (dans la console si possible et sinon la dernière dans logs/ elles ont leur année, mois, jour, heure, minute et seconde de lancement donc vous pouvez pas vous tromper, normalement) et ne supprimez pas ces fichiers car vous pouvez vous tromper et les anciennes logs peuvent être utiles.
Si vous avez envoyé une photo, merci de nous faire une phrase avec les choses à faire pour reproduire le bug.

## 4. Traductions

### 4.1 Le projet a besoin de votre aide

Vous pouvez aider la traduction du projet en faisant un pull request ou en m'envoyant le fichier en MP ou par mail.
Merci de ne pas mettre de traduction troll (ce sera vérifié avec Google Traduction et/ou DeepL).  

### 4.2 Forme du fichier

Respectez la convention de nommage suivante pour le fichier : ``langue_REGION.lang`` (ex: "fr_FR.lang", "en_UK.lang", "en_US.lang", "es_ES.lang"...)
Pareil pour les indices (ex:"all.name="), veillez à ne pas les modifier et à bien mettre votre traduction entre les guillemets (je suis assez tolérant et testerai avant pour modifier s'il y a un problème).  

### 4.3 Pull Request

Si vous envoyez votre traduction via un pull request, mettez votre fichier ``.lang`` dans le dossier [/assets/translations/](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/assets/translations/) et d'ajouter le nom (nom du fichier sans le ``.lang``) à la variable self.langs de [src/utils/translations.py](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/src/utils/translations.py) en l'ajoutant avant le ] de cette façon : ``, "nom"`` (ex: ``, "en_UK"``).

### 4.4 Autre forme d'envoi

Vous pouvez m'envoyer le fichier ``.lang`` en envoyant un message sur mon [Discord](https://discord.gg/NaV9vwaUdx) dans le salon [#général](https://discord.com/channels/529301599143723008/807293011452231720) en précisant que c'est pour Minecraft Server Downloader.

Si tu n'as pas Discord (qui n'a pas Discord mais bon ça arrive), tu peux m'envoyer un email à [sikino.gaming@gmail.com](mailto:sikino.gaming@gmail.com) en me mettant comme sujet ``Traduction Minecraft Server Downloader`` et ton ficher en pièce jointe.

## 5. Liens

### 5.1 Le projet a besoin de votre aide

Vous pouvez aider le projet en ajoutant des liens. Ces liens peuvent être trouvés sur des sites en cherchant "JAR Server MC {VERSION}" sur google. Je conseil les sites [mcversions.net](mcversions.net) et [minecraft.net](minecraft.net) (dans les arcticles sortis avec la mise à jour (le nom suis ce partern : "MINECRAFT {VERSION} RELEASED")). Vérifiez a bien prendre les lien des SERVEURS en JAR et SUR LES SERVEURS DE MOJANG (launcher.mojang.com) pour les serveurs vanilla. Les version serons vérifiés.

### 5.2 Pull Request

Si vous envoyez vos liens via un pull request, ajoutez une ligne avec le paterne suivant : ``"{VERSION}" : "{LIEN}",`` sous la catégorie du serveur (Vanilla, Spigot, ...).  Les liens sont a ranger de la version la plus jeune (en haut) à la plus vieille (en bas) dans le [link.json](https://github.com/SikinoGaming/Minecraft-Server-Downloader/tree/Python/src/utils/links.json).

### 5.3 Autres formes d'envoi

Vous pouvez m'envoyer le fichier ou un message avec le texte a ajouter sur mon [Discord](https://discord.gg/NaV9vwaUdx) dans le salon [#général](https://discord.com/channels/529301599143723008/807293011452231720) en précisant que c'est pour Minecraft Server Downloader.

Si tu n'as pas Discord (qui n'a pas Discord mais bon ça arrive), tu peux m'envoyer un email à [sikino.gaming@gmail.com](mailto:sikino.gaming@gmail.com) en me mettant comme sujet ``Ajout Liens Minecraft Server Downloader`` et ton ficher en pièce jointe ou les liens avec les versions dans en message.

## 6 Contributeurs

Sikino (Traduction, Liens, Code): [YouTube](https://www.youtube.com/channel/UC08jBD4MwfhkNOR2gUS06CQ), [Instagram](https://www.instagram.com/sikinogaming/), [GitHub](https://github.com/SikinoGaming), [Discord](https://discord.gg/NaV9vwaUdx)