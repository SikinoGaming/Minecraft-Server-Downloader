package fr.sikino.minecraftserverdownloader.utils;

import fr.sikino.minecraftserverdownloader.windows.scenes.MainController;
import me.marnic.jdl.CombinedSpeedProgressDownloadHandler;
import me.marnic.jdl.Downloader;
import me.marnic.jdl.SizeUtil;
import sun.awt.OSInfo;
import sun.awt.OSInfo.OSType;

public class DownloadsManager {
	
	MainController mainController = new MainController();
	String link;
	String serverVersion;
	String minecraftVersion;
	
	public String setJarVersion(String serverVersion, String minecraftversion) {
		
		this.serverVersion = serverVersion.toLowerCase();
		this.minecraftVersion = minecraftversion;
		String link = null;
		
		if (serverVersion == "vanilla") {
			
			if (minecraftversion == "1.18.2") {
				link = "https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar";
			}
			else if (minecraftversion == "1.17.1") {
				link = "https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar";
			}
			else if (minecraftversion == "1.16.5") {
				link = "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar";
			}
			else if (minecraftversion == "1.15.2") {
				link = "https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar";
			}
			else if (minecraftversion == "1.14.4") {
				link = "https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar";
			}
			else if (minecraftversion == "1.13.2") {
				link = "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar";
			}
			else if (minecraftversion == "1.12.2") {
				link = "https://launcher.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar";
			}
			else if (minecraftversion == "1.11.2") {
				link = "https://launcher.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar";
			}
			else if (minecraftversion == "1.10.2") {
				link = "https://launcher.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar";
			}
			else if (minecraftversion == "1.9.4") {
				link = "https://launcher.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar";
			}
			else if (minecraftversion == "1.8.9") {
				link = "https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar";
			}
		}
		return this.link = link;
	}
	
	public void downloadFile(String path) {
		
		if (!path.endsWith("/")) {
			path = path + "/";
		}
		
		System.out.println("------  Programme par Sikino  -------");
		System.out.println(" --- Minecraft Server Downloader ---");
		if (serverVersion == "Vanilla") {
			System.out.println("Serveur en " + serverVersion);
		} else {
			System.out.println("Serveur sous " + serverVersion);
		}
		System.out.println("Et en " + minecraftVersion);
		System.out.println("Téléchargé à " + path);
		System.out.println("Téléchargé depuis " + link);
		
		Downloader downloader = new Downloader(false);
		
		final String FINALPATH = path;
		
        Thread downloadThread = new Thread(new Runnable() {
            @Override
            public void run() {
            	downloader.downloadFileToLocation(link, FINALPATH + "server.jar");
            }
        });
        
        if (OSInfo.getOSType() == OSType.WINDOWS) {
        	
        	downloader.setDownloadHandler(new CombinedSpeedProgressDownloadHandler(downloader) {
    			
                @Override
                public void onDownloadProgress(int downloaded,int maxDownload,int percent) {
                	float flpercent = percent;
                	mainController.percentText.setText(percent + "%");
                	mainController.fileSize.setText((Math.round(SizeUtil.toMBFB(downloaded) * 100) / 100) + "/" + (Math.round(SizeUtil.toMBFB(maxDownload) * 100) / 100) + "Mo");
                	mainController.progressBar.setProgress(flpercent / 100);
                }
                
                @Override
                public void onDownloadTickPerSec(int bytesPerSec) {
                	mainController.downloadSpeed.setText((Math.round(SizeUtil.toMBFB(bytesPerSec) * 100) / 100) + " Mo/s");
                }

    			@Override
                public void onDownloadFinish() {
    				System.out.println("Download Finished");
    				System.exit(0);
                }
                
    			@Override
                public void onDownloadStart() {
                	/*mainController.progressBar.setVisible(true);
                	mainController.downloadSpeed.setVisible(true);
                	mainController.percentText.setVisible(true);
                	mainController.fileSize.setVisible(true);
                	mainController.separator.setVisible(true);*/
                }

    			@Override
    			public void onDownloadSpeedProgress(int downloaded, int maxDownload, int percent, int bytesPerSec) {
    				// Obligatoire
    			}
        	});
        	
        } else {
			
			downloader.setDownloadHandler(new CombinedSpeedProgressDownloadHandler(downloader) {
    			
                @Override
                public void onDownloadProgress(int downloaded,int maxDownload,int percent) {
                	System.out.println(SizeUtil.toMBFB(downloaded) + "Mb downloaded of " + maxDownload + ", " + percent);
                }
                
                @Override
                public void onDownloadTickPerSec(int bytesPerSec) {
                	System.out.println((Math.round(SizeUtil.toMBFB(bytesPerSec) * 100) / 100) + " Mo/s");
                }

    			@Override
                public void onDownloadFinish() {
    				System.out.println("Download Finished");
    				System.exit(0);
                }
                
    			@Override
                public void onDownloadStart() {
                	System.out.println("Starting Download");
                }

    			@Override
    			public void onDownloadSpeedProgress(int downloaded, int maxDownload, int percent, int bytesPerSec) {
    				// Obligatoire
    			}
            });
		}
		downloadThread.start();
	}

}
