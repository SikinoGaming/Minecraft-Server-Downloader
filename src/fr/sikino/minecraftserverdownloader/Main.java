package fr.sikino.minecraftserverdownloader;

import fr.sikino.minecraftserverdownloader.utils.ScreenController;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

public class Main extends Application {
	
	public static Parent root;
	public static Stage stage;
	public static ScreenController screenController;

	public static void main(String[] args) {
		launch(args);
	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		stage = primaryStage;
		Parent root = FXMLLoader.load(getClass().getResource("./scenes/Main.fxml"));
		primaryStage.setTitle("Minecraft Server Downloader");
		primaryStage.setScene(new Scene(root, 600, 400));
		primaryStage.getIcons().add(new Image(Main.class.getResourceAsStream("../../../resources/server.png")));
		primaryStage.show();
		
		ScreenController screenController = new ScreenController(FXMLLoader.load(getClass().getResource("./scenes/Main.fxml")));
		Main.screenController = screenController;
		screenController.screenMap.put("Main", FXMLLoader.load(getClass().getResource("./scenes/Main.fxml")));
		screenController.screenMap.put("EULA", FXMLLoader.load(getClass().getResource("./scenes/EULA.fxml")));
	}
}