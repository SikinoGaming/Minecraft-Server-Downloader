#!/usr/bin/bash
command -v wget
if [$? = 1]; then sudo apt install wget -y; fi

echo
echo "Merci d'utiliser MinecraftServerDownloader"
echo
echo "Les types de serveur disponibles sont :"
echo "      vanilla"
echo
echo "Merci d'écrire votre version ou votre type de serveur tel qu'ils sont montrés et sans virgules."
echo

echo "Quel est le type de serveur ?"
read type

echo
echo "Votre type de serveur est $type"
echo "Les version de Minecraft disponibles sont :"
echo "      1.8.9, 1.9.4, 1.10.2, 1.11.2, 1.12.2, 1.13.2, 1.14.4, 1.15.2, 1.16.5, 1.17.1 et 1.18.2"

echo Quel est la version de Minecraft ?
read version
echo  

if [ "$type" = "vanilla" ] ; then
    if [ $version = "1.18.2" ]; then link="https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar"; fi
    if [ $version = "1.17.1" ]; then link="https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar"; fi
    if [ $version = "1.16.5" ]; then link="https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"; fi
    if [ $version = "1.15.2" ]; then link="https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar"; fi
    if [ $version = "1.14.4" ]; then link="https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar"; fi
    if [ $version = "1.13.2" ]; then link="https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"; fi
    if [ $version = "1.12.2" ]; then link="https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar"; fi
    if [ $version = "1.11.2" ]; then link="https://launcher.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar"; fi
    if [ $version = "1.10.2" ]; then link="https://launcher.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar"; fi
    if [ $version = "1.9.4" ]; then link="https://launcher.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar"; fi
    if [ $version = "1.8.9" ]; then link="https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar"; fi
else
    echo "Votre type de serveur est incorrect"
fi
echo "Téléchargement du serveur $type en $version"
echo "Le lien est $link"
echo  
mkdir Minecraft-Server
cd server
wget $link
mv server.jar "Server-$version-$type.jar"