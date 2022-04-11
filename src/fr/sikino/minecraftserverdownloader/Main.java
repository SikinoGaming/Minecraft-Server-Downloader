package fr.sikino.minecraftserverdownloader;

import fr.sikino.minecraftserverdownloader.linux.CommandPrompt;
import fr.sikino.minecraftserverdownloader.windows.scenes.ScreenController;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import sun.awt.OSInfo;
import sun.awt.OSInfo.OSType;

public class Main extends Application {
	
	public static Parent root;
	public static Stage stage;
	public static ScreenController screenController;

	public static void main(String[] args) {
		if (OSInfo.getOSType() == OSType.WINDOWS) {
			launch(args);
			CommandPrompt.init();
		} else {
			//CommandPrompt.init();
			System.out.println("Désolé mais votre system d'exploitation n'est pas supporté. Essayez de télécharger la verzsion linux du programme si vous êtes vous Mac ou Linux.");
		}
	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		stage = primaryStage;
		Parent root = FXMLLoader.load(getClass().getResource("./windows/scenes/Main.fxml"));
		primaryStage.setTitle("Minecraft Server Downloader");
		primaryStage.setScene(new Scene(root, 600, 400));
		primaryStage.getIcons().add(new Image(Main.class.getResourceAsStream("../../../resources/server.png")));
		primaryStage.show();
		
		ScreenController screenController = new ScreenController(root.getScene());
		Main.screenController = screenController;
		screenController.screenMap.put("Main", FXMLLoader.load(getClass().getResource("./windows/scenes/Main.fxml")));
		screenController.screenMap.put("EULA", FXMLLoader.load(getClass().getResource("./windows/scenes/EULA.fxml")));
	}
}