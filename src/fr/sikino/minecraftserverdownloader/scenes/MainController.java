package fr.sikino.minecraftserverdownloader.scenes;

import java.net.URL;
import java.util.ResourceBundle;

import fr.sikino.minecraftserverdownloader.utils.DownloadsManager;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.TextField;
import javafx.scene.text.Text;

public class MainController implements Initializable{

	@FXML
	public ChoiceBox<String> serverVersion;
	@FXML
	public ChoiceBox<String> minecraftVersion;
	@FXML
	public TextField serverPath;
	@FXML
	private Button download;
	@FXML
	private Text ilManqueUnServer;
	@FXML
	private Text ilManqueUneVersion;
	@FXML
	public ProgressBar progressBar;
	@FXML
	public Text downloadSpeed;
	@FXML
	public Text percentText;
	@FXML
	public Text fileSize;
	@FXML
	public Text separator;

	private String[] serverVersionList = {"Vanilla",
										  "Sponge *NOT DEVELOPED YET*",
										  "Bukkit *NOT DEVELOPED YET*",
										  "Forge *NOT DEVELOPED YET*",
										  "Fabric *NOT DEVELOPED YET*"
										 };
	
	private String[] minecraftVersionList = {"1.17.1", "1.16.5", "1.15.2", "1.14.4", "1.13.2", "1.12.2", "1.11.2", "1.10.2", "1.9.4", "1.8.9"};

	@Override
	public void initialize(URL arg0, ResourceBundle arg1) {
		serverVersion.getItems().addAll(serverVersionList);
		minecraftVersion.getItems().addAll(minecraftVersionList);
	}
	
	public void download(ActionEvent event) {
		
		if (serverVersion.getValue() == null) {
			ilManqueUnServer.setVisible(true);
			cantDownload();
		}
		
		else if (minecraftVersion.getValue() == null) {
			ilManqueUneVersion.setVisible(true);
			cantDownload();
			
		} else {
			canDownload();
		}
	}
	
	private void canDownload() {
		DownloadsManager dm = new DownloadsManager();
		dm.setJarVersion(serverVersion.getValue(), minecraftVersion.getValue());
		dm.downloadFile(serverPath.getText());
	}
	
	private void cantDownload() {
		new Thread() {
			
			public void run() {
				try {
					Thread.sleep(2000);
					ilManqueUneVersion.setVisible(false);
					ilManqueUnServer.setVisible(false);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			
		}.start();
	}
}
