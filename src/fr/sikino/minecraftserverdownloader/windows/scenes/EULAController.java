package fr.sikino.minecraftserverdownloader.windows.scenes;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Button;

public class EULAController {

	@FXML
	public Button acceptButton;
	
	public void acceptButton(ActionEvent event) {
		System.out.println("EULA Acceptée !");
	}
	
}
