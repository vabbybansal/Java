package vaibhavb.andrew.cmu.edu.project4android;

import android.os.AsyncTask;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;


public class FetchData {

    static MainActivity mainClassCallback = null;

    public static String getData(MainActivity me, String searchItem){

        FetchData.mainClassCallback = me;
        new FetchDataThread().execute(searchItem);
        return null;
    }

    //Create class extended from AsyncTask to connect to the network
    private static class FetchDataThread extends AsyncTask<String, Void, String>{
        @Override
        protected String doInBackground(String... searchLocations) {

            //Access the stringLocation query item to be sent to the external API
            String searchLocation = searchLocations[0];
            String response = hitUrlAndFetch(searchLocation);
            return response;
        }

        @Override
        protected void onPostExecute(String returnedData) {
            //Use the data from API
            mainClassCallback.useReturnedData(returnedData);
        }

        //Function to process url and initiate connection
        public static String hitUrlAndFetch(String searchLocation) {

            int indexOfSpace;

            //handle spaces in the city name
            if((indexOfSpace = searchLocation.indexOf(" ")) >=0)
            {
                searchLocation = searchLocation.replaceAll(" ", "%20");
            }

//            String urlString = "https://hidden-everglades-32424.herokuapp.com/RESTBeerOutletsService/city=" + searchLocation;
//            urlString = "http://10.0.2.2:8090/Project4Maven/Project4Task2Service/city=" + searchLocation;

            String urlString = "https://quiet-mountain-11920.herokuapp.com/Project4Task2Service/city=" + searchLocation;


            //Read using client's doGet
            String response = read(urlString);


            return response;
        }

        //Proxy methods to handle HTTP responses
        public static String read(String url) {
            Result r = new Result();
            int status = 0;
            if((status = doGet(url,r)) != 200) return "";
            return r.getValue();
        }

        //Proxy to create HTTPURLConnection to the web service
        public static int doGet(String urlString, Result r){

            String response = "";
            int statusCode = -1;

            //Create HTTP Connection
            try {
                URL url = new URL(urlString);

                //Create an HttpURLConnection
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("GET");
                // tell the server what format we want back
                connection.setRequestProperty("Accept", "application/json");

                connection.setRequestProperty("fancy", "fancier");

                // wait for response
                statusCode = connection.getResponseCode();


                //Process statuscode
                if(statusCode != 200)
                {
                    return statusCode;
                }

                // Read all the text returned by the server
                BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "UTF-8"));
                String str;

                // Read each line of "in" until done, adding each to "response"
                while ((str = in.readLine()) != null) {
                    // str is one line of text readLine() strips newline characters
                    response += str;
                }
                in.close();
            } catch (Exception e) {

                // Do something reasonable.  This is left for students to do.
                String x = e.getMessage();
                String p = x;
            }

            r.setValue(response);
            return statusCode;
        }


    }


}

//doGet Proxy to read
class Result {
    String value;

    public String getValue() {
        return value;
    }
    public void setValue(String value) {
        this.value = value;
    }
}
