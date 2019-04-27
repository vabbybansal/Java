/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.cmu.andrew.vaibhavb.model;

import edu.cmu.andrew.vaibhavb.project4maven.Project4Task2Service;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

/**
 *
 * @author vabby
 */
public class BeerOutletBusinessLogic {

    //API KEY for the beermapping web API
    public static final String BEER_MAPPING_API_KEY = "92bcf9cbd660aeefda899eab01ebc943";
    
    //WebService endpoint for list of outlets by city name
    public static final String BEER_MAPPING_ENDPOINT_BY_CITYNAME  = "http://beermapping.com/webservice/loccity/" + BeerOutletBusinessLogic.BEER_MAPPING_API_KEY +  "/";
    
    //constant string to be appended to each hit to beer mapping to fetch JSON instead of XML
    public static final String REQUEST_JSON_CONSTANT = "&s=json";

    
    

    public static String reFormatAPIResponse(String apiResponse){
        apiResponse = apiResponse.replace("\\", "");
        return apiResponse;
    }
    
    //Method to fetch the beer outlets list based on the city
    public static String fetchOutletsByCityName(String cityName){
        
        String beerMappingAPI = BeerOutletBusinessLogic.BEER_MAPPING_ENDPOINT_BY_CITYNAME + cityName + BeerOutletBusinessLogic.REQUEST_JSON_CONSTANT;
        
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
            
            //check if the beermapping API return null
            if(jsonArraySize == 1)
            {
                JSONObject tempJsonObj = (JSONObject) jsonArray.get(0);
                if(tempJsonObj.get("overall") == null)
                {
                    return listOfBeerOutlets;
                }
            }
            
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

    
}
