package fr.sikino.minecraftserverdownloader.linux;

import java.util.Scanner;

import fr.sikino.minecraftserverdownloader.utils.DownloadsManager;

public class CommandPrompt {

	public static void init() {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Bienvenue sur Minecraft Server Downloader.");
		System.out.println("Pour avoir  des infos, tappez 'help'.");
		
		System.out.println("Minecraft Server Downloader > ");
		String command = sc.next();
		sc.close();
		
		if (command.contains("help")) {
			
			System.out.println("Commandes :");
			System.out.println("\n");
			System.out.println("	download <version de minecraft> <type de serveur> <dossier de destination>");
			System.out.println("\n");
			System.out.println("<type de serveur> : vanilla");
			System.out.println("<dossier de destination> : ./dossier ou /home/sikino/server");
			System.out.println("<version de minecraft> : 1.8.9, 1.9.4, 1.10.2, 1.11.2, 1.12.2, 1.13.2, 1.14.4, 1.15.2, 1.16.4, 1.17.1, 1.18.2");
			
		} else if (command.contains("download")) {
			final String SPLITER = " ";
			String[] cmd = command.split(SPLITER);
			DownloadsManager dm = new DownloadsManager();
			dm.setJarVersion(cmd[1], cmd[0]);
			dm.downloadFile(cmd[2]);
		}
		
	}
	
}
