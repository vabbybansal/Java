package sorts;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.geometry.VPos;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Menu;
import javafx.scene.control.MenuBar;
import javafx.scene.control.MenuItem;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class sortGraphic extends Application{
	static BorderPane root = new BorderPane();
	GridPane grid = new GridPane();
	Stage primaryStage;
	static Label[] labels = null;


	//Setter Getter of root which will be accessed from many places
	//Can be modified to place constraints on such an important variable
	public static BorderPane getRoot() {
		return root;
	}

	public static void setRoot(BorderPane root) {
		sortGraphic.root = root;
	}


	public static void main(String[] args) {
		launch(args);
	}



	public sortGraphic(){

	}

	@Override
	public void start(Stage primaryStage) throws Exception {

		this.primaryStage = primaryStage;

		//Set the BorderPane 'root' as the Scene of the JavaFX interface
		Scene scene = new Scene(root, 500, 300);
		primaryStage.setTitle("WordNerd");
		primaryStage.setScene(scene);
		primaryStage.show();
		
		
		
		startGrid();
		
		Task task = new Task<Void>(){

			@Override
			protected Void call() throws Exception {

				
				insertionSorts obj = new insertionSorts();
				

//				insertionSorts.myArray = obj.insertionSortBasic(insertionSorts.myArray, 1);
				obj.insertionSortBinary(insertionSorts.myArray, 1);

				
				return null;
			}
			
		};
		new Thread(task).start();
		
//		System.out.println(insertionSorts.arrayToString());
//		insertionSorts obj = new insertionSorts();
//		obj.insertionSortBinary(insertionSorts.myArray, 1);
//		System.out.println(insertionSorts.arrayToString());
//		insertionSorts.findIndexInSortedArray(obj.myArray, 0, obj.myArray.length-1, 0);
//		System.out.println("SEARCHED INDEX: " + insertionSorts.foundIndex);
//		System.out.println(insertionSorts.arrayToString());
//		insertionSorts.reArrangeValInArray(obj.myArray, 0, 9);
		
//		System.out.println(insertionSorts.arrayToString());
		
	}
	
	public void startGrid(){
		root.setCenter(grid);
		grid.setAlignment(Pos.CENTER);
		grid.setHgap(10);
		labels = new Label[insertionSorts.myArray.length];

		for(int i=0; i<insertionSorts.myArray.length; i++)
		{
			labels[i] = new Label();
			labels[i].setStyle("-fx-background-color: red;");
			labels[i].setMinHeight(insertionSorts.myArray[i]*10);
			labels[i].setMinWidth(10);
			labels[i].setPadding(new Insets(2,2,2,2));
			grid.setValignment(labels[i], VPos.BOTTOM);
			grid.add(labels[i], i, 0);
		}
		
	}
	
	public static void insertionBasicUpdate(int index, int value, String color){
		labels[index].setMinHeight(value*10);
		insertionBasicUpdate(index, color);
	}
	public static void insertionBasicUpdate(int index, int value){
		labels[index].setMinHeight(value*10);
	}
	public static void insertionBasicUpdate(int index, String color){
		labels[index].setStyle("-fx-background-color:" +  color + ";");
	}
	
	public static void insertionBasicIndexColor(int index){
	}
}
