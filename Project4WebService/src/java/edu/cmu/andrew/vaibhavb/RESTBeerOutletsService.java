
package edu.cmu.andrew.vaibhavb;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;


@WebServlet(name = "RESTBeerOutletsService", urlPatterns = {"/RESTBeerOutletsService/*"})
public class RESTBeerOutletsService extends HttpServlet {

    //API KEY for the beermapping web API
    public static final String BEER_MAPPING_API_KEY = "92bcf9cbd660aeefda899eab01ebc943";
    
    //WebService endpoint for list of outlets by city name
    public static final String BEER_MAPPING_ENDPOINT_BY_CITYNAME  = "http://beermapping.com/webservice/loccity/" + RESTBeerOutletsService.BEER_MAPPING_API_KEY +  "/";
    
    //constant string to be appended to each hit to beer mapping to fetch JSON instead of XML
    public static final String REQUEST_JSON_CONSTANT = "&s=json";

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        
        String getQuery = (request.getPathInfo());
        
        
        String cityName = getQuery.substring(getQuery.indexOf("=")+1);
        //check if query is empty        
        
        
        //////////////////////////////// HANDLE SPACES in CITY, HANDLE NO QUERY
        
        
        if(cityName.length() == 0)
            cityName = "Pittsburgh";
        
        //Fetch outlets by the city name
        String beerMappingResponse = fetchOutletsByCityName(cityName);

        //Reformat the String API response
        beerMappingResponse = reFormatAPIResponse(beerMappingResponse);
        
        //Form a JSON from the API response
        List listOfBeerOutlets = RESTBeerOutletsService.objectifyJson(beerMappingResponse);
        
        //Sort the list according to the overall rating in the descending order
        Collections.sort(listOfBeerOutlets);
              
        //Send all the data back to client
        //Covert the required jsonobjects to jsonarray and then string
        JSONArray jsonArrayToSend = reJSONifyForOutput(listOfBeerOutlets, 0, listOfBeerOutlets.size()-1);
        String jsonArrayString = jsonArrayToSend.toJSONString();
        
        printOnHtml(request, response, jsonArrayString);

    }

    public static String reFormatAPIResponse(String apiResponse){
        apiResponse = apiResponse.replace("\\", "");
        return apiResponse;
    }
    
    //Method to fetch the beer outlets list based on the city
    public String fetchOutletsByCityName(String cityName){
        
        String beerMappingAPI = RESTBeerOutletsService.BEER_MAPPING_ENDPOINT_BY_CITYNAME + cityName + RESTBeerOutletsService.REQUEST_JSON_CONSTANT;
        
        String returnedResponse = fetchDataFromExternalAPI(beerMappingAPI);
        
        return returnedResponse;
        
    }

    public static String fetchDataFromExternalAPI(String urlString){
        
        String response = "";
        try {
            URL url = new URL(urlString);
            
            //Create an HttpURLConnection
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            
            // Read all the text returned by the server
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "UTF-8"));
            String str;
            
            // Read each line of "in" until done, adding each to "response"
            while ((str = in.readLine()) != null) {
                // str is one line of text readLine() strips newline characters
                response += str;
            }
            in.close();
        } catch (IOException e) {
            System.out.println("Eeek, an exception");
            // Do something reasonable.  This is left for students to do.
        }
        
        return response;
    }
    
    
    @Override
    public String getServletInfo() {
        
        return "Short description";
    }

    public static List<BeerOutlet> objectifyJson(String beerMappingResponse) {
        
        //Access information from the JSON object
        JSONParser parser = new JSONParser();

        //List of beeroutlets
        List<BeerOutlet> listOfBeerOutlets = new ArrayList<BeerOutlet>();        
        
        //Get access to all the variables fetched from the client
        try {
            //Parse the jsonText to fetch various variables in the json
            Object obj = parser.parse(beerMappingResponse);
            
            //Create json Array for the list returned
            JSONArray jsonArray = (JSONArray) obj;
            int jsonArraySize = jsonArray.size();
            
            
            
            //Temporary variables
            BeerOutlet beerOutlet;
            JSONObject jsonObj;
            
            //Add all the outlets in the list
            for(int i=0; i<jsonArraySize; i++)
            {
                jsonObj = (JSONObject) jsonArray.get(i);
                beerOutlet = new BeerOutlet(jsonObj, jsonObj.get("overall").toString());
                listOfBeerOutlets.add(beerOutlet);
            }
            
        } catch (ParseException pe) {
            System.out.println("position: " + pe.getPosition());
            System.out.println(pe);            
        }

        return listOfBeerOutlets;
        
    }

    private void printOnHtml(HttpServletRequest request, HttpServletResponse response, String message) {
        
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            /* TODO output your page here. You may use following sample code. */
            
            out.println(message);
            
        } catch (IOException ex) {
            Logger.getLogger(RESTBeerOutletsService.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }

    //Helper method to stick startIndex to endIndex json objects in a JSON Array
    private JSONArray reJSONifyForOutput(List<BeerOutlet> listOfBeerOutlets, int startIndex, int endIndex) {
        
        JSONArray jsonArrayToSend = new JSONArray();
        for(int i=startIndex; i <= endIndex; i++)
        {            
            jsonArrayToSend.add(listOfBeerOutlets.get(i).beerOutletJSONObject);            
        }
        
        return jsonArrayToSend;
    }

}
