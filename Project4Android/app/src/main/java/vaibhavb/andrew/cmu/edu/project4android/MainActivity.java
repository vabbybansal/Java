package vaibhavb.andrew.cmu.edu.project4android;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    public static FetchData fetchDataProxy = new FetchData();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final MainActivity me = this;


        //Attach events
        attachEvents(me);

    }

    private void attachEvents(final MainActivity me) {

        //attach button onclicklistener
        Button beerItButton = (Button) findViewById(R.id.button_beerIt);
        beerItButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

        //Make the previous searchResults empty
        ((TextView) findViewById(R.id.searchResults)).setText("");

        //Fetch the location entered by the user
        EditText searchEditText = (EditText) findViewById(R.id.edit_text_searchLocation);
        String searchLocation = searchEditText.getText().toString();

        //Fetch Data for the searchLocation query from the web service

        String response = fetchDataProxy.getData(me, searchLocation);


            }
        });
    }

    public void showDataFromAPI(String incomingData) {

//        String processedData = processAPIReturnAsJSON(incomingData);
            TextView text1 = (TextView) findViewById(R.id.searchResults);
            text1.setText(incomingData);
    }

    //Create jsonArray from the incoming string from API
    private String processAPIReturnAsJSON(String incomingData) {

        JSONArray jsonArray = null;

        //Read the JSON string and convert it to a JSON Array object
        try {
            jsonArray = new JSONArray(incomingData);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        return Integer.toString(jsonArray.length());

    }


    //Use the returned array to place on the view
    public void useReturnedData(String returnedData) {

        JSONArray returnedJSONArray = null;
        String jsonRating = "";
        boolean correctJSON = true;
        String fallbackErrorMessage = "";

        //Handle empty response
        if (returnedData.length() == 0 || returnedData.equals("[]")) {
            printErrorOnApp("No response from server");
            return;
        }

        //convert the string to JSON
        try {
            returnedJSONArray = new JSONArray(returnedData);
        } catch (JSONException e) {
            e.printStackTrace();
            correctJSON = false;

        }

        //If no issues with building the JSON
        JSONObject tempJson = null;
        String name;
        String rating;
        StringBuilder viewString = new StringBuilder();

        //Show maximum 5 best Beer Outlets
        int maxResults = Math.min(returnedJSONArray.length(), 5);

        //Show results label
        if (correctJSON) {
            ((TextView) findViewById(R.id.labelResults)).setVisibility(View.VISIBLE);
        }

        //Convert the JSONArray to a list
        for (int i = 0; i < maxResults; i++) {
            //get the jsonObject
            try {
                tempJson = (JSONObject) returnedJSONArray.get(i);
            } catch (JSONException e) {
                e.printStackTrace();
                printErrorOnApp("Corrupt JSON");
            }

            //Access Json data
            try {
                //Create data to place in the view
                viewString.append(Integer.toString(i + 1));
                viewString.append(". ");
                viewString.append(tempJson.get("name"));
                viewString.append(" : ");
                viewString.append(tempJson.get("overall"));
                viewString.append("\n");
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }

        //Print JSON rating
        TextView tempTextView = (TextView) findViewById(R.id.searchResults);
        tempTextView.setText(viewString);


    }

    //Place error in case no return
    private void printErrorOnApp(String s) {
        TextView tempTextView = (TextView) findViewById(R.id.searchResults);
        tempTextView.setText("Error from Server! Check spelling of city, else try again!!");
    }
}
